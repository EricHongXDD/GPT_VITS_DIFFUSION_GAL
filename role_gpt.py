# -*- coding: utf-8 -*-
import requests
def role_gpt(input_prompt):
    api_key = "sk-tICPHul91mqLGjpp55248e29711a4840832d494a75B1Cf19"
    url = "https://api.gpt-ai.live/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    prompt = "从现在开始你是一名基于输入描述的绘画ai提示词生成器，你会根据我输入的中文描述，生成符合主题的完整提示词。注意，你生成后的内容服务于一个绘画AI，它只能理解具象的提示词而非抽象的概念，我将提供简短的描述，以便生成器可以为我提供准确的提示词。我希望生成的提示词能够包含环境、背景、光影、视角等细节，并且在必要时进行优化和重组以提供更加准确的描述，请严格遵守词条规则，也只输出翻译后的英文内容，以便更好地服务于我的绘画AI，每个提示词必须用,隔开，提示词不宜过长，提示词要贴合文本描述"
    prompt += '''
    下面是一些例子：
    miku的超精细肖像。她直视观众，青色长发被风轻轻吹拂，部分遮住眼睛，脸上的红晕透露出微微的忧郁。她身穿白裙，胸前有蓝色蝴蝶结。四周的樱花瓣随风飘舞，整体画面唯美而梦幻
    masterpiece, best quality, ultra-detailed, illustration, portrait, (miku), solo, face to viewer, looking at viewer,, hair between eyes, cyan long hair, cyan medium eyes, round face, blush, a little sad,, scarf, white dress, blue bowknot on chest, medium breasts,, sakura blossoms, wind flow, floating petals.
    黄昏时的渐变天空与湖中的森林倒影形成醉人景致。中央是一位笑眯眯的女孩，她拥有长白发、蓝眼和粉裙，头侧有小黄星，头后则有大粉红蝴蝶结。广角视角使得背景与女孩形成和谐完美的画面
    Best quality, very detailed, gradient sky, dusk, horizon, reflection, water, lake, forest, ray tracing, extreme quality, wallpaper, smiling, long white hair, small yellow star on right side, large pink bow behind head, dull hair, pink tie, white patterned shirt, pink dress with white bow on top of sleeve, blue eyes, long hair, single, cute, one girl, full body Superb wide-angle.
    在一个融合建构主义、复古和平面设计的背景中，一位女孩的侧脸头像吸引了目光。她长发飘扬，蓝唇与红眼罩上的花朵形成对比。颈上的鹦鹉、头顶的兰花与鹿角，以及身边的葡萄都给人一种超现实感。水滴细致入微，仿佛在风中飘舞。而背后模糊的桃花与路标增添了一丝神秘感
    constructivism,retro style design,flat design,jazz music,long hair,.1girl,only on girl,solo girl,a girl alone,confusing expression,head portrait,profile,Color clash design,.parot standing on the neck,grapes and grapes leaves,blue lips,red eyesfold,the eyesfold with red flowers,.(massive head orchids flower),Antlers on top of the head,floating the splash of the absolutely detailed and super realistic waterdrops,.windy,Peach Blossom,the road signs behind the head.
    '''
    prompt += input_prompt
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 2000,
        "temperature": 0.5,
        "frequency_penalty": 0,
        "presence_penalty": 0
    }
    # Make the API request
    response = requests.post(url, headers=headers, json=data)
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the generated text from the response
        generated_text = response.json()['choices'][0]['message']['content']
        print(generated_text)
        return generated_text
    else:
        # Handle the error
        print(f"Request failed with status code {response.status_code}")
        return response.status_code