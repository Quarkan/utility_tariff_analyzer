import sqlite3 as sq


with sq.connect('indications_tariff.db') as sun:
    cur = sun.cursor()

    cur.execute('DROP TABLE IF EXISTS data')
    cur.execute("""CREATE TABLE IF NOT EXISTS data
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    UNIT_OF_MEASUREMENT TEXT,
    age INTEGER,
    name TEXT,
    cost INTEGER

    )
    """)
    #формируем базу данных

    #2014
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 Гкал',2014,'отопление',3393.68)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 м3',2014,'вода',29.56)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за кВт.ч',2014,'Электроэнергия',4.57)")

    #2015
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 Гкал',2015,'отопление',3555.34)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 м3',2015,'вода',30.79)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за кВт.ч',2015,'Электроэнергия',4.76)")

    #2016
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 Гкал',2016,'отопление',3836.18)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 м3',2016,'вода',34.19)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за кВт.ч',2016,'Электроэнергия',5.24)")

    #2017
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 Гкал',2017,'отопление',3967.16)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 м3',2017,'вода',36.02)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за кВт.ч',2017,'Электроэнергия',5.75)")

    #2018
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 Гкал',2018,'отопление',4117.02)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 м3',2018,'вода',39.92)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за кВт.ч',2018,'Электроэнергия',6.09)")

    #2019
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 Гкал',2019,'отопление',4322.4)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 м3',2019,'вода',43.38)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за кВт.ч',2019,'Электроэнергия',4.57)")

    #2020
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 Гкал',2020,'отопление',4450.8)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 м3',2020,'вода',44.13)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за кВт.ч',2020,'Электроэнергия',4.81)")

    #2021
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 Гкал',2021,'отопление',4605.6)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 м3',2021,'вода',45.81)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за кВт.ч',2021,'Электроэнергия',5.02)")

    #2022
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 Гкал',2022,'отопление',4742.4)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 м3',2022,'вода',71.54)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за кВт.ч',2022,'Электроэнергия',7.58)")

    #2023
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 Гкал',2023,'отопление',5924.04)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 м3',2023,'вода',106.03)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за кВт.ч',2023,'Электроэнергия',8.41)")

    #2024
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 Гкал',2024,'отопление',6587.44)")
    cur.execute("INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за 1 м3',2024,'вода',116.56)")
    cur.execute( "INSERT INTO data(UNIT_OF_MEASUREMENT,age,name,cost) VALUES('Руб. за кВт.ч',2024,'Электроэнергия',9.68)")


