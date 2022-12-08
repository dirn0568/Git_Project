import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
uvData = requests.get('https://weather.naver.com/',headers=headers)

uvSoup = BeautifulSoup(uvData.text, 'html.parser')


uvStatus = uvSoup.select_one('#lifeIndex > div.inner_card > div > div > ul > li:nth-child(1) > div').text.strip()
uvScore = 0

if (uvStatus=="낮음") :
    uvScore=15
elif (uvStatus=="보통"):
    uvScore = 10
elif (uvStatus=="높음"):
    uvScore = 5
elif (uvStatus == "매우높음"):
    uvScore = 0
elif (uvStatus == "위험"):
    uvScore = -20
else:
    uvScore = '표시 내용이 없습니다'

uv_list=[uvStatus,uvScore]

print("s322323451234")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/uv', methods=['GET'])
def uv_get():
   return jsonify({'uv':uv_list})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)