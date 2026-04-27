class Solution:

    class Task:
        def __init__(self, task, repeats):
            self.task = task
            self.repeats = -repeats
            self.lastSched = -9999

        def __lt__(self, other):
            return self.repeats < other.repeats


    def leastInterval(self, tasks: List[str], n: int) -> int:
        ans = 0
        taskCount = {}
        for task in tasks:
            taskCount[task] = taskCount.get(task, 0) + 1
        
        tasks = [self.Task(task, repeat) for task, repeat in taskCount.items()]
        heapq.heapify(tasks)

        waitStack = deque([])
        while tasks or waitStack:
            while waitStack and ans - waitStack[0].lastSched >= n:
                heapq.heappush(tasks, waitStack.popleft())

            if tasks:
                task = heapq.heappop(tasks)
                ans += 1
                task.repeats += 1
                task.lastSched = ans

                if task.repeats != 0:
                    waitStack.append(task)

            else:
                ans = waitStack[0].lastSched + n

        return ans


        






