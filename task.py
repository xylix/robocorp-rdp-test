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


from pyngrok import ngrok
# from RPA.Robocorp.Vault import Vault

# VAULT = Vault()

# def reading_secrets():
#     # return VAULT.get_secret('ngrok_token')["token"]
#     


# ngrok.set_auth_token()
http_tunnel = ngrok.connect(8080, "tcp")
print(http_tunnel)
import backend
backend.main()

