import unittest
from stringutils import reverse


class TestStringutils(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse('hello world'), 'dlrow olleh')
        self.assertEqual(reverse(''), '')
        self.assertEqual(reverse('中文', '文中'))
