import csv_reader



def get_country_population(country, data):
    try: 
        def yearificator(tuple):
            pyear =tuple[0]
            return pyear[:4], tuple[1]

        countrylist = list(filter(lambda x: x['Country/Territory'] == country , data))
        countrydict = countrylist[0]
        countryitems = list(countrydict.items())
        years = filter(lambda x: 'Population' in x[0] and not 'Percentage' in x[0], countryitems)
        years = map(yearificator, years)
        #print(list(years))

        yeardic = {x:int(y) for x,y in years}
        #labels = [key for key, value in yeardic.items()]
        #values = [value for key, value in yeardic.items()]
        return list(yeardic.keys()), list(yeardic.values())
    except IndexError:
        print("país no encontrado :c")
        return [],[]
    
def get_population_percentage(data):

    dict_countries = []
    dict_popupercentage = []
    for row in data: dict_countries.append({x:y for x,y in row.items() if x == 'Country/Territory'})
    for row in data: dict_popupercentage.append({x:y for x,y in row.items() if x == 'World Population Percentage'})
    labels=[key['Country/Territory'] for key in dict_countries]
    values = [key['World Population Percentage'] for key in dict_popupercentage]
    return labels, values
    #values = map(filter(lambda x: x == x['World Population Percentage'], data ), data)

   
        
    
    

if __name__ == "__main__":
   # get_country_population('Argentina', csv_reader.readcsv(r"C:\codigos\python\app\data.csv"))
    print(get_population_percentage(csv_reader.readcsv(r"C:\codigos\python\app\data.csv")))


