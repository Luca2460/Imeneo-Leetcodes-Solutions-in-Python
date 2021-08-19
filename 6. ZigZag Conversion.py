def convert(s, numRows): # (I did not come up with this one myself, however, I understood the solution thoroughly)

    if numRows == 1 or len(s) < numRows:
        return s
    step = 1
    pos = 1 # which row are we currently into
    lines = {} # key = row, value = what is read along that row when string is written in ZigZag. HASH TABLE
    for c in s:
        if pos not in lines:
            lines[pos] = c
        else:
            lines[pos]+=c
        pos+=step
        if pos==1 or pos==numRows:
            step*=-1
    sol = ""
    for i in range(1, numRows+1):
            sol+=lines[i]
    return sol

    # TIME complexity: O(N), where N is the length of the string (the number or rows does not really impact the time complexity too much)
    # SPACE complexity: O(M), where M is the number of rows. Because for each row we will create a new entry in the hash table.
