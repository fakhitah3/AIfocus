import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

selangor = pd.read_csv('https://raw.githubusercontent.com/fakhitah3/AIfocus/refs/heads/main/data/selangor_data.csv')

# Pie chart for 'STATUS PEMAKANAN'
status_pemakanan_counts = selangor['STATUS PEMAKANAN'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(status_pemakanan_counts, labels=status_pemakanan_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Status Pemakanan Distribution')
plt.show()
st.pyplot(plt.gcf())

# Bar plot for 'STATUS PEMAKANAN' vs 'PENDAPATAN KELUARGA'
plt.figure(figsize=(12, 6))
sns.countplot(x='PENDAPATAN KELUARGA', hue='STATUS PEMAKANAN', data=selangor)
plt.title('Status Pemakanan vs Pendapatan Keluarga')
plt.xlabel('Pendapatan Keluarga')
plt.ylabel('Count')
plt.legend(title='Status Pemakanan')
plt.show()
st.pyplot(plt.gcf())
