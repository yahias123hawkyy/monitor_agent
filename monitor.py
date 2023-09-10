import docker
import time

def monitor_containers(duration_seconds):
    client = docker.from_env()

    start_time = time.time()
    end_time = start_time + duration_seconds

    while time.time() < end_time:
        for container in client.containers.list():
            stats = container.stats(stream=False)
            container_name = container.name
            cpu_percent = stats['cpu_stats']['cpu_usage']['total_usage'] / stats['cpu_stats']['system_cpu_usage'] * 100.0
            memory_usage = stats['memory_stats']['usage']

            print(f"Container Name: {container_name}")
            print(f"CPU Percent: {cpu_percent}%")
            print(f"Memory Usage: {memory_usage} bytes")

        time.sleep(1)  

if __name__ == "__main__":
    monitor_duration = 5  
    monitor_containers(monitor_duration)
