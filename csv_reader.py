import csv

def readcsv(path):
    with open(path, 'r') as file:
        #charge the csv and makes it an iterable that uses lists:
        readfile = csv.reader(file, delimiter=',') # delimiter because some codes are separated by other characters like ";"
        header = next(readfile)          #Here you iterate manually the first row         
        data = []
        for row in readfile:     #starts from the second row, because we have already iterated it
            dictionary = {eheader: erow for eheader, erow in zip(header, row)}
            data.append(dictionary)
        return data
            
    

if __name__ == "__main__":
    data = readcsv(r"C:\codigos\python\app\data.csv")
    print(data)