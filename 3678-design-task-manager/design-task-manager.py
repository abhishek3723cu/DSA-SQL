import heapq

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task_map = {}  # taskId -> (userId, priority)
        self.heap = []      # max-heap storing (-priority, -taskId, taskId)
        
        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId: int, newPriority: int) -> None:
        userId, _ = self.task_map[taskId]
        self.task_map[taskId] = (userId, newPriority)
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]  # lazy removal (won’t remove from heap immediately)

    def execTop(self) -> int:
        while self.heap:
            priority, negTaskId, taskId = heapq.heappop(self.heap)
            if taskId in self.task_map:
                userId, storedPriority = self.task_map[taskId]
                if storedPriority == -priority:  # ensure priority is latest
                    del self.task_map[taskId]
                    return userId
        return -1
