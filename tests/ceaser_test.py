import unittest

from ceaser import decrypt, encrypt, handleDecrypt, handleEncrypt, get_int_input, get_offset

class ceaser_test(unittest.TestCase):

    #entire alpabet wrap aroung 1, -1, 2, -2
    def test_decrypt_wraparound_at_alphabet_edges(self):
        self.assertEqual(decrypt("a", -1), "b")
        self.assertEqual(decrypt("a", 1), "z")
        self.assertEqual(decrypt("z", -1), "a")
        self.assertEqual(decrypt("z", 1), "y")
        self.assertEqual(decrypt("a", -2), "c")
        self.assertEqual(decrypt("a", 2), "y")
        self.assertEqual(decrypt("z", -2), "b")
        self.assertEqual(decrypt("z", 2), "x")
    
    #uppercase only, lowercase only and mixed case
    def test_decrypt_case_sensitivity(self):
        self.assertEqual(decrypt("abc", -1), "bcd")
        self.assertEqual(decrypt("ABC", -1), "BCD")
        self.assertEqual(decrypt("aBc", -1), "bCd")

    #mixed case and content A b-c!
    def test_decrypt_mixed_case_content(self):
        self.assertEqual(decrypt("A b-c!" -1), "B c-d!")
        self.assertEqual(decrypt("1234", -1), "1234")

    #very large and very large negative offset
    def test_decrypt_large_and_negative_offset(self):
        self.assertEqual(decrypt("abc", 53), "zab")
        self.assertEqual(decrypt("abc", -53), "bcd")

    #empty string and spaces only cypher
    def test_decrypt_empty_string_and_spaces(self):
        self.assertEqual(decrypt("", 5), "")
        self.assertEqual(decrypt("    ", 5), "    ")

    #round trip integrety
    def test_decrypt_round_trip_with_encrypt(self):
        self.assertEqual(decrypt(encrypt("hello", 5), 5), "hello")
        self.assertEqual(decrypt(encrypt("hello", 30), 30), "hello")
        self.assertEqual(decrypt(encrypt("hello", -5), -5), "hello")
        self.assertEqual(decrypt(encrypt("hello", -30), -30), "hello")


    #tests the basic functioinality of the decrypt function
    def test_standard_decrypt(self):
        self.assertEqual(decrypt("bcd", 1), "abc")
        self.assertEqual(decrypt("abc", 0), "abc")
        self.assertEqual(decrypt("abc", 26), "abc")

    #tests the basic functionality of the decrypt function
    def test_standard_encrypt(self):
        self.assertEqual(encrypt("abc", 1), "bcd")
        self.assertEqual(encrypt("abc", 0), "abc")
        self.assertEqual(encrypt("abc", 26), "abc")
        self.assertEqual(encrypt("abc", -1), "zab")
        self.assertEqual(encrypt("abc", 27), "bcd")
        self.assertEqual(encrypt("abc", -27), "zab")
        self.assertEqual(encrypt(decrypt("hello", 5), 5), "hello")


if __name__ == '__main__':
    unittest.main()