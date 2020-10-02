class HashMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000000
        self.map = [None] * self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        key_value = [key, value]

        # check if key exists
        if self.map[key] is None:
            self.map[key] = list([key_value])
        # if key exists, update the value
        else:
            for pair in self.map[key]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            # if didn't find a match - new key
            self.map[key].append(key_value)
            return True

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        if self.map[key] is not None:
            for pair in self.map[key]:
                if pair[0] == key:
                    return pair[1]
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        if self.map[key] is None:
            return -1
        # need index to remove from list
        for i in range(len(self.map[key])):
            if self.map[key][i][0] == key:
                self.map[key].pop()
                return True
