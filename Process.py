#!/usr/bin/python3

import numpy as np
import pandas as pd
from pprint import pprint


PATH = "practices/Salaries.csv"
COVID_URL = "https://covid19.who.int/WHO-COVID-19-global-table-data.csv"

data = pd.read_csv(PATH,low_memory=False)
#print(data.info())
#print("\n")


#print("[*] Getting the headers")
#headers = [i for i in data]
#print(headers)

# deleting values with "Not Provided in the values"
data = data[data['BasePay'] != "Not Provided"]



# the column names
# ['Id', 'EmployeeName', 'JobTitle', 'BasePay', 'OvertimePay', 'OtherPay', 'Benefits', 'TotalPay', 'TotalPayBenefits', 'Year', 'Notes', 'Agency', 'Status']



def getting_the_mean():

    print("the mean of the column")
    data['BasePay'] = pd.to_numeric(data['BasePay'])
    print(data['BasePay'].mean())




def getting_from_year():
    
    print(data[data['Year'] < 2014]['Year'])
    print(len(data[data['Year'] < 2014]['Year']))


def getting_info_from_agency():


    stack = []
    for x in data['Agency']:
        
        if x not in stack:
            stack.append(x)

    print(stack)



def getting_info_title():
    
    stack = []
    for x in data['JobTitle']:
        if x not in stack:
            stack.append(x)
    print(stack)





def playing_with_the_years():

    print("getting all the variants of years")
    
    headers = list()
    stack_year = list()
    data_analysis = list()
    
    for j in data:
        headers.append(j)
    print(headers)

    for x in data['Year']:
        
        if x not in stack_year:
            stack_year.append(x)

    

    stack_analysis = list()
    for i in stack_year:
        #print(i)
        #print("The mean of base pay from the year {}".format(i))
        #stack_analysis.append(pd.to_numeric(data[data['Year'] == int(i)]['BasePay']).mean())
        
        data_analysis.append({i: pd.to_numeric(data[data['Year'] == int(i)]['BasePay']).mean()})

    pprint(data_analysis)


    #print("Printing about the base pay from the year 2011")
    #print(pd.to_numeric(data[data['Year'] == 2011]['BasePay']).mean())

print(data['Benefits'].dropna())
playing_with_the_years()



def viewing_status():
        
    stack = []
    for x in data['Status']:
        if x not in stack:
            stack.append(x)

    print(stack)



def viewing_covid():

    headers = list()
    all_data = list()

    covid = pd.read_csv(COVID_URL)
    
    for x in covid:
        if x not in headers:
            headers.append(x)

    #print(headers)
    #print(covid[covid['Name'] == "Ecuador"][['Name', 'Cases - cumulative total']])


    covid = covid[covid['Name'] == 'Ecuador']
     
    #print(covid)

    for x in covid:

        all_data.append({x: covid[x]})

    #pprint(all_data)

    for k in all_data:

        print(k)






