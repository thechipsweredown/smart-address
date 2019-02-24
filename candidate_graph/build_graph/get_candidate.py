from ner_crf import ner_crf
from candidate_graph.build_graph import query
import hashlib

str = "Đại Cồ Việt, Hai Bà Trưng, Hà Nội"
map_entity = ner_crf.detect_entity(str)
fields = ["project","street","ward","district","city"]
map_results = {}
for i in range(len(fields)):
    q = query.buildQuery(str,fields[i])
    candidate = query.match(q)
    map_results[fields[i]] = candidate

print(map_results)