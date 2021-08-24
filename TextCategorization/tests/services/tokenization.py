from django.test import TestCase

from TextCategorization.services.tokenization import TokenizationService


class TokenizationServiceTestCase(TestCase):

    def test_tokenize_document(self):
        text = TokenizationService.tokenize_document(['remove the :)'])
        self.assertEqual([['remove', 'the']], text)
        self.assertNotEqual(['remove', 'the'], text)
