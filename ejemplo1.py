
# Esta librería no forma parte de la instalación standard de Python y debe ser obtenida mediante pip
import psutil

# Get CPU usage
cpu_percent = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_percent}%")

# Get memory usage
memory = psutil.virtual_memory()
print(f"Memory Usage: {memory.percent}%")

# Get disk usage
disk = psutil.disk_usage('/')
print(f"Disk Usage: {disk.percent}%")