"""
Design HashMap

Link: https://leetcode.com/problems/design-hashmap/

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.


Example

```
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // returns 1
hashMap.get(3);            // returns -1 (not found)
hashMap.put(2, 1);         // update the existing value
hashMap.get(2);            // returns 1 
hashMap.remove(2);         // remove the mapping for 2
hashMap.get(2);            // returns -1 (not found) 
```

- All keys and values will be in the range of [0, 1000000].
- The number of operations will be in the range of [1, 10000].
- Please do not use the built-in HashMap library.

"""


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


hashMap = HashMap()
hashMap.put(1, 1)
hashMap.put(2, 2)
hashMap.get(1)
hashMap.get(3)
hashMap.put(2, 1)
hashMap.get(2)
hashMap.remove(2)
hashMap.get(2)
