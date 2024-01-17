def read_line(path):
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            yield line