import unittest
# import vim_ubuntu_pastebin as sut
from .. import vim_ubuntu_pastebin as sut


class VimUbuntuPastebinTests(unittest.TestCase):

    def test_create_buffer_with_total_returns_properly_formated_list(self):
        """ we can treat vim text as buffer list"""
        buffer_contents = ['25', '25', '25']
        expected_results = ['25', '25', '25', '==========', 'Total: 75']
        acutal_result = sut.create_buffer_with_total(buffer_contents)
        self.assertEqual(expected_results, acutal_result)

    def test_create_buffer_with_total_returns_properly_formated_list_and_strings(self):
        """ we can treat vim text as buffer list"""
        buffer_contents = ['Beff: 25', 'Roast: 25', 'Steak: 25']
        expected_results = ['Beff: 25', 'Roast: 25', 'Steak: 25', '==========', 'Total: 75']
        acutal_result = sut.create_buffer_with_total(buffer_contents)
        self.assertEqual(expected_results, acutal_result)
