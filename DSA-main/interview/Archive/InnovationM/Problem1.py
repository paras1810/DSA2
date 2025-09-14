# # Online Python compiler (interpreter) to run Python online.
# # Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")

df=[Employee_name, Address_1, Address_2, Address_id]
df["Address_id"]=df.index
melted_df = [Employee_name, Address_id, Address]

Employee_name Address_Id
Address_Id Address

Employee_name Address_1
Employee_name Address_2

melted_df=df.melt([Employee_name,Address_id], [Address_1, Address_2], "Address" )

df1=melted_df[Employee_name,Address_id].unique
df2=melted_df[Adress_id, "Address"].unique

Employee_Table
Employee_id
Employee_name
Address
Salary
Department

Select employee_id, max(Salary) from employee_table
where Salary<(Select employee_id, max(Salary) from employee_table)

Select employee_id, Salary from employee_table
order by Salary desc;







# import threading as th
# import time


# def print_input(n):
#     print(f"number is {n}")
    
# th1=th.Thread(target=print_input(1), name="A")
# th2=th.Thread(target=print_input(2), name="B")
# th3=th.Thread(target=print_input(3), name="C")

# th1.start()
# th2.start()
# th3.start()

# th1.run()
# th2.run()
# th3.run()