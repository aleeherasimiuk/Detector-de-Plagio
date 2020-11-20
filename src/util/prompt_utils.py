import itertools

import time
import sys

done = False
# here is the animation


def animate():
  for c in itertools.cycle(['|', '/', '-', '\\']):
    if done:
        break
    sys.stdout.write('\rProcesando ' + c)
    sys.stdout.flush()
    time.sleep(0.1)


def finish(text):
    done = True
    sys.stdout.write('\r{}                              \n'.format(text))
    #sys.stdout.flush()


# long process here
# time.sleep(10)
##done = True
