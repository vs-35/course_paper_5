# -*- coding: utf-8 -*-
import psycopg2


def create_database(database_name: str, params: dict):
    """Создание базы данных и таблиц для сохранения данных."""

    conn = psycopg2.connect(dbname='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    cur.close()
    conn.close()

    conn = psycopg2.connect(dbname=database_name, **params)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE employers (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            )
        """)

    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE vacancies (
                name VARCHAR(255) NOT NULL,
                employer VARCHAR NOT NULL,
                salary INT,
                employer_id SERIAL REFERENCES employers(id),
                url TEXT 
            )
        """)

    conn.commit()
    conn.close()


def save_employers_to_db(data, database_name: str, params: dict):
    """Сохранение данных в базу данных."""

    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        for employer in data:
            query = "INSERT INTO employers (id, name) VALUES (%s, %s) ON CONFLICT DO NOTHING"
            cur.execute(query, (employer))

    conn.commit()
    conn.close()


def save_vacancies_to_db(data, database_name: str, params: dict):
    """Сохранение данных в базу данных."""

    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        for vacancy in data:
            query = "INSERT INTO vacancies (name, employer, salary, employer_id, url) VALUES (%s, %s, %s, %s, %s)"
            cur.execute(query, (vacancy))

    conn.commit()
    conn.close()