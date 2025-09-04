import pandas as pd
import numpy as np

'''df = pd.DataFrame({
    "Name": ["Ali", None, "Usman", np.nan],
    "Age": [25, None, 30, 40],
    "City": ["Lahore", None, None, None]
})'''
#df.dropna(inplace=True) will    works
#df1=df.dropna(subset=['Age']) will works as assiged

#df.dropna(subset=['Age']) will not works

#df.dropna() not works only assigned works
#df.dropna(how='all') nothing happening 


import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Ali", None, "Usman", np.nan, None],
    "Age": [25, None, 30, 40, None],
    "City": ["Lahore", None, None, None, None]
})

df = df.dropna(how='all')  # or use inplace=True
print(df)


df3=df["Age"].dropna()#just drop the specific but not reliable as return the only col so 
print("testing",df3)