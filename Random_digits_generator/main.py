from random import *
import pickle
randlist=[]
for i in range (150):
    randlist.append(randint(1,10000))

file_name="randomlist"
open_file= open(file_name,"wb")
pickle.dump(randlist,open_file)
open_file.close

open_file=open(file_name,"rb")
loaded_list=pickle.load(open_file)
print(loaded_list)