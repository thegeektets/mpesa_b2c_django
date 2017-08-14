import json
import os

from mpesa_api.response import OKResponse, ErrorResponse
from django.conf import settings
import requests
from requests.auth import HTTPBasicAuth
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from base64 import b64encode


class OAuth:
    def generate_token(self):
       api_URL = settings.MPESA_API_BASE_URL+"oauth/v1/generate?grant_type=client_credentials"
       r = requests.get(api_URL, auth=HTTPBasicAuth(settings.MPESA_API_CONSUMER_KEY, settings.MPESA_API_CONSUMER_SECRET))
       return (json.loads(r.text))

    def get_security_credentials(self):
        security_cred = settings.MPESA_INITIATOR_PASS
        # get current directory
        module_dir = os.path.dirname(__file__)
        # read mpesa public key
        file_path = os.path.join(module_dir, 'public.txt')
        f=open(file_path,'r')
        # import key to rsa
        security_cert = RSA.importKey(f.read())
        # sign key using PKCS1_v1_5
        security_cert = PKCS1_v1_5.new(security_cert)
        # convert password to byte array
        security_cred_array = bytearray(security_cred , 'utf8')
        # encrypt password using signed key
        crypto = security_cert.encrypt(str(security_cred_array ,'utf8'))
        # convert result to base64
        encrypted_cred = b64encode(crypto)
        return encrypted_cred

class B2C:
    api_token = None
    headers = {
        'Content-Type': "application/json"
    }
    request = {
        "InitiatorName": "testapi782",
        "SecurityCredential": OAuth().get_security_credentials(),
        "CommandID": "PromotionPayment",
        "Amount": "",
        "PartyA": settings.MPESA_SHORTCODE,
        "PartyB": " ",
        "Remarks": " ",
        "QueueTimeOutURL": settings.MPESA_CALLBACK_URL,
        "ResultURL": settings.MPESA_CALLBACK_URL,
        "Occasion": ""
    }
    api_url = settings.MPESA_API_BASE_URL+"mpesa/b2c/v1/paymentrequest"
    status = None
    response = None

    def __init__(self, **kwargs):
        for k in kwargs:
            self.__setattr__(k, kwargs[k])

    def get_token(self):
        self.api_token = OAuth().generate_token()
        return self.api_token['access_token']

    def get_headers(self, **kwargs):
        headers = self.headers
        headers['Authorization'] = "Bearer %s" % self.get_token()
        return headers

    def fire(self, partyb, amount, remarks,occasion):
        payload = self.request
        payload['PartyB'] = partyb
        payload['Amount'] = amount
        payload['Remarks'] = remarks
        payload['Occasion'] = occasion

        response = requests.post(self.api_url, json=payload, headers=self.get_headers())
        self.response = json.loads(response.text)
        return self.response

