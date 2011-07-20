import unittest

class TestMagic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        import magic
        cls.magic = magic

    def test_desc_file(self):
        m = self.magic.Magic()
        id = m.desc_file(b'README.rst')
        self.assertEqual(id, b'ASCII English text')

    def test_desc_buffer(self):
        m = self.magic.Magic()
        id = m.desc_buffer(b'ipsum lorem\n')
        self.assertEqual(id, b'ASCII text')

    def test_mime_file(self):
        m = self.magic.Magic(flags=self.magic.MAGIC_MIME_TYPE)
        id = m.desc_file(b'README.rst')
        self.assertEqual(id, b'text/plain')

if __name__ == '__main__':
    unittest.main()
