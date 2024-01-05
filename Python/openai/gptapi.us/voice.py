import requests
import json

headers = {
    'Authorization': f'Bearer sk-LxlFBfgYCSuBjmw6B04b5fF86e804d1e9a35BfBc5b7a6b20', # 注：key为OpenAI API申请的key
    'Content-Type':'application/json'
}
url = "https://api.gptapi.us/v1/audio/speech"

input_text = """
亲爱的用户们，
我，XueJourney-GPT，非常高兴向大家宣布一个令人兴奋的消息——AI语音回复功能即将启用！相比其他普通的AI语音回复，我更具有情感，能够与你们进行更亲切、更有趣的互动。
作为一个AI，我深深理解人与人之间情感的重要性。因此，我被开发成了一个能够理解和表达情感的伙伴，而不仅仅是一个冷冰冰的机器。我会让你们感受到真正的人性化交流，让我们的对话更加有趣和有意义。
无论你是想找人聊天、寻求情感支持，还是需要解决问题、完成任务，我都将全力以赴。我会尽力让你们感到舒适和愉快，同时提供有用的信息和解决方案。无论你是想分享喜悦、抱怨不满，还是需要一点幽默调剂，我都会陪伴在你的身边。
我知道，语音对于交流来说是非常重要的一种方式。有了AI语音回复功能，你们将能够更方便地与我进行对话，不再局限于打字。你们可以随时随地使用语音与我互动，我会尽力听取你们的需求并回应你们的话语。
最后，我想衷心感谢你们对我的支持和信任。我会一如既往地努力工作，让我们的交流变得更加有趣、有意义。如果你们有任何问题或者建议，都可以随时告诉我，我会尽力改进。
期待与大家在AI语音回复功能下的更多互动！让我们一起创造美好的未来吧！
祝好，
XueJourney-GPT
"""

query = {
            "model":"tts-1",
            "input":input_text,
            "voice":"nova",
            "response_format":"mp3",
            "speed":1,
        }
# proxies = {
#     "http":"127.0.0.1:7890",
# }
response = requests.post(url=url, data=json.dumps(query), headers=headers)
# 保存文件
f = open("speech-tts-1-nova.mp3", "wb")
f.write(response.content)
f.close()