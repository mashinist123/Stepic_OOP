from string import ascii_lowercase, digits


class CardCheck:
    a = 2
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits

    @staticmethod
    def check_card_number(number):
        template = 'XXXX-XXXX-XXXX-XXXX'
        if len(number) != 19:
            return False
        else:
            for x in range(len(template)):
                if template[x] == 'X' and number[x] not in digits:
                    return False
                elif template[x] == '-' and template[x] != number[x]:
                    return False
            else:
                return True
    @classmethod
    def check_name(cls, name):
        return set(x for x in name.replace(' ', '')) <= set(x for x in cls.CHARS_FOR_NAME)



is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV")
print(is_number, is_name)
print(CardCheck())

f = '1234556'
print(type(digits))
print(set(f.replace('5', '')))

print(CardCheck.CHARS_FOR_NAME)