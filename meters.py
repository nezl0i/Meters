import os
import sqlite3
from datetime import datetime
import pandas
import query as qw


def to_real_time(stamp):
    return datetime.fromtimestamp(int(stamp)).strftime("%d.%m.%Y")


def to_stamp_time(realtime):
    return int(datetime.timestamp(datetime.strptime(realtime, "%d.%m.%Y")))


def fill_append(fill: list, i, j, num, val):
    fill.clear()
    fill.append(i)
    fill.append(j)
    fill.append(num)
    fill.append(val) if num != 3 else fill.append(val * 100)
    fill.append(to_stamp_time(datetime.now().strftime("%d.%m.%Y")))


class Meters:
    def __init__(self):
        self.drop_devices = "DROP TABLE IF EXISTS devices;"
        self.drop_meters = "DROP TABLE IF EXISTS meters;"
        self.drop_filial = "DROP TABLE IF EXISTS filial;"
        self.drop_parameter = "DROP TABLE IF EXISTS parameter;"

        self.insert_device = "INSERT INTO devices(meter_name) VALUES(?);"
        self.insert_filial = "INSERT INTO filial(filial_firstname, filial_lastname) VALUES(?,?);"
        self.insert_parameter = "INSERT INTO parameter(name) VALUES(?);"
        self.insert_meters = "INSERT INTO meters(filial_id, device_id, parameter_id, value, date) VALUES(?,?,?,?,?);"

        self.select_all = f"SELECT filial_id, device_id, parameter_id, value, date " \
                          f"FROM meters " \
                          f"WHERE parameter_id != 3 AND date={to_stamp_time(datetime.now().strftime('%d.%m.%Y'))}"

        self.db_name = None
        self.conn = None
        self.cur = None

    def set_db_name(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        return

    def db_create(self):
        if self.db_name is not None:
            self.cur.execute(self.drop_devices)
            self.cur.execute(self.drop_filial)
            self.cur.execute(self.drop_meters)
            self.cur.execute(self.drop_parameter)

            self.cur.execute(qw.table['table_device'])
            self.cur.execute(qw.table['table_filial'])
            self.cur.execute(qw.table['table_parameter'])
            self.cur.execute(qw.table['table_meters'])

            self.cur.executemany(self.insert_device, qw.devices)
            self.cur.executemany(self.insert_filial, qw.filial)
            self.cur.executemany(self.insert_parameter, qw.parameter)

            self.conn.commit()
            print('Database "meters" successfully create! ')
        else:
            print('No database name.. Create database!')
        return

    def parse_excel(self, path: str, insert=False):

        files = os.listdir(path)
        tmp_list = {}
        fill, total = [], []
        files = [i for i in files]
        _skip = 47
        for k in range(11):
            _excel = pandas.read_excel(
                f'{path}/{files[k]}',
                engine='openpyxl',
                sheet_name='Разбивка по филиалам',
                header=None,
                nrows=1,
                skiprows=_skip,
                usecols='E:AK'
            )
            # columns = _excel.columns.tolist()
            values = _excel.values.tolist()
            tmp_list[k + 1] = values[0]
            _skip += 1
        for i in range(1, 12):
            fill.clear()
            start = 0
            end = 3
            for j in range(1, 12):
                fill.clear()
                for num, val in enumerate(tmp_list[i][start:end], 1):
                    fill_append(fill, i, j, num, val)
                    total.append(tuple(fill))
                start += 3
                end += 3
        print(f'{len(files)} files in path "{path}" parse successfully!')
        print(f'Find files {files}')

        if insert:
            if self.db_name is not None:
                self.cur.executemany(self.insert_meters, total)
                self.conn.commit()
                print(f'Inserting values in {self.db_name} successfully!')
            else:
                print("No database name..Create database!")
        return total

    def all(self):
        if self.db_name is not None:
            self.cur.execute(self.select_all)
            # self.conn.commit()
            answer = self.cur.fetchall()
        else:
            print("No database name..Create database!")
            return
        return answer









    def sql_qw(self, device=None, parameter=None, filial_firstname=None, filial_lastname=None, date=None):

        if filial_lastname is not None:
            last_filial = qw.f_lastname[filial_lastname]
        else:
            last_filial = 12

        if device is not None:
            dev = qw.d_dict[device]
        else:
            dev = qw.d_dict['ИТОГО']

        if parameter is not None:
            param = qw.p_dict[parameter]
        else:
            param = qw.p_dict['Всего']

        if date is not None:
            from_date = date
        else:
            from_date = '17.12.2021'

        if filial_firstname is not None:
            first_filial = qw.f_firstname[filial_firstname]

            query = f'SELECT vf.filial_firstname, ' \
                    f'm.value ' \
                    f'FROM meters m ' \
                    f'LEFT JOIN filial vf ' \
                    f'ON m.filial_id = vf.filial_id ' \
                    f'WHERE m.device_id = {dev} ' \
                    f'AND m.date = "{from_date}" ' \
                    f'AND m.parameter_id = {param} ' \
                    f'AND m.filial_id = {first_filial} ' \
                    f'ORDER by value DESC'
        else:
            first_filial = 12
            last_filial = 12

            query = f'SELECT vf.filial_firstname, ' \
                    f'm.value ' \
                    f'FROM meters m ' \
                    f'LEFT JOIN filial vf ' \
                    f'ON m.filial_id = vf.filial_id ' \
                    f'WHERE m.device_id = {dev} ' \
                    f'AND m.date = "{from_date}" ' \
                    f'AND m.parameter_id = {param} ' \
                    f'ORDER by value DESC'

        self.cur.execute(query)

        # self.cur.execute("""
        # SELECT vf.filial_firstname as Филиал,
        # m.value as Всего
        # FROM meters m
        # LEFT JOIN filial vf
        # ON m.filial_id = vf.filial_id
        # WHERE m.device_id = 11 AND m.date = "17.12.2021"
        # AND m.parameter_id = 1
        # ORDER by value DESC
        # """)
        print(f'Отчет по параметрам:\n'
              f'Филиал: {[key for key, val in qw.f_firstname.items() if val == first_filial][0]} '
              f'({[key for key, val in qw.f_lastname.items() if val == last_filial][0]}) \n'
              f'Тип ПУ: {[key for key, val in qw.d_dict.items() if val == dev][0]}\n'
              f'Показатель: {[key for key, val in qw.p_dict.items() if val == param][0]}\n')

        answer = self.cur.fetchall()
        count = 0
        for row in answer:
            count += row[1]
            print("{:18}{:10}".format(row[0], row[1]))
        print(f'ИТОГО: {count}')

    def sql_qw2(self, filial_firstname):
        self.cur.execute(f'SELECT vf.filial_firstname as Филиал, '
                         f'm.value as Всего '
                         f'FROM meters m '
                         f'LEFT JOIN filial vf '
                         f'ON vf.filial_firstname = "{filial_firstname}" '
                         f'WHERE m.device_id = 11 '
                         f'AND m.date = "17.12.2021"AND '
                         f'm.parameter_id = 1 '
                         f'ORDER by value DESC')
        answer = self.cur.fetchall()
        count = 0
        for row in answer:
            count += row[1]

            print("{:18}{:10}".format(row[0], row[1]))
        print(f'ИТОГО: {count}')
