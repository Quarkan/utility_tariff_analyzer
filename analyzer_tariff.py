import sqlite3 as sq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import matplotlib.gridspec as gridspec

with sq.connect('indications_tariff.db') as sun:
    cur = sun.cursor()

    # вывод данных в analyzer_tariff
    cur.execute("SELECT age FROM data WHERE name LIKE 'отопление'")
    result_const = cur.fetchall()
    cur.execute("SELECT cost FROM data WHERE name LIKE 'отопление'")
    result_1 = cur.fetchall()
    cur.execute("SELECT cost FROM data WHERE name LIKE 'вода'")
    result_2 = cur.fetchall()
    cur.execute("SELECT cost FROM data WHERE name LIKE 'Электроэнергия'")
    result_3 = cur.fetchall()

    result_list_const = []
    result_list_1 = []
    result_list_2 = []
    result_list_3 = []
    result = []

    #сумма всех комунальных услуг
    for cost in result_1:
        result_list_1.append(cost[0])
    for age in result_const:
        result_list_const.append(age[0])
    for cost in result_2:
        result_list_2.append(cost[0])
    for cost in result_3:
        result_list_3.append(cost[0])
    for i in range(11):
        ress = (result_list_1[i] + result_list_2[i] + result_list_3[i])
        oct_ress = round(ress,2)
        result.append(oct_ress)
#отправляем последние изменения
sun.commit()

f1 = plt.figure(figsize=(7,4))
f1.set_facecolor('#eee')
gs = gridspec.GridSpec(2,3,figure=f1)

ax = f1.add_subplot(gs[1,:])

y = np.array([result[i] for i in range(11)])
x = np.array([result_list_const[i] for i in range(11)])

ax.xaxis.set_major_locator(MaxNLocator(13))

ax.plot(x, y, 'r-o')

for i,v in enumerate(result):
    plt.text(x=x[i],y=v,s=str(v)+'₽',ha='center')

ax.set_title('COST TARIFF IN RUB')
ax.set_ylabel('cost')
ax.set_xlabel('age')
plt.grid()
plt.show()
