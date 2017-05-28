import heapq


class Node:
    def __init__(self):
        self.elements = []

    def isEmpty(self):
        return len(self.elements) == 0

    def put(self, element, targetFunction):
        heapq.heappush(self.elements, (targetFunction, element))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def contains(self, element):
        for nodeElement in self.elements:
            if nodeElement[1] == element:
                return True
        return False

    def checkTargetFunction(self, element):
        for nodeElement in self.elements:
            if nodeElement[1] == element:
                return nodeElement[0]
        return -1

