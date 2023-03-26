import numpy as np
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
from datetime import timedelta
from datetime import timezone


#user data
# registed1 = pd.DataFrame(columns=['id','pw','history','borrow_num','deadline'])
# registed = registed1.set_index('id')


registed1 = pd.read_csv("registed.csv",encoding="big5")
registed = registed1.set_index('id')
print(registed)

#booklist
# df1 = pd.read_excel("midterm_data1.xlsx",)
# df2 = pd.read_excel("midterm_data2.xlsx",)
# new_df = pd.concat([df1,df2],axis=0).reset_index()
# new_df['borrowable'] = 1
# new_df['id'] = new_df.index
# new_df.to_excel("newdf.xlsx")
# new_df.to_csv("all.csv")
new_df = pd.read_excel("newdf.xlsx")
print(new_df.head())

print(new_df['id'][0])
print(new_df['題名'][0])
print(new_df['borrowable'][0])
# testdate = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
# testdate = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M")
# print(testdate)
# print(datetime.datetime.now())



# print(registed["history"]["rr"])
# t = registed["history"]["rr"]
# print(type(t))
# print(type(eval(t)))
# t2 = eval(t)+["123"]
# registed["history"]["rr"] =t2
# print("newval",registed["history"]["rr"])

# d = eval(registed["deadline"]["yy"])
# print(d)
# j = d+[(5,"123")]
# print(j)