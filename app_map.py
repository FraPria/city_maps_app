#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Francesca Priante
"""

import streamlit as st
import osmnx as ox
import io
import matplotlib.pyplot as plt

# To make it faster
ox.config(use_cache=True, log_console=True)


# %%
dpi = 100
walk=0.2

def show_city():
    place = st.text_input('Insert adress here', value = 'Torino, via Roma')
    dist = st.slider("Radius in meters", min_value= 500, max_value = 10000, value = 1000, step =100)    
    col1, col2, col3 = st.columns(3)

    with col1:
        bgcolor = st.color_picker('Background color','#000000')    
    with col2:
        edgecol = st.color_picker('Streets colors','#FFFFFF')

    street_widths = {'footway' : walk,
                     'steps' : walk,
                     'pedestrian' : walk,
                     'path' : walk,
                     'track' : 0.5,
                     'service' : 0.5,
                     'residential' : 0.5,
                     'primary' : 1,
                     'motorway' : 2,
                     'cycleway' : 0.5,
                     'steps' : walk,
                     'corridor' : 0.5,
                     'elevator' : 0.5,
                     'escalator' : 0.5,
                     'proposed' : 0.5,
                     'construction' : 0.5,
                     'bridleway' : 0.5,
                     'abandoned' : 0.5,
                     'platform' : 0.5,
                     'raceway' : 0.5,
                     'highway' : 2
                    }


    fig, ax = ox.plot_figure_ground(address=place, network_type='all', 
    default_width=0.5, dpi=dpi, dist = dist, street_widths=street_widths,
    edge_color=edgecol, bgcolor =  bgcolor, smooth_joints=False)
    
    st.pyplot(fig=fig, clear_figure=None)

    fn = 'MAP.pdf'
    plt.savefig(fn)
    with open(fn, "rb") as img:
        st.download_button(
            label="Download image",
            data=img,
            file_name=fn,
            mime="image/pdf"
            )
    
    fn = 'MAP.pdf'
    img = io.BytesIO()
    plt.savefig(img, format='pdf')

# Icons
# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.set_page_config(page_title="Cool Maps", page_icon=":burrito:") #  📹
st.markdown("# Cool maps")
st.markdown(
"""
Insert the address of the city of your interest and create minimalist maps.
You can also choose the background and streets colors. Then download it with the PDF button.

Keep in mind that it can take few minutes to display the map depending on how complex the city is. So the higher the radius, the slower it can be.

App developed with [Streamlit](https://github.com/streamlit/streamlit) and [OSMnx package](https://github.com/gboeing/osmnx) by [Francesca Priante](https://frapria.github.io/)
"""
)
    
show_city()
