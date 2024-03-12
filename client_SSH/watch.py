import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import docker

class Watcher:
    DIRECTORY_TO_WATCH = "/path/to/your/directory"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

class Handler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(('.xlsx', '.xls')):
            print(f"Detected new Excel file: {event.src_path}")
            trigger_docker_action()

def trigger_docker_action():
    # Host docker IP
    remote_docker_url = 'tcp://your.docker.host.ip:2375'
    client = docker.DockerClient(base_url=remote_docker_url)

    # 運行命令
    container = client.containers.run("ubuntu:latest", "echo Hello from the Docker container", detach=True)
    print(f"Started container {container.id}")
    
    # 其他可以做的事情

if __name__ == '__main__':
    w = Watcher()
    w.run()
