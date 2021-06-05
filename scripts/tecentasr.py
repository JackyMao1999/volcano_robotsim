#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import rospy
from volcano_robotsim.msg import TencentStamped
import os
import speech_recognition as sr
import json
import time
import base64
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models


# 获取语音数据
def get_file_content(filepath):
    data = ""
    with open(filepath,"rb") as f:
        data = base64.b64encode(f.read()) 
    str_data = str(data,encoding = 'utf-8')
    f.close()
    return str_data # base64数据

# 向01.wav中写入要识别的内容
def write_file_data(filepath,audio):
    with open(filepath,"wb") as f:
        f.write(audio.get_wav_data())
    f.close()

# 向腾讯云发送要识别的数据
def send_data_to_tencentcloud():
    result = ""
    try: 
        cred = credential.Credential("", "") 
        httpProfile = HttpProfile()
        httpProfile.endpoint = "asr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = asr_client.AsrClient(cred, "", clientProfile) 
        
        req = models.SentenceRecognitionRequest()
        params = {
            "ProjectId": 0,
            "SubServiceType": 2,
            "EngSerViceType": "8k_zh",
            "SourceType": 1,
            "VoiceFormat": "wav",
            "UsrAudioKey": "test",
            "Data": get_file_content("01.wav")
        }
        req.from_json_string(json.dumps(params))

        resp = client.SentenceRecognition(req) 
        result = get_data_from_tencentcloud(resp.to_json_string())
    except TencentCloudSDKException as err: 
        print(err) 
    return result


# 从腾讯云返回的数据获取需要的数据
def get_data_from_tencentcloud(resp):
    #print(resp) 
    js_res = json.loads(resp)
    print(js_res["Result"])
    return js_res["Result"]

# 使用pocketsphinx实现语音唤醒
def wake_up():
    wakeup_flag = 0
    r = sr.Recognizer()
    # obtain audio from the microphone
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
        print('say something')
        # os.system("aplay \"dd.wav\"")
        audio = r.listen(source)
        # recognize speech using Sphinx
        try:
            phrase = r.recognize_sphinx(audio,language="zh-CN")
            print("Sphinx thinks you said " + phrase)
            if str(phrase) == "你好小科":
                wakeup_flag = 1
                os.system("ekho  \"我在，你说\" ")
                print("正在录音...")
                audio = r.record(source,4,3) # 从第3秒开始计时5秒
                print("录音完成")
                os.system("ekho  \"好的，主人\" ")
            else:
                print("未能唤醒")
                wakeup_flag = 0
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
            wakeup_flag = 0
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
            wakeup_flag = 0
        return wakeup_flag,audio

if __name__ == "__main__":
    rospy.init_node("Tencent_voice", anonymous=True)
    phrase_pub = rospy.Publisher("volcano/tencent_phrase", TencentStamped, queue_size=1)
    phrase_msg = TencentStamped()
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        wakeup_flag, audio = wake_up()
        if wakeup_flag:
            write_file_data("01.wav", audio)
            result = send_data_to_tencentcloud()
            phrase_msg.tencent_phrase = result
        else:
            phrase_msg.tencent_phrase = "无"
        phrase_pub.publish(phrase_msg)
        rate.sleep()
