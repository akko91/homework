from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
from bs4 import BeautifulSoup

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/order', methods=['POST'])
def orderPost():
    postName = request.form['postName']
    postNum = request.form['postNum']
    postAdr = request.form['postAdr']
    postTel = request.form['postTel']

    print(postName, postNum, postAdr, postTel);

    doc = {
        'name': postName,
        'num': postNum,
        'adr': postAdr,
        'tel': postTel
    }

    db.shopping.insert_one(doc);

    return jsonify({'result': 'success', 'msg': '주문이 완료되었습니다.'})


@app.route('/order', methods=['GET'])
def orderGet():
    orderList = list(db.shopping.find({}, {"_id": False}))
    print(orderList);

    returnVal = {'result': 'success', 'data': orderList}

    return jsonify(returnVal)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
