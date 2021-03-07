class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        return self.min_length <= len(name)

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    def validate(self, email):
        user_name, after_at = email.split("@")
        user_mail, user_domain = after_at.split(".")
        return self.__validate_name(user_name) and self.__validate_domain(user_domain) and self.__validate_mail(user_mail)


import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev.min_length, 5)
        self.assertEqual(ev.mails, ["me"])
        self.assertEqual(ev.domains, ["you", "he"])

    def test_private_validate_name(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__validate_name("abc"), False)
        self.assertEqual(ev._EmailValidator__validate_name("abcdef"), True)

    def test_private_validate_mail(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__validate_mail("me"), True)
        self.assertEqual(ev._EmailValidator__validate_mail("you"), False)

    def test_private_validate_domain(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev._EmailValidator__validate_domain("he"), True)
        self.assertEqual(ev._EmailValidator__validate_domain("she"), False)

    def test_validate(self):
        ev = EmailValidator(5, ["me"], ["you", "he"])
        self.assertEqual(ev.validate("itsme@me.you"), True)
        self.assertEqual(ev.validate("me@me.you"), False)
        self.assertEqual(ev.validate("itsme@me.she"), False)
        self.assertEqual(ev.validate("itsme@you.he"), False)


if __name__ == "__main__":
    unittest.main()