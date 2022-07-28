class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    # def __index__(self):


class LinkedList:
    def __init__(self, **value):
        self.first = None
        self.last = None
        self.cnt = 0

    def __str__(self):
        # FIXME: убрать вывод запятой после последнего элемента
        if self.first is not None:
            current = self.first
            if self.first.value == None:
                out = f'LinkedList [ '
            else:
                out = f'LinkedList [{str(current.value)}'

            while current.next is not None:
                current = current.next
                out += f',{str(current.value)}'

            return out + ']'
        return 'LinkedList []'

    def __getitem__(self, index):
        i = 0

        current_value = self.first
        while i <= index:
            if i == index:
                return current_value.value
            else:
                i += 1
                current_value = current_value.next
        raise IndexError(f'Индекс {index} не найден')

    def __setitem__(self, index, value):
        i = 0

        current_value = self.first
        while i <= index:
            if i == index:
                current_value.value = value
                return

            else:
                i += 1
                current_value = current_value.next
        raise IndexError(f'Индекс {index} не найден')

    def clear(self):
        """
        Очищаем список
        """
        # TODO: реализовать очистку списка
        if self.first is None:
            raise TypeError('Список пустой')
        else:
            self.cnt = 0
            current_node = self.first
            self.first = None
            while current_node:
                del_node = current_node
                current_node = current_node.next
                del_node.next = None
                del_node.value = None

                return

    #
    def add(self, value):
        """
        Добавляем новое значение value в конец списка
        """
        new_node = Node(value, None)  # Создаем новый узел
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тотже узел, т.к. он единственный
            self.last = new_node
            self.first = new_node

        else:
            self.last.next = new_node
            self.last = new_node
        self.cnt += 1

    #
    def push(self, value):
        """
        Добавляет элемент со значением value в начало списка
        """
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тотже узел
            self.last = self.first = Node(value, None)
        else:
            new_node = Node(value, self.first)
            self.first = new_node
        self.cnt += 1

    #
    def insert(self, value, index):
        """
        Вставляет узел со значением value на позицию index
        """
        if self.first is None:
            return 'Empty List'
        elif index == 0:
            self.push(value)
            return
        else:

            i = 0
            current_node = self.first
            while current_node:
                test = current_node.value

                if i == index - 1:
                    next_change = current_node
                    if current_node == self.last:
                        next_change.next = self.last = Node(value)
                        self.cnt += 1
                        return
                elif i == index:
                    next_to_new = current_node
                    if current_node.next == None:
                        next_change.next = Node(value, next_to_new)
                        self.cnt += 1
                        return

                i += 1
                current_node = current_node.next

            raise IndexError(f'Нет такого индекса {index}')

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        i = 0

        current_node = self.first

        while i < self.cnt:
            if current_node.value == value:
                return i
            else:
                i += 1
                current_node = current_node.next
        return f"значение '{value}' не найдено"

    def len(self):

        return self.cnt


#
#
if __name__ == "__main__":
    L = LinkedList()
    print("empty list = ", L)
    L.add(0)
    L.add(1)
    L.add(2)
    L.add(4)

    print("list = ", L)

    L.insert(3, 3)
    print("list = ", L)
    L.insert(5, 5)
    print("list = ", L)
    L.insert(10, 0)
    print("list = ", L)
    print(L.len())
    L.clear()
    print("list clear = ", L)
    print(L.len())

    L.add(0)
    L.add(1)
    L.add(2)
    L.add(4)
    print(L)
    print(L[0])
    L[0] = 666
    L.__setitem__(0, 666)
    print(L)
    print(L.find(6666))

#
#     # TODO: реализовать интерфейс итерации
#     # for el in L:
#     #     print(el)
#     # Напомню принцип работы итератора:
#     # iterator_L = iter(L) L.__iter__()
#     # next(iterator_L) it.__next__()
#     # next(iterator_L)
#     # next(iterator_L)
#     # next(iterator_L)
#
#     # TODO: реализовать обращение по индексу и изменение значение по индексу
#     # print(L[0])
#     # L[0] = "new"
#     # print(L[0])
#
#     # TODO: реализовать создание нового списка с задание начальных элементов
#     # L = LinkedList(2, 4, 6, -12)
#     # print(L)
