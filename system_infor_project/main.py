import psutil
import platform
import datetime



print("=" * 50)
print("         SYSTEM METRICE REPORT    ")
print("=" * 50)


try:
    curent_time = datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")
    print(f"Date & Time: {curent_time}")

except Exception as e:
    print(f"Error fetching date/time: {e}")

try:
    os_sys = platform.system()
    os_plat = platform.machine()

    print(f"Operating System: {os_sys}")
    print(f"Processor: {os_plat}")

except Exception as e:
    print(F"Error fetching system/processor: {e}")



try:
  virtual_ram = psutil.virtual_memory()

  print(f"Total RAM: {virtual_ram.total / (1024 ** 3):.2f} GB")
  print(f"Available RAM: {virtual_ram.available / (1024**3):.2f} GB")



except Exception as e:
     print(F"Error fetching RAM : {e}")


try:
  disk_usage = psutil.disk_usage('/')

  print(f"{disk_usage.free / (1024 ** 3):.2f} free / {disk_usage.total / (1024 ** 3):.2f}total")

except Exception as e:
     print(F"Error fetching Disk Usage : {e}")


print("=" * 50)



