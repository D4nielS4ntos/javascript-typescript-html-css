import random
import pickle

import numpy as np
from nltk.tokenize import RegexpTokenizer

from keras._tf_keras.keras.models import load_model

from gerar_modelo import n_words, tokens_unicos, tokens_unicos_index, tokenizer


model = load_model("mymodel.h5")


def predict_next_word(input_text, n_best):
    input_text = input_text.lower()
    X = np.zeros((1, n_words, len(tokens_unicos)))
    for i, word in enumerate(input_text.split()):
        X[0, i, tokens_unicos_index[word]] = 1

    predictions = model.predict(X)[0]
    return np.argpartition(predictions, -n_best)[-n_best:]


def generate_text(input_text, text_length, creativity=3):
    word_sequense = input_text.split()
    current = 0
    for _ in range(text_length):
        sub_sequence = " ".join(tokenizer.tokenize(" ".join(word_sequense).lower())[current:current + n_words])
        try:
            choice = tokens_unicos[random.choice(predict_next_word(sub_sequence, creativity))]
        except:
            choice = random.choice(tokens_unicos)
        word_sequense.append(choice)
        current += 1
    return " ".join(word_sequense)

mensagem = generate_text("He will need to go at", 100, 5)
print(mensagem)
