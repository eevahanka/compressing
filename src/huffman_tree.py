class Nodde:
    def __init__(self, value, symbol, left_child=None, right_child=None) -> None:
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
        self.symbol = symbol
    
    def __gt__(self, another_nodde):
        ''' This makes heaps work if there are 2 or more same frequencies in data
        '''
        return True
        

def create_node(value, symbol):
    new_node = Nodde(value, symbol)
    return new_node

def add_node(left_child, right_child):
    new_node = Nodde(left_child.value + right_child.value, None, left_child, right_child)
    return new_node
