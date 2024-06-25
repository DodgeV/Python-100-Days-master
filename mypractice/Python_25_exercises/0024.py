'''
第 0024 题： 使用 Python 的 Web 框架，做一个 Web 版本 TodoList 应用。
'''
# 不想搞web，跳过本题

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Web 版本 TodoList 应用...'

app.run()