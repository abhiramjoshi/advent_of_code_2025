# We will get the puzzle and manintin a monotonic increasing stack of length 2
import sys

INPUT_FILE = sys.argv[1]

lines = []
with open(INPUT_FILE, "r") as f:
    lines = f.readlines()

if not lines:
    print("There was an error parsing input")
    exit(1)

def num_from_list(l):
    n = len(l)
    
    s = 0
    for i in range(n):
        s *= 10
        s += l[i]

    return s

# Go through each line and get the two highest numbers sequentially
def highest_nums(nums: str, k: int) -> int:
    nums = nums.rstrip("\n")
    curr = [0]*k
    
    for n in nums:
        num = int(n)
        for i in range(1, k):
            if curr[i] > curr[i-1]:
                curr[i-1:k-1] = curr[i:k]
                curr[-1] = num
                break
        
        if num > curr[-1]:
            curr[-1] = num
        
    
    return num_from_list(curr)


s = 0
for nums in lines:
    s += highest_nums(nums, 12)

print("The sum of all the nums is:", s)
