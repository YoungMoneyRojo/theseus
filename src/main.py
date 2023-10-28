from flask import Flask, redirect, url_for, request, render_template
from graph import IndoorNav
from Feature import Feature
from Edge import Edge
from Landmark import Landmark

app = Flask(__name__)
graph = IndoorNav()

f1 = Feature("101")
f2 = Feature("102")
f3 = Feature("103")
f4 = Feature("104")
l1 = Landmark("1")

f5 = Feature("201")
f6 = Feature("202")
f7 = Feature("203")
f8 = Feature("204")
l2 = Landmark("2")

f9 = Feature("301")
f10 = Feature("302")
f11 = Feature("303")
f12 = Feature("304")
l3 = Landmark("3")
    
e1 = Edge(l1, f1)
e2 = Edge(l1, f2)
e3 = Edge(l1, f3)
e4 = Edge(l1, f4)

e5 = Edge(l2, f5)
e6 = Edge(l2, f6)
e7 = Edge(l2, f7)
e8 = Edge(l2, f8)

e9 = Edge(l3, f9)
e10 = Edge(l3, f10)
e11 = Edge(l3, f11)
e12 = Edge(l3, f12)

e13 = Edge(l1, l2, 2)
e14 = Edge(l2, l3, 2)

graph.add_edge(e1)
graph.add_edge(e2)
graph.add_edge(e3)
graph.add_edge(e4)
graph.add_edge(e5)
graph.add_edge(e6)
graph.add_edge(e7)
graph.add_edge(e8)
graph.add_edge(e9)
graph.add_edge(e10)
graph.add_edge(e11)
graph.add_edge(e12)
graph.add_edge(e13)
graph.add_edge(e14)

f13 = Feature("401")
f14 = Feature("402")
l4 = Landmark("4")

e15 = Edge(l4, f13)
e16 = Edge(l4, f14)
e17 = Edge(l4, f5)
e18 = Edge(l4, f9, 3)
    
graph.add_edge(e15)
graph.add_edge(e16)
graph.add_edge(e17)
graph.add_edge(e18)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':

        if request.form.get('run') == 'Run Program!':
            path = graph.find_shortest_path(graph.find_node_by_name(request.form.get("from")), graph.find_node_by_name(request.form.get("to")))
            
            render_template('homepage.html', instructions = graph.print_path(path))
            pass



if __name__ == '__main__':
    graph = IndoorNav()

    f1 = Feature("101")
    f2 = Feature("102")
    f3 = Feature("103")
    f4 = Feature("104")
    l1 = Landmark("1")

    f5 = Feature("201")
    f6 = Feature("202")
    f7 = Feature("203")
    f8 = Feature("204")
    l2 = Landmark("2")

    f9 = Feature("301")
    f10 = Feature("302")
    f11 = Feature("303")
    f12 = Feature("304")
    l3 = Landmark("3")
    
    e1 = Edge(l1, f1)
    e2 = Edge(l1, f2)
    e3 = Edge(l1, f3)
    e4 = Edge(l1, f4)

    e5 = Edge(l2, f5)
    e6 = Edge(l2, f6)
    e7 = Edge(l2, f7)
    e8 = Edge(l2, f8)

    e9 = Edge(l3, f9)
    e10 = Edge(l3, f10)
    e11 = Edge(l3, f11)
    e12 = Edge(l3, f12)

    e13 = Edge(l1, l2, 2)
    e14 = Edge(l2, l3, 2)

    graph.add_edge(e1)
    graph.add_edge(e2)
    graph.add_edge(e3)
    graph.add_edge(e4)
    graph.add_edge(e5)
    graph.add_edge(e6)
    graph.add_edge(e7)
    graph.add_edge(e8)
    graph.add_edge(e9)
    graph.add_edge(e10)
    graph.add_edge(e11)
    graph.add_edge(e12)
    graph.add_edge(e13)
    graph.add_edge(e14)

    f13 = Feature("401")
    f14 = Feature("402")
    l4 = Landmark("4")

    e15 = Edge(l4, f13)
    e16 = Edge(l4, f14)
    e17 = Edge(l4, f5)
    e18 = Edge(l4, f9, 3)
    
    graph.add_edge(e15)
    graph.add_edge(e16)
    graph.add_edge(e17)
    graph.add_edge(e18)
    

    path = graph.find_shortest_path(f10, f14)
    print(graph.print_path(path))
    
    # print(len(graph.paths))
    # for path in graph.paths:
    #     print(graph.print_path(path))


    #app.run(debug=True)

