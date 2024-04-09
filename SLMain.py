import streamlit as st
import numpy as np
import pandas as pd

def sinu_data(n = 100):
    x = np.linspace(0, 2*np.pi, n)
    y = np.sin(x)
    df = pd.DataFrame({'x': x, 'y': y})
    return df

def sawtooth_data(freq=1, amp=1, phase=0, n=100):
    x = np.linspace(0, 2*np.pi, n)
    y = amp * (2 * (x * freq + phase) / (2*np.pi) % 1 - 0.5)
    df = pd.DataFrame({'x': x, 'y': y})
    return df

def triangle_data(freq=1, amp=1, phase=0, n=100):
    x = np.linspace(0, 2*np.pi, n)
    y = amp * (2 * (x * freq + phase) / (2*np.pi) % 1 - 0.5)
    y = 2 * np.abs(y) - 1
    df = pd.DataFrame({'x': x, 'y': y})
    return df

def plot_data(df: pd.DataFrame):
    st.line_chart(data=df, x='x', y='y')

def hello_world():
    st.write("Hello, world!")
    st.write("Here's some data:")
    wave_titles = ['Sine wave',
                   'Sawtooth wave',
                   'Triangle wave']
    df_sine = sinu_data()
    df_saw = sawtooth_data()
    df_tri = triangle_data()
    for data, title in zip([df_sine, df_saw, df_tri], wave_titles):
        st.write(f"This is a {title} waveform")
        plot_data(data)

def main():
    hello_world()

if __name__ == "__main__":
    main()
