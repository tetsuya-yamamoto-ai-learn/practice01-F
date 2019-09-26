"""
Simple BBS
簡単な掲示板

要件:
1. ページ上部に大きくSimple BBSと書かれている
2. Username と Messageを入力するフォームがある
3. 送信と書かれたスイッチがある
4. 入力された文字が掲示板に表示されていく（下段に追加されていく）
5. Username に何も入力されていない状態で送信された場合は名無しさんにする
6. Message に何も入力されていない状態で送信された場合は空欄にする

"""
import os

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # 初めてページが選択された時
    if request.method == 'GET':

        # コメントの読み込み
        documents = []
        if os.path.isfile("document.txt"):
            with open('document.txt', 'r') as file:
                line = file.readline()[:-1]
                while line:
                    line_list = line.split(',')
                    # print(line_list)
                    documents.append(line_list)
                    line = file.readline()[:-1]

        return render_template('BBS.html', documents=documents)

    # 送信がクリックされた時
    if request.method == 'POST':
        username = request.form['username']
        message = request.form['message']

        # usernameがないときは"名無しさん"に変更
        if username == '':
            username = '名無しさん'

        # コメントの書き込み
        with open('document.txt', mode='a') as file:
            file.write(f'{username},{message}\n')

        # コメントの読み込み
        with open('document.txt', 'r') as file:
            documents = []
            line = file.readline()[:-1]
            while line:
                line_list = line.split(',')
                # print(line_list)
                documents.append(line_list)
                line = file.readline()[:-1]

        return render_template('BBS.html', documents=documents)


if __name__ == '__main__':
    app.run(debug=True)
