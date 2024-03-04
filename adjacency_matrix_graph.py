class AdjacencyMatrixGraph:
    def __init__(self, adjacency_matrix: list[list[int]], labels: list[str]):
        self.adjacency_matrix = adjacency_matrix
        self.labels = labels

    def get_neighbours_by_index(self, index: int) -> list[int]:
        kids = self.get_kids_by_index(index)
        parents = self.get_parents_by_index(index)
        return sorted(kids + parents)

    def get_kids_by_index(self, index: int) -> list[int]:
        kids = []
        for line in range(len(self.labels)):
            if self.adjacency_matrix[index][line] > 0:
                kids.append(line)
        return kids

    def get_parents_by_index(self, index: int) -> list[int]:
        parents = []
        for line in range(len(self.labels)):
            if self.adjacency_matrix[line][index] > 0:
                parents.append(line)
        return parents

    def is_path_by_names(self, path: list[str]) -> bool:
        path = [self.get_index_by_name(name) for name in path]
        return self.is_path_by_indexes(path)

    def is_path_by_indexes(self, path: list[int]) -> bool:
        for index in range(1, len(path)):
            parent, kid = path[index-1], path[index]
            if self.adjacency_matrix[parent][kid] == 0:
                return False
        return True

    def get_index_by_name(self, name: str) -> int:
        for index, value in enumerate(self.labels):
            if value == name:
                return index
        raise ValueError

    def get_indexes_sum_incident_edges_more_than(self, criterion: int) -> list[int]:
        filtered_vertexes = []
        for vertex in range(len(self.adjacency_matrix)):
            sum_incident_edges = 0
            for line in range(len(self.adjacency_matrix)):
                sum_incident_edges += self.adjacency_matrix[line][vertex]
                sum_incident_edges += self.adjacency_matrix[vertex][line]
            if sum_incident_edges > criterion:
                filtered_vertexes.append(vertex)
        return filtered_vertexes

    def get_count_of_edges(self) -> int:
        count = 0
        for i in range(len(self.adjacency_matrix)):
            for j in range(len(self.adjacency_matrix)):
                if self.adjacency_matrix[i][j] > 0:
                    count += 1
        return count

