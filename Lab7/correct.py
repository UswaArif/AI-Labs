# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 14:11:13 2023

@author: TORA TECH
"""

import random

cities = ["1", "2", "3", "4"]
distances = {
    ("1", "2"): 10,
    ("2", "1"): 10,
    ("1", "4"): 20,
    ("1", "3"): 15,
    ("2", "4"): 25,
    ("2", "3"): 35,
    ("3", "2"): 35,
    ("3", "4"): 30,
    ("3", "1"): 15,
    ("4", "1"): 20,
    ("4", "2"): 25,
    ("4", "3"): 30,
}

population_size = 100
mutation_rate = 0.01
crossover_rate = 0.7  
generations = 10

def create_individual(cities):
    return random.sample(cities, len(cities))

def calculate_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        city1, city2 = route[i], route[i + 1]
        total_distance += distances[(city1, city2)]
    return total_distance + distances[(route[-1], route[0])]  


def genetic_algorithm(cities, distances, population_size, mutation_rate, crossover_rate, generations):
    population = [create_individual(cities) for _ in range(population_size)]

    for generation in range(generations):
        population = sorted(population, key=lambda x: calculate_distance(x, distances))
        best_route = population[0]
        print(f"Generation {generation}: Best distance = {calculate_distance(best_route, distances)}")

        new_population = [best_route]

        while len(new_population) < population_size:
            if random.random() < crossover_rate:
                parent1, parent2 = random.choices(population[:10], k=2)
                crossover_point = random.randint(0, len(parent1))
                child = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
            else:
                child = random.choice(population)

            if random.random() < mutation_rate:
                index1, index2 = random.sample(range(len(child)), 2)
                child[index1], child[index2] = child[index2], child[index1]

            new_population.append(child)

        population = new_population

    return best_route, calculate_distance(best_route, distances)

best_route, best_distance = genetic_algorithm(cities, distances, population_size, mutation_rate, crossover_rate, generations)
print(f"Best route: {best_route}")
print(f"Total distance: {best_distance}")
