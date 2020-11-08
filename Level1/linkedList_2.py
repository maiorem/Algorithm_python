class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def getLength(self):
        return self.nodeCount

    def popAt(self, pos) :
        # 인덱스 값이 잘못된 경우
        if pos < 1 or pos > self.nodeCount :
            raise IndexError

        # 삭제하려는 노드가 헤드면서 유일한 값인 경우
        if pos == 1 and self.nodeCount==1 :
            curr=self.getAt(pos).data
            self.head=None
            self.tail=None
            self.nodeCount=0
            return curr
            
        # 삭제하려는 노드가 헤드면서 유일한 값이 아닌 경우
        elif pos == 1 and self.nodeCount > 1 :
            curr=self.getAt(pos).data
            self.head=curr.next
            self.tail=self.getAt(self.nodeCount)
            self.nodeCount-=1
            return curr
        # 삭제하려는 노드값이 헤드가 아닌 경우
        else :
            # 삭제하려는 노드가 테일인 경우
            if pos == self.nodeCount:
                curr=self.getAt(pos).data
                prev=self.getAt(pos-1)
                self.tail=prev
                prev.next=None
                self.nodeCount-=1
                return curr
            # 삭제하려는 노드가 중간값인 경우
            else :
                curr=self.getAt(pos).data
                prev=self.getAt(pos-1)
                prev.next=curr.next
                self.nodeCount-=1
                return curr

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount