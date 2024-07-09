
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px


# se guarda el dataset
df_crops = pd.read_csv('files/datasets/output/a01_dataset_ge_crops_cleaned.csv')



# se imprimen las primeras 5 filas del DataFrame
df_crops.head()


# se imprimen la información del DataFrame
df_crops.info()


# convertir 'year' a tipo fecha
df_crops['year'] = pd.to_datetime(df_crops['year'], format='%Y')


# Estadísticas descriptivas de del porcentaje sembrado del total del maíz
print("Estadísticas descriptivas del cultivo total sembrado de maíz:")
df_crops[df_crops['crop'] == 'corn']['pct_(%)'].describe()


print("Estadísticas descriptivas del cultivo total sembrado de algodón:")
df_crops[df_crops['crop'] == 'cotton']['pct_(%)'].describe()


print("Estadísticas descriptivas del cultivo total sembrado de soya:")
df_crops[df_crops['crop'] == 'soybean']['pct_(%)'].describe()


# se filtra el DataFrame por el tipo de modificación genética, en donde se incluyan sólo las todos los tipos
df_all_ge = df_crops[~(df_crops['variety'] == 'All GE varieties')]
df_all_ge.head()


print("Estadísticas descriptivas de del porcentaje de los cultivo transgénicos sembrados:")
df_all_ge['pct_(%)'].describe()


# Visualización de la distribución de del porcentaje de los cultivos gené ticamente modifcados ('pct_(%)') a lo largo de los años
plt.figure(figsize=(12, 6))

fig1 = sns.boxplot(data= df_all_ge,
                   x= df_crops['year'].dt.year,
                   y= 'pct_(%)'
                   )

fig1.set_title('Distribución del Porcentaje de Cultivos Transgénicos Sembrados por Año')
fig1.set_xlabel('Año')
fig1.set_ylabel('Porcentaje de Cultivos Transgénicos Sembrados (%)')
plt.xticks(rotation= 45)

# se guarda la figura fig2 con el método savefig()
plt.savefig('data_visualization/a02_fig1.png')
plt.show()

# se grafica un histograma para la distribución del porcentaje de cultivos
fig2 =  px.histogram(df_all_ge,
                     x= 'pct_(%)',
                     title= 'Distribución del porcentaje de llamadas perdidas para los operadores',
                     nbins= 100
                     )
fig2.show()

# se guarda la figura fig2 con el método write_image() de Plotly
fig2.write_image("data_visualization/a02_fig2.png")




# Visualización de la tendencia temporal de adopción promedio por año
plt.figure(figsize=(12, 6))

fig3 = df_all_ge.groupby(df_crops['year'].dt.year)['pct_(%)'].mean().plot(marker='o')
fig3.set_title('Tendencia de Adopción de Cultivos Transgénicos')
fig3.set_xlabel('Año')
fig3.set_ylabel('Adopción Promedio de Cultivos Trangénicos (%)')
plt.grid(False)

# se guarda la figura fig3 con el método savefig()
plt.savefig('data_visualization/a02_fig3.png')
plt.show()


# Gráfico de barras de los estados con mayor adopción promedio

# se agrupan los 10 estados con mayor porcentaje de cultivos trangénicos
top_states = df_all_ge.groupby('state')['pct_(%)'].mean().nlargest(10).reset_index()


fig4 = px.bar(top_states, x='state', y='pct_(%)', 
             title='Top 10 Estados con Mayor Adopción de Cultivos Transgénicos', 
             labels={'state': 'Estado', 'pct_(%)': 'Adopción Promedio (%)'},
             color_discrete_sequence=['darkcyan'])

fig4.update_layout(xaxis_title='Estado', yaxis_title='Adopción Promedio (%)')

fig4.show()

# se guarda la figura fig4 con el método write_image() de Plotly
fig4.write_image("data_visualization/a02_fig4.png")



# Gráfico de líneas para mostrar adopción por cultivo a lo largo de los años
plt.figure(figsize=(12, 6))

fig5 = sns.lineplot(data= df_all_ge,
                    x='year', 
                    y='pct_(%)', 
                    hue= 'crop',  
                    palette='viridis', 
                    errorbar= None
                    )
fig5.set_title('Adopción de Cultivos Transgénicos por Año y Tipo de Cultivo')
fig5.set_xlabel('Año')
fig5.set_ylabel('Adopción (%)')

plt.legend(title='Cultivo')
plt.grid(False)

# se guarda la figura fig5 con el método savefig()
plt.savefig('data_visualization/a02_fig5.png')
plt.show()



#gráfico Adopción de Cultivos Transgénicos por Cultivo y Tipo de Modificación Genética
plt.figure(figsize=(12, 6))

fig6 = sns.barplot(df_all_ge, 
            x="crop", 
            y="pct_(%)", 
            hue="variety", 
            palette='viridis'
            )

fig6.set_title('Adopción de Cultivos Transgénicos por Cultivo y Tipo de Modificación Genética')
fig6.set_xlabel('Cultivo')
fig6.set_ylabel('Porcentaje Sembrado')

plt.legend(title='Tipo de Modificación Genética')
# plt.grid(False)
# se guarda la figura fig6 con el método savefig()
plt.savefig('data_visualization/a02_fig6.png')
plt.show()


df_all_ge.info()


# se filtra sólo para el maíz sembrado
df_corn = df_all_ge[df_all_ge["crop"] == "corn"]
df_corn.head()


# Gráfico de líneas para mostrar la adopción de los tipos de modificación genética para el maíz a lo largo de los años
plt.figure(figsize=(12, 6))

fig7 = sns.lineplot(data= df_corn,
                    x='year', 
                    y='pct_(%)', 
                    hue= 'variety',  
                    palette='viridis', 
                    errorbar= None
                    )
fig7.set_title('Adopción de Maíz Transgénico por Año')
fig7.set_xlabel('Año')
fig7.set_ylabel('Porcetaje Sembrado')

plt.legend(title= 'Tipo de Modificación Genética')
plt.grid(False)

# se guarda la figura fig7 con el método savefig()
plt.savefig('data_visualization/a02_fig7.png')
plt.show()




# se filtra sólo para el algodón sembrado
df_cotton = df_all_ge[df_all_ge["crop"] == "cotton"]
df_cotton.head()


# Gráfico de líneas para mostrar la adopción de los tipos de modificación genética para el algodón a lo largo de los años
plt.figure(figsize=(12, 6))

fig8 = sns.lineplot(data= df_cotton,
                    x='year', 
                    y='pct_(%)', 
                    hue= 'variety',  
                    palette='viridis', 
                    errorbar= None
                    )
fig8.set_title('Adopción de Algodón Transgénico por Año')
fig8.set_xlabel('Año')
fig8.set_ylabel('Porcetaje Sembrado')

plt.legend(title= 'Tipo de Modificación Genética')
plt.grid(False)

# se guarda la figura fig8 con el método savefig()
plt.savefig('data_visualization/a02_fig8.png')
plt.show()



# se filtra sólo para el algodón sembrado
df_soy = df_all_ge[df_all_ge["crop"] == "soybean"]
df_soy.head()


# Gráfico de líneas para mostrar la adopción de los tipos de modificación genética para la soya a lo largo de los años
plt.figure(figsize=(12, 6))

fig9 = sns.lineplot(data= df_soy,
                    x='year', 
                    y='pct_(%)', 
                    hue= 'variety',  
                    palette='viridis', 
                    errorbar= None
                    )
fig9.set_title('Adopción de Soya Transgénica por Año')
fig9.set_xlabel('Año')
fig9.set_ylabel('Porcetaje Sembrado')

plt.legend(title= 'Tipo de Modificación Genética')
plt.grid(False)

# se guarda la figura fig7 con el método savefig()
plt.savefig('data_visualization/a02_fig9.png')
plt.show()
