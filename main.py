import matplotlib.pyplot as plt

# Функція для зчитування координат
def read_dataset(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(int, line.split())
            points.append((x, y))
    return points

# Функція для відображення точок
def plot_points(points):
    plt.figure(figsize=(9.6, 5.4))
    plt.xlim(0,960) 
    plt.ylim(0,540) 
    x_coords, y_coords = zip(*points)
    plt.scatter(x_coords, y_coords, color='orange') 
    plt.savefig('output_image.png')

# Виклик програми
if __name__ == "__main__":
    dataset_file = 'DS5.txt'  
    points = read_dataset(dataset_file)
    plot_points(points)
