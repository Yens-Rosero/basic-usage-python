# utils.py

def get_population(country_dict):
    # """
    # Obtiene los datos de población de un país dado en forma de diccionario.
    
    # Args:
    #     country_dict (dict): Diccionario que contiene los datos de un país.
    
    # Returns:
    #     tuple: Tupla de dos elementos. El primer elemento es una lista de etiquetas
    #            de años y el segundo elemento es una lista de valores de población.
    # """
    population_dict = {
        '2022' : int(country_dict['2022 Population']),
        '2020' : int(country_dict['2020 Population']),
        '2015' : int(country_dict['2015 Population']),
        '2010' : int(country_dict['2010 Population']),
        '2000' : int(country_dict['2000 Population']),
        '1990' : int(country_dict['1990 Population']),
        '1980' : int(country_dict['1980 Population']),
        '1970' : int(country_dict['1970 Population']),
    }

    labels = population_dict.keys()
    values = population_dict.values()
    return population_dict.keys(), population_dict.values()

def filter_by_countries(data, countries):
    # """
    # Filtra los datos por países especificados.
    
    # Args:
    #     data (list): Lista de diccionarios que contienen los datos de los países.
    #     countries (list): Lista de nombres de países a filtrar.
    
    # Returns:
    #     list: Lista de diccionarios filtrados que contienen los datos de los países especificados.
    # """
    return [country for country in data if country['Country'] in countries]
