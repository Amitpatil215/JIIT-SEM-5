import pandas as pd
from matplotlib import pyplot as plt

# Read data
data = pd.read_csv(
    'D:\Work\JIIT\Sem__5\Sem_5\OpenSourceLab\LabTest-1\Sales_Data.csv')

month = data['Month']
Product_A = data['Product A']
Product_B = data['Product B']
Product_C = data['Product C']
Product_D = data['Product D']
Product_E = data['Product E']
Product_F = data['Product F']

m = []
prod_a_list = []
prod_b_list = []
prod_c_list = []
prod_d_list = []
prod_e_list = []
prod_f_list = []

for item1 in month:
    m.append(item1)

for item2 in Product_A:
    prod_a_list.append(item2)

for item2 in Product_B:
    prod_b_list.append(item2)

for item2 in Product_C:
    prod_c_list.append(item2)

for item2 in Product_D:
    prod_d_list.append(item2)

for item2 in Product_E:
    prod_e_list.append(item2)

for item2 in Product_F:
    prod_f_list.append(item2)

fig, ax = plt.subplots()

# Plot Multiline graph
ax.plot(m, prod_a_list, label='Product A')
ax.plot(m, prod_b_list, label='Product B')
ax.plot(m, prod_c_list, label='Product C')
ax.plot(m, prod_d_list, label='Product D')
ax.plot(m, prod_e_list, label='Product E')
ax.plot(m, prod_f_list, label='Product F')

ax.legend()
ax.set_title('Product Sales per Month')
ax.set_xlabel('Month')
ax.set_ylabel('Sales')

plt.show()
