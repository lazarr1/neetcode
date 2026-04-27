def distance(x1, x2, y1, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def distanceToOrigin(x1, y1):
    return distance(x1, 0, y1, 0)

class Solution:

    class Point:
        def __init__(self, point):
            self.point = point
            self.distance = -distanceToOrigin(point[0], point[1])

        
        def __lt__(self, other):
            return self.distance < other.distance

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        test = [self.Point(point) for point in points]
        heapq.heapify(test)

        while len(test) > k:
            heapq.heappop(test)

        
        return [point.point for point in test]


        