# QUE.1)HOW MANY UNIQUE STUDENTS ARE INCLUDED IN THE DATASET?

import pandas as pd
df=pd.read_excel('DAD.xlsx')
print(df[['Email ID','First Name']]).unique()
