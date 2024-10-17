# 这里是循环链表

# 节点
class Node:
    # data里面将会存info，之后可以调用info的打印函数

    def __init__(self, data):
        self.obj = data.obj
        self.sym = data.sym
        self.cla = data.cla
        self.prev = None
        self.next = None

    def getSym(self):
        return self.sym

    def getInfo(self):
        return {self.obj, self.sym, self.cla}

    def show(self):
        print(
            f'Object:{self.obj}\n'
            f'Sym:{self.sym}\n'
            f'Class:{self.cla}\n'
        )


class DoublyLinkedList:
    # 构造函数
    def __init__(self):
        # 当前位置
        self.head = None
        # 计数用的，不过好像也用不上，看看吧
        self.num = 0

    # 获取当前节点
    def get_current(self):
        return self.head

    # 获取数量
    def getnum(self):
        return self.num

    # 往右边移动
    def to_right(self):
        if self.num < 2:
            print('无效移动')
        else:
            self.head = self.head.next

    # 往左边移动
    def to_left(self):
        if self.num < 2:
            print('无效移动')
        else:
            self.head = self.head.prev

    # 添加一个节点，只有一个的情况
    def add_one(self, data):
        self.head = Node(data)
        self.num += 1

    def add_one(self, data):
        self.head = Node(data)
        self.num += 1

    # 删除一个节点：只有一个的情况
    def del_one(self):
        self.head = None
        self.num -= 1

    # 删除当前的节点：默认向左移动
    def del_cur(self):
        self.num -= 1
        left = self.head.prev
        right = self.head.next
        left.next = right
        right.prev = left
        self.head = left

    # 向右添加：
    def add_right(self, data):
        new_node = Node(data)
        if self.num >= 5:
            print('Can not add..')
            return

        if self.head is None:
            self.head = new_node
        elif self.num == 1:
            # 特殊情况
            current = self.head
            current.next = new_node
            current.prev = new_node
            new_node.prev = current
            new_node.next = current
        else:
            current = self.head
            right = current.next
            current.next = new_node
            new_node.next = right
            new_node.prev = current
            right.prev = new_node
        self.num += 1

    # 向左添加：
    def add_left(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        elif self.num == 1:
            # 特殊情况
            current = self.head
            current.next = new_node
            current.prev = new_node
            new_node.prev = current
            new_node.next = current
        else:
            current = self.head
            left = current.prev
            current.prev = new_node
            new_node.next = current
            new_node.prev = left
            left.next = new_node
        self.num += 1

    # 显示链表中所有的节点， 调试用的, 这个没用
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

    # 展示，如果是1个，就返回当前节点，否则返回三个，作为一个列表
    def display(self):
        current = self.head
        # 一张的情况
        if self.num == 1:
            return current
        else:
            # 返回相临三个
            return [self.head.prev, self.head, self.head.next]
