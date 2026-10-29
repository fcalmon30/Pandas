import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:1234@localhost:3306/cinema')

df = pd.read_sql("SELECT * FROM filmes", engine)

print(df)
print()
print(df.head())
print('\n', df[df["genero"] == "Drama"])    
print('\n', df["titulo"])
print('\n', df["ano"])
print('\n', df["genero"].value_counts())
print('\n', df["ano"].min())
