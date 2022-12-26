class MenuPool:

    def __init__(self):
        self.menus = {}
        self.modifiers = []
        self.discovered = False

    def get_renderer(self, request):
        self.discover_menus()
        # Returns a menu pool wrapper that is bound
        # to the given request and can perform
        # operations based on the given request.
        return MenuRenderer(pool=self, request=request)

    def discover_menus(self):
        if self.discovered:
            return
        autodiscover_modules('cms_menus')
        from menus.modifiers import register
        register()
        self.discovered = True

    def get_registered_menus(self, for_rendering=False):
        """
        Returns all registered menu classes.

        :param for_rendering: Flag that when True forces us to include
            all CMSAttachMenu subclasses, even if they're not attached.
        """
        self.discover_menus()
        registered_menus = {}

        for menu_class_name, menu_cls in self.menus.items():
            if isinstance(menu_cls, Menu):
                # A Menu **instance** was registered,
                # this is non-standard, but acceptable.
                menu_cls = menu_cls.__class__
            if hasattr(menu_cls, "get_instances"):
                # It quacks like a CMSAttachMenu.
                # Expand the one CMSAttachMenu into multiple classes.
                # Each class is bound to the instance the menu is attached to.
                _get_menu_class = partial(_get_menu_class_for_instance, menu_cls)

                instances = menu_cls.get_instances() or []
                for instance in instances:
                    # For each instance, we create a unique class
                    # that is bound to that instance.
                    # Doing this allows us to delay the instantiation
                    # of the menu class until it's needed.
                    # Plus we keep the menus consistent by always
                    # pointing to a class instead of an instance.
                    namespace = "{0}:{1}".format(
                        menu_class_name, instance.pk)
                    registered_menus[namespace] = _get_menu_class(instance)

                if not instances and not for_rendering:
                    # The menu is a CMSAttachMenu but has no instances,
                    # normally we'd just ignore it but it's been
                    # explicitly set that we are not rendering these menus
                    # via the (for_rendering) flag.
                    registered_menus[menu_class_name] = menu_cls
            elif hasattr(menu_cls, "get_nodes"):
                # This is another type of Menu, cannot be expanded, but must be
                # instantiated, none-the-less.
                registered_menus[menu_class_name] = menu_cls
            else:
                raise ValidationError(
                    "Something was registered as a menu, but isn't.")
        return registered_menus

    def get_registered_modifiers(self):
        return self.modifiers

    def clear(self, site_id=None, language=None, all=False):
        """
        This invalidates the cache for a given menu (site_id and language)
        """
        if all:
            cache_keys = CacheKey.objects.get_keys()
        else:
            cache_keys = CacheKey.objects.get_keys(site_id, language)

        to_be_deleted = cache_keys.distinct().values_list('key', flat=True)

        if to_be_deleted:
            cache.delete_many(to_be_deleted)
            cache_keys.delete()

    def register_menu(self, menu_cls):
        from menus.base import Menu
        assert issubclass(menu_cls, Menu)
        if menu_cls.__name__ in self.menus:
            raise NamespaceAlreadyRegistered(
                "[{0}] a menu with this name is already registered".format(
                    menu_cls.__name__))
        # Note: menu_cls should still be the menu CLASS at this point.
        self.menus[menu_cls.__name__] = menu_cls

    def register_modifier(self, modifier_class):
        from menus.base import Modifier
        assert issubclass(modifier_class, Modifier)
        if modifier_class not in self.modifiers:
            self.modifiers.append(modifier_class)

    def get_menus_by_attribute(self, name, value):
        """
        Returns the list of menus that match the name/value criteria provided.
        """
        # Note that we are limiting the output to only single instances of any
        # specific menu class. This is to address issue (#4041) which has
        # cropped-up in 3.0.13/3.0.0.
        # By setting for_rendering to False
        # we're limiting the output to menus
        # that are registered and have instances
        # (in case of attached menus).
        menus = self.get_registered_menus(for_rendering=False)
        return sorted(list(set([(menu.__name__, menu.name)
                                for menu_class_name, menu in menus.items()
                                if getattr(menu, name, None) == value])))

    def get_nodes_by_attribute(self, nodes, name, value):
        return [node for node in nodes if node.attr.get(name, None) == value]



import os
from typing import List

class Explorer:
    def __init__(self, root_dir: str):
        self.paths = []
        self.root = root_dir
        self.explorer_file(root_dir)

    def explorer_file(self, root):
        files = os.listdir(root)
        for file in files:
            path = os.path.join(root, file)
            if os.path.isdir(path):
                self.explorer_file(path)
            else:
                # if os.path.splitext(path)[1] == '.c' or os.path.splitext(path)[1] == '.h' or os.path.splitext(path)[1] == '.java' or os.path.splitext(path)[1] == '.py':
                #     self.paths.append(path)
                if os.path.splitext(path)[1] == '.py':
                    self.paths.append(path)
                else:
                    continue

    def get_paths(self) -> List:
        return self.paths