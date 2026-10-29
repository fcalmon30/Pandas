import pandas as pd

df = pd.DataFrame({
    "titulo": ["Forrest Gump", "Dracula", "Guerra ao Terror", "Matrix"],
    "genero": ["Drama", "Drama", "Acao", "Ficcao"],
    "ano": [1994, 1996, 2005, 1999]
})

print(df)
print()
print(df.head(2))
print()
print(df["titulo"])
print()
print(df[df["ano"] > 1995])
print()
print(df.sort_values("ano"))
print()
print(df["ano"].mean())
