import gensim


class TokenizationService:

    @classmethod
    def tokenize_document(cls, data):
        return list(list(cls._tokenize([[data]])))

    @staticmethod
    def _tokenize(sentences):
        for sentence in sentences:
            yield gensim.utils.simple_preprocess(str(sentence), deacc=True)
