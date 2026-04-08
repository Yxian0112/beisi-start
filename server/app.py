from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
# 开启跨域支持，这样你本地打开的 HTML 才能访问到这个 Python 服务
CORS(app)

# 任务书要求：校验账号密码（硬编码）
ADMIN_USER = "admin"
ADMIN_PWD = "123456"

@app.route('/api/login', methods=['POST'])
def login():
    # 获取前端发送的 JSON 数据
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # 逻辑校验
    if username == ADMIN_USER and password == ADMIN_PWD:
        # 成功响应：code 0，模拟 Token
        return jsonify({
            "code": 0,
            "message": "Login successful",
            "data": {
                "token": "abcdef123456-flask-mock-token"
            }
        }), 200
    else:
        # 失败响应：code 1
        return jsonify({
            "code": 1,
            "message": "Invalid username or password",
            "data": None
        }), 200

if __name__ == '__main__':
    # 启动服务，默认端口 5000
    print("后端服务正在启动，监听地址：http://127.0.0.1:5000")
    app.run(debug=True, port=5000)