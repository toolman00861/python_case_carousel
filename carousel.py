import json  # 解析json的库函数
import os  # 系统的一些操作，用了cls 清屏
import time  # 这里只用到一个函数： time.sleep(1)

import circle_dlink_list as l
import art


# 自己定义的info类
class info:
    def __init__(self, obj, sym, cla):
        self.obj = obj  # 名字
        self.sym = sym  # 符号
        self.cla = cla  # 类别


# 创建一个双向链表实例
dll = l.DoublyLinkedList()

data = info("tiger", "tiger's symbol", "animal")

dll.add_one(data)

# 这里存了json表情包数据
emojis = []

# 读取JSON文件
# 格式：两个字典0，1，其中包括class 和 emojis ，emojis 通过访问键来找到对应图标
with open('emojis.json', 'r', encoding='UTF-8') as file:
    emojis = json.load(file)


def cls():
    os.system('cls')


def pause():
    input('type any key to continue...')


def menu(num):
    if num == 0:
        print('add: add a emoji frame')
        print('q: quit the program')
        print()
    elif num == 1:
        print('add: add a emoji frame')
        print('del: delete current emoji frame')
        print('info: retrieve info about current frame')
        print('q: quit the program')
        print()
    else:
        print('l: move to left')
        print('r: move to right')
        print('add: add a emoji frame')
        print('del: delete current emoji frame')
        print('info: retrieve info about current frame')
        print('q: quit the program')
        print()


while True:
    cls()

    # 展示：基本逻辑： 数量不为0： 为1 ，就展示一个节点：头结点
    # 数量为2 或者多个： 先获取一个列表：[左节点，中间节点，右节点]
    # 对他进行展示： 展示的逻辑： 依次替换动画中的 () 。
    # 函数是： replace("()", sym[0,1,2], 数量1 )
    if dll.num != 0:
        # 传入需要展示的内容，传入数量
        art.show(dll.display(), dll.getnum())

    print('Type any of the following commands to perform the action:')
    menu(dll.getnum())

    command = input()

    # 退出指令
    if command == 'q':
        exit(0)

    # 分数量讨论
    if dll.getnum() == 0:
        #  添加指令
        if command == 'add':
            print('what do you want to add?')
            obj = input()  # 输入需要的名字
            flag = False  # 设置找到标志
            clazz = ''
            sym = ''
            #  遍历列表中的两个字典
            for item in emojis:
                # 如果说 obj 在字典（的键）中
                if obj in item['emojis']:
                    #  拿到符号
                    sym = item['emojis'][obj]
                    #  拿到类别
                    clazz = item['class']
                    # 设置找到标志
                    flag = True

            # 如果找到，添加到循环双向链表中
            if flag:
                dll.add_one(info(obj, sym, clazz))
                art.add()
            else:
                # 没有找到就提示没找到
                print('no found...')
            time.sleep(1)

    elif dll.getnum() == 1:
        # 展示当前节点的内容
        if command == 'info':
            cur = dll.get_current()
            cur.show()
            input('press any to continue...')

        # 删除当前节点
        if command == 'del':
            dll.del_one()
            art.single_del()
            time.sleep(1)
        elif command == 'add':
            print('what do you want to add?')
            obj = input()
            flag = False
            clazz = ''
            sym = ''
            for item in emojis:
                if obj in item['emojis']:
                    sym = item['emojis'][obj]
                    clazz = item['class']
                    flag = True
            if flag:
                direction = input('on which direction you want to add?(left/right):')
                if direction == 'left':
                    dll.add_left(info(obj, sym, clazz))
                    art.single_add_left()
                elif direction == 'right':
                    dll.add_right(info(obj, sym, clazz))
                    art.single_add_right()
            else:
                print('no found...')
            time.sleep(1)

    else:
        if command == 'info':
            cur = dll.get_current()
            cur.show()
            input('press any to continue...')
        elif command == 'l':
            dll.to_left()
            art.to_left()
            time.sleep(1)
        elif command == 'r':
            dll.to_right()
            art.to_right()
            time.sleep(1)
        elif command == 'del':
            dll.del_cur()
            art.del_()
            time.sleep(1)
        elif command == 'add':
            print('what do you want to add?')
            obj = input()
            flag = False
            clazz = ''
            sym = ''
            for item in emojis:
                if obj in item['emojis']:
                    sym = item['emojis'][obj]
                    clazz = item['class']
                    flag = True
            if flag:
                direction = input('on which direction you want to add?(left/right):')
                if direction == 'left':
                    dll.add_left(info(obj, sym, clazz))
                    cls()
                    art.add_left()
                elif direction == 'right':
                    dll.add_right(info(obj, sym, clazz))
                    cls()
                    art.add_right()
            else:
                print('no found...')
            time.sleep(1)
