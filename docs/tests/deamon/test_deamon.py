import daemon
import time

def main():
    print('hello')
    time.sleep(5)

with daemon.DaemonContext():
    main()