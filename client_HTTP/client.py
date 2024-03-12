import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests

class Watcher:
    DIRECTORY_TO_WATCH = "/path/to/watched/directory"  # 被監控的目錄

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def on_created(event):
        if not event.is_directory and event.src_path.endswith('.xlsx'):
            print(f"Excel file created: {event.src_path}")
            # 記得換成主機IP
            response = requests.post('http://192.168.1.100/process', files={'file': open(event.src_path, 'rb')})
            if response.status_code == 200:
                print("File successfully processed by server.")
            else:
                print(f"Server error or file not processed, status code: {response.status_code}")
            print(f"Response from server: {response.status_code}")

if __name__ == '__main__':
    w = Watcher()
    w.run()