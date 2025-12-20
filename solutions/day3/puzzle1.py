# We will get the puzzle and manintin a monotonic increasing stack of length 2
import sys

INPUT_FILE = sys.argv[1]

lines = []
with open(INPUT_FILE, "r") as f:
    lines = f.readlines()

if not lines:
    print("There was an error parsing input")
    exit(1)



# Go through each line and get the two highest numbers sequentially
def highest_nums(nums: str) -> int:
    nums = nums.rstrip("\n")
    first = 0
    second = 0
    curr_max = 0
    for n in nums:
        num = int(n)
        if second > first:
            first = second
            second = num
        elif num > second:
            second = num

        curr_max = max(curr_max, 10*first + second)
    return curr_max


s = 0
for nums in lines:
    s += highest_nums(nums)

print("The sum of all the nums is:", s)
