import streamlit as st
st.title('loan application app')
st.number_input('Enter your amount for loan')
s=st.number_input('Enter your salary')
c=st.number_input('Enter your credit score')
if s>=2000 and c>=400:
    st.write('congratution')
else:
    st.write('we are sorry')
