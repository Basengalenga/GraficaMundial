import matplotlib.pyplot as plt

def barchart(labels,values):
    fig, ax = plt.subplots()
    ax.bar(labels,values)
    plt.show()

def piechart(labels,values):
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels) #porque así funciona el piechart xd y hay que seguir las reglas xdddd
    ax.axis('equal') #centra y dice que será un círculo
    plt.show()

if __name__ == '__main__':
    labels = ['a','b','0']
    values = [1,2,3]
    piechart(labels,values)