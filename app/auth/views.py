from flask import render_template, redirect, flash, request, session, url_for, app, send_file, send_from_directory
# 导入表单处理方法
from werkzeug.security import check_password_hash, generate_password_hash

from . import bp_auth
from ..model import User, db
import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


@bp_auth.route('/', methods=['GET', 'POST'])
def welcome():
    session.clear()
    # connection = db.engine.raw_connection()
    # cursor = connection.cursor()
    # #cursor.execute('call doctor_popular()')
    # cursor.execute('call doctor_top()')
    # doctorlist=(cursor.fetchall())
    #return render_template('mainpage.html',doctorlist=doctorlist,notice=notice)
    #return "ok"
    #return render_template('mainpage.html')
    #return redirect(url_for('auth.login'))
    session["user_id"] = 1
    basedir = os.path.abspath(os.path.dirname(__file__))
    maindir = os.path.dirname(basedir)
    pdir = os.path.dirname(maindir)
    print(maindir)
    return send_from_directory(pdir+'/projectfile/1/11',filename='in.zip', as_attachment=True)

    #return redirect(url_for('auth.login'))
    #return redirect(url_for('project.homepage'))


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(email)
        print(password)
        # #whether it is testresult/ administor
        # if userID == 'admin' and password=='a':
        #     session.clear()
        #     session["user_id"] = userID
        #     return redirect(url_for('testresult.homepage'))

        error = None
        error = check_user(email, password)

        if error is None:
            # store the wechat id in a new session and return to the index
            session.clear()
            user = User.query.filter(User.email == email).first()
            session["user_id"] = user.id
            print(user.id)
            #return "ok"
            return redirect(url_for('project.homepage'))
        flash(error)

    return render_template("auth/page-login.html")


@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        error = None
        name = request.form["name"]
        print(name)
        email = request.form["email"]
        print(email)
        password = request.form["password"]
        print(password)


        if User.query.filter(User.email == email).first() is not None:
            error = "User {0} is already registered.".format(email)
            flash(f'Your account has been created!', 'success')
            print("no")

        if error is None:
            db.session.add(User(name=name, email=email, password=generate_password_hash(password)))
            db.session.commit()
            print("here?")
            return redirect(url_for("auth.login"))

    return render_template('auth/page-register.html')


@bp_auth.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == "POST":
        email = request.form["email"]
        # smtpserver = "smtp.qq.com"
        # smtpport = 465
        # from_mail = "919769592@qq.com"
        # to_mail = [email]
        # password = "njcaytofvudobfij"  # 16位授权码
        #
        # subject = "test report"
        # from_name = "AFL测试平台"
        newpassword='12345678'


        msg_from = '919769592@qq.com'  # 发送方邮箱
        passwd = 'njcaytofvudobfij'  # 填入发送方邮箱的授权码
        msg_to = email  # 收件人邮箱

        subject = "重置密码"  # 主题
        content = "你的密码是：" + newpassword
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['From'] = msg_from
        msg['To'] = msg_to
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(msg_from, passwd)
            s.sendmail(msg_from, msg_to, msg.as_string())
            print("发送成功")

        except s.SMTPException as e:
            print("发送失败")
        finally:
            s.quit()


        #return redirect(url_for("auth.login"))
        return "ok"
    return render_template('auth/pages-forget.html')

def check_user(email, password):
    error = None
    user = User.query.filter(User.email == email).first()
    if user is None:
        error = "Incorrect username."
    elif not check_password_hash(user.password, password):
        error = "Incorrect password."

    return error

