import unittest

import magic


class TestMagic(unittest.TestCase):

    def test_has_version(self):
        self.assertTrue(magic.__version__)

    def test_consistent_database(self):
        with magic.Magic() as m:
            self.assertTrue(m.consistent)

    def test_invalid_database(self):
        self.assertRaises(magic.MagicError, magic.Magic,
                paths=['test/magic/_false_'])

    def test_use_after_closed(self):
        with magic.Magic() as m:
            pass
        self.assertRaises(magic.MagicError, m.list, 'setup.py')

    def test_id_filename(self):
        with magic.Magic(paths=['tests/magic/python']) as m:
            id = m.id_filename('setup.py')
            self.assertEqual(id, 'Python script, ASCII text executable')

    def test_id_buffer(self):
        with magic.Magic(paths=['tests/magic/python']) as m:
            id = m.id_buffer('#!/usr/bin/env python\n')
            self.assertEqual(id, 'Python script, ASCII text executable')

    def test_mime_type_file(self):
        with magic.Magic(paths=['tests/magic/python'],
                flags=magic.MAGIC_MIME_TYPE) as m:
            id = m.id_filename('setup.py')
            self.assertEqual(id, 'text/x-python')

    def test_mime_type_desc(self):
        with magic.Magic(paths=['tests/magic/python'],
                flags=magic.MAGIC_MIME_TYPE) as m:
            id = m.id_buffer('#!/usr/bin/env python\n')
            self.assertEqual(id, 'text/x-python')

    def test_mime_encoding_file(self):
        with magic.Magic(paths=['tests/magic/python'],
                flags=magic.MAGIC_MIME_ENCODING) as m:
            id = m.id_filename('setup.py')
            self.assertEqual(id, 'us-ascii')

    def test_mime_encoding_desc(self):
        with magic.Magic(paths=['tests/magic/python'],
                flags=magic.MAGIC_MIME_ENCODING) as m:
            id = m.id_buffer('#!/usr/bin/env python\n')
            self.assertEqual(id, 'us-ascii')


if __name__ == '__main__':
    unittest.main()
