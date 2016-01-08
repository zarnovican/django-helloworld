
import os
import sys
import time

while True:
    print('')
    print('='*100)
    for k, v in os.environ.items():
        print(k, v)
    sys.stdout.flush()
    time.sleep(10)

