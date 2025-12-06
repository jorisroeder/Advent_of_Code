f = open("input.txt")
text = f.read()

pairs = text.split(",")
result = []
for pair in pairs:
    a, b = map(int, pair.split("-"))
    result.append((a, b))

for a,b in result:
    print(f"({a}, {b})")
ranges = []
for a,b in result:
  ranges.extend(range(a, b+1))



invalid = []

for i in ranges:
      s = str(i)
      
      for k in range(2, len(s) + 1):          # try k = 2 .. length of s
          if len(s) % k != 0:
              continue                       # need exact equal-sized parts
          part_len = len(s) // k
          parts = [s[j*part_len:(j+1)*part_len] for j in range(k)]
          if all(p == parts[0] for p in parts):
              invalid.append(i)
              break                          
  
total = sum(invalid)
print("Total: " + str(total))


