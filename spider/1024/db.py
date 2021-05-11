# Coding : utf-8
# Author : chyh
# Date   : 2021/3/8 21:01


from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import sqlite3
import webbrowser

from film_bean import film_bean

baseUrl = "https://cl.298x.xyz/"


class db:

    def __init__(self) -> None:
        engine = create_engine('sqlite:///online_links.db?check_same_thread=False', echo=False)
        self.db_session = sessionmaker(bind=engine)
        self.create_table()

    def add_proxy(self, new_film):
        session = self.db_session()
        session.add(new_film)
        result = 0
        try:
            session.commit()
        except Exception as e:
            print(e)
            result = 1
        finally:
            session.close()
        return result

    def create_table(self):
        try:
            conn = self.connect_database()
            cursor = conn.cursor()
            cursor.execute('''
            create table ONLINE_LINKS(
            TITLE varchar(100),
            URL varchar(100),
            POST_DATE date,
            REPLY_COUNT int,
            STATUS int
            );''')
        except sqlite3.OperationalError:
            print('create table failed')
        finally:
            cursor.close()
            conn.close()

    def open_10(self):
        session = self.db_session()
        rows = session.query(film_bean).filter(film_bean.reply_count > 0).filter(film_bean.status == 0).order_by(
            desc(film_bean.reply_count)).limit(10).all()
        for row in rows:
            webbrowser.open(baseUrl + row.url)
            row.status = 1
        session.commit()
        session.close()

    def update_1_to_2(self):
        session = self.db_session()
        rows = session.query(film_bean).filter(film_bean.status == 1).all()
        for row in rows:
            row.status = 2
        session.commit()
        session.close()

    @staticmethod
    def connect_database():
        return sqlite3.connect('online_links.db')


db_instance = db()
