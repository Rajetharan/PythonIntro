import pandas as pd

df = pd.DataFrame({'$a':[1,2], '$b': [3,4], 
                   '$c':[5,6], '$d':[7,8], 
                   '$e':[9,10]})

print(df)

#df.rename(lambda x: x[1:], axis='columns', inplace=True)

df.rename(columns = lambda x: x[1:], inplace=True)

print(df)

#Note x[1:]
#if x = $abcd, then x[1:] would take abcd and ignore index 0.
# x[start:stop] NOT x[row:column]
