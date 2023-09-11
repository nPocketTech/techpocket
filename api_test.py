import requests

url = 'https://api.npocket.tech/text_to_speech'
params = {'token': '07706CC302695C383D78229D71BE5D5DAFFC47F0',    # 寫上您的密鑰
          'text': '石獅寺前有四十四隻石獅子，寺前樹結了四十四個澀柿子'}    # 想產生的內容

res = requests.post(url, data=params)
res = res.json()
print(res)