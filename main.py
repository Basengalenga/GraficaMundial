import csv_reader
import valuator
import charts

data = csv_reader.readcsv("data.csv")
request = input("Desea consultar la población de un país en específico o el porcentaje de población mundial? (p/m)").lower()

if request == 'p': #Población de país
    country = input('Escriba el país al que va a consultar: ').capitalize()
    labels, values = valuator.get_country_population(country, data)

    if len(labels) != 0:
        print("País encontrado con éxito")
        grafica = input('Desea barras o pastel? (b/p))').lower()
        if grafica == 'b':
            charts.barchart(labels,values)
        elif grafica == 'p':
            charts.piechart(labels,values)
        else:
            print("Error: No se ha encontrado la gráfica que desea")

elif request == 'm': #Población mundial
    labels, values = valuator.get_population_percentage(data)
    charts.piechart(labels,values)