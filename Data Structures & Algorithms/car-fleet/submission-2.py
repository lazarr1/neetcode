class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        posSpeed = zip(position, speed)

        sortedZip = sorted(posSpeed, key=lambda i: i[0])
        posSpeed = list(sortedZip)

        ans = len(position)
        maxStack = [ans - 1]
        for i in range(len(posSpeed) - 2, -1, -1):
            limitingCar = posSpeed[maxStack[-1]]
            if (((target - limitingCar[0]) / limitingCar[1]) >= ((target - posSpeed[i][0]) / posSpeed[i][1])):
                ans -= 1
            else:
                maxStack.append(i)
            
        return ans