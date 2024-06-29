#!/home/xzc/demo/venv/bin/python3

import requests
from json import JSONDecodeError
import urllib.request
import urllib.parse
import json



def translate_text(text,source_lang='',target_lang=''):
    # text: 需要翻译的文本
    # source_lang: 源语言 （此参数若不填写，将会进行自动检测
    # target_lang: 目标语言（此参数若不填写，将会自动翻译成中文）
    url = f"https://findmyip.net/api/translate.php?text={text}&source_lang={source_lang}&target_lang={target_lang}"
    response = requests.get(url)
    try:
        data = response.json()
        print(data)
        if response.status_code == 200:
            if data['code']== 200:
                translation = data['data']['translate_result']
                return translation
            elif data['code'] == 400:
                return data['error']
            else:
                return "内部接口错误，请联系开发者"
        else:
            return "内部接口错误，请联系开发者"    
    except JSONDecodeError as e:
        return f"JSON decoding error: {e}"
    except requests.RequestException as e:
        return f"Request error: {e}"    


def translate_en2ch(content):
    url = 'https://dict.youdao.com/webtranslate'
    data = {}
    data['i'] = content
    data['from'] = 'zh-CHS'
    data['to'] = 'en'
    data['useTerm'] = 'false'
    data['domain'] = '0'
    data['dictResult'] = 'true'
    data['keyid'] = 'webfanyi'
    data['sign'] = '74e77712f5cd61e87f9c619c4110845a'
    data['client'] = 'fanyideskweb'
    data['product'] = 'webfanyi'
    data['appVersion'] = '1.0.0'
    data['vendor'] = 'web'
    data['pointParam'] = 'client,mysticTime,product'
    data['mysticTime'] = '1719405055233'
    data['keyfrom'] = 'fanyi.web'
    data['mid'] = '1'
    data['screen'] = '1'
    data['model'] = '1'
    data['network'] = 'wifi'
    data['abtest'] = '0'
    data['yduuid'] = 'abcdefg'
    data = urllib.parse.urlencode(data).encode('utf-8')

    response = urllib.request.urlopen(url,data)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    return f"翻译结果{target['translateResult'][0][0]['tgt']}"


text_to_translate = "下面这段话将翻译成韩语:关于源语言和目标语言的代码，请自行谷歌“语言代码表”，自行进行对照填写"
translation_result = translate_text(text_to_translate, 'zh', 'en')
print("翻译结果:", translation_result)

print(translate_en2ch(text_to_translate))

