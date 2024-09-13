import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('trained_model.sav','rb'))

st.title('crop to cultivate? :seedling:')

N = st.slider("ratio of Nitrogen content in soil",0,140)
P= st.slider("ratio of Phosphorous content in soil",5,145)
K = st.slider("ratio of Potassium content in soil",5,205)
temperature= st.slider("temperature in degree Celsius :thermometer:",8.00,44.00)
humidity= st.slider("relative humidity in %",14.00,100.00)
ph= st.slider("ph value of the soil",3.00,10.00)
rainfall=st.slider(" rainfall in mm :rain_cloud:",20.00,300.00)

def predict():
    float_features = [float(x) for x in [N,P,K,temperature,humidity,ph,rainfall]]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    label = prediction[0]
    
    print(type(label))
    print(label)

    st.success('Recommended crop to grow is : ' + str(label) + ' :thumbsup:')
    
trigger = st.button('Predict', on_click=predict)

 
