# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 11:26:07 2024

@author: KeichiTS
"""


import geopandas as gpd
import matplotlib.pyplot as plt

# Ler o GeoJSON como um GeoDataFrame
gdf_bairros = gpd.read_file("distritos-sp.geojson")

# Definir as densidades populacionais para os bairros
densidades = {
    "ITAQUERA": 500,
    "PINHEIROS": 1000,
    "BUTANTA": 1500
}

# Atribuir as densidades populacionais aos bairros correspondentes no GeoDataFrame
for bairro, densidade in densidades.items():
        gdf_bairros.loc[gdf_bairros['ds_nome'] == bairro, 'Densidade_Populacional'] = densidade
        
gdf_bairros['Densidade_Populacional'] = gdf_bairros['Densidade_Populacional'].fillna(0)

# Plotar o mapa
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
gdf_bairros.plot(column='Densidade_Populacional', cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
plt.title('Mapa de São Paulo')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()