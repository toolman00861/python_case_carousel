# 处理 art文件：
art_map = {
    'multi': """
                             ↓↓
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   |                            |   |          
           |   |                            |   |          
 ()        |   |             ()             |   |        ()
           |   |                            |   |          
 __________|   |                            |   |__________
               |____________________________|

""",
    'single': """
                             ↓↓
               |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    
               |                            |          
               |                            |        
               |             ()             |       
               |                            |         
               |                            |  
               |____________________________|

                             
"""
    , 'del': """
                             /\ 
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾/  \‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   |           /    \           |   |                   
           |   |          /_    _\          |   |                   
 ()        |   |            |  |            |   |        ()        
           |   |            |  |            |   |                  
 __________|   |            |  |            |   |__________
               |____________|  |____________|
                            |__|
""",
    'single_del': """
                             /\ 
               |‾‾‾‾‾‾‾‾‾‾‾‾/  \‾‾‾‾‾‾‾‾‾‾‾‾|   
               |           /    \           |                    
               |          /_    _\          |           
               |            |  |            |       
               |            |  |            |                  
               |            |  |            |   
               |____________|  |____________|
                            |__|
                             
""",
    'right': """
                                         |\\
 __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \     __________
           |   |                         |  \   |                   
           | |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \  |                   
 ()        | |            Right               | |        ()        
           | |___________________________    /  |                  
 __________|   |                         |  /   |__________
               |_________________________| /
                                         |/
""",
    'add_right':
        """
                                             |\\
     __________    |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \     __________
               |   |                         |  \   |                   
               | |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \  |                   
     ()        | |        Adding Right            | |        ()        
               | |___________________________    /  |                  
     __________|   |                         |  /   |__________
                   |_________________________| /
                                             |/
    
    """,
    'single_add_right':
        """
                                             |\\
                   |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| \  
                   |                         |  \          
                 |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾    \          
                 |        Adding Right            |    
                 |___________________________    /    
                   |                         |  /  
                   |_________________________| /
                                             |/
    
    """,
    'left': """
                 /|                      
 __________     / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   /  |                         |   |                   
           |  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |                   
 ()        | |              Left              | |        ()        
           |  \    ___________________________| |                  
 __________|   \  |                         |   |__________
                \ |_________________________|
                 \|                      
""",
    'add_left': """
                 /|                      
 __________     / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|    __________
           |   /  |                         |   |                   
           |  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾| |                   
 ()        | |           Adding Left          | |        ()        
           |  \    ___________________________| |                  
 __________|   \  |                         |   |__________
                \ |_________________________|
                 \|                      
                             
""",
    'single_add_left':
        """
                     /|                      
                    / |‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|   
                   /  |                         |          
                  /    ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾|      
                 |           Adding Left          |       
                  \    ___________________________|             
                   \  |                         |   
                    \ |_________________________|
                     \|                      
    
    """
    ,
    'add': """
                            |‾‾|
               |‾‾‾‾‾‾‾‾‾‾‾‾|  |‾‾‾‾‾‾‾‾‾‾‾‾|   
               |            |  |            |                   
               |            |  |            |                    
               |           _|  |_           |   
               |          \      /          |                
               |           \    /           |   
               |____________\  /____________|
                             \/
                            
"""
}

# 展示：基本逻辑： 数量不为0：
# 为1 ，就展示一个节点：头结点
# 数量为2 或者多个： 先获取一个列表：[左节点，中间节点，右节点]
# 对他进行展示： 展示的逻辑： 依次替换动画中的 () 。
# 函数是： replace("()", sym[0,1,2], 数量1 )
def show(info, num):
    # info将会传来一个list或者一个info类型的对象
    if num == 1:
        art = art_map['single'].replace('()', info.sym)
    else:
        art = art_map['multi'].replace('()', info[0].sym, 1)
        art = art.replace('()', info[1].sym, 1)
        art = art.replace('()', info[2].sym, 1)
    print(art)

def to_left():
    print(art_map['left'])

def to_right():
    print(art_map['right'])

def del_():
    print(art_map['del'])

def single_del():
    print(art_map['single_del'])

def add():
    print(art_map['add'])

def add_left():
    print(art_map['add_left'])

def add_right():
    print(art_map['add_right'])

def single_add_left():
    print(art_map['single_add_left'])

def single_add_right():
    print(art_map['single_add_right'])




