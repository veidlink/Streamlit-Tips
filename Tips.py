import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sb
import streamlit as st
from matplotlib.ticker import MaxNLocator

tips = sb.load_dataset('tips')

st.write("""
# Визуализация датасета по чаевым
""")

st.write("""
### Шаг 4 | Гистограмма - общий счет
""")

fig4 = plt.figure(figsize=(5,5))       
sb.histplot(tips, x="total_bill")
sb.set_style("white")
st.pyplot(fig4)

st.write("""
### Шаг 5 | Диаграмма рассеивания - связь размера счета и размера чаевых
""")
         
fig5 = plt.figure(figsize=(5,5))       
sb.scatterplot(tips, y='tip', x='total_bill', hue='size', size='size')
sb.set_style("white")
st.pyplot(fig5)

st.write("""
### Шаг 7 | График, связывающий размер счета, размер группы и чаевые
""")
         
sb.set_style("dark")

fig7 = plt.figure(figsize=(5,5))       
ax7 = sb.scatterplot(tips, y='tip', x='total_bill', hue='size',
                      size='size', palette='crest')

norm = plt.Normalize(tips['size'].min(), tips['size'].max())
sm = plt.cm.ScalarMappable(cmap="crest", norm=norm)
sm.set_array([])

# Remove the legend and add a colorbar

ax7.get_legend().remove()
ax7.figure.colorbar(sm)



st.pyplot(fig7)


# Тут странный график получился

st.write("""
### Шаг 8 | Cвязь между днем недели и размером счета
""")

tips9 = tips.sort_values(by='total_bill').reset_index()
tips9['day'] = pd.Categorical(tips9['day'],
                            categories=['Thur', 'Fri', 'Sat', 'Sun'], ordered=True)
tips9_sorted = tips9.groupby('day')['total_bill'].mean()

fig9 = plt.figure(figsize=(5,5))       
sb.lineplot(tips9_sorted)
sb.set_style("white")
st.pyplot(fig9)


st.write("""
### Шаг 9 | Диаграмма рассеивания - чаевые по дням недели
""")

tips9 = tips.sort_values(by='total_bill').reset_index()
tips9['day'] = pd.Categorical(tips9['day'],
                            categories=['Thur', 'Fri', 'Sat', 'Sun'], ordered=True)
tips9_sorted = tips9.sort_values('day')


fig9 = plt.figure(figsize=(5,5))       
sb.scatterplot(tips9, y='tip', x='day', hue='sex')
sb.set_style("white")
st.pyplot(fig9)

st.write("""
### Шаг 10 | Ящик с усами - сумма счетов за каждый день по времени
""")
         
fig10 = plt.figure(figsize=(5,5))         
tips10_sorted = tips.sort_values('day')         
g = sb.boxplot(x="day", y="total_bill",
                hue="time", data=tips10_sorted);
st.pyplot(fig10)

st.write("""
### Шаг 11 | 2 гистограммы - чаевые на обед и ланч
""")

df11 = pd.DataFrame(tips, columns=['tip', 'time'])
grouped_data11 = df11.groupby('time')['tip'].sum()

fig11 = plt.figure(figsize=(5,5))       
sb.histplot(tips, x='time', hue='time')
sb.set_style("white")
st.pyplot(fig11)

st.write("""
### Шаг 12 | 2 диаграммы рассеивания по полу - связь размера счета и чаевых
""")
         
sb.set_style('dark')

fig12, axes = plt.subplots(1, 2, figsize=(12, 5))

ax1 = sb.scatterplot(tips9_sorted[tips9_sorted['sex']=='Female'], ax=axes[0], x='total_bill',y='tip', hue='smoker', size='size')
ax1.xaxis.set_major_locator(MaxNLocator(nbins='auto'))
ax1.set_title('Females')

ax2 = sb.scatterplot(tips9_sorted[tips9_sorted['sex']=='Male'], ax=axes[1], x='total_bill',y='tip', hue='smoker', size='size')
ax2.xaxis.set_major_locator(MaxNLocator(nbins='auto'))
ax2.set_title('Males')

st.pyplot(fig12)
