#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np


def main():
    

    # creating data to plot in the chart
    # in this case we've built a exponential chart

    x = np.linspace(0,5,11)
    y = x ** 2
    #plt.plot(x,y, 'r-')
    #plt.xlabel("axis")
    #plt.ylabel("ordenates")
    #plt.title("My first chart")
    plt.subplot(1,2,1)
    plt.plot(x,y, 'r-')


    plt.subplot(1,2,2)
    plt.plot(y,x,'b-')

    plt.show()
    

def creating_figure():

    x = np.linspace(0,5,11)
    y = x ** 2

    figure = plt.figure()
    axes = figure.add_axes([0.1,0.1,0.8,0.8])

    axes.plot(x,y)
    axes.set_xlabel("axis")
    axes.set_ylabel("ordenates")
    axes.set_title("Title figure")
    plt.show()



def chart_inside_another():

    x = np.linspace(0,5,11)
    y = x ** 2
    
    figure = plt.figure()
    axes_1 = figure.add_axes([0.1,0.1,0.8,0.8])
    axes_2 = figure.add_axes([0.2,0.5,0.4,0.3])



    axes_1.plot(x,y)
    axes_2.plot(y,x)



    plt.show()


if __name__  == '__main__':


    #main()
    #creating_figure()
    chart_inside_another()







