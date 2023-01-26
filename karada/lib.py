#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import json, numpy, os

def setup():

    config = open('karada.json', mode='r', encoding='utf-8')
    data = json.load(config)
    config.close()
    
    version = data['karada']['version']
    
    language = data['config']['language']
    sendrate = data['config']['sendrate']
    
    langpack = open(f'./lang/{language}.json', mode='r', encoding='utf-8')
    langjson = json.load(langpack)
    langpack.close()
    
    try:
        import cv2 as tlib
    except:
        print(f'''{langjson['error_msg']['LIBRARY']}''')
        return -1
        
    try:
        tracking()
    except:
        print(f'''{langjson['error_msg']['UNKNOWN']}''')
        return -1
    
    return 0

def tracking():
    
    
    return 0