import logging
from datetime import datetime
today = datetime.now().date().strftime("%b-%d-%Y")

fmtstr = "%(asctime)s -> [%(levelname)s]:  %(message)s"
datestr = "%I:%M:%S %p "

def init_logger():
    logging.basicConfig(
        filename="../logs/{}.log".format(today),
        level=logging.INFO,
        filemode="w",
        format=fmtstr,
        datefmt=datestr,
    )

def debug(message):
  logging.debug(message)

def error(message):
  logging.error(message)

def warning(message):
  logging.warning(message)

def info(message):
  logging.info(message)