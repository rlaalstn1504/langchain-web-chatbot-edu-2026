import streamlit as st
import pandas as pd
import numpy as np

st.header("출력 요소 예제")

data = pd.DataFrame({
    'x': np.arange(1, 6),
    'y': np.random.randint(1, 100, 5)
})

st.dataframe(data)
st.bar_chart(data.set_index('x'))