
import streamlit as st
import sympy as sym
import numpy as np
from sympy.abc import x
from sympy import integrate, simplify
import matplotlib.pyplot as plt

def int_col1(expr):
	fx = simplify(expr)
	st.write('Your Function Is:')
	st.write(fx)

	int_x = sym.integrate(expr)
	st.write('The Integral Is:')
	st.write(int_x)

	int_xx = sym.integrate(int_x)
	st.write('The Second Integral Is:')
	st.write(int_xx)


def int_col2(expr):
	plt.rcParams['xtick.labelsize'] = 25
	plt.rcParams['ytick.labelsize'] = 25
	plt.rcParams['legend.fontsize'] = 35

	xx = np.linspace(-5,5,200)

	fxx = simplify(expr)
	int_x = sym.integrate(expr)
	int_xx = sym.integrate(int_x)
	
	fxx = sym.lambdify(x, fxx)
	int_x = sym.lambdify(x, int_x)
	int_xx = sym.lambdify(x, int_xx)

	fig, ax = plt.subplots()
	fig.set_size_inches(15,15)

	if np.size(fxx(xx)) > 1:
		ax.plot(xx,fxx(xx), linewidth=7, label='$f(x)$')

	if np.size(int_x(xx)) > 1:
		ax.plot(xx,int_x(xx), linewidth=7, label='$\\int{f(x) ~dx}$')

	if np.size(int_xx(xx)) > 1:
		ax.plot(xx,int_xx(xx), linewidth=7, label='$\\int \\int{f(x) ~dx}$')

	ax.grid()
	ax.legend(loc='upper left')
	st.pyplot(plt.gcf())
