# Coding : utf-8
# Author : chyh
# Date   : 2021/5/11 15:26


from film_bean import film_bean
from db import db_instance


def open_10():
    db_instance.update_1_to_2()
    db_instance.open_10()


if __name__ == '__main__':
    open_10()
