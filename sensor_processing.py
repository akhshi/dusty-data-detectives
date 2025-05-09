# sensor_processing.py

def calculate_average(values):
    """Compute the average of a list of numbers."""
    return sum(values) / len(values) if values else 0

def display_stations(stations):
    """Print each station’s ID and its PM2.5 reading."""
    for station_id, pm25 in stations:
        print(f"{station_id} -> {pm25}")

def report_status(stations, threshold):
    """Compare each station’s PM2.5 to the threshold and print status."""
    for station_id, pm25 in stations:
        status = "ALERT" if pm25 >= threshold else "OK"
        print(f"{station_id} {'has high pollution' if status == 'ALERT' else 'is within safe range'} → {status}")

if __name__ == "__main__":
    # Sample data
    data = [["A1", 62], ["B2", 110], ["C3", 47]]
    print("Average PM2.5:", calculate_average([pm for _, pm in data]))
    display_stations(data)
    report_status(data, 100)

