from candidate_graph.build_graph import query
def get_candidate(addr,field):
    map_results = {}
    q = query.buildQuery(addr,field)
    candidate = query.match(q)
    map_results[field] = candidate
    return  map_results
