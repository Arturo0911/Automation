#!/usr/bin/python3



import seaborn as sns
import matplotlib.pyplot as plt

def main():


    """
        sns.joinplot() use two columns to draw in the chart
        warning:
            - every column should  have numerics information
    """

    tips = sns.load_dataset('tips')
    print(tips.head())
    
    #sns.displot(tips['total_bill'], kde=False, bins = 30)
    
    # sns.jointplot(x= "total_bill", y="tip", data = tips, kind="reg")
    # sns.pairplot(tips, hue= "sex")
    #sns.rugplot(tips['total_bill'])
    sns.displot(tips['total_bill'], kde=True)
    plt.show()


if __name__ == '__main__':
    main()
