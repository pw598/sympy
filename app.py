
import streamlit as st
import re
from sympy import simplify
import sympy as sym

from differentiation import diff_col1, diff_col2
from integration import int_col1, int_col2

def main():	

	menu = ['Differentiation', 'Integration']
	choice = st.sidebar.selectbox('Menu', menu)

	if choice:
		st.title(choice + ' With Sympy')

	col1, col2 = st.columns([2,3])

	with col1:

		label = 'Enter a single-variable function. Use * for multiplication.'
		expr = st.text_input(label, "x**3 - 3*x**2 + 50")
		cleaned = re.sub('e',str(2.71828),expr)

		if cleaned:
			if choice == 'Differentiation':
				diff_col1(cleaned)
			else:
				int_col1(cleaned)

	with col2:
		if cleaned:
			if choice == 'Differentiation':
				diff_col2(cleaned)
			else:
				int_col2(cleaned)


if __name__ == "__main__":
    main()

