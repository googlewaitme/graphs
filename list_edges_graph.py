from collections import namedtuple, defaultdict


Edge = namedtuple("Edge", ["parent", "kid", "weight"])


class ListEdgesGraph:
    def __init__(self, adjacency_matrix: list[list[int]], labels: list[str]):
        self.labels = labels
        self.edges: list[Edge] = []
        self.set_of_edges = set()
        self.__init_list_of_edges(adjacency_matrix)

    def __init_list_of_edges(self, adjacency_matrix) -> None:
        for parent_id in range(len(self.labels)):
            for kid_id in range(len(self.labels)):
                edge = Edge(parent_id, kid_id, adjacency_matrix[parent_id][kid_id])
                if edge.weight:
                    self.edges.append(edge)
                    self.set_of_edges.add((parent_id, kid_id))

    def get_neighbours_by_index(self, index: int) -> list[int]:
        kids = self.get_kids_by_index(index)
        parents = self.get_parents_by_index(index)
        return sorted(kids + parents)

    def get_kids_by_index(self, parent_index: int) -> list[int]:
        kids = []
        for edge in self.edges:
            if edge.parent == parent_index:
                kids.append(edge.kid)
        return kids

    def get_parents_by_index(self, kid_index: int) -> list[int]:
        parents = []
        for edge in self.edges:
            if edge.kid == kid_index:
                parents.append(edge.parent)
        return parents

    def is_path_by_names(self, path: list[str]) -> bool:
        path = [self.get_index_by_name(name) for name in path]
        return self.is_path_by_indexes(path)

    def is_path_by_indexes(self, path: list[int]) -> bool:
        path_edges = set()
        for index in range(1, len(path)):
            path_edges.add((path[index-1], path[index]))
        return path_edges.issubset(self.set_of_edges)

    def get_index_by_name(self, name: str) -> int:
        for index, value in enumerate(self.labels):
            if value == name:
                return index
        raise ValueError

    def get_indexes_sum_incident_edges_more_than(self, criterion: int) -> list[int]:
        vertexes_sum_incident_edges = defaultdict(int)
        for edge in self.edges:
            vertexes_sum_incident_edges[edge.parent] += edge.weight
            vertexes_sum_incident_edges[edge.kid] += edge.weight
        filtered_vertexes = []
        for vertex, sum_incident_edges in vertexes_sum_incident_edges.items():
            if sum_incident_edges > criterion:
                filtered_vertexes.append(vertex)
        return sorted(filtered_vertexes)

    def get_count_of_edges(self) -> int:
        return len(self.edges)

