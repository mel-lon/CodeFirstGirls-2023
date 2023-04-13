import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    try:
        # connection is stored in a variable
        cnx = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            auth_plugin='mysql_native_password', # sets the authorisation we'll use, authenitcates it on mysql
            database=db_name
        )
        return cnx
        pass
    except Exception as e:
        print(f'failed to connect + {str(e)}')

# _connect_to_db('tests')


# EXAMPLE 1
def get_all_records():
    try:
        db_name = 'tests'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to DB: {db_name}')
# set up or connection in the DB

        query = """SELECT * FROM abcreport"""
        # use the cursor to execute the query
        cur.execute(query)
        result = cur.fetchall()
# set up a query and ran it through the cursor
        for i in result:
            print(i)
# printed the results
        cur.close() # must close the query
# closed the cursor

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")
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
        db_name = 'tests'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to DB: {db_name}')

        query = f"""SELECT Item, Units, Total FROM abcreport WHERE Rep = '{rep_name}'; """
        cur.execute(query)
        result = cur.fetchall()

        for i in result:
            print(i)

        cur.close()
        comp = round(calc_commission(result, commission=10), 2)
        # rounding to 2 dep when calculating commission


    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print('DB Connection is closed')
        pass

    # print("Commission for {} is £{}".format(rep_name, comp))
    # return rep_name, comp


# EXAMPLE 3 - INSERT INTO TABLE

import datetime as dt

record = {
    'OrderDate': '2020-12-15',
    'Region': 'Central',
    'Rep': 'hi',
    'Item': 'post-it-notes',
    'Units': 220,
    'UnitCost': 2.5,
    'Total': 220 * 2.5,
}


def insert_new_record(record):
    try:
        db_name = 'tests'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to DB:{db_name}')

        query = """INSERT INTO abcreport ({}) VALUES ('{}', '{}', '{}', '{}', {}, {}, {})""".format(
            ', '.join(record.keys()),
            record['OrderDate'],
            record['Region'],
            record['Rep'],
            record['Item'],
            record['Units'],
            record['UnitCost'],
            record['Total'],
        )

        cur.execute(query)
        #need to use DB connection to commmit the changes- like the transactions

        db_connection.commit()
        cur.close()



    # connects the variables into one string in the record, separated by a comma and a string
    # for the values,


    except Exception as e:
        print(f'Error raised - {str(e)}')
        raise DbConnectionError("Failed to read data from DB")
    # how to specifically see what the error is


    finally:
        if db_connection:
            db_connection.close()
            print('DB connection is closed')

    print("Record added to DB")



def update_record(col, new_value, filter_column, filter_value):
    try:
        db_name = 'tests'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to DB: {db_name}')

        # query = """
        #         UPDATE abcreport
        #         SET Item = 'Pencils'
        #         WHERE Rep = 'Fatma'
        # """
# static, hard coded new values, so how can i make it dynamic?

        query = f"""
                UPDATE abcreport
                SET {col} = '{new_value}'
                WHERE {filter_column} = '{filter_value}'
        """
        cur.execute(query)
        db_connection.commit()
        cur.close()
        print('values added')



    except Exception as e:
        print(f"Error raised = {str(e)}")
        raise DbConnectionError('Failed to read from DB')

    finally:
        if db_connection:
            db_connection.close()
            print('DB connection is closed')










def main():
    pass
    # get_all_records()
    # get_all_records_for_rep('Morgan')
    # insert_new_record(record)
    update_record(col='Item', new_value='Pencils', filter_column='Rep', filter_value='Johnson')


if __name__ == '__main__':
    main()
