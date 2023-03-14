class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)

    def to_list(self):
        lst = []
        node = self.head
        while node:
            lst.append(node.data)
            node = node.next_node
        return lst

    def get_data_by_id(self, id):
        node = self.head
        try:
            while node:
                if node.data['id'] == id:
                    return node.data
                node = node.next_node
            return None
        except TypeError:
            print("Данные не являются словарем или в словаре нет id")


#ll = LinkedList()
#ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
#ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
#ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
#ll.insert_beginning({'id': 0, 'username': 'serebro'})

#lst = ll.to_list()
#for item in lst: print(item)

#user_data = ll.get_data_by_id(3)
#print(user_data)

ll = LinkedList()
ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
ll.insert_at_end('idusername')
ll.insert_at_end([1, 2, 3])
ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
user_data = ll.get_data_by_id(2)
print(user_data)
