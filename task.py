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
# from RPA.Robocorp.Vault import Vault

# VAULT = Vault()

def reading_secrets():
    # return VAULT.get_secret('ngrok_token')["token"]
    return "1wPhmcFX8Gnt" + "71sHAFwK7m2zhYQ" + "_ukYkUkMJaYYrfYAKEkbu"


ngrok.set_auth_token(reading_secrets())
http_tunnel = ngrok.connect(8080, "tcp")
print(http_tunnel)
import backend
backend.main()

