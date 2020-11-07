import logging

fmtstr = "%(asctime)s -> [%(levelname)s]:  %(message)s"
datestr = "%m/%d/%Y %I:%M:%S %p "

def init_logger():
    logging.basicConfig(
        filename="logfile.log",
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