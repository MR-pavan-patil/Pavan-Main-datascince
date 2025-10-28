import itertools

def tsp_dynamic_programming(cost_matrix):
    n = len(cost_matrix)
    all_cities = list(range(n))
    memo = {}

    def tsp_helper(mask, pos):
        if mask == (1 << n) - 1:
            return cost_matrix[pos][0]
        if (mask, pos) in memo:
            return memo[(mask, pos)]

        min_cost = float('inf')

        for city in range(n):
            if (mask >> city) & 1 == 0:
                new_cost = cost_matrix[pos][city] + tsp_helper(mask | (1 << city), city)
                min_cost = min(min_cost, new_cost)

        memo[(mask, pos)] = min_cost
        return min_cost

    return tsp_helper(1, 0)

# Example usage
if __name__ == "__main__":
    cost_matrix = [
        [0, 29, 20, 21],
        [29, 0, 15, 18],
        [20, 15, 0, 16],
        [21, 18, 16, 0]
    ]

    shortest_route_cost = tsp_dynamic_programming(cost_matrix)
    print("Shortest route cost:", shortest_route_cost)