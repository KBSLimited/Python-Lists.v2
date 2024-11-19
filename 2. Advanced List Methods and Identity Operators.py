#Task 1: Given the two lists:
# Task 1: Given the two lists
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Find students who both submitted assignments and attended the class
both = set(submitted) & set(attended)

print(f"Students who both submitted assignments and attended the class: {', '.join(both)}")