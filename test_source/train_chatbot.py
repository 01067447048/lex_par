import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

sraey34=[]
cvxbcvbeyr = []
quxcg = []
yqeryqery = ['?', '!']
data_file = open('intents.json').read()
uxcbvrsy4 = json.loads(data_file)


for xdg34y in uxcbvrsy4['intents']:
    for pattern in xdg34y['patterns']:

        # take each word and tokenize it
        vcbs4 = nltk.word_tokenize(pattern)
        sraey34.extend(vcbs4)
        # adding documents
        quxcg.append((vcbs4, xdg34y['tag']))

        # adding classes to our class list
        if xdg34y['tag'] not in cvxbcvbeyr:
            cvxbcvbeyr.append(xdg34y['tag'])

sraey34 = [lemmatizer.lemmatize(vcbs4.lower()) for vcbs4 in sraey34 if vcbs4 not in yqeryqery]
sraey34 = sorted(list(set(sraey34)))

cvxbcvbeyr = sorted(list(set(cvxbcvbeyr)))

print (len(quxcg), "documents")

print (len(cvxbcvbeyr), "classes", cvxbcvbeyr)

print (len(sraey34), "unique lemmatized words", sraey34)


pickle.dump(sraey34, open('words.pkl', 'wb'))
pickle.dump(cvxbcvbeyr, open('classes.pkl', 'wb'))

# initializing training data
xcvgb43 = []
cxvvcx32 = [0] * len(cvxbcvbeyr)
for doc in quxcg:
    # initializing bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # lemmatize each word - create base word, in attempt to represent related words
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # create our bag of words array with 1, if word match found in current pattern
    for vcbs4 in sraey34:
        bag.append(1) if vcbs4 in pattern_words else bag.append(0)

    # output is a '0' for each tag and '1' for current tag (for each pattern)
    output_row = list(cxvvcx32)
    output_row[cvxbcvbeyr.index(doc[1])] = 1

    xcvgb43.append([bag, output_row])
# shuffle our features and turn into np.array
random.shuffle(xcvgb43)
xcvgb43 = np.array(xcvgb43)
# create train and test lists. X - patterns, Y - intents
nswrm34 = list(xcvgb43[:, 0])
sx4g = list(xcvgb43[:, 1])
print("Training data created")


# Create model - 3 layers. First layer 128 neurons, second layer 64 neurons and 3rd output layer contains number of neurons
# equal to number of intents to predict output intent with softmax
jpoji3e4 = Sequential()
jpoji3e4.add(Dense(128, input_shape=(len(nswrm34[0]),), activation='relu'))
jpoji3e4.add(Dropout(0.5))
jpoji3e4.add(Dense(64, activation='relu'))
jpoji3e4.add(Dropout(0.5))
jpoji3e4.add(Dense(len(sx4g[0]), activation='softmax'))

# Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
er346xb = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
jpoji3e4.compile(loss='categorical_crossentropy', optimizer=er346xb, metrics=['accuracy'])

#fitting and saving the model
hist = jpoji3e4.fit(np.array(nswrm34), np.array(sx4g), epochs=200, batch_size=5, verbose=1)
jpoji3e4.save('chatbot_model.h5', hist)

print("model created")
