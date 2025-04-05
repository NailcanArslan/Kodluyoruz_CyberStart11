import math

# Noktaların tanımlanması
points = [(1, 2), (4, 6), (5, 1), (9, 7)]

# Öklid mesafesi hesaplayan fonksiyon
def euclideanDistance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Mesafeleri saklayacağımız liste
distances = []

# Tüm nokta çiftleri için mesafeleri hesaplama
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)
        print(f"{points[i]} ile {points[j]} arasındaki mesafe: {dist:.2f}")

# Minimum mesafeyi bulma
min_distance = min(distances)
print(f"\nMinimum Öklid mesafesi: {min_distance:.2f}")