from django.test import TestCase

from TextCategorization.services.text_processing import TextProcessingService


class TextProcessingServiceTestCase(TestCase):

    def test_remove_stopwords(self):
        stopwords_removed = TextProcessingService.remove_stopwords([['the', 'a', 'notastopword', 'word']])
        self.assertEqual([['notastopword', 'word']], stopwords_removed)
        self.assertNotEqual([['word']], stopwords_removed)
