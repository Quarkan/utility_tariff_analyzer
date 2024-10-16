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

ax = f1.add_subplot(gs[1,0:2])
ax1 = f1.add_subplot(gs[0,0:2])
ax2 = f1.add_subplot(gs[0,2])
ax3 = f1.add_subplot((gs[1,2]))

#Основной график
y = np.array([result[i] for i in range(11)])
x = np.array([result_list_const[i] for i in range(11)])

#отопление
y1 = np.array([result_list_1[i] for i in range(11)])
x1 = np.array([result_list_const[i] for i in range(11)])

#вода
y_water = np.array([result_list_2[i] for i in range(11)])
x2 = np.array([result_list_const[i] for i in range(11)])

#электричество
y_electricity= np.array([result_list_3[i] for i in range(11)])
x3 = np.array([result_list_const[i] for i in range(11)])

#круговая диограмма
vals = [718127,719646,712619,710567,707408,702831,699429,684709,667956,667956,667956]
labels = [2014,2015,2016,2017,2018,2019,2020,2021,2022,2023,2024]

ax.xaxis.set_major_locator(MaxNLocator(13))
ax1.xaxis.set_major_locator(MaxNLocator(13))
ax2.xaxis.set_major_locator(MaxNLocator(13))

ax.plot(x, y, 'r-o')
ax1.bar(x1,y1,color='b',label='heating')
ax1.bar(x2,y_water,color='r',width=0.5,label='water')
ax2.bar(x3,y_electricity,color='y')
ax3.pie(vals,labels=labels,autopct='%1.1f%%')
ax3.axis('equal')

for i,v in enumerate(result):
    ax.text(x=x[i],y=v,s=str(v)+'₽',ha='center')
for i,v in enumerate(result_list_1):
    ax1.text(x=x[i], y=v, s=str(v) + '₽', ha='center')
for i,v in enumerate(result_list_2):
    ax1.text(x=x[i], y=v, s=str(v) + '₽', ha='center')
for i,v in enumerate(result_list_3):
    ax2.text(x=x[i], y=v, s=str(v) + '₽', ha='center')

ax.set_title('COST TARIFF UTILITY IN RUB')
ax1.set_title('COST TARIFF WATER AND HEATING')
ax2.set_title('COST TARIFF ELECTRICITY')
ax3.set_title('POPULATION')

ax.set_ylabel('cost')
ax1.set_ylabel('cost')
ax2.set_ylabel('cost')
ax.set_xlabel('age')

ax1.legend()
plt.show()
