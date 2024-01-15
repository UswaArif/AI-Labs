# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:32:52 2023

@author: TORA TECH
"""
# CLASS NODE
class Node:
    def __init__(self, value):
        self.vertex = value
        self.next = None

#CLASS GRAPH
class Graph:
    def __init__(self, number):
        self.Vertex = number
        self.graph = [None] * self.Vertex

    def add_edge(self, s, d):
        node = Node(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = Node(s)
        node.next = self.graph[d]
        self.graph[d] = node

    def print_graph(self):
        for i in range(self.Vertex):
            print("Vertex " , i ,": ", end="")
            temp = self.graph[i]
            while temp:
                print(" -> ",temp.vertex, end="")
                temp = temp.next
            print(" \n")

    def delete_edge(self, s, d):
        temp = self.graph[s]
        if temp and temp.vertex == d:
            self.graph[s] = temp.next
            temp = None
            return

        while temp:
            if temp.vertex == d:
                break
            prev = temp
            temp = temp.next

        if not temp:
            return

        prev.next = temp.next
        temp = None

        temp = self.graph[d]
        if temp and temp.vertex == s:
            self.graph[d] = temp.next
            temp = None
            return

        while temp:
            if temp.vertex == s:
                break
            prev = temp
            temp = temp.next

        if not temp:
            return

        prev.next = temp.next
        temp = None
        
    def get_connected_nodes(self, node_name):
        connected_nodes = []
        
        for i in range(self.Vertex):
            temp = self.graph[i]
            while temp:
                if temp.vertex == node_name:
                    connected_nodes.append(i)
                temp = temp.next

        return connected_nodes

    def get_edge(self, node1, node2):
        for i in range(self.Vertex):
            if i == node1:
                temp = self.graph[i]
                while temp:
                    if temp.vertex == node2:
                        return (node1, node2)
                    temp = temp.next
        return None

    def are_connected(self, node1, node2):
        for i in range(self.Vertex):
            if i == node1:
                temp = self.graph[i]
                while temp:
                    if temp.vertex == node2:
                        return True
                    temp = temp.next
        return False

    def is_valid_path(self, path):
        for i in range(len(path) - 1):
            if not self.are_connected(path[i], path[i + 1]):
                return False
        return True


Vertex = 5

graph = Graph(Vertex)
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 2)
#printing graph
graph.print_graph()

#deleting Edge
graph.delete_edge(0, 2)

print("After deleting edge, the graph is: ")
graph.print_graph()

#Checking connecting nodes to a specific node
connected_nodes = graph.get_connected_nodes(0)
print("Connected nodes to vertex 0:", connected_nodes)

#getting edge between two nodes
edge = graph.get_edge(0, 3)
print("Edge between node 0 and node 3:", edge)

#Checking nodes between two nodes
connected = graph.are_connected(0, 3)
print("Nodes 0 and 3 are connected:", connected)

#Checking if a path is valid or not
valid_path = graph.is_valid_path([0,1,2])
print("Is [0, 1, 2] a valid path:", valid_path)