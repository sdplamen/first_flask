from random import choice
from string import ascii_letters, digits, punctuation

class passlib():
    pass_lenght = 10
    @staticmethod
    def gen_pass(type=0, lenght=pass_lenght):
        if not lenght or not isinstance(lenght, int):
            lenght = passlib.pass_lenght
        pass_chars = [ascii_letters, ascii_letters+digits, ascii_letters+digits+punctuation][type]
        ret_pass = str()
        for _ in range(lenght):
            ret_pass += choice(pass_chars)
        return ret_pass, lenght


if __name__ == '__main__':
    pass_obj = passlib()
    print(pass_obj.gen_pass())
