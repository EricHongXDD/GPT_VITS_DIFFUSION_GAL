import requests
import io
import base64
from PIL import Image

url = "http://isaachong.work:61272"
def scene_txt2img(prompt,negative_prompt,scene_filename):
    prompt = prompt + ",best quality,(masterpiece:1.3),ultra-detailed,unity 8k wallpaper,(no people:1.4)"
    # negative_prompt = negative_prompt + "(worst quality, low quality:1.4), (badhandv4:1.3), negative_hand Negative Embedding,verybadimagenegative_v1.3, monochrome,lowres,fewer digits,blurry,signature,water mark,text,symbol, logo, door frame, window frame, mirror frame"
    negative_prompt = negative_prompt + "(worst quality, low quality:1.4), negative_hand Negative Embedding,verybadimagenegative_v1.3, monochrome,lowres,fewer digits,blurry,signature,water mark,text,symbol, logo, door frame, window frame, mirror frame"
    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        # 关键词相关性
        "cfg_scale": 7,
        "steps": 25,
        # 采样方法
        "sampler_index": "DPM++ 2M SDE Karras",
        # 模型选择
        "override_settings": {
            "sd_model_checkpoint" :"规则深背景_A Regular Deep Background_奥行のあるいつも_V1.0.safetensors [d4620223b4]"
        },
        # # 高清修复
        # "enable_hr": True,
        # "hr_scale": 1.7,
        # "hr_upscaler": "R-ESRGAN 4x+ Anime6B",
        # 尺寸
        "width": 1280,
        "height": 720,
    }
    session = requests.Session()
    session.cookies.clear()
    result = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

    r = result.json()
    # data = json.loads(result.text)
    # print(data)

    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",", 1)[0])))
        image.save('images/'+scene_filename+'.png')
        print('images/'+scene_filename+'.png保存完成')