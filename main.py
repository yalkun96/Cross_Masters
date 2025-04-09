import attribute
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.pyplot import bar_label
from functions import *

df = pd.read_excel('/Users/zzzzzz/PycharmProjects/Cross_Masters/Data.xlsx')


#first task
#group all products by quantity sold
sum_of_all_product_sales = df.groupby('Product name')['Quantity'].sum()
#find the highest turnover
highest_tunrover = sum_of_all_product_sales.max()
#check what item has the highest turnover
for item, price in sum_of_all_product_sales.items():
    if price == highest_tunrover:
        print(f"""Most sold: {item}  Quanity: {price}""")


#group products by quantity for every month
grouped = df.groupby(['Date', 'Product name'])['Quantity'].sum().unstack(fill_value=0)
#make a plot
fig, ax = plt.subplots(layout='constrained')
ax = grouped.plot(kind='bar', figsize=(15,5), ax=ax)
ax.bar('Product name', "Q")
ax.set_ylabel('Quantity')
ax.set_title('Monthly Turnover by Product')
ax.legend(title='Product Name', loc='upper left', bbox_to_anchor=(1.0, 1.0))
plt.xticks(rotation=45)
plt.show()


#second task
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Weekday'] = df['Date'].dt.day_name()

highest_day_sales = df.groupby('Weekday')['Quantity'].sum()
highest_item = highest_day_sales.max()
#checking the day of the week where sales a highest
for day, quantity in highest_day_sales.items():
    if quantity == highest_item:
        print(f"""Day: {day}  Quanity: {quantity}""")

#thrid task
df["Typ"] = df['Product name'].apply(check_type)

type_and_day = df.groupby(['Typ', 'Weekday'] )['Quantity'].sum()

max_quantity = 0
for (type, day), quantity in type_and_day.items():
    if quantity > max_quantity:
        max_quantity = quantity
    print((type, day), max_quantity)


#fourth task
df['Period'] = df['Date'].apply(lambda x: 'Before' if x < pd.to_datetime('2022-03-18') else 'After')

summary = df.groupby('Period')['Quantity'].agg(['sum', 'mean', 'count']).rename(columns={
    'sum': 'Total Sold',
    'mean': 'Average per Day',
    'count': 'Number of Sales Records'
})
print(summary)

