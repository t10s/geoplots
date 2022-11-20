# -*- coding: utf-8 -*-
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as cx

#make dataframe of stations and lat, long from distanceto.com
df = pd.DataFrame(
    {"Station": ["Cardiff", "Redhill", "Rainham", "Gravesend", "London King's Cross", 
            "Doncaster", "Stockport", "Edinburgh Haymarket"],
     "Latitude": [51.4760,51.4760,51.4760,51.4412,51.5310,53.5222,53.4058,55.9456],
     "Longitude": [-3.1790,-0.1661,-0.1908,-0.3667,-0.1246,-1.1393,-2.1624,-3.2183]})
#convert to geo df
gdf = gpd.GeoDataFrame(df,
                       geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
#read map
world = gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
#filter country
uk = world[world.name =="United Kingdom"]

#change coord ref sys to match base map
uk_crs = uk.to_crs(epsg=3857)
gdf2 = gdf
gdf2.crs = gdf2.set_crs = "EPSG:4326" #add crs because data set didn't have one
gdf2 = gdf2.to_crs(epsg=3857) #convert to crs to match base map
texts = [] #don't need because adjust text not working for this plot (See below)

#plot stns and add base map
fig, ax = plt.subplots(figsize=(10,10))
uk_crs.plot(ax=ax, alpha=0, edgecolor='white')
gdf2.plot(ax=ax, color="black", markersize=30, edgecolor="white")
cx.add_basemap(ax, source=cx.providers.Stamen.TerrainBackground)
ax.axis("off")
ax.text(-400000, 6730000, r'Cardiff', fontsize=10)
ax.text(-400000, 7560000, r'Edinburgh Haymarket', fontsize=10)
ax.text(-400000, 7090000, r'Stockport', fontsize=10)
ax.text(-200000, 7100000, r'Doncaster', fontsize=10)
ax.text(-200000, 6750000, r"London King's Cross", fontsize=10)
ax.text(30000, 6710000, r'Rainham', fontsize=10)
ax.text(0000, 6670000, r'Gravesend', fontsize=10)
ax.text(-120000, 6640000, r'Redhill', fontsize=10)

fig.savefig("pltfm_zero_map.png", dpi = 300, bbox_inches='tight')








