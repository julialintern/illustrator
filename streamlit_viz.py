import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt

st.title("Visualization of Patent Topics")
st.write("'This is patently important!")


viz_data = pd.read_csv('viz_data.csv')
n_clusters = 15

# add topics
topics = ['electronics','invention','elec engineering','pharmaceuticals','electronics2','mobile','mechanical',
 'image data','optics','motors','fluid engineering','composites','biology','computers','chemistry']

topic_map={}
for i in range(15):
    topic_map[i]=topics[i]

viz_data['topics']=viz_data['clusters'].map(topic_map)

viz_data2=pd.read_csv('viz_data2')
#viz_data2.clusters==viz_data2.clusters.astype(str)

viz_sample=viz_data2.sample(50)

graph = alt.Chart(viz_data.reset_index()).mark_point(filled=True, size=60).encode(
    x=alt.X('Component 0'),
    y=alt.Y('Component 1'),
    #shape=alt.Size('year', scale=alt.Scale(domain=[str(i) for i in range(1970,2022)])),
    color=alt.Color('clusters', scale=alt.Scale(domain=[i for i in range(n_clusters)])),
    tooltip=['year', 'topics','abs_clean']
    ).interactive()

st.altair_chart(graph, use_container_width=True);

def visualize_data(viz_data, x_axis, y_axis, n_clusters):
    graph = alt.Chart(viz_data.reset_index()).mark_bar().encode(
        x=alt.X('abs_clean', sort='y'),
        y=alt.Y(str(y_axis)+":Q"),
        color=alt.Color('clusters', scale=alt.Scale(domain=[i for i in range(n_clusters)])),
        tooltip=['year','abs_clean']
    ).interactive()
    st.altair_chart(graph, use_container_width=True)

x_axis = list(viz_sample['abs_clean'])
y_axis = st.selectbox("Choose a variable for the y-axis", list(viz_sample.columns)[7:], index=0)
visualize_data(viz_sample, x_axis, y_axis, n_clusters)

