from persistent import Persistent
from persistent.mapping import PersistentMapping
from BTrees.OOBTree import OOBTree

class File(Persistent):
    def __init__(self, name, content=''):
        self.name = name
        self.content = content

class Directory(PersistentMapping):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.contents = OOBTree()