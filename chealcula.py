import streamlit as st
import math
import calc

st.write('''
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
table {
	font-family: monospace;
	font-size: 12px;
	width: 100%;
}

@media screen and (max-with: 800px){
	table {
		display: none;
	}
}

</style>

<table border="0" class='hidden'>
  <tbody>
    <tr>
      <td align='center'>+</td>
      <td align='center'>-</td>
      <td align='center'>*</td>
      <td align='center'>/</td>
      <td align='center'>%</td>
      <td align='center'>**</td>
      <td align='center'>//</td>
      <td align='center'>(</td>
      <td align='center'>)</td>
      <td align='center'>.</td>
    </tr><tr>
      <td align='center' >root(x,y)</td>
      <td align='center' >sqrt(x)</td>
      <td align='center'>fact(x)</td>
      <td align='center'>sin(x)</td>
      <td align='center'>cos(x)</td>
      <td align='center'>tan(x)</td>
      <td align='center'>log(x,y)</td>
      <td align='center'>ln(x)</td>
      <td align='center'>pi</td>
      <td align='center'>e</td>
    </tr>
  </tbody>
</table><br>
	''', unsafe_allow_html= True)

main_menu = st.sidebar.selectbox(
    "Menu",
    ("Basic Math", "Bussiness Math", "History",'About')
)

if main_menu == 'Basic Math':
	menu = st.sidebar.selectbox('Extension',('Basic Calculation','Pytagoras','Quadratic Equality','Mean, Median, Mode'), index=0)

	if menu == 'Pytagoras':
		calc.pytagoras()
	elif menu == 'Basic Calculation':
		calc.calculation()
	elif menu == 'Mean, Median, Mode':
		calc.mean_median_mode()
	elif menu == 'Quadratic Equality':
		calc.quadratic_equality()

elif main_menu == 'Bussiness Math':
	menu = st.sidebar.selectbox('Extension',('Derivative','',''), index=0)
	if menu == 'Derivative':
		calc.derivative()

elif main_menu == 'History':
	calc.history()


elif main_menu == 'About':
	st.header('Chealculator')
	st.write('''
		A calculator to make life easier for prasetiya mulya university students. It was conceived as an expansion of the previous idea which was a formula application calculator with a display that was not user friendly--only programmers could use it. But now you can use it even if you are not a programmer. \n\n''')
	# st.table(data.operation)

	st.write('''	
		##### Developed by
		- Anas Satria, REE 2022
		- Aziz Rahmad Isnanto, SE 2022
		- Dwi Mahrani Pohan, PDE 2022
		- Kautsaradea Assabila, REE 2022 \n
		
		''')
	
	
	def form():
		with st.form(key='Submission Form', clear_on_submit=True):
			st.write('##### Contact Us')
			name = st.text_input('Name: ')
			email = st.text_input('Email: ')
			message = st.text_area('Message: ')

			submission = st.form_submit_button(label='Submit')

			if submission and name and email and message:
				st.success('Succesfully Submited')
				st.balloons()
	
	# form()


hide_menu = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu, unsafe_allow_html=True)