from meters import Meters


m = Meters(db_name="meters.db", path='report', db_create=False)
# m.set_db_name("meters.db")
# m.db_create()
# m.parse_excel(insert=True)
print(m.all())
# m.sql_qw2("Славянские ЭС")
# m.sql_qw(filial_firstname='Славянские ЭС', device='МИР', parameter='Процент', date='17.12.2021')
