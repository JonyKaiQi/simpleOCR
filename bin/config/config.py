#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 配置文件

import os



ACCESS_TOKEN = ''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ID,KEY的配置信息
INFO_CONFIG = {
    # 'ID': '14348843',
    # 'API_KEY': 'wc68dHtiY9mwuD7980EXr1I2',
    # 'SECRET_KEY': 'dCaMG095LvB9pdtRqbn5eWP4RFSLnj74'
    # 'ID': '14868017',
    # 'API_KEY': '6epPHS8EPX1k8GjdCzez7OLT',
    # 'SECRET_KEY': 'onZaVAlgYzEBchooR91xQf8j7kgoFG4W'
    # 'ID': '16988244',
    # 'API_KEY': 'ZGln1SSiSXMgRB4mUUnGyClw',
    # 'SECRET_KEY': 'HDNSmAXvfkxGY41njWuhGL5aagk8ISFT'
    # 'ID': '16988681',
    # 'API_KEY': 'ux7bIXK4Hn71BWAGtpZ1Y24F',
    # 'SECRET_KEY': 'i00zjqNNGGuKoDYf2n4QiUs3z9YVnpTX'
    # 'ID': '16988711',
    # 'API_KEY': 'l138nasf9D1Mjhb3rxGhL27r',
    # 'SECRET_KEY': 'cx8attE2EunMGWaSxUhHS0DF3NgozZDD'
    # 'ID': '16989684',
    # 'API_KEY': 'GR8amSQCmrk4fGvlvzUFEh89',
    # 'SECRET_KEY': 'AF71cRtt7CcrhYxGMxBzRgi5sdbuNPIa'
    'ID': '16989757',
    'API_KEY': 'IO85kW09w9RNaFUNyBvcGKzO',
    'SECRET_KEY': 'ur1ueFiHg56BDOM5U9AdCXY1lVlsIY60'
}

# 本地路径配置
LOCALHOST_PATH = {
    'PATH': os.path.join(BASE_DIR, 'simpleOCR/img/')
}

# URL配置
URL_LIST_URL = {
    # ACCESS_TOKEN_URL用于获取ACCESS_TOKEN, POST请求,
    #  grant_type必须参数,固定为client_credentials,client_id必须参数,应用的API Key,client_secre 必须参数,应用的Secret Key.
    'ACCESS_TOKEN_URL': 'https://aip.baidubce.com/oauth/2.0/token?' + 'grant_type=client_credentials&client_id={API_KEYS}&client_secret={SECRET_KEYS}&'.format(
        API_KEYS=INFO_CONFIG['API_KEY'], SECRET_KEYS=INFO_CONFIG['SECRET_KEY']),
    # 通用文字识别, 接口POST请求,
    'GENERAL_BASIC': 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic',
    # 通用文字识别(高精度版)
    'ACCURATE_BASIC': 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic',
    # 通用文字识别（含位置信息版）
    'GENERAL': 'https://aip.baidubce.com/rest/2.0/ocr/v1/general',
    # 通用文字识别（含位置高精度版）
    'ACCURATE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate',
    # 通用文字识别（含生僻字版）
    'GENNERAL_ENHANCED': 'https://aip.baidubce.com/rest/2.0/ocr/v1/general_enhanced',
    # 身份证识别
    'IDCARD': 'https://aip.baidubce.com/rest/2.0/ocr/v1/idcard',
    # 行驶证识别
    'VEHICLE_LICENSE': 'https://aip.baidubce.com/rest/2.0/ocr/v1/vehicle_license',

}
