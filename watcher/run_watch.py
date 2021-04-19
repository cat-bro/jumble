import os
import argparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_any_event(self, event):   # could define functions for on_created, on_deleted, on_modified, on_moved
        print(event.event_type, event.src_path)

def main():
    parser = argparse.ArgumentParser( description='Watch a directory until interrupted')
    parser.add_argument('directory', help='Path to watch')
    args = parser.parse_args()

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(
        event_handler,
        path=args.directory,
        recursive=True
    )
    observer.start()

    while True:
        try:
            pass
        except KeyboardInterrupt:
            observer.stop()


if __name__ == '__main__':
    main()

