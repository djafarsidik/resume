# accounts.utils
import datetime
import jwt
from django.conf import settings

import codecs
import hashlib
import hmac
from random import randint
import calendar
import time
from datetime import datetime, timezone


def generate_access_token(user):
    access_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=10),
        'iat': datetime.datetime.utcnow(),
    }
    access_token = jwt.encode(access_token_payload,
                              settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
    return access_token


# def generate_refresh_token(user, token_version):
def generate_refresh_token(user):
    refresh_token_payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=10),
        'iat': datetime.datetime.utcnow()
    }
    refresh_token = jwt.encode(
        refresh_token_payload, settings.SECRET_KEY, algorithm='HS256').decode('utf-8')
    # refresh_token_payload, settings.REFRESH_TOKEN_SECRET, algorithm = 'HS256').decode('utf-8')

    return refresh_token


def generate_signature2(param):
    # try:
    #     command = param['command']
    #     username = param['username']
    #     password = param['password']
    #     timestamp = param['timestamp']
    #     b_token = codecs.utf_8_encode(settings.TOKEN_SIGNATURE)
    #     strmsg = command + "" + username + "" + password + "" + str(timestamp)
    #     b_strmsg = codecs.utf_8_encode(strmsg)
    #     signature = hmac.new(b_token[0], b_strmsg[0], hashlib.sha1).hexdigest()
    #
    #     return signature
    #
    # except Exception as e:
    #     return "Error Create Signature + " +str(e)
    print(param['command'])
    command = param['command']
    username = param['username']
    password = param['password']
    timestamp = param['timestamp']
    b_token = codecs.utf_8_encode(settings.TOKEN_SIGNATURE)
    strmsg = command + "" + username + "" + password + "" + str(timestamp)
    b_strmsg = codecs.utf_8_encode(strmsg)
    signature = hmac.new(b_token[0], b_strmsg[0], hashlib.sha1).hexdigest()
    return signature


def generate_partner_token():
    return randint(100000, 999999)


def gmdate(str_formate, int_timestamp=None):
    if int_timestamp == None:
        return time.strftime(str_formate, time.gmtime())
    else:
        return time.strftime(str_formate, time.gmtime(int_timestamp))


def get_timestamp():
    current_utcdatetime = datetime.now(timezone.utc)
    current_utctimestamp = current_utcdatetime.timestamp()

    return int(current_utctimestamp)


def generate_signature(param):
    # try:
    email = param['email']
    password = param['password']
    if 'token' in param:
        b_token = codecs.utf_8_encode(param['token'])
    else:
        b_token = codecs.utf_8_encode(settings.TOKEN_SIGNATURE)

    timestamp = param['timestamp']
    strmsg = email + "" + password + "" + str(timestamp)
    b_strmsg = codecs.utf_8_encode(strmsg)
    signature = hmac.new(b_token[0], b_strmsg[0], hashlib.sha1).hexdigest()

    return signature
    #
    # except:
    #     return "Error Create Signature"


# def custom_exception_handler(exc, context):
#     # Call REST framework's default exception handler first,
#     # to get the standard error response.
#     response = exception_handler(exc, context)
#
#     # Now add the HTTP status code to the response.
#     if response is not None:
#         response.data['status_code'] = response.status_code
#         response.data['status'] = False
#
#     return response


import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


def check_mail(email):
    if (re.search(regex, email)):
        return True
    else:
        return False
