# https://leetcode.com/problems/redundant-connection/description/?envType=daily-question&envId=2025-01-29
from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0] * len(edges)
        print(parent)
        def find(x):
            if parent[x] == 0:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            if rootx == rooty:
                return False
            parent[rootx] = rooty
            return True
        for x, y in edges:
            if not union(x - 1, y - 1):
                return [x, y]
        return []
if __name__ == "__main__":
    edges = [[1,2], [1,3], [2,3]]
    print(Solution().findRedundantConnection(edges))  # [2, 3]
    edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    print(Solution().findRedundantConnection(edges))  # [1, 4]
    edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]
    print(Solution().findRedundantConnection(edges))  # [2, 5]
    edges = [[1,4],[3,4],[1,3],[1,2],[4,5]]
    print(Solution().findRedundantConnection(edges))  # [1, 3]
    edges = [[1,4],[3,4],[1,3],[1,2],[4,5],[2,5]]
    print(Solution().findRedundantConnection(edges))  # [2, 5]
    edges = [[1,4],[3,4],[1,3],[1,2],[4,5],[2,5],[1,5]]
    print(Solution().findRedundantConnection(edges))  # [1, 5]
    edges = [[1,4],[3,4],[1,3],[1,2],[4,5],[2,5],[1,5],[2,3]]
    print(Solution().findRedundantConnection(edges))  # [2, 3]
    edges = [[1,4],[3,4],[1,3],[1,2],[4,5],[2,5],[1,5],[2,3],[1,5]]
    print(Solution().findRedundantConnection(edges))  # [1, 5]
    edges = [[1,4],[3,4],[1,3],[1,2],[4,5],[2,5],[1,5],[2,3],[1,5],[1,4]]
    print(Solution().findRedundantConnection(edges))  # [1, 4]
    edges = [[1,4],[3,4],[1,3],[1,2],[4,5],[2,5],[1,5],[2,3],[1,5]]

# Time: O(N)
# Space: O(N)
# Runtime: 52 ms, faster than 99.46% of Python3 online submissions for Redundant Connection.
# Memory Usage: 14.6 MB, less than 49.35% of Python3 online submissions for Redundant Connection.
