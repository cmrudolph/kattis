# https://open.kattis.com/problems/lost

# OK: Interesting graph problem. We traverse the graph using recursion to
# compute all our costs and then sum them up to determine the overall min.

import sys
import json


def dbg(str):
    print(str, file=sys.stderr)


def process_vertex(graph, results, vertex_name, dist):
    # dbg(f"Process Vertex -- Vertex:{vertex_name}; DistFrom:{dist}")
    vertex_dict = graph[vertex_name]

    neighbors_to_visit = []

    for neighbor_name in sorted(vertex_dict, key=vertex_dict.get):
        cost = vertex_dict[neighbor_name]
        # dbg(f"Checking Edge -- {vertex_name} --> {neighbor_name} = {cost}")

        known_result = results.get(neighbor_name, None)
        if known_result is None:
            results[neighbor_name] = (dist, cost)
            dbg(f"New -- Vertex:{neighbor_name}; Dist:{dist}; Cost:{cost}")
            neighbors_to_visit.append(neighbor_name)
        else:
            known_dist = known_result[0]
            known_cost = known_result[1]
            if dist < known_dist or (dist == known_dist and cost < known_cost):
                results[neighbor_name] = (dist, cost)
                dbg(f"Better -- Vertex:{neighbor_name}; OldD:{known_dist}; " +
                    f"NewD:{dist}; OldC:{known_cost}; NewC:{cost}")
                neighbors_to_visit.append(neighbor_name)

    for neighbor_name in neighbors_to_visit:
        process_vertex(graph, results, neighbor_name, dist + 1)


def main():
    init_splits = input().split()
    lang_count = int(init_splits[0])
    trans_count = int(init_splits[1])
    langs = input().split()

    dbg(f"LangCount:{lang_count}")
    dbg(f"TransCount:{trans_count}")
    dbg(f"Langs:{langs}")

    graph = {"English": {}}
    for lang in langs:
        graph[lang] = {}

    results = {"English": (0, 0)}

    for i in range(trans_count):
        splits = input().split()
        lang1 = splits[0]
        lang2 = splits[1]
        cost = int(splits[2])

        graph[lang1][lang2] = cost
        graph[lang2][lang1] = cost

    # dbg(f"Graph:{json.dumps(graph, indent=1)}")

    process_vertex(graph, results, "English", 1)

    # dbg(f"Results:{json.dumps(results, indent=1)}")

    langs_reachable = set()
    total_cost = 0
    for k in results:
        if k != "English":
            langs_reachable.add(k)
            cost = results[k][1]
            total_cost += cost

    if len(langs_reachable) == len(langs):
        print(str(total_cost))
    else:
        print("Impossible")


if __name__ == "__main__":
    main()
