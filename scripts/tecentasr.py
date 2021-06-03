#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import rospy
from volcano_robotsim.msg import TencentStamped
from volcano_robotsim.msg import VolcanoGoal
import os
import speech_recognition as sr
import json
import time
import base64
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models as  asr_models
from tencentcloud.nlp.v20190408 import nlp_client, models as  nlp_models
SecretId = ""
SecretKey = ""

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
        cred = credential.Credential(SecretId, SecretKey) 
        httpProfile = HttpProfile()
        httpProfile.endpoint = "asr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = asr_client.AsrClient(cred, "", clientProfile) 
        
        req = asr_models.SentenceRecognitionRequest()
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
        result_asr = get_data_from_tencentcloud(resp.to_json_string(),0)
        result_nlp,is_move = robot_is_move(result_asr)
    except TencentCloudSDKException as err: 
        print(err) 
    return result_nlp,is_move

# 机器人是否需要移动
def robot_is_move(result_asr):
    goal_msg = VolcanoGoal()
    is_move = 0
    type_b = 0
    result_nlp = " "
    if result_asr.find("马克思主义")!=-1 or result_asr.find("列宁主义")!=-1 or result_asr.find("毛泽东思想")!=-1 or result_asr.find("邓小平理论")!=-1:
        goal_msg.goal_name = "A"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("哲学")!=-1 or result_asr.find("宗教")!=-1:
        goal_msg.goal_name = "B"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("社会科学总论")!=-1:
        goal_msg.goal_name = "C"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("政治")!=-1 or result_asr.find("法律")!=-1:
        goal_msg.goal_name = "D"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("军事")!=-1:
        goal_msg.goal_name = "E"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("经济")!=-1:
        goal_msg.goal_name = "F"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("文化")!=-1 or result_asr.find("科学")!=-1 or result_asr.find("教育")!=-1 or result_asr.find("体育")!=-1:
        goal_msg.goal_name = "G"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("语言")!=-1 or result_asr.find("文字")!=-1:
        goal_msg.goal_name = "F"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("工业技术")!=-1:
        goal_msg.goal_name = "T"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("一般工业技术")!=-1:
        goal_msg.goal_name = "TB"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("矿业工程")!=-1:
        goal_msg.goal_name = "TD"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("石油")!=-1 or result_asr.find("天然气工业")!=-1:
        goal_msg.goal_name = "TE"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("冶金工业")!=-1:
        goal_msg.goal_name = "TF"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("金属学与金属工艺")!=-1:
        goal_msg.goal_name = "TG"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("机械")!=-1 or result_asr.find("仪表工业")!=-1:
        goal_msg.goal_name = "TH"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("武器工业")!=-1:
        goal_msg.goal_name = "TJ"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("能源与动力工程")!=-1:
        goal_msg.goal_name = "TK"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("电子能技术")!=-1:
        goal_msg.goal_name = "TL"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("电工技术")!=-1:
        goal_msg.goal_name = "TM"
        goal_msg.build_type = type_b
        is_move = 1
    elif result_asr.find("光线电电子学")!=-1 or result_asr.find("电信技术")!=-1:
        goal_msg.goal_name = "TN"
        goal_msg.build_type = type_b
        is_move = 1
    else:
        result_nlp = nlp_client_to_tencentcloud(result_asr)
        is_move = 0
    if is_move:
        goal_pub.publish(goal_msg);
    return result_nlp,is_move

# 从腾讯云返回的数据获取需要的数据
def get_data_from_tencentcloud(resp,find):
    #print(resp) 
    if  find == 0:
        js_res = json.loads(resp)
        print(js_res["Result"])
        return js_res["Result"]
    else:
        js_res = json.loads(resp)
        print(js_res["Reply"])
        return js_res["Reply"]

# 腾讯云NLP自然语义识别
def nlp_client_to_tencentcloud(resp):
    try: 
        cred = credential.Credential(SecretId, SecretKey) 
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile) 

        req = nlp_models.ChatBotRequest()
        params = {
            "Query": resp
        }
        req.from_json_string(json.dumps(params))

        resp = client.ChatBot(req) 
        result_nlp = get_data_from_tencentcloud(resp.to_json_string(),1)
        return result_nlp

    except TencentCloudSDKException as err: 
        print(err) 


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
                
                print("正在录音...")
                audio = r.record(source,4,3) # 从第3秒开始计时5秒
                print("录音完成")
                
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
    goal_pub = rospy.Publisher("/volcano/goal", VolcanoGoal, queue_size=1)
    phrase_msg = TencentStamped()
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        wakeup_flag, audio = wake_up()
        if wakeup_flag:
            write_file_data("01.wav", audio)
            result,is_move = send_data_to_tencentcloud()
        
            if is_move == 0:
                result_str = "ekho \"{0}\"".format(result)
                os.system(result_str)
                phrase_msg.tencent_phrase = result
            else:
                os.system("ekho 好的")
        else:
            phrase_msg.tencent_phrase = "无"
        phrase_pub.publish(phrase_msg)
        rate.sleep()
