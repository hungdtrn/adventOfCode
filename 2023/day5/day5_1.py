from collections import defaultdict, deque
import heapq

input_path = "day5.txt"
ans = 0
data = []
with open(input_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()        
        data.append(line)

def to_list(s):
    return [int(i) for i in s.split(" ") if i]

ans = 0
base_regex = ":(.|\n)+?\n\n"
cats = ["seeds", "seed-to-soil map", "soil-to-fertilizer map",
        "fertilizer-to-water map", "water-to-light map", "light-to-temperature map",
        "temperature-to-humidity map", "humidity-to-location map"]

prev_data = []
prev_cat = ""
mappings = {}
for l in data:
    for cat in cats:
        if cat in l:
            if prev_cat:
                mappings[prev_cat] = {
                    "raw": prev_data,
                    "values": [],
                    "mappings": {},
                }
            prev_cat = cat
            prev_data = []
    
    prev_data.append(l)
mappings[prev_cat] = {
    "raw": prev_data,
    "values": [],
    "mappings": {},
}


for k, data in mappings.items():
    for line in data["raw"]:
        line = line.replace(f"{k}:", "").strip()
        if line:
            values = to_list(line)
            data["values"].append(values)
            if "map" in k:
                start_src, start_dst, value_range = values[1], values[0], values[2]
                data["mappings"][(start_src, start_src + value_range)] = start_dst, start_dst + value_range


seeds = mappings["seeds"]["values"][0]
ans = float("inf")
for s in seeds:
    next_value = s
    print(next_value)
    for cat in cats[1:]:
        for (src_start, src_end), (dst_start, dst_end) in mappings[cat]["mappings"].items():
            if src_start <= next_value <= src_end:
                next_value = dst_start + (next_value - src_start)
                break
        print(cat, next_value)
    ans = min(ans, next_value)
    print("----")
print(ans)