
import geopandas as gpd
import matplotlib.pyplot as plt

lakes = gpd.read_file('C.../HydroLAKES_polys_v10.shp')
de_lakes = lakes.loc[lakes['Country'] == 'Germany']
countries = gpd.read_file('C.../DEU_adm0.shp')
de = countries.loc[countries['name'] == 'Germany']


fig, ax = plt.subplots(dpi=300)
countries.plot(ax=ax, facecolor='black', edgecolor='black', lw=0.1)
de_lakes.plot(ax=ax, facecolor='#00FFFF')
ax.axis('off')
fig.savefig('de_lakes.png', dpi=300, bbox_inches='tight')
plt.show()