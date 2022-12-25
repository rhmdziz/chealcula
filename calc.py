import math
import numpy as np
import streamlit as st

from scipy import stats

data_history = []

pi = 22/7
e = 2.71828182846

def sqrt(x):
	return math.sqrt(x)

def root(x, y):
	return x**(1/y)

def fact(x):
	factprev = 1
	for i in range(x):
		fact = factprev * (i+1)
		factprev = fact
	return fact

def sin(x):
	pass

def cos(x):
	pass

def tan(x):
	pass

def log(x, y):
	for i in range(100):
		if x**i == y:
			return i

def ln(x):
	pass



def calculation():
	def calc(x):
		try:
			return eval(x)
		except:
			pass

	st.subheader('''# Basic Calculation''')

	a = st.text_input('input your calculation here',placeholder='example: 2*(10/3)')
	
	if a:
		result = calc(a)
		st.write('answer')
		if result == None:
			st.error(result)
		else:
			st.success(result)
			data_history.append([a, result])
	else:
		st.write('answer')
		st.text_input(' ',label_visibility='collapsed',disabled=True)

	
	
	

def mean_median_mode():
	st.subheader('''# Mean, Median, Mode''')
	st.write('Input your list here')
	listA = st.text_input('Input your list here',label_visibility='collapsed',placeholder='example: 2 4 4 3 4 (separate with a space)')
	

	if listA:
		listA = list(map(str, listA.split()))

		
		try:
			
			for i in range(0, len(listA)):
				listA[i] = int(listA[i])
			st.write('Mean')
			st.success(np.mean(listA))
		except:
			pass
			# mean = st.text_input(' ',label_visibility='collapsed',disabled=True)

		
		try:
			for i in range(0, len(listA)):
				listA[i] = int(listA[i])
			st.write('Median')
			st.success(np.median(listA))
		except:
			pass
			# median = st.text_input('',label_visibility='collapsed',disabled=True)

		st.write('Mode')
		try:
			for i in range(0, len(listA)):
				listA[i] = str(listA[i])
			st.success(stats.mode(listA))
		except:
			pass


		
	else:
		st.write('Mean')
		mean = st.text_input(' ',label_visibility='collapsed',disabled=True)
		st.write('Median')
		median = st.text_input('',label_visibility='collapsed',disabled=True)
		st.write('Mode')
		mode = st.text_input('-',label_visibility='collapsed',disabled=True)


def pytagoras():
	def calc(x, y):
		try:
			x = eval(x)
			y = eval(y)
			return math.sqrt(x**2 + y**2)
		except:
			pass

	st.subheader('''# Pytagoras''')
	a = st.text_input('a')
	b = st.text_input('b')

	if a and b:
		result = calc(a, b)
		st.write('c')
		if result == None:
			st.error(result)
		else:
			st.success(result)
			data_history.append([['pytagoras',a, b], result])

	else:
		st.write('c')
		st.text_input(' ',label_visibility='collapsed',disabled=True)



def quadratic_equality():
	def calc(a,b,c):
		try:
			a = eval(a)
			b = eval(b)
			c = eval(c)

			x1 = (-b + sqrt(b**2 - 4 * a * c))/(2*a)
			x2 = (-b - sqrt(b**2 - 4 * a * c))/(2*a)
			return x1, x2
		except:
			pass

	st.subheader('''# Find x Values from Quadratic Equality''')
	st.write('input a,b, and c from ax^2 + bx + c')
	a = st.text_input('a')
	b = st.text_input('b')
	c = st.text_input('c')

	if a and b and c:
		result = calc(a, b, c)
		st.write('x')
		if result == None:
			st.error(result)
		else:
			st.success(result)
			data_history.append([['quadratic equality',a, b,c], result])
	else:
		st.write('x')
		st.text_input(' ',label_visibility='collapsed',disabled=True)

def derivative():
	st.subheader('# Derivative')
	brank = st.selectbox('Highest rank: ',(1,2,3,4,5,6))
	if brank == 1:
		a = st.text_input('input a from ax')
		if a:
			st.write(str(a)+'x + C')
			st.success(a)

	elif brank == 2:
		a = st.text_input('input a from ax^2')
		b = st.text_input('input b form bx')
		if a and b:
			st.write(a+'x^2 +',b+'x + C')
			result = str(int(a)*2)+'x + '+ b
			st.success(result)
	

## HISTORY
def history():
	st.subheader('# History')

	data_history.reverse()

	# for i in range(len(data_history)):

	#	st.write(data_history[i][1], data_history[i][0])

	st.write(data_history)

