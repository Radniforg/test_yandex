import unittest
import requests
import example

class API_test(unittest.TestCase):

    def setUp(self):
        self.api = example.API_KEY
        self.url = example.URL
        self.basic_pairs_eng = [('привет', 'hi'), ('Прощай', 'Goodbye'),
                            ('Не забудьте поесть пока проверяете работы студентов',
                             "Don't forget to eat while you are checking the work of students"),
                            ('Приятного вам дня', 'Have a nice day')]


    def test_translation_ru_eng(self):
        for pair in self.basic_pairs_eng:
            self.assertEqual(pair[1], example.translate_it(pair[0], 'en'))

    def test_connection(self):
        params = {
            'key': self.api,
            'text': 'текст',
            'lang': 'ru-{}'.format('en'),
        }
        response = requests.get(self.url, params=params)
        self.assertIn('Response [200]', str(response))

    def test_negative_translation(self):
        self.assertNotEqual('salary', example.translate_it('ветка', 'en'))

    def test_negative_format(self):
        self.assertRaises(KeyError, example.translate_it, 'ветка', 'ре')

    def test_negative_nothing_to_translate(self):
        self.assertRaises(KeyError, example.translate_it, '', 'en')

