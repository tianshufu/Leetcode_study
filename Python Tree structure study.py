class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

class Tree:
    #Clarify the root of the tree
    def __init__(self,root=None):
        self.root=root

    def PrintTree(self):
        print(self.data)

    def add(self,item):
        node=Node(item)
        #if the data is empty, then return nothing
        if self.root is None:
            self.root=node
            return
        #if not,put the data into a queue
        queue=[self.root]
        while queue:
            #Select the judge node from the queue
            cur_node=queue.pop(0)
            # if the node's left child is empty
            if cur_node.left is None:
                # put the node under the left child of the node
                cur_node.left=node
                return
            else:
                #if the left child is not empty, then we should put it into the try list
                queue.append(cur_node.left)
            if cur_node.right is None:
                cur_node.right=node
                return
            else:
                queue.append(cur_node.right)

    def breadth_travel(self):
        # First ,put the root into the queue
        queue=[self.root]
        print("Breadth traverse:")
        while queue:
            cur_node=queue.pop(0)
            print(cur_node.data)
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)




    def depth_travel_xianxu(self,node,list):
        #xianxu traverse
        #if the node is empty

        if node==None:
            return
        print(node.data)
        list.append(node.data)
        #return node.data
        #list.append(node.data)
        #return node.data
        self.depth_travel_xianxu(node.left,list)
        self.depth_travel_xianxu(node.right,list)
        return list
        #return node.data

    #define a function to get the list of the answer of depth travel







    def depth_travel_zhongxu(self,node):
        if node==None:
            return
        self.depth_travel_zhongxu(node.left)
        print(node.data)
        self.depth_travel_zhongxu(node.right)


    def depth_travel_houxu(self,node):
        if node==None:
            return
        self.depth_travel_zhongxu(node.left)
        self.depth_travel_zhongxu(node.right)
        print(node.data)

    def averageOfLevels(self, root):
        queue = [self.root]
        #print("Breadth traverse:")
        #define a list to store the final value

        # define a list to store the temp value of each layer
        temp=[]
        #answer.append(self.root.data)
        #print(answer)
        cur_level_nodes=[]
        cur_level_nodes.append(self.root.data)
        answer=[]
        while queue:
            #定义list记录本层次的节点
            res=[]
            #定义list存放下一层次的节点
            next_level_nodes=[]
            #print(cur_node.data)
            for point in queue:
                #将本次次的节点放入List中
                res.append(point.data)
                #将本层节点中的节点放入到下一层的列表中
                if point.left is not None:
                    next_level_nodes.append(point.left)

                if point.right is not None:
                    next_level_nodes.append(point.right)
            answer.append(sum(res)/len(res))

            queue=next_level_nodes

        print(answer)
        return answer

    #define a function to calculate the height of a tree
    def height(self,node):
        if not node:
            return 0
        else:
            left_height=self.height(node.left)
            right_height=self.height(node.right)
            height=1+max(left_height,right_height)

        return height

    #define a function to find out if the tree is balanced
    def is_balance_tree(self,node):
        if not node:
            return True

        if (abs(self.height(node.left)-self.height(node.right))<2):
            is_node_true=True
        return (is_node_true&(self.is_balance_tree(node.left))&self.is_balance_tree(node.right))




if __name__ == '__main__':
    Tree1: Tree=Tree()
    Tree1.add(3)
    Tree1.add(9)
    Tree1.add(20)
    Tree1.add(15)
    Tree1.add(17)
    #Tree1.averageOfLevels(Tree1.root)
    Final_list=[]
    Tree1.depth_travel_xianxu(Tree1.root,Final_list)


    print(Final_list)
    print(Tree1.is_balance_tree(Tree1.root))
    print(Tree1.height(Tree1.root))







