#from matplotlib import pyplot as plt
from matplotlib import style
#import numpy as np
import pandas
#import csv
from sklearn.preprocessing import LabelEncoder
style.use('ggplot')
readdata=open('training.csv','r')
table=pandas.read_csv(readdata,sep=';')
readdata.close()
z=map(tuple,table)
x=pandas.DataFrame(z[0],columns=['0'])

la=LabelEncoder()
y=la.fit_transform(x)



#can't store string values in arrays(0,3,4,5,6,8,9,11,12,16,18)in
# seperated lists to transfer it to intergers.
#as it's my first experiance with Machine learning with such big data.
#I wish i had more time.




#data=[]
#for row in x:
    #data.append(row)
#data.pop(0)
#q1=[]
#for i in range(len(data)):
    #q1.append(int(data[i][0]))
#print('mean of 1:    ', (np.mean(q1)))
print (y)
