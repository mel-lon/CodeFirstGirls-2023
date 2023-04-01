import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    try:
        """
        YOUR CODE HERE
        """
        pass
    except Exception as e:
        print(f'failed to connect + {str(e)}')



# EXAMPLE 1
def get_all_records():
    try:
        """
        YOUR CODE HERE
        """
        pass
    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        """
        YOUR CODE HERE
        """
        pass


# EXAMPLE 2

def calc_commission(sold_items, commission):
    sales = []

    for item in sold_items:
        sales.append(item[2])

    commission = sum(sales) * (commission / 100)
    return commission


def get_all_records_for_rep(rep_name):
    try:
        """
        YOUR CODE HERE
        """

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        """YOUR CODE HERE"""
        pass

    # print("Commission for {} is £{}".format(rep_name, comp))
    # return rep_name, comp


# EXAMPLE 3 - INSERT INTO TABLE

import datetime as dt

record = {
    'OrderDate': '2020-12-15',
    'Region': 'Central',
    'Rep': 'Johnson',
    'Item': 'post-it-notes',
    'Units': 220,
    'UnitCost': 2.5,
    'Total': 220 * 2.5,
}


def insert_new_record(record):
    try:
        """YOUR CODE HERE"""

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        """YOUR CODE HERE"""

    print("Record added to DB")


def main():
    pass
    # get_all_records()
    # get_all_records_for_rep('Morgan')
    # insert_new_record(record)


if __name__ == '__main__':
    main()
