import gensim
from gensim.models import LdaModel
from gensim.corpora import Dictionary

model = LdaModel.load("science_model_30_topics")


class LDAModel:

    @classmethod
    def evaluate_topics(cls, data):
        new_model = cls.train_new_model(data, 1, 1000, 200, 1, 9, 20, 100)
        topics_list = new_model.show_topics(num_topics=1, num_words=30, formatted=False)
        topics_words = [(topic[0], [word[0] for word in topic[1]]) for topic in topics_list]
        topics_words_without_scores = [topics_words[0][1]]
        new_corpus = [model.id2word.doc2bow(text) for text in topics_words_without_scores]
        return model[new_corpus[0]]

    @staticmethod
    def train_new_model(data, alpha, chunksize, iterations, num_topics, workers, passes, random_state):
        id2word = Dictionary(data)
        texts = data
        corpus = [id2word.doc2bow(text) for text in texts]

        return gensim.models.LdaModel(
            corpus=corpus,
            id2word=id2word,
            alpha=alpha,
            chunksize=chunksize,
            iterations=iterations,
            num_topics=num_topics,
            #workers=workers,
            passes=passes,
            random_state=random_state,
            eval_every=None,
        )
