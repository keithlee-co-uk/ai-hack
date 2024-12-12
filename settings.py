from logging import basicConfig, DEBUG, INFO, getLogger

debug = True

level = INFO
if debug:
    level = DEBUG

logging_file = "logs/ai-hack.log"
basicConfig(filename=logging_file,
            format='%(asctime)s (%(levelname)s) %(message)s',
            level=DEBUG,
            datefmt='%d.%m.%Y %H:%M:%S')
logger = getLogger(__name__)

key = "<replace with api key>"