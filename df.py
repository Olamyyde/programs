import pandas as pd
import io

lst=['x data,y data',
 '-969.0,-52.12282,',
 '-959.0,-49.436077,',
 '-948.0,-46.615,',
 '-938.0,-44.59994,',]

dframe=pd.read_csv(io.StringIO('\n'.join(s[:-1] for s in lst)))
print(dframe)

dframe1=pd.DataFrame([x.strip(',').split(',') for x in data[1:]], columns=data[0].split(','))
print(dframe1)
