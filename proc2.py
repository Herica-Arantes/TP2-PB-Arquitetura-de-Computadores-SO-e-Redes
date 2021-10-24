import psutil, time

for i in range(10):
    print("Uso de CPU:", psutil.cpu_percent(), "%")
    time.sleep(1)