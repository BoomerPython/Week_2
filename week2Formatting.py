# Python has been called executable pseudocode - why is that?

# Instead of braces [] - Python uses whitespace or indents

for count in range(5):
    print(count + 1, end = " ")


# For loop example


# Semicolons

a = 5
b = 6; c = 7
print(a)
print(b)
print(c)

# Comments
# Note:  Your file location will be different

f = open("C:\DSA_OU\\boomerText.txt")
results = []
for line in f:
    # keep the empty lines for now
    # if len(line) == 0;
        # continue
    results.append(line.replace('foo', 'bar'))

print(results)

# Variables and argument passing

a = [1, 2, 3]
b = a
print(b)

a.append(4)
print(b)

# Dynamic references


a = 5
print(type(a))

a = 'foo'
print(type(a))


