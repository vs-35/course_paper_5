# -*- coding: utf-8 -*-
from config import config
from utils import get_employers_data, get_vacancies_data
from creator import create_database, save_employers_to_db, save_vacancies_to_db
from DBmanager import DBManager


def main():
    params = config()

    create_database('hh', params)
    employers = get_employers_data()
    vacancies = get_vacancies_data()

    save_employers_to_db(employers, 'hh', params)
    save_vacancies_to_db(vacancies, 'hh', params)

    db_manager = DBManager('hh', params)
    db_manager.get_companies_and_vacancies_count()
    db_manager.get_avg_salary()
    db_manager.get_all_vacancies()
    db_manager.get_vacancies_with_higher_salary()
    db_manager.get_vacancies_with_keyword("водитель")


if __name__ == '__main__':
    main()