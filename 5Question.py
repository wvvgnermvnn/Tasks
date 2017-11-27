"""
Суть задания была в том, чтобы посчитать тремя способами численного исчисления(Симпсона, Трапеций и Прямоугольников)
посчитать значение интеграла от функции x * ln(x). Каждому способу в программе соответствует собственный класс.
Задача является типовой проблемой мат.моделирования, использовать
"""
import math

from math import sin
from math import cos
from math import log
from math import  sqrt
from math import factorial
import numpy as np
#Импортируем один из пакетов Matplotlib
import pylab
#Импортируем пакет со вспомогательными функциями
from matplotlib import mlab
import matplotlib.pyplot as pyplot
import matplotlib.patches as ptchs
import matplotlib.pylab as plt
import sys


class MyFunction():
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

	def func(x):
		f = x * log(x)
		return f

	def derivative(x):
		return log(x) + 1

	def second_derivative(x):
		return 1 / x

	def fourth_derivative(x):
		return 3 / (x ** 4)

def _step_of_interpolation():
    l = [1.0]
    i = 0
    h = float(input("введите шаг интерполяции(обязательно меньше еденицы,для точности намного меньше 1): "))
    while l [i] <= 2.0:
        el = l[i]+h
        l.append(el)
        i += 1
    for m in range(len(l)):
    	if l[m] > 2.0:
    		del(l[m])
    l.append(2.0)
    # print("Узлы: ",l)
    print()
    return l
    global h
    global l

class Rectangle():
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

	def rectangle():
		values_of_func = []
		for i in l:
			values_of_func.append(MyFunction.func(i))
		return h * sum(values_of_func)

	def R_rect():
		values_of_deriv = []
		for i in l:
			values_of_deriv.append(MyFunction.derivative(i))
		return (1/2) * h ** 2 * sum(values_of_deriv)

class Trapeze():
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

	def trapeze():
		values_of_trap = []
		for i in l:
			values_of_trap.append(MyFunction.func(i - h) + MyFunction.func(i))
		return  (1/2) * h * sum(values_of_trap)

	def R_trap():
		values_of_second_deriv = []
		for i in l:
			values_of_second_deriv.append(MyFunction.second_derivative(i))
		return  ((h ** 3)/12) * abs(sum(values_of_second_deriv))

class Simpson():
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg

	def simpson():
		values_of_simp = []
		for i in l:
			values_of_simp.append(MyFunction.func(i + h) + 4 * MyFunction.func(i) + MyFunction.func(i - h))
		return  (h/6) * sum(values_of_simp)

	def R_simp():
		values_of_fourth_deriv = []
		for i in l:
			values_of_fourth_deriv.append(MyFunction.fourth_derivative(i))
		return ((h ** 5)/2880) * sum(values_of_fourth_deriv)

def main():
    _step_of_interpolation()
    print('  Метод  ', '       Значение интеграла', '      Ошибка')
    print()
    print('Прямоугольник: ', Rectangle.rectangle(), '  R =', Rectangle.R_rect())
    print()
    print('Трапеция:      ', Trapeze.trapeze(), '  R =', Trapeze.R_trap())
    print()
    print('Симпсон:       ', Simpson.simpson(), '  R =', Simpson.R_simp())
    print('')
    print('Hello World')
    print('Точное значение интеграла  :0,636294361119891')


if  __name__ == '__main__':
    main()