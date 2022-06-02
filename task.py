from urllib.request import urlopen, Request
# 
from time import sleep
# import app

import logging
import sys

from xvfbwrapper import Xvfb
vdisplay = Xvfb()
vdisplay.start()

stdout = logging.StreamHandler(sys.stdout)

logging.basicConfig(
    level=logging.INFO,
    format="[{%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
    handlers=[stdout],
)

LOGGER = logging.getLogger(__name__)


httprequest = Request("https://icanhazip.com", headers={"Accept": "application/json"})
with urlopen(httprequest) as response:
    LOGGER.warn(response.status)
    LOGGER.warn(response.read().decode())

sleep(30)
import backend
backend.main()

