## pip install pandas
import pandas as pd
url="C:\\Users\\User\\Desktop\\courseWorkspace\\aws0323\\samples\\demo.csv"
url2="./../samples/demo.csv"
df=pd.read_csv(url)
### aplicamos metodos de pandas

df.to_parquet('./samples/demoparquet.parquet') #dependiendo de donde esta

print(df.head())


################
