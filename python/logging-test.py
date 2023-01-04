import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


logger = logging.getLogger()
logger.setLevel(logging.INFO)

foo = 'adjslad'
bar = None
logger.info(f'abcde {foo} {bar} {None}')