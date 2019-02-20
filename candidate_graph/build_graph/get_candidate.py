from ner_crf import ner_crf
from candidate_graph.build_graph import query

str = "Đại Cồ Việt, Hai Bà Trưng, Hà Nội"
map_entity = ner_crf.detect_entity(str)

q = query.buildQuery(map_entity)
candidate = query.matchMultiFields(q)

print(candidate)