import pandas as pd

df= pd.read_csv("pratice.csv")

print(df.to_string)

print(df.loc[0])

mydataset={
    "cars":["BWN","Volvo","Ford","toyota"],
    "passing":[3, 4 ,5, 6]
}
joy=pd.DataFrame(mydataset)
print(joy)  



a=[1,2,3]
myvar=pd.Series(a,index=["x","y","z"])
print(myvar)
