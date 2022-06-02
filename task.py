import logging
import sys
import os
from time import sleep
from urllib.request import urlopen, Request
# import app

from sys import platform
if platform == "linux" or platform == "linux2":
    # linux
    from xvfbwrapper import Xvfb
    vdisplay = Xvfb()
    vdisplay.start()
    print(os.environ['DISPLAY'])
elif platform == "darwin":
    # OS X
    pass
elif platform == "win32":
    # Windows...
    pass


stdout = logging.StreamHandler(sys.stdout)

logging.basicConfig(
    level=logging.INFO,
    format="[{%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
    handlers=[stdout],
)

LOGGER = logging.getLogger(__name__)


# httprequest = Request("https://icanhazip.com", headers={"Accept": "application/json"})
# with urlopen(httprequest) as response:
#     LOGGER.info(response.status)
#     LOGGER.info(response.read().decode())


from pyngrok import ngrok
http_tunnel = ngrok.connect(8080, "tcp")
import backend
backend.main()

