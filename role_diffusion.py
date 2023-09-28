

import requests
import io
import base64
from PIL import Image
import json

# def flood_fill(data, x, y, target_color, threshold=40):
#     """
#     Flood fill algorithm to identify background pixels.
#     :param data: Pixel data (list of tuples).
#     :param x: Starting x position.
#     :param y: Starting y position.
#     :param target_color: The color of the starting pixel.
#     :param threshold: Tolerance for color difference.
#     :return: Set of background pixel coordinates.
#     """
#     width, height = len(data[0]), len(data)
#     visited = set()
#     to_fill = {(x, y)}
#
#     while to_fill:
#         x, y = to_fill.pop()
#         if (x, y) in visited or x < 0 or x >= width or y < 0 or y >= height:
#             continue
#         visited.add((x, y))
#
#         current_color = data[y][x]
#
#         if all([abs(current - target) <= threshold for current, target in zip(current_color, target_color)]):
#             to_fill.update({(x-1, y), (x+1, y), (x, y-1), (x, y+1)})
#     return visited
#
# def make_background_transparent(input_file, output_file):
#     img = Image.open(input_file)
#     img = img.convert('RGBA')
#     data = list(img.getdata())
#     width, height = img.width, img.height
#
#     # Convert 1D data to 2D
#     data_2d = [data[i * width:(i + 1) * width] for i in range(height)]
#
#     # Starting from top-left corner to determine background color
#     background_coords = flood_fill(data_2d, 0, 0, data_2d[0][0])
#
#     for x, y in background_coords:
#         index = y * width + x
#         data[index] = (255, 255, 255, 0)  # Set as transparent
#
#     img.putdata(data)
#     img.save(output_file, "PNG")

url = "http://isaachong.work:61272"
def role_txt2img(prompt,negative_prompt,scene_filename):
    prompt = prompt + ",masterpiece,best quality,solo,beautiful detailed eyes,delicate face"
    # negative_prompt = negative_prompt + "(worst quality, low quality:1.4), (badhandv4:1.3), negative_hand Negative Embedding,verybadimagenegative_v1.3, monochrome,lowres,fewer digits,blurry,signature,water mark,text,symbol, logo, door frame, window frame, mirror frame"
    negative_prompt = negative_prompt + "NSFW, (worst quality:2), (badhandv4:1.3), (low quality:2), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, age spot, (ugly:1.331), (duplicate:1.331), (morbid:1.21), (mutilated:1.21), (tranny:1.331), mutated hands, (poorly drawn hands:1.5), blurry, (bad anatomy:1.21), (bad proportions:1.331), extra limbs, (disfigured:1.331), (missing arms:1.331), (extra legs:1.331), (fused fingers:1.61051), (too many fingers:1.61051), (unclear eyes:1.331), lowers, bad hands, missing fingers, extra digit,bad hands, missing fingers, (((extra arms and legs))),nsfw,badhandv4, EasyNegative, verybadimagenegative_v1.3, illustration, 3d, sepia, painting, cartoons, sketch, (worst quality:1.74), (low quality:1.74), (normal quality:1.44), lowres, bad anatomy, normal quality, ((monochrome)), ((grayscale)), ((letters)), ((english)), capital"
    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        # 关键词相关性
        "cfg_scale": 7,
        "steps": 17,
        # 采样方法
        "sampler_index": "Euler a",
        # 模型选择
        "override_settings": {
            "sd_model_checkpoint":"Everyone.safetensors [ae9e11bc14]"
        },
        # 高清修复
        "enable_hr": True,
        "denoising_strength": 0.45, # 降噪强度

        "hr_scale": 2,
        "hr_upscaler": "R-ESRGAN 4x+ Anime6B",
        "hr_second_pass_steps": 8,
        # # 尺寸
        # "width": 720,
        # "height": 1152,
        # 尺寸
        "width": 640,
        "height": 360,
        # "alwayson_scripts": {
        #     "ControlNet": {
        #         "args": [
        #             {
        #                 "control_mode": 0,
        #                 "enabled": True,
        #                 "guidance_end": 1,
        #                 "guidance_start": 0.0,
        #                 "input_image": "data:image/png;base64,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",
        #                 "lowvram": False,
        #                 "model": "control_v11p_sd15_openpose_fp16 [73c2b67d]",
        #                 "module": None,
        #                 "pixel_perfect": False,
        #                 "processor_res": 64,
        #                 "resize_mode": 1,
        #                 "threshold_a": 0,
        #                 "threshold_b": 0,
        #                 "weight": 1
        #             },
        #         ]
        #     }
        # }

    }
    session = requests.Session()
    session.cookies.clear()
    result = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

    r = result.json()
    data = json.loads(result.text)
    print(data)

    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",", 1)[0])))
        image.save('images/'+scene_filename+'.png')
        print('images/'+scene_filename+'.png保存完成')
        return

# role_txt2img("masterpiece,best quality,1 girl,loli,cute,solo,beautiful detailed eyes,delicate face,sweater,pink hair,side bun,violet eyes,highlight dyeing,blouse,microskirt,black pantyhose,see-through,street,clock tower,depth of field,colored with greyscale background.","","testtt")
