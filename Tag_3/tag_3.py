# read file once
with open("input.txt") as f:
    banks = [line.strip() for line in f if line.strip()]  # remove empty lines

print(len(banks))
total = 0
for x in banks:
    digits = [int(c) for c in x]
    highest_int = max(digits)

    # last index of highest digit
    last_index = len(digits) - 1 - digits[::-1].index(highest_int)

    # cut digits before last highest digit
    cut_digits = digits[:last_index]

    if cut_digits:  
        second_highest = max(cut_digits)
        final_highest = int(str(second_highest) + str(highest_int))
        total += final_highest
    else:
        second_highest = None
        final_highest = highest_int  

    print(f"Original: {x}")
    print(f"Highest int: {highest_int} at last index {last_index}")
    print(f"Cut digits: {cut_digits}")
    print(f"Second highest: {second_highest}")
    print(f"Final highest: {final_highest}\n")
print("Sum of final highest values: " + str(total))