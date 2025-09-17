import heapq
from collections import defaultdict

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.foodToCuisine = {}
        self.foodToRating = {}
        self.cuisineToHeap = defaultdict(list)
        
        for f, c, r in zip(foods, cuisines, ratings):
            self.foodToCuisine[f] = c
            self.foodToRating[f] = r
            heapq.heappush(self.cuisineToHeap[c], (-r, f))  # max-heap behavior

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.foodToCuisine[food]
        self.foodToRating[food] = newRating
        heapq.heappush(self.cuisineToHeap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisineToHeap[cuisine]
        # Lazy cleanup: remove outdated entries
        while heap:
            rating, food = heap[0]
            if -rating == self.foodToRating[food]:
                return food
            heapq.heappop(heap)  # discard stale entry
