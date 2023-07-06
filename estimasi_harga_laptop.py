import pickle
import streamlit as st

model = pickle.load(open('estimasi_harga_laptop.sav', 'rb'))

st.title('Estimasi Harga Laptop')

ram = st.selectbox('Ram_(GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

weight = st.number_input('Weight_(KG)')

touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

ips = st.selectbox('Ips', ['No', 'Yes'])

hdd = st.selectbox('HDD(GB)', [0, 128, 256, 512, 1024, 2048])

ssd = st.selectbox('SSD(GB)', [0, 8, 128, 256, 512, 1024])

if st.button('Estimasi Harga'):
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0
    predict = model.predict(
        [[ram, weight, touchscreen, ips, hdd, ssd]]
    )
    st.write('Estimasi harga Laptop (rupiah) :', predict*16300)
