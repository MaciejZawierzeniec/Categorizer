import gensim
from gensim.models.phrases import Phraser, Phrases


class NgramsService:

    @staticmethod
    def make_bigrams(data):
        bigram = Phrases(data, min_count=1, threshold=5)
        bigram_mod = gensim.models.phrases.Phraser(bigram)
        return [bigram_mod[doc] for doc in data]
