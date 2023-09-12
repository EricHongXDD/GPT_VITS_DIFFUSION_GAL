# -*- coding: utf-8 -*-
import requests
def scene_gpt(input_prompt):
    api_key = "sk-tICPHul91mqLGjpp55248e29711a4840832d494a75B1Cf19"
    url = "https://api.gpt-ai.live/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    prompt = "从现在开始你是一名基于输入描述的绘画ai提示词生成器，你会根据我输入的中文描述，生成符合主题的完整提示词。注意，你生成后的内容服务于一个绘画AI，它只能理解具象的提示词而非抽象的概念，我将提供简短的描述，以便生成器可以为我提供准确的提示词。我希望生成的提示词能够包含环境、背景、光影、视角等细节，并且在必要时进行优化和重组以提供更加准确的描述，请严格遵守词条规则，也只输出翻译后的英文内容，以便更好地服务于我的绘画AI，每个提示词必须用,隔开，提示词不宜过长"
    prompt += '''
    下面是一些例子：
    小径的尽头是一栋传统的日式木屋，屋前有一小片精心修剪的庭院，池塘中的锦鲤穿梭其中，金色和白色的鱼鳞在阳光下闪闪发光
    High definition, 8k, masterpiece, best quality, traditional Japanese wooden house, at the end of the path, meticulously trimmed courtyard, koi fish swimming in the pond, shining in the sunlight, golden and white fish scales
    踏入屋内，榻榻米的香气扑鼻而来，墙角摆放的花瓶里插着新鲜的樱花
    HD, 8k, masterpiece, best quality, entering the room, tatami, fragrant aroma, fresh cherry blossoms, vase in the corner
    宽敞的阳台上摆放着躺椅，可以在此看日出日落，感受海风的吹拂。室内，海洋风格的装饰，墙上挂着贝壳和海星，沙发上铺着蓝白相间的毯子
    Spacious balcony, HD, 8k, masterpiece, best quality, sun loungers, overlooking the sunrise and sunset, feeling the gentle sea breeze, Indoors, ocean-themed decor, walls adorned with seashells and starfish, sofa covered with blue and white patterned blankets
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