import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

arr1 = np.random.normal(1, 1, size=100)
fig1, ax = plt.subplots()
ax.hist(arr1, bins=20)

arr2 = np.random.normal(1, 1, size=100)
fig2, ax = plt.subplots()
ax.hist(arr2, bins=20)

st.pyplot(fig1)
st.pyplot(fig2)