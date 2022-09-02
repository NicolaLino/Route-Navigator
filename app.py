from turtle import color
import folium
from numpy import source
from shortestpathsalgos import *
from graph import create_graph
from rich.console import Console
from rich import print
from rich.columns import Columns
import webbrowser
import networkx as nx


console = Console()
g, points = create_graph()
console.print("\n\nShortest Path Finder By Nicola && Omar",
              style="bright_red", justify="center")
console.print("\nCities : ", style="bright_red underline")
console.print(Columns(points), style="bright_white underline")
webbrowser.open_new_tab('map.html')
cities = []
console.print('''
        1. Walking
        2. driving
    Enter A Number : 
    ''', style="bold bright_blue")
ch = int(input())
for key in points:
    cities.append(key)
while True:
    console.print('''
        Choose Shortest path algorithm :
        1. BFS
        2. greedy
        3. A*
        0. exit

    Enter A Number : 
    ''', style="bold bright_blue")
    while True:
        choice = int(input())
        if choice == 1:
            console.print("Enter source City: ", style="bright_blue")
            source = (input()).capitalize()
            if source not in cities:
                print("Enter a exciting city")
                break
            console.print("Enter target City: ", style="bright_blue")
            dest = (input()).capitalize()
            path = BFS(g, source, dest)
            break
        elif choice == 2:
            console.print("Enter source City: ", style="bright_blue")
            source = (input()).capitalize()
            console.print("Enter target City: ", style="bright_blue")
            dest = (input()).capitalize()
            path = BFS(g, source, dest)
            path = greedy(g, source, dest)
            break
        elif choice == 3:
            console.print("Enter source City: ", style="bright_blue")
            source = (input()).capitalize()
            console.print("Enter target City: ", style="bright_blue")
            dest = (input()).capitalize()
            path = BFS(g, source, dest)
            path = astar(g, source, dest, heuristic=None, weight="weight")
            break
        elif choice == 0:
            exit()
        else:
            console.print("Enter a Valid Number!",
                          style="bright_red bold underline")

    console.print(f"PATH : {path}")
    m = folium.Map(location=[31.70487, 35.20376], zoom_start=8)
    for key, [lat, long] in points.items():
        folium.Marker([lat, long], popup=key).add_to(m)

    pts = []
    for city in path:
        pts.append((points[city][0], points[city][1]))
    folium.PolyLine(pts, color="red").add_to(m)
    m.save('map.html')
    # webbrowser.open_new_tab('map.html')
