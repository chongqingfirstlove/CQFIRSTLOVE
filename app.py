from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/register',methods=['GET'])
def register():
    return render_template('register.html')

@app.route('/register2',methods=['GET','POST'])
def register2():
    #可以放在一个里面，用不同方法来区分
    if request.method=='GET':
        return render_template('register2.html')
    else:
        print(request.form)#通过post形式发送过来的数据
        print()
        print(request.form.get('USER'))
        print(request.form.getlist('领域'))
        return "注册成功"
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        print(request.form.get('user'))
        print(request.form.get('SWD'))
        return "登录成功"    
@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/do/reg')
# def do():
#     #1.接受数据
#     #2.返回结果
#     print(request.args)#通过get形式发送过来的数据
#     print()
#     print(request.args.get())
#     return "注册成功"

# @app.route('/post/reg',methods=['POST'])
# def do2():
#     #1.接受数据
#     #2.返回结果
#     print(request.form)#通过post形式发送过来的数据
#     print()
#     print(request.form.get('USER'))
#     print(request.form.getlist('领域'))
#     return "注册成功"
if __name__ == "__main__":
    app.run()