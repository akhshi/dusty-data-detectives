import matplotlib.pyplot as plt

def plot_pm25(stations):
    labels = [station[0] for station in stations]
    sizes = [station[1] for station in stations]

    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['cyan', 'pink', 'lightcoral'])
    plt.title("PM2.5 Proportions by Station")
    plt.show()

if __name__ == "__main__":
    data = [["A1", 62], ["B2", 110], ["C3", 47]]
    plot_pm25(data)
