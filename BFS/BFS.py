import queue


class BFS():
    def __init__(self, adj, source):
        self.q = queue.queue()
        for vertex in adj:
            vertex.color = 'white'
            vertex.parent = None
            vertex.distance = None

        source.color = 'grey'
        source.distance = 0
        self.q.enqueue(source)

        while not self.q.isEmpty():
            frontier = self.q.dequeue()
            for neighbor in frontier.neighbors:
                if neighbor.color is 'white':
                    neighbor.color = 'grey'
                    neighbor.distance = frontier.distance + 1
                    neighbor.parent = frontier
                    self.q.enqueue(neighbor)
            frontier.color = 'black'
