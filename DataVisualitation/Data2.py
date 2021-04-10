#!/usr/bin/python3



import seaborn as sns
import matplotlib.pyplot as plt

def main():

    tips = sns.load_dataset('tips')
    print(tips.head())
    
    #sns.displot(tips['total_bill'], kde=False, bins = 30)
    
    #sns.jointplot(x= "total_bill", y="tip", data = tips, kind="reg")
    sns.pairplot(tips, hue= "sex")
    plt.show()


if __name__ == '__main__':
    main()
