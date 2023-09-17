import json
import requests
import os

def vits(message,people,language,speed,key,sheet,character):
    url = "http://isaachong.work:61273"

    payload = {
        "data": [message, people, language, int(speed)],
        "event_data": None,
        "fn_index": 0,
    }

    session = requests.Session()
    session.cookies.clear()
    result = requests.post(url=f'{url}/run/predict', json=payload)

    data = json.loads(result.text)
    res = str(data["data"][1]["name"])
    res = "http://isaachong.work:61273/file=" + res
    # print(res)

    # 确保响应状态是200，这意味着请求是成功的
    response = requests.get(res, stream=True)
    if response.status_code == 200:
        # 确保 'audio' 文件夹存在
        if not os.path.exists('audio'):
            os.makedirs('audio')

        # 将音频文件保存到 'audio' 文件夹
        filepath = "audio/"+str(sheet)+"_"+str(character)+"_"+str(key)+".wav"
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        return True
    else:
        print(f"Error: Unable to download file. Status code: {response.status_code}")
        return False