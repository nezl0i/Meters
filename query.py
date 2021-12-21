table = {
    'table_device': """ 
                        CREATE TABLE IF NOT EXISTS devices(
                        device_id INTEGER PRIMARY KEY,
                        meter_name TEXT);
                    """,
    'table_filial': """
                        CREATE TABLE IF NOT EXISTS filial(
                        filial_id INTEGER PRIMARY KEY,
                        filial_firstname TEXT,
                        filial_lastname TEXT);
                    """,
    'table_parameter': """
                        CREATE TABLE IF NOT EXISTS parameter(
                        parameter_id INTEGER PRIMARY KEY,
                        name TEXT);
                       """,
    'table_meters': """
                        CREATE TABLE IF NOT EXISTS meters(
                        meter_id INTEGER PRIMARY KEY,
                        filial_id INT,
                        device_id INT,
                        parameter_id INT,
                        value INT,
                        date INT);
                    """
}

parameter = [('Всего',), ('Опрашивается',), ('Процент',)]

p_dict = {'Всего': 1, 'Опрашивается': 2, 'Процент': 3}

devices = [('Матрица',), ('Матрица SFSK',), ('Матрица FSK',), ('РиМ',), ('МИР',),
           ('Энергомера',), ('Квант,Миртек',), ('СЭТ,ПСЧ',), ('Меркурий',), ('Альфа',), ('ИТОГО',)]

d_dict = {'Матрица': 1, 'Матрица SFSK': 2, 'Матрица FSK': 3, 'РиМ': 4, 'МИР': 5,
          'Энергомера': 6, 'Квант,Миртек': 7, 'СЭТ,ПСЧ': 8, 'Меркурий': 9, 'Альфа': 10, 'ИТОГО': 11}

filial = [('Адыгейские ЭС', 'АдЭС'), ('Армавирские ЭС', 'АрмЭС'), ('Краснодарские ЭС', 'КрЭС'),
          ('Лабинские ЭС', 'ЛабЭС'), ('Ленинградские ЭС', 'ЛенЭС'), ('Славянские ЭС', 'СлЭС'),
          ('Сочинские ЭС', 'СочЭС'), ('Тимашевские ЭС', 'ТимЭС'), ('Тихорецкие ЭС', 'ТихЭС'),
          ('Усть-Лабинские ЭС', 'УлЭС'), ('Юго-Западные ЭС', 'ЮЗЭС'), ('Все', 'Все')]

f_firstname = {'Адыгейские ЭС': 1, 'Армавирские ЭС': 2, 'Краснодарские ЭС': 3,
               'Лабинские ЭС': 4, 'Ленинградские ЭС': 5, 'Славянские ЭС': 6,
               'Сочинские ЭС': 7, 'Тимашевские ЭС': 8, 'Тихорецкие ЭС': 9,
               'Усть-Лабинские ЭС': 10, 'Юго-Западные ЭС': 11, 'Все': 12}

f_lastname = {'АдЭС': 1, 'АрмЭС': 2, 'КЭС': 3,
              'ЛабЭС': 4, 'ЛенЭС': 5, 'СлЭС': 6,
              'СочЭС': 7, 'ТимЭС': 8, 'ТихЭС': 9,
              'УлЭС': 10, 'ЮЭС': 11, 'Все': 12}

excel_column = {
    1: ['C5', 'D5', 'F5', 'G5', 'I5', 'J5', 'L5', 'M5', 'O5', 'P5',
        'R5', 'S5', 'U5', 'V5', 'X5', 'Y5', 'AA5', 'AB5', 'AD5', 'AE5'],
    2: ['C5', 'D5', 'F5', 'G5', 'I5', 'J5', 'L5', 'M5', 'O5', 'P5',
        'R5', 'S5', 'U5', 'V5', 'X5', 'Y5', 'AA5', 'AB5', 'AD5', 'AE5'],
    3: ['C5', 'D5', 'F5', 'G5', 'I5', 'J5', 'L5', 'M5', 'O5', 'P5',
        'R5', 'S5', 'U5', 'V5', 'X5', 'Y5', 'AA5', 'AB5', 'AD5', 'AE5'],
    4: ['C5', 'D5', 'F5', 'G5', 'I5', 'J5', 'L5', 'M5', 'O5', 'P5',
        'R5', 'S5', 'U5', 'V5', 'X5', 'Y5', 'AA5', 'AB5', 'AD5', 'AE5'],
    5: ['C5', 'D5', 'F5', 'G5', 'I5', 'J5', 'L5', 'M5', 'O5', 'P5',
        'R5', 'S5', 'U5', 'V5', 'X5', 'Y5', 'AA5', 'AB5', 'AD5', 'AE5'],
    6: ['C6', 'D6', 'F6', 'G6', 'I6', 'J6', 'L6', 'M6', 'O6', 'P6',
        'R6', 'S6', 'U6', 'V6', 'X6', 'Y6', 'AA6', 'AB6', 'AD6', 'AE6'],
    7: ['C7', 'D7', 'F7', 'G7', 'I7', 'J7', 'L7', 'M7', 'O7', 'P7',
        'R7', 'S7', 'U7', 'V7', 'X7', 'Y7', 'AA7', 'AB7', 'AD7', 'AE7'],
    8: ['C8', 'D8', 'F8', 'G8', 'I8', 'J8', 'L8', 'M8', 'O8', 'P8',
        'R8', 'S8', 'U8', 'V8', 'X8', 'Y8', 'AA8', 'AB8', 'AD8', 'AE8'],
    9: ['C9', 'D9', 'F9', 'G9', 'I9', 'J9', 'L9', 'M9', 'O9', 'P9',
        'R9', 'S9', 'U9', 'V9', 'X9', 'Y9', 'AA9', 'AB9', 'AD9', 'AE9'],
    10: ['C10', 'D10', 'F10', 'G10', 'I10', 'J10', 'L10', 'M10', 'O10', 'P10',
         'R10', 'S10', 'U10', 'V10', 'X10', 'Y10', 'AA10', 'AB10', 'AD10', 'AE10'],
    11: ['C11', 'D11', 'F11', 'G11', 'I11', 'J11', 'L11', 'M11', 'O11', 'P11',
         'R11', 'S11', 'U11', 'V11', 'X11', 'Y11', 'AA11', 'AB11', 'AD11', 'AE11'],
    12: ['C12', 'D12', 'F12', 'G12', 'I12', 'J12', 'L12', 'M12', 'O12', 'P12',
         'R12', 'S12', 'U12', 'V12', 'X12', 'Y12', 'AA12', 'AB12', 'AD12', 'AE12'],
}

for key, value in excel_column.items():
    for i in value:
        print(i)
