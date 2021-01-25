import pandas as pd

dir = "D:\\bigdata\\学习计划"

'''
for i in range(1, 12):
    data = pd.read_excel(dir + "\\学习计划" + str(i) + ".xlsx")
    print(data)
'''
data1 = pd.read_excel(dir + "\\学习计划" + str(2) + ".xlsx", usecols=[0, 1],skiprows = [0])
data2 = pd.read_excel(dir + "\\学习计划" + str(3) + ".xlsx", usecols=[0, 1],skiprows = [0])
print(data1)
print(data2)
