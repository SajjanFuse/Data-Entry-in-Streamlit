import streamlit as st 
import time 

st.balloons() 

st.subheader("Progress Bar") 

st.progress(16) 

with st.spinner("wait for something"):
    time.sleep(9)


import graphviz as graphviz

st.graphviz_chart('''    digraph 
                {        
                Big_shark -> Tuna
                Tuna -> Mackerel
                Mackerel -> Small_fishes
                Small_fishes -> Shrimp
                }
            ''')