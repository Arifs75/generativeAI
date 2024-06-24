import pandas as pd
import numpy as np

df=pd.read_csv('SIPRI-Milex-data-1949-2022.csv', index_col=None, header=0)
df

df.head()

df.set_index('Country',inplace=True)

df

df=df.transpose()

df

import matplotlib.pyplot as plt

plt.figure(figsize=(14,8))
plt.plot(df.index, df['Algeria'], label='Algeria')
plt.plot(df.index, df['Libya'], label='Libya')
plt.plot(df.index, df['Morocco'], label='Morocco')
plt.plot(df.index, df['Tunisia'], label='Tunisia')
plt.title('Country Data from 2000 to 2022')
plt.xlabel('Year')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.ylabel('Values')


plt.legend()

# Show the plot
plt.tight_layout()  # Adjust layout to make room for rotated x-axis labels
plt.show()