from pathlib import Path
import csv
import plotly.express as px

path = Path("eq_data/world_fires_1_day.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)

lats, lons, brighs = [], [], []
for row in reader:
    lat = float(row[0])
    lon = float(row[1])
    brigh = float(row[2])
    lats.append(lat)
    lons.append(lon)
    brighs.append(brigh)

title = "Fires burning in different locations around the globe"
fig = px.scatter_geo(lat=lats, lon=lons, size=brighs, title=title,
                     color=brighs, color_continuous_scale='viridis',
                     labels={'color':'Brightness'}, projection='hyperelliptical'
                    )

fig.show()