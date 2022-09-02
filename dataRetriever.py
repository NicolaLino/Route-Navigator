import pandas as pd


def getGraphPoints():
    df = pd.read_csv('DBC.csv')
    gp = df.to_dict()
    cities = []
    city_list = pd.read_csv('Lat_Long.csv')

    for i in city_list['City']:
        cities.append(i)

    gp.pop('Unnamed: 0')
    graph = {}
    for key in gp:
        tem = {}
        for j in gp[key]:
            tem[cities[j]] = gp[key][j]
        graph[key] = tem

    data_lat_long = pd.read_csv('Lat_Long.csv')
    dict_data_lat = data_lat_long.to_dict()
    points = {}
    for i in range(len(cities)):
        points[dict_data_lat['City'][i]] = (
            dict_data_lat['Latitude'][i], dict_data_lat['Longitude'][i])
    return (graph, points)
