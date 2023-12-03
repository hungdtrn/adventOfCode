from collections import defaultdict

input_path = "day2.txt"
ans = 0
with open(input_path, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        game, data = line.split(":")
        game_id = int(game.replace("Game", "").strip())
        sets = data.split(";")
        count = defaultdict(int)
        for set_str in sets:            
            colors = set_str.split(",")
            for color in colors:
                if "blue" in color:
                    key = "blue"
                elif "red" in color:
                    key = "red"
                elif "green" in color:
                    key = "green"
                
                cnt = int(color.replace(key, "").strip())
                count[key] = max(count[key], cnt)

        
        power = 1
        for v in count.values():
            power *= v

        ans += power
        
        

print(ans)