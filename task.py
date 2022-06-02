import logging
import sys
import os
from time import sleep
from urllib.request import urlopen, Request
# import app


from xvfbwrapper import Xvfb
vdisplay = Xvfb()
vdisplay.start()

print(os.environ['DISPLAY'])

stdout = logging.StreamHandler(sys.stdout)

logging.basicConfig(
    level=logging.INFO,
    format="[{%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
    handlers=[stdout],
)

LOGGER = logging.getLogger(__name__)


httprequest = Request("https://icanhazip.com", headers={"Accept": "application/json"})
with urlopen(httprequest) as response:
    LOGGER.info(response.status)
    LOGGER.info(response.read().decode())

sleep(30)
import backend
backend.main()

