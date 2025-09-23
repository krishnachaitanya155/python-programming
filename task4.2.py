# Create a Tuple: Define a tuple with elements of different data types
tuple1 = (10, 'hello', 3.14, 'world')
print(tuple1)

# Access Elements: Access individual elements and slices of the tuple
for i in tuple1:
    print(i)

print(tuple1[1:3])   # Slice from index 1 to 2 (hello, 3.14)
print(tuple1[:-1])   # Slice from start to second last element (10, 'hello', 3.14)

# Concatenate Tuples: Combine two tuples to create a new tuple
t2 = (5, 0.5)
t3 = tuple1 + t2
print(t3)

# Immutable Nature: Attempt to modify elements of the tuple and handle the resulting error
try:
    tuple1[3] = "PI"  # This will raise a TypeError because tuples are immutable
except TypeError as e:
    print(f"Error: {e}")
