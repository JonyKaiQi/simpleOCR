#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 行驶证识别
import os
import base64
import requests
from bin.AccessToken.AccessToken import AccessToken
from bin.config.config import LOCALHOST_PATH, URL_LIST_URL

ACCESS_TOKEN = AccessToken().getToken()['access_token']

VEHICLE_LICENSE_URL = URL_LIST_URL['VEHICLE_LICENSE'] + '?access_token={}'.format(ACCESS_TOKEN)


class VehicleLicenseSuper(object):
    pass


class VehicleLicense(VehicleLicenseSuper):

    def __init__(self, image=None, detect_direction=True, accuracy='normal'):
        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.IMAGE_CONFIG = {
            'detect_direction': detect_direction,
            'accuracy': accuracy
        }

        if image is not None:
            imagepath = os.path.exists(LOCALHOST_PATH['PATH'] + image)
            if imagepath == True:
                images = LOCALHOST_PATH['PATH'] + image
                with open(images, 'rb') as images:
                    self.IMAGE_CONFIG['image'] = base64.b64encode(images.read())

    def postVehicleLicense(self):
        if self.IMAGE_CONFIG.get('image', None) == None:
            return 'image参数不能为空！'
        vehicleLicense = requests.post(url=VEHICLE_LICENSE_URL, headers=self.HEADER,
                                       data=self.IMAGE_CONFIG)
        return vehicleLicense.json()
