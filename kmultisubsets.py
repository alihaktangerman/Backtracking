kmultisubset = []
counter = 0

def kmultisubsets(s,k):
	global counter
	if k == 0:
		counter += 1
		print(kmultisubset)
		return
	if not s:
		return
	kmultisubset.append(s[0])
	kmultisubsets(s,k-1)
	kmultisubset.pop()
	kmultisubsets(s[1:],k)

def kmultisubsets(s, k):
    if k == 0:
        return [[]]
    if not s:
        return []
    # Include the first element (can be included multiple times)
    with_first = [[s[0]] + m for m in kmultisubsets(s, k-1)]
    # Exclude the first element entirely
    without_first = kmultisubsets(s[1:], k)
    return with_first + without_first

print(kmultisubsets([1,2,3,4,5],3))
print(counter)