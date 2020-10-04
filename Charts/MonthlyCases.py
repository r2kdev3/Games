import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/karan/Desktop/Git/Games/Charts/data.csv")


print(df)

sb.lineplot(data = df, x = "Months", y = "King County")
sb.lineplot(data = df, x = "Months", y = "Snohomish County")

plt.show()