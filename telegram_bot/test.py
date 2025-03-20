""" The file to test python logging setup. """

from logging import getLogger

log = getLogger(__name__)

print('before log')
log.info("HELLO I'm here!")
print('after log')
