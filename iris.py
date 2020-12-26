import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("Iris_1.csv")
df1=df.shape
print(df1)
df2=df.isnull()
print(df2)
df3=df.isnull().sum()
print(df3)
df4=df.describe()
print(df4)
df5=df.dropna()
print(df5)
df.to_excel("my1.xlsx")

df.to_html("my1.html")

df.to_json("my1.json")


#SepalLengthCm Vs Species (line graph).
# plt.plot(df["SepalLengthCm"], df["Species"])
# plt.title("line Graph ")
# plt.xlabel("SepalLengthCm")
# plt.ylabel("Species")
# plt.show()

#SepalLengthCm Vs Species (bar graph).
# plt.bar(df["SepalLengthCm"], df["Species"])
# plt.title("bar Graph ")
# plt.xlabel("SepalLengthCm")
# plt.ylabel("Species")
# plt.show()

#SepalLengthCm Vs Species (scatter graph).
# plt.scatter(df["SepalLengthCm"], df["Species"])
# plt.title("scatter Graph ")
# plt.xlabel("SepalLengthCm")
# plt.ylabel("Species")
# plt.show()

#SepalWidthCm Vs Species (line graph).
# plt.plot(df["SepalWidthCm"], df["Species"])
# plt.title("line Graph ")
# plt.xlabel("SepalWidthCm")
# plt.ylabel("Species")
# plt.show()

#SepalWidthCm Vs Species (bar graph).
# plt.bar(df["SepalWidthCm"], df["Species"])
# plt.title("bar Graph ")
# plt.xlabel("SepalWidthCm")
# plt.ylabel("Species")
# plt.show()

#SepalWidthCm Vs Species (scatter graph).
# plt.scatter(df["SepalWidthCm"], df["Species"])
# plt.title("scatter Graph ")
# plt.xlabel("SepalWidthCm")
# plt.ylabel("Species")
# plt.show()

#PetalLengthCm Vs Species (line graph).
# plt.plot(df["PetalLengthCm"], df["Species"])
# plt.title("line Graph ")
# plt.xlabel("PetalLengthCm")
# plt.ylabel("Species")
# plt.show()

#PetalLengthCm Vs Species (bar graph).
# plt.bar(df["PetalLengthCm"], df["Species"])
# plt.title("bar Graph ")
# plt.xlabel("PetalLengthCm")
# plt.ylabel("Species")
# plt.show()

# PetalLengthCm Vs Species (scatter graph).
# plt.scatter(df["PetalLengthCm"], df["Species"])
# plt.title("scatter Graph ")
# plt.xlabel("PetalLengthCm")
# plt.ylabel("Species")
# plt.show()

#PetalWidthCm Vs Species (bar graph).
# plt.bar(df["PetalWidthCm"], df["Species"])
# plt.title("bar Graph ")
# plt.xlabel("PetalWidthCm")
# plt.ylabel("Species")
# plt.show()

#PetalWidthCm Vs Species (bar graph).
# plt.scatter(df["PetalWidthCm"], df["Species"])
# plt.title("scatter Graph ")
# plt.xlabel("PetalWidthCm")
# plt.ylabel("Species")
# plt.show()

#SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm Vs Species (line graph).
# plt.plot(df["SepalLengthCm"], df["Species"] ,color='red',label='line1')
# plt.plot(df["SepalWidthCm"], df["Species"],color='blue',label='line2')
# plt.plot(df["PetalLengthCm"], df["Species"],color='yellow',label='line3')
# plt.plot(df["PetalWidthCm"], df["Species"],color='black',label='line4')
# plt.title("line Graph ")
# plt.xlabel("SepalLengthCm , SepalWidthCm , PetalLengthCm , PetalWidthCm")
# plt.ylabel("Species")
# plt.show()

#SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm Vs Species (bar graph).
# plt.bar(df["SepalLengthCm"], df["Species"] ,color='red',label='line1')
# plt.bar(df["SepalWidthCm"], df["Species"],color='blue',label='line2')
# plt.bar(df["PetalLengthCm"], df["Species"],color='yellow',label='line3')
# plt.bar(df["PetalWidthCm"], df["Species"],color='black',label='line4')
# plt.title("bar Graph ")
# plt.xlabel("SepalLengthCm , SepalWidthCm , PetalLengthCm , PetalWidthCm")
# plt.ylabel("Species")
# plt.show()

#SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm Vs Species (scatter graph).
# plt.scatter(df["SepalLengthCm"], df["Species"] ,color='red',label='line1')
# plt.scatter(df["SepalWidthCm"], df["Species"],color='blue',label='line2')
# plt.scatter(df["PetalLengthCm"], df["Species"],color='yellow',label='line3')
# plt.scatter(df["PetalWidthCm"], df["Species"],color='black',label='line4')
# plt.title("scatter Graph ")
# plt.xlabel("SepalLengthCm , SepalWidthCm , PetalLengthCm , PetalWidthCm")
# plt.ylabel("Species")
# plt.show()


print("--------------------------------------------------")

#print(df)
# print("-------------------------X DATA------------------------------")
# x=df.iloc[0:, 1:5]
# print(x)
# print("-------------------------Y DATA-------------------------------")
# y=df.iloc[0:, 5]
# print(y)
# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=20)
# print("-----------------------x_train-------------------")
# print(x_train)
# print(x_train.shape)
# print("-----------------------x_test-------------------")
# print(x_test)
# print(x_test.shape)
# print("-----------------------y_train-------------------")
# print(y_train)
# print(y_train.shape)
# print("-----------------------y_test-------------------")
# print(y_test)
# print(y_test.shape)
import seaborn as sns
plt.subplot(2,2,1)
sns.distplot(df.SepalLengthCm)
plt.subplot(2,2,2)
sns.distplot(df.SepalWidthCm)
plt.subplot(2,2,3)
sns.distplot(df.PetalLengthCm)
plt.subplot(2,2,4)
sns.distplot(df.PetalWidthCm)
plt.show()
