# Why multiple inheritance in Python
# Class A, B and C inheriting both of these its variable can access A and B or not.
# Method Resolution Order C A B

# Which framework for data processing you will used
# Core Pandas, Numpy, Dask, Polars, PySpark, Vaex
# Specialized ETL: Apache Airflow, Luigi, Kedro, Prefect
# 

#Polymorphism in Python
# Duck Typing
# Method Overriding
# Operator Overloading
# Function Overloading

class A:

    def __init__(self, a, b, c):
        self.__A = a
        self._B = b 
        self.C = c 

class B(A):

    
    def __init__(self,a,b,c,d):
        super.__init__(a, b, c)
        self.D = d

object_a = A(2,3,5)
print(B.__mro__)
