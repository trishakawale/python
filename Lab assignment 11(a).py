import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset (you can replace with CSV file)
data = {
    'month': ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    'facecream': [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900],
    'facewash': [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760],
    'toothpaste': [5200,5100,4550,5870,6000,6500,7000,7100,6800,6200,5900,6100],
    'bathingsoap': [9200,6100,9550,8870,9000,8600,8800,8900,9100,9200,9300,9400],
    'shampoo': [1200,2100,3550,1870,1560,1780,1890,1780,2100,2300,2400,1800],
    'moisturizer': [1500,1300,1200,1400,1500,1600,1700,1800,1900,2000,2100,2200]
}

df = pd.DataFrame(data)

# Total profit (sum of all products)
df['total'] = df.iloc[:,1:].sum(axis=1)

# a) Line Plot
plt.plot(df['month'], df['total'])
plt.title("Total Profit per Month")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# b) Multiline Plot
for col in df.columns[1:-1]:
    plt.plot(df['month'], df[col], label=col)

plt.legend()
plt.title("Sales Data of All Products")
plt.show()

# c) Bar Chart (Facecream & Facewash)
x = range(len(df['month']))
plt.bar(x, df['facecream'], width=0.4, label='Facecream')
plt.bar([i+0.4 for i in x], df['facewash'], width=0.4, label='Facewash')
plt.xticks(x, df['month'])
plt.legend()
plt.title("Facecream vs Facewash Sales")
plt.show()

# d) Pie Chart (Yearly Product Sales)
total_sales = df.iloc[:,1:-1].sum()

plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%')
plt.title("Yearly Sales Distribution")
plt.show()
