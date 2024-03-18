# main.py

import utils
import read_csv
import charts

def run(): 
    # """
    # Función principal que carga los datos, filtra por países ingresados por el usuario
    # y genera gráficos de población para cada país.
    # """
    data = read_csv.load_data('data.csv')
    countries = input('Ingrese los países a graficar: ').split(',')

    for country in countries:
        result = utils.filter_by_countries(data, [country])
        if len(result) > 0:
            country_data = result[0]
            label, values = utils.get_population(country_data)
            charts.generate_bar_chart(label, values, country)
        else:
            print(f'No se encontraron datos para {country}')

if __name__ == '__main__':
    run()
