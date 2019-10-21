""" QuickUnion is a lazy approach.

*Limitations:*

- Trees can get too tall
- Find too expensive (could be N array accesses)
"""


class QuickUnion:
    """ data[i] is parent of i. Root of i is id[id[...id[i]...]] """
    def __init__(self, n):
        """ Initializing list of size n where value is same as index
            Here it means that each node is a root of it's own tree

        Time Complexity: O(n)

        :param n: number of elements
        """
        self.data = []
        for i in range(n):
            self.data.append(i)

    def root(self, elem):
        """ Finding the root of element

        :param elem: element of which root is needed
        :return: root of elem
        """
        while elem != self.data[elem]:
            elem = self.data[elem]
        return elem

    def connected(self, elem1, elem2):
        """ elem1 and elem2 are connected iff they have same root

        :param elem1: element 1
        :param elem2: element 2
        :return: returns true iff two elem1 and elem2  are connected, else
            false
        :rtype: bool
        """
        return self.root(elem1) == self.root(elem2)

    def union(self, elem1, elem2):
        """ To merge components containing elem1 and elem2, set the id of
        elem1's root to the id of elem2's root

        :param elem1: element 1
        :param elem2: element 2
        """
        root_elem1 = self.root(elem1)
        root_elem2 = self.root(elem2)
        self.data[root_elem1] = root_elem2

