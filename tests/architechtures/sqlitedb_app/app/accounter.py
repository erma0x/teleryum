
# import time module, Observer, FileSystemEventHandler
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
  
  
class WatchDogTrader:
    watchDirectory = sys.path[0]+"/messages.txt"
    print('Trader Operative')
    print('WatchDog setted at the following directory: \n',watchDirectory)
  
    def __init__(self):
        self.observer = Observer()
  
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(2)
        except:
            self.observer.stop()
            print("Observer Stopped")
  
        self.observer.join()
  
  
class Handler(FileSystemEventHandler):
  
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        if event.event_type == 'modified':
            # Event is modified, you can process it now
            #print("Watchdog received modified event - % s." % event.src_path)
            print('Accounter writing OrderBook')
            writeOrderBook()


def getBalanceData():
    pass

def writeOrderBook():
    pass

  
if __name__ == '__main__':
    watch = WatchDogTrader()
    watch.run()