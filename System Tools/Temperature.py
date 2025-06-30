while True:
    with open('/sys/class/thermal/thermal_zone0/temp', 'r') as file:
            cpu_temp = float(file.read()) / 1000
    print(f"CPU Temperature: {cpu_temp}°C")
