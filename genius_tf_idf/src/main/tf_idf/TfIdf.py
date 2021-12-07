import collections
import math


class TfIdf:
    @staticmethod
    def compute_tf(text):
        # На вход берем текст в виде списка (list) слов
        # Считаем частотность всех терминов во входном массиве с помощью
        # метода Counter библиотеки collections
        tf_text = collections.Counter(text)
        for i in tf_text:
            # для каждого слова в tf_text считаем TF путём деления
            # встречаемости слова на общее количество слов в тексте
            tf_text[i] = tf_text[i]/float(len(text))
        # возвращаем объект типа Counter c TF всех слов текста
        return tf_text

    @staticmethod
    def compute_idf(word, corpus):
        # на вход берется слово, для которого считаем IDF
        # и корпус документов в виде списка списков слов
        # количество документов, где встречается искомый термин
        # считается как генератор списков
        return math.log10(len(corpus)/sum([1.0 for i in corpus if word in i]))

    @staticmethod
    def compute_tfidf(corpus):
        documents_list = []
        for text in corpus:
            tf_idf_dictionary = {}
            computed_tf = TfIdf.compute_tf(text)
            for word in computed_tf:
                tf_idf_dictionary[word] = computed_tf[word] * TfIdf.compute_idf(word, corpus)
            documents_list.append(tf_idf_dictionary)
        return documents_list
