class Node:
    def __init__(self,value=None,type=None,parent=None,childs=[],score=0,level=None,id=None,MCS=0,doc_id=None):
        self._value = value
        self._type = type
        self._parent = parent
        self._childs = childs
        self._score = score
        self._level = level
        self._id = id
        self._MCS = MCS
        self._doc_id = doc_id

    def get_value(self):
        return self._value
    def get_type(self):
        return self._type
    def get_parent(self):
        return self._parent
    def get_childs(self):
        return self._childs
    def get_score(self):
        return self._score
    def get_level(self):
        return self._level
    def get_id(self):
        return self._id
    def get_MCS(self):
        return self._MCS
    def get_doc_id(self):
        return self._doc_id

    def set_value(self,value):
        self._value = value
    def set_type(self,type):
        self._type = type
    def set_parent(self,parent):
        self._parent = parent
    def set_childs(self,childs):
        self._childs = childs
    def set_score(self,score):
        self._score = score
    def set_level(self,level):
        self._level = level
    def set_id(self,id):
        self._id = id
    def set_MCS(self,MCS):
        self._MCS = MCS
    def set_doc_id(self,doc_id):
        self._doc_id = doc_id

    def add_child(self,node):
        id = node.get_id()
        if id not in self._childs:
            self._childs.append(id)

