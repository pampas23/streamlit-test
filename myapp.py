import time

import streamlit as st

import numpy as np
import pandas as pd
st.title('我的第一個應用程式 Hello World')

st.write("嘗試創建**表格**：")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.line_chart(chart_data)

if st.button('Let it celebrate!'):
    st.balloons()

