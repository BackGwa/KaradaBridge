#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import json, os
import numpy as nlib

def setup(config_path, language_path, camera_index):

    config = open(f'{config_path}/karada.json', mode='r', encoding='utf-8')
    data = json.load(config)
    config.close()
    
    version = data['karada']['version']
    
    language = data['config']['language']
    sendrate = data['config']['sendrate']
    
    langpack = open(f'{language_path}/{language}.json', mode='r', encoding='utf-8')
    langjson = json.load(langpack)
    langpack.close()
    
    try:
        import cv2 as clib
        import mediapipe as mlib
    except:
        print(f'''{langjson['error_msg']['LIBRARY']}''')
        return -1
        
    try:
        tracking(clib,mlib, langjson, camera_index)
    except:
        print(f'''{langjson['error_msg']['UNKNOWN']}''')
        return -1
    
    return 0

def tracking(clib, mlib, langjson, camera_index):
    
    drawing = mlib.solutions.drawing_utils
    drawing_styles = mlib.solutions.drawing_styles
    poseset = mlib.solutions.pose
    
    cap = clib.VideoCapture(camera_index)
    with poseset.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as pose:
        
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print(f'''{langjson['error_msg']['CAMERA']}''')
                continue

            image.flags.writeable = False
            image = clib.cvtColor(image, clib.COLOR_BGR2RGB)
            results = pose.process(image)

            image.flags.writeable = True
            image = clib.cvtColor(image, clib.COLOR_RGB2BGR)
            
            drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                poseset.POSE_CONNECTIONS,
                landmark_drawing_spec=drawing_styles.get_default_pose_landmarks_style())

            clib.imshow('Karada Preview', clib.flip(image, 1))

    cap.release()
    return 0