#!/usr/bin/python3


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
@author: Arturo Negreiros
"""


def read_csv_method(name):
    return "practices/{}.csv".format(name)


def facebook_view():
    facebook = pd.read_csv(read_csv_method("FB_data"))
    stack_headers = list()

    for x in facebook:
        stack_headers.append(x)

    print("headers =>\n %s \n" % stack_headers)
    print(facebook)
    sns.pairplot(facebook, hue="Open")
    plt.show()


def phone_data_viewing():

    phone_data = pd.read_csv(read_csv_method("phone_data"))
    stack_headers = list()
    stack_world = list()
    stack_network = list()


    for i in phone_data:
        stack_headers.append(i)

    for j in phone_data["network_type"]:
        if j not in stack_world:
            stack_world.append(j)

    for k in phone_data["network"]:
        if k not in stack_network:
            stack_network.append(k)

    print(stack_headers)
    print(stack_world)
    print(stack_network)
    #print(phone_data)



def main():
    #facebook_view()
    phone_data_viewing()

if __name__ == '__main__':
    main()
