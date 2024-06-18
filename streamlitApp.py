import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt

st.title("Mod 4 Prep App")

def load_data(file_path):
    data = pd.read_csv(file_path)
    return data

def main():
    st.title("Streamlit App with Dataset Loading")

    # File path of the dataset (update with your actual file path)
    file_path = '/Users/laurendominello/Desktop/mod 4 prep/car_data.csv'

    # Load the dataset
    data = load_data(file_path)

    # Display the dataset
    st.subheader('Dataset')
    st.write(data)  # Display the dataset in a table

    st.sidebar.title('Filter Options')
    min_hp = int(data['horsepower'].min())
    max_hp = int(data['horsepower'].max())
    hp_range = st.sidebar.slider('Select a range of horsepower', min_hp, max_hp, (min_hp, max_hp))

    filtered_data = data.copy()
    filtered_data = filtered_data[(filtered_data['horsepower'] >= hp_range[0]) & (filtered_data['horsepower'] <= hp_range[1])]

    if st.button('See Graph'):
        plt.figure(figsize=(10,6))
        plt.scatter(data['horsepower'], data['acceleration'], marker='o')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Cars Graph')
        st.pyplot()


        







if __name__ == '__main__':
    main()