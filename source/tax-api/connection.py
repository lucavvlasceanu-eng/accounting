import requests
from zeep import Client
from zeep.transports import Transport
from zeep.wsse.signature import Signature
import ssl

session = requests.Session()

session.cert = (
    ""
)
