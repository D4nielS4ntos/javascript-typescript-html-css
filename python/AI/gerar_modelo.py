import numpy as np
import pandas as pd
from nltk.tokenize import RegexpTokenizer

from keras._tf_keras.keras.models import Sequential
from keras._tf_keras.keras.layers import LSTM, Dense, Activation
from keras._tf_keras.keras.optimizers import RMSprop

texto_df = pd.read_csv("Tweets.csv")
texto = list(texto_df.text.values)
texto_junto = " ".join(texto)
texto_parcial = texto_junto[:10000]
tokenizer = RegexpTokenizer(r"\w+")
tokens = tokenizer.tokenize(texto_parcial.lower())
tokens_unicos = np.unique(tokens)
tokens_unicos_index = {token: idx for idx, token in enumerate(tokens_unicos)}

n_words = 10
input_words = []
next_words = []

for i in range(len(tokens) - n_words):
    input_words.append(tokens[i:i + n_words])
    next_words.append(tokens[i + n_words])

X = np.zeros((len(input_words), n_words, len(tokens_unicos)), dtype=bool)
Y = np.zeros((len(next_words), len(tokens_unicos)), dtype=bool)

for i, words in enumerate(input_words):
    for j, word in enumerate(words):
        X[i, j, tokens_unicos_index[word]] = 1
    Y[i, tokens_unicos_index[next_words[i]]] = 1

model = Sequential()
model.add(LSTM(128, input_shape=(n_words, len(tokens_unicos)), return_sequences=True))
model.add(LSTM(128))
model.add(Dense(len(tokens_unicos)))
model.add(Activation("softmax"))
model.compile(loss="categorical_crossentropy", optimizer=RMSprop(learning_rate=0.01), metrics=["accuracy"])
model.fit(X, Y, batch_size=128, epochs=10, shuffle=True)

model.save("mymodel.h5")
