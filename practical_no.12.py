# Develop a Location Coordinate Processing System for storing and manipulating fixed GPS coordinates.
# Tuples, indexing, tuple operations
# Location Coordinate Processing System

# Storing GPS coordinates using tuples
location1 = (18.5204, 73.8567)  # Pune
location2 = (19.0760, 72.8777)  # Mumbai
location3 = (28.6139, 77.2090)  # Delhi

# Display coordinates
print("Location 1:", location1)
print("Location 2:", location2)
print("Location 3:", location3)

# Indexing
print("\nLatitude of Location 1:", location1[0])
print("Longitude of Location 1:", location1[1])

# Negative indexing
print("Longitude using negative index:", location1[-1])

# Tuple operations
print("\nTuple Length:", len(location1))

# Concatenation
combined = location1 + location2
print("Combined Tuple:", combined)

# Repetition
print("Repeated Location:", location1 * 2)

# Membership operation
print("\nIs latitude 18.5204 present?",
      18.5204 in location1)

# Comparison
print("Are Location 1 and Location 2 equal?",
      location1 == location2)

# Slicing
print("First coordinate value:", location1[:1])
print("Complete coordinate:", location1[:])