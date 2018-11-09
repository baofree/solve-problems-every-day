"""
A robot on an infinite grid starts at point (0, 0) and faces north.
The robot can receive one of three possible types of commands:

-2: turn left 90 degrees
-1: turn right 90 degrees
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles.

The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])

If the robot would try to move onto them,
the robot stays on the previous grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will be from the origin.


Example 1:
Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)

Example 2:
Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and going to (1, 8)


"""


class Solution:

    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        result = 0
        direction_x = [0, 1, 0, -1]
        direction_y = [1, 0, -1, 0]
        cur_direction = 0  # 0:north, 1:east, 2:south, 3:west
        position = [0, 0]
        obstacle_set = set(map(tuple, obstacles))
        for command in commands:
            if command in [-1, -2]:
                if command == -1:
                    cur_direction = (cur_direction + 1) % 4
                elif command == -2:
                    cur_direction = (cur_direction - 1) % 4
            else:
                for step in range(command):
                    if (position[0] + direction_x[cur_direction],
                        position[1] + direction_y[cur_direction]) not in obstacle_set:
                        position[0] += direction_x[cur_direction]
                        position[1] += direction_y[cur_direction]
                        result = max(result, position[0] ** 2 + position[1] ** 2)
        return result


if __name__ == '__main__':
    solution = Solution()
    # print(solution.robotSim([-1, -1, -1, -1, -1, -1], []))
    # print(solution.robotSim([4, -1, 3], []))  # (3, 4)
    print(solution.robotSim([4, -1, 4, -2, 4], [[2, 4]]))  # (1, 8)
    # print(solution.robotSim([4, -1, 4, -2, 4], [[2, 4], [1, 2]]))  # (1, 8)
