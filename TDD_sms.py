
import unittest
import sms

class TestGlobalFunctions(unittest.TestCase):

    def setUp(self):
        with self.assertRaises(TypeError):sms.text()

    def testsms_send(self):
        SMS = sms.text(254711835117, "Hi Everyone")
        print
        self.assertEqual(SMS[0]['status'], "Success", msg="The function should return the word 'Success' after successfully sending a text")


    def testtext_send_to_wrong_number(self):
        SMS = sms.text(123456, "Hi Everyone")
        self.assertEqual(SMS[0]['status'], "Invalid Phone Number", msg="The function should return the number if it is not divisible by 3 or 5")

if __name__ == '__main__':
    unittest.main()
