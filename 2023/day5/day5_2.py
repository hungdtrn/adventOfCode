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
for i in range(0, len(seeds), 2):
    seed_start, seed_range = seeds[i], seeds[i+1]
    intervals = [(seed_start, seed_start + seed_range)]
    
    for cat in cats[1:]:
        new_intervals = []
        while intervals:
            query_start, query_end = intervals.pop()
            chopped_intervals = []
            found = False
            for (key_start, key_end), (value_start, value_end) in mappings[cat]["mappings"].items():
                if key_start <= query_start < key_end and key_end >= query_end:
                    # the interval is completely contained in the mapping
                    new_intervals.append((value_start + query_start - key_start, value_start + (query_end - key_start)))
                    found = True
                elif key_start <= query_start < key_end:
                    # the interval starts in the mapping
                    new_intervals.append((value_start + query_start - key_start, value_end))

                    # put the non-overlapping part back to the list 
                    intervals.append((key_end, query_end))
                    found = True
                elif key_start < query_end <= key_end:
                    # the interval ends in the mapping
                    new_intervals.append((value_start, value_start + (query_end - key_start)))

                    # put the non-overlapping part back to the list 
                    intervals.append((query_start, key_start))
                    found = True
            
            if not found:
                # No overlapping
                new_intervals.append(interval)

        intervals = new_intervals

    for interval in intervals:
        ans = min(ans, query_start)
print(ans)