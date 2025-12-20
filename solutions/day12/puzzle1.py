import sys
import re

INPUT_FILE = sys.argv[1]


def parse_puzzle_file(file_path):
    with open(file_path, "r") as f:
        content = f.read()

    parts = re.split(r"(?=\d+x\d+:)", content, maxsplit=1)
    presents_block = parts[0]
    configs_block = parts[1] if len(parts) > 1 else ""

    presents = {}
    presents_sizes = {}
    present_matches = re.findall(r"(\d+):\s+([#.\s]+?)(?=\n\d+:|\Z)", presents_block)

    for p_id, p_shape in present_matches:
        # Clean up lines and filter out empty strings
        lines = [line.strip() for line in p_shape.strip().split("\n") if line.strip()]
        presents[int(p_id)] = lines
        presents_sizes[int(p_id)] = sum([s.count("#") for s in lines])

    configurations = []
    config_matches = re.findall(r"(\d+x\d+):\s+([\d\s]+)\n", configs_block)
    for dims, sequence in config_matches:
        configurations.append(
            {
                "dimensions": dims,
                "sequence": [int(x) for x in sequence.split()],
                "size": int(dims.split("x")[0]) * int(dims.split("x")[1]),
            }
        )

    return presents, presents_sizes, configurations


presents, presents_sizes, configurations = parse_puzzle_file(INPUT_FILE)
print(presents)
print(presents_sizes)
print(configurations)

total_valid = 0
total_valid_by_shape = 0
for config in configurations:
    dims, seq, size = config.values()
    total_size = 0
    total_presents = 0

    n = len(seq)
    for i in range(n):
        total_size += presents_sizes[i] * int(seq[i])
        total_presents += int(seq[i])

    if total_size <= size:
        total_valid += 1

    dims = list(map(int, dims.strip().split("x")))

    print(dims, dims[0] // 3 * dims[1] // 3)
    if dims[0] // 3 * dims[1] // 3 >= total_presents:
        total_valid_by_shape += 1

print("Total valid:", total_valid)
print("Total valid by shape:", total_valid_by_shape)
