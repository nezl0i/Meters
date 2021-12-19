from meters import Meters


m = Meters()
m.set_db_name("meters.db")
# m.db_create()
# m.parse_excel(path='report', insert=True)
print(m.all())
# m.sql_qw2("Славянские ЭС")
# m.sql_qw(filial_firstname='Славянские ЭС', device='МИР', parameter='Процент', date='17.12.2021')
