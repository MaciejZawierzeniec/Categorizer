from nltk import WordNetLemmatizer
from nltk.corpus import stopwords


class TextProcessingService:

    @staticmethod
    def remove_stopwords(texts):
        return [[word for word in text if word not in stopwords.words('english')] for text in texts]

    @staticmethod
    def lemmatize(data):
        lemmatizer = WordNetLemmatizer()
        return [[lemmatizer.lemmatize(token) for token in doc] for doc in data]
