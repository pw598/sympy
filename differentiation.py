
import streamlit as st
import sympy as sym
import numpy as np
from sympy.abc import x
from sympy import diff, simplify
import matplotlib.pyplot as plt

def diff_col1(expr):
	fx = simplify(expr)
	st.write('Your Function Is:')
	st.write(fx)

	dx = sym.diff(expr)
	st.write('The Derivative Is:')
	st.write(dx)

	dxx = sym.diff(dx)
	st.write('The Second Derivative Is:')
	st.write(dxx)


def diff_col2(expr):

	plt.rcParams['xtick.labelsize'] = 25
	plt.rcParams['ytick.labelsize'] = 25
	plt.rcParams['legend.fontsize'] = 35

	xx = np.linspace(-5,5,200)

	fxx = simplify(expr)
	dx = sym.diff(expr)
	dxx = sym.diff(dx)
	
	fxx = sym.lambdify(x, fxx)
	dx = sym.lambdify(x, dx)
	dxx = sym.lambdify(x, dxx)

	fig, ax = plt.subplots()
	fig.set_size_inches(15,15)

	if np.size(fxx(xx)) > 1:
		ax.plot(xx,fxx(xx), linewidth=7, label='$f(x)$')

	if np.size(dx(xx)) > 1:
		ax.plot(xx,dx(xx), linewidth=7, label='$f\'(x)$')

	if np.size(dxx(xx)) > 1:
		ax.plot(xx,dxx(xx), linewidth=7, label='$f\'\'(x)$')

	ax.grid()
	ax.legend(loc='upper left')
	st.pyplot(plt.gcf())

