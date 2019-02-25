from sagel.candidate_graph import get_candidate
from sagel.candidate_graph.type_enum import Type
from sagel.candidate_graph.node import Node

addr = "Đại Cồ Việt, Hai Bà Trưng, Hà Nội"
fields = ["project", "street", "ward", "district", "city"]
map_level = {"project" : 0, "street" : 1, "ward" : 2, "district" : 3, "city" : 4, "country" : 5}
graph = {}

def create_node_id(field,value):
    str_type = str(map_level[field])
    return value +"|"+str(str_type)

def check_parent(node):
    if node.get_level() == 5:
        return False
    else:
        return True

def get_field_parent(level_child):
    if  level_child == 0 or level_child == 1 or level_child ==2:
        return "district"
    if level_child == "district" or level_child == 3:
        return "city"
    if level_child == "city" or level_child == 4:
        return "country"
    else:
        return ""

def add_node(value, score, field, type, doc_id):
    node_id = create_node_id(field,value)
    node = graph.get(node_id,None)
    level = map_level[field]
    if node is None:
        node = Node(value=value,level=level,id=node_id,doc_id=doc_id)
    if type == Type.EXPLICIT:
        node.set_type(type)
        node.set_score(score)
    else:
        score = 0
        type = Type.IMPLICIT
        node.set_score(score)
        node.set_type(type)
    return node

def add_child(node_parent,node_child):
    node_parent.add_child(node_child)
    node_child.set_parent(node_parent.get_id())
    new_mcs = node_child.get_score() + node_child.get_MCS()
    mcs = node_parent.get_MCS()
    if new_mcs > mcs:
        node_parent.set_MCS(new_mcs)

def build():
    for i in range(len(fields)):
        field = fields[i]
        candidate = get_candidate.get_candidate(addr,field)
        for j in range(len(candidate[field])):
            score = candidate[field][j]["_score"]
            doc_id = candidate[field][j]["_id"]
            source = candidate[field][j]["_source"]
            for k,v in source.items():
                if k == "code" or k == "lat" or k == "lng":
                    continue
                if k == field:
                    cnode = add_node(v,score,k,Type.EXPLICIT,doc_id)
                    graph[cnode.get_id()] = cnode
                    while(check_parent(cnode)):
                        field_parent = get_field_parent(cnode.get_level())
                        pnode = add_node(source[field_parent],0,field_parent,Type.IMPLICIT,doc_id)
                        add_child(pnode,cnode)
                        cnode = pnode

build()
print(graph)



