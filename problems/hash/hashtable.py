# %% [markdown]
# # Hash Table

# %% [markdown]
# The objective of this notebook is to discuss hash tables, which are commonly used in statistical natural language processing. When discussing hash tables, we are basically referring to dictionaries. The idea of a hash function is to translate arbitrary data into a numeric representation, which becomes convenient and useful for a variety of different purposes such as lookup tables (i.e. dictionaries). A hash Table is a set of key-value pairs with no keys being duplicated. It is also referred to as "Dictionary" or "Hash Map". There are three components of the Hash Table. First is the array, which is the data structure for storing the data. Secondly is the hash function as it converts the key into an array index. The third aspect is collision handling, where multiple key/value pairs maps to the same cell.

# %% [markdown]
# ### Dictionary:
# 
# The following code blocks walks through the basics of implementing a dictionary in python, which in essence is a hash table. First, we initialize an empty dictionary as such:

# %%
Dict = {} #Emptpy dictionary

# %% [markdown]
# The dictionary is populated with the following structure: Dict['key'] = value. The string used to index the hash table "Dict" is termed as the "key". And to access the data stored in the hash table, the format is: dict['key_name']

# %%
Dict['A'] = "Hello World"
Dict['B'] = 25
Dict['C'] = [1,2,3,4]

print "Dictionary:"
print Dict #print dictionary
print "\nThe key is 'A', what is the value?"
print Dict['A'] #Access value given the key

# %% [markdown]
# And if we wanted to loop through all the values or keys, we can use the following for loop. We can also loop through all of the keys/value pairs together:

# %%
#Loop through all the keys in the dictionary:
print "All Keys:"
for i in Dict.keys():
    print i
#Loop through all the values in the dictionary:   
print "\nAll Values:"
for j in Dict.values():
    print j
    
#Loop through all key/value pairs in the dictionary:    
print "\nKey/Value Pairs:"
for k,v in Dict.items():
    print k,':',v

# %% [markdown]
# Now, suppose we have an array that contains our key and another array that contains the value of that key. How do we pair the two in a dictionary?

# %%
key = ['A','B','C']
value = ["Hello World",25,[1,2,3,4]]
dic = {k:v for k,v in zip(key,value)} #Dictionary {}
print "Hash Table: \n%s" % dic 

# %% [markdown]
# ### Hash Tables Explained
# 
# Hash tables are a collection of items that are stored in a way that allows for easy access in finding the item by it's hash value. The "slot" is referred as the position where the item in the hash table is stored. The hash function maps and item and the slot where the corresponding item belongs in the hash table. The hash function will take any item in the collection and return an integer; each slot contains an item and is referenced by an integer, starting at 0 and goes to n-1. For numerical values, one hash function example is known as the "remainder method", `item % size = remainder`. This takes the item, say for example 25, and divides it by the size of the table (i.e. 4). Divide 25 by 4 equals 6.25. Therefore the remainder rounds up to 3 and thus will be the hash value for 25. Here's an example of a table size = 11 (i.e. 0-10) and the items corresponding hash value using the remainder method. Right away you may be thinking that this method only works if each item maps to a unique location in the hash table. For instance, if an item is added to the hash table and it's value is 31, well 33%11 = 0, but we already have an item with the hash value of 0. This is an instance known as "collision", which creates a problem for the hashing technique. This will be discussed in the following section.
# 
# 
# ![Screen Shot 2016-08-11 at 3.38.40 PM.png](https://udacity-github-sync-content.s3.amazonaws.com/_imgs/26272/1470947930/Screen_Shot_2016-08-11_at_3.38.40_PM.png)
# 
# 
# We can create hash function in python for both character-based items (i.e. strings) or numerical values. Let's look at character-based items first. Suppose we have the string "python", we can use the function `ord()` to get the [ASCII](https://en.wikipedia.org/wiki/ASCII) value of each character. Implementing a "for" loop, we can add up the values of each char and use the remainder method to get a hash value. There are a number of additional ways to compute hash values for items in a given collection. Below is one example; note the usage of the positional value (i) as a weighting factor when computing the unique hash value. 

# %%
#Characters:
def hashing(string,size):
    sum = 0
    for i in range(len(string)):
        sum = sum + ord(string[i])*(i+1)
    return sum%size

string = "python"
size  = 100
hashing(string,size)

# %%
#Integers:
def hashing(integer,size):
    sum = 0
    for i in range(len(integer)):
        sum = sum + i
    return sum%size

hashing(15692,10)

# %% [markdown]
# ### Hash Table Example 
# 
# In the following script, we will explore creating a hash table for a  fictitious group of students and their corresponding university they attend. The array length for this example will be 10. In reality, this would be much longer but the point here is to illustrate when a collision occurs. The following source utilized as a guide for creating the hash table can be found ['here'](https://www.youtube.com/watch?v=9HFbhPscPU0).

# %%
#Initialize HashTable class:
class HashTable:
    
    def __init__(self):
        
        self.size = 10 #set size of the array
        
        #initial set every cell to "None", force array to fixed length
        self.map = [None] * self.size 
    
    def _get_hash(self,key): #assigning index to place key/value in
        hash = 0 #intialize to Zero
        for char in key:
            hash += ord(char)
            #print hash [!debug]
            #print hash % self.size [!debug]
        return hash % self.size

    def add_key_val(self,key,value):
        key_hash = self._get_hash(key) # get index we are placing key/value in
        key_value = [key,value] #key and value we want to assert in that cell

        # check first if that cell is empty:
        if self.map[key_hash] is None: #if contains None, it is empty
            self.map[key_hash] = list([key_value])
        else: # if the cell is not empty
        #check if key is already existing and if so, we can just update the value
            for pair in self.map[key_hash]: 
                if pair[0] == key:
                    pair [1] == value
                    return True
            self.map[key_hash].append(key_value) #if not match, the create a new key
        return True
    
    '''Next, get the hash given the key and locate the cell; if the cell is 
    not none then iterate through the pairs in the cell and find the value that matched
    the key and return the value, if we don't find the key, return None'''
    
    def get_key_value(self,key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
                
    def print_data(self):
        print "Students:\n"
        for item in self.map:
        #prints out every non None cell in the array
            if item is not None:
                print(str(item))
                
    def delete_entry(self,key):
        key_hash = self._get_hash(key) #first locate key to get the index
        #check if cell is none
        if self.map[key_hash] is None:
            return False # if False, key/value pair does not exist
        #iterate through cells
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
            #when locate the item you want to remove you "pop" the item for the list
                self.map[key_hash].pop(i) 
                return True

# %% [markdown]
# ### Execute Hash Table

# %%
h = HashTable()

h.add_key_val("Trent","Texas A&M")
h.add_key_val("Lindsay","Baylor University")
h.add_key_val("Michelle","Louisiana State University")
h.add_key_val("Allan","Southern Methodist University")
h.add_key_val("Brent","Rice University")
h.add_key_val("Lauren","University of Alabama")
h.add_key_val("Lauren", "Auburn University")
h.add_key_val("George","University of Miami")
h.add_key_val("Todd","Arizona State University")
h.add_key_val("Jeremy", "Kent State")
h.add_key_val("Brittnay","Florida State University")
h.print_data()

h.delete_entry('Todd')

print "\n"
h.print_data()
print "\n"

print "Trent Attends the following university: %s" % (h.get_key_value('Trent'))


