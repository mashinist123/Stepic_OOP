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
        if name.count(' ') > 1:
            return False
        return set(x for x in name.replace(' ', '')) <= set(x for x in cls.CHARS_FOR_NAME)