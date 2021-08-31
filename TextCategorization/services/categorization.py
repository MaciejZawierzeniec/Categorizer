from toolz import pipe

from TextCategorization.constants import MAPPINGS
from TextCategorization.services.ngrams import NgramsService
from TextCategorization.services.text_processing import TextProcessingService
from TextCategorization.services.tokenization import TokenizationService
from TextCategorization.lda_model import LDAModel


class Categorization:

    @classmethod
    def get_categories(cls, content):
        return pipe(content,
                    TokenizationService.tokenize_document,
                    TextProcessingService.remove_stopwords,
                    TextProcessingService.lemmatize,
                    NgramsService.make_bigrams,
                    list,
                    LDAModel.evaluate_topics,
                    cls.map_categories,
                    )

    @classmethod
    def map_categories(cls, data):
        return pipe(data,
                    cls._sort_by_values,
                    cls._sum_scores,
                    cls._get_percentage_values
                    )

    @staticmethod
    def _sort_by_values(data):
        return sorted(data, key=lambda k: k[1], reverse=True)

    @staticmethod
    def _sum_scores(data):
        categories = {}
        for value in data:
            if value[0] in MAPPINGS:
                for val in MAPPINGS[value[0]]:
                    categories.update({val: value[1]})
        return categories

    @staticmethod
    def _get_percentage_values(data):
        percentage_values = {key: str(round(value / sum(data.values()) * 100)) + '%' for key, value in data.items()}
        return ', '.join(['{} {}'.format(k, v) for k, v in percentage_values.items()])
