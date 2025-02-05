class TreeNode:
   def __init__(self, data, left = None, right = None):
      self.data = data
      self.left = left
      self.right = right


def insert(temp,data):
   que = []
   que.append(temp)
   while (len(que)):
      temp = que[0]
      que.pop(0)
      if (not temp.left):
         if data is not None:
            temp.left = TreeNode(data)
         else:
            temp.left = TreeNode(0)
         break
      else:
         que.append(temp.left)
      if (not temp.right):
         if data is not None:
            temp.right = TreeNode(data)
         else:
            temp.right = TreeNode(0)
         break
      else:
         que.append(temp.right)
def make_tree(elements):
   Tree = TreeNode(elements[0])
   for element in elements[1:]:
      insert(Tree, element)
   return Tree

class Solution(object):
   def isValidBST(self, root):
      return self.solve(root,-1000000000000000000000,1000000000000000000000)
   def solve(self,root,min_val,max_val):
      if root == None or root.data == 0:
         return True
      if (root.data <= min_val or root.data >=max_val):
         return False
      return self.solve(root.left,min_val,root.data) and self.solve(root.right,root.data,max_val)
ob1 = Solution()

tree = make_tree([3,1,4,None,2,None,5])
print(ob1.isValidBST(tree))
tree = make_tree([5,1,4,None,None,3,6])
print(ob1.isValidBST(tree))