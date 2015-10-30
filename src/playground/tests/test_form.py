import unittest

from playground import form


class FormTest(unittest.TestCase):
    def test_form(self):
        frm = form.ListPage(None, None)
        frm.handleDelete(frm, None)

        self.assertEqual(frm.status, u'Stuff deleted.')
