from list_edges_gpaph import ListEdgesGraph
from adjacency_matrix_graph import AdjacencyMatrixGraph
from list_edges_graph import ListEdgesGraph

adjacency_matrix = [
    [0, 0, 0, 5, 0, 0],
    [2, 0, 0, 3, 0, 0],
    [0, 1, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 4, 7, 0, 1],
    [0, 0, 4, 7, 0, 0]
]
labels = ['Rook', 'Knight', 'Bishop', 'Pawn', 'King', 'Queen']

graphs = {
    "0": ListEdgesGraph(adjacency_matrix, labels),
    "1": AdjacencyMatrixGraph(adjacency_matrix, labels),
    "2": ListEdgesGraph(adjacency_matrix, labels)
}

def calc(graph_id: str, algorithm_id):
    graph = graphs[graph_id]
    if algorithm_id == "1":
        node_index = input("Index need for find neighbours: ")
        result = graph.get_neighbours_by_index(int(node_index))
        print("neighbours:", result)
    elif algorithm_id == "2":
        count_of_edges = graph.get_count_of_edges()
        print("Count of edges", count_of_edges)
    elif algorithm_id == "3":
        criterion = int(input("Input criterie: "))
        result = graph.get_indexes_sum_incident_edges_more_than(criterion)
        print(f"Indexes with sum incident edges more than {criterion}:", result)
    elif algorithm_id == "4":
        print("Input path on next line(example: King Queen Bishop)")
        path = input().split()
        result = graph.is_path_by_names(path)
        print('Path is exists:', result)
    else:
        print('ERROR COMMAND NOT FOUND')


def main():
    while True:
        print("$$$ new cycle $$$")
        choose_graph_question = """choose format
    0) list_of_edges
    1) adjacency_matrix
    2) array_of_records:
    write "exit" to exit
input here: """
        graph_id = input(choose_graph_question)

        if graph_id.lower().strip() == "exit":
            print('bye bye')
            return
        if graph_id not in graphs:
            print('choose digit 0, 1, 2')
            continue
        
        choose_algorithm_question = """choose algorithm
    1) get neighbours
    2) get count of edges
    3) get indexes sum incident edges more than
    4) check is path
input here: """
        algorithm_id = input(choose_algorithm_question) 
        if (not algorithm_id.isdigit()) or int(algorithm_id) not in [1, 2, 3, 4]:
            print('choose digit 1, 2, 3 or 4')
            continue
        calc(graph_id, algorithm_id)
        

if __name__ == "__main__":
    main()
