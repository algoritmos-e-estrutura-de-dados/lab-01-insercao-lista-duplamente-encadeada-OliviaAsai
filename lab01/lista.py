
class Node:

    def __init__(self, x):
        self.x = x
        self.next = None
        self.prev = None


class Lista:

    def __init__(self):
        self.init = None
        self.tail = None

    def append(self, node):
        """
        Método para inserir um elemento no final

        :param node:
        :return:
        """
        if self.init is None:
            self.init = node
            self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node


    def add(self, node):
        """
        Inserir um elemento sempre no inicio da lista

        :param node:
        :return:
        """
        if self.init is None:
            self.init = node
            self.tail = node
            return

        self.init.prev = node
        node.next = self.init
        self.init = node

    def __str__(self):
        str_aux = '['
        node_aux = self.init
        while(node_aux is not None):
            str_aux += str(node_aux.x) + ','
            node_aux = node_aux.next
        str_aux += ']'
        return str_aux


if __name__ == '__main__':
    lista = Lista()
    lista.append(Node(x=65))
    lista.add(Node(x=890))
    lista.add(Node(x=27))
    lista.add(Node(x=1))
    lista.append(Node(x=7))
    lista.add(Node(x=567))
    print(lista)
    lista.add(Node(x=99))
    lista.append(Node(x=5))
    lista.append(Node(x=19))
    lista.add(Node(x=78))
    print(lista)

