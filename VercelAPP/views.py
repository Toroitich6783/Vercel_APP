from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
import geemap
import ee
import folium
import geemap.foliumap as geemap

#MapLayout
class map(TemplateView):
        template_name = 'index.html'
        def get_context_data(request):
            figure = folium.Figure()
            Map = geemap.Map(
# plugin_Draw = True, 
#     Draw_export = True
)
            Map.add_to(figure)
            Map.set_center(37.842, 0.156, 6)

            style = {'color': '131313', 'fillColor':' FD0505'}
    
            basemaps = {
        'Google Maps': folium.TileLayer(
tiles = 'https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
attr = 'Google',
name = 'Google Maps',
overlay = False,
control = True
),
'Esri Satellite': folium.TileLayer(
tiles = 'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
attr = 'Esri',
name = 'Esri Satellite',
overlay = True,
control = True
),'Google Satellite Hybrid': folium.TileLayer(
tiles = 'https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
attr = 'Google',
name = 'Google Satellite',
overlay = False,
control = True
),
                
                }     
            basemaps['Google Satellite Hybrid'].add_to(Map)
            basemaps['Esri Satellite'].add_to(Map)
            
            Map.add_child(folium.LayerControl())
    
            figure.render()
    
            return{"map": figure}
    