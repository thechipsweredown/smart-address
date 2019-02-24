class Node:
    def __init__(self,type,parent,childs,score, level, id, MCS):
        self._type = type
        self._parent = parent
        self._childs = childs
        self._score = score
        self._level = level
        self._id = id
        self._MCS = MCS

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
    def get_docId(self):
        return self._id
    def get_MCS(self):
        return self._MCS

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

    def addChild(self,node):
        self._childs.append(node)

