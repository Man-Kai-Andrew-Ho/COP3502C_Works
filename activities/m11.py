from unittest import TestCase

from functions import *


class TestPrime(TestCase):

    def test_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(13))


    def test_non_prime(self):
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(0))


class TestRemoveVowels(TestCase):
    def test_remove_vowels(self):
        self.assertEqual(remove_vowels('hello world'),"hll wrld")
        self.assertEqual(remove_vowels('Test'),"Tst")
        self.assertEqual(remove_vowels('aeiou'),"")
        self.assertEqual(remove_vowels(''),"")
        self.assertEqual(remove_vowels('AEIOU'), "")
        self.assertEqual(remove_vowels('qwrty'),"qwrty")