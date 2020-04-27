from flask import render_template, redirect, flash, request, session, url_for, app, send_file, send_from_directory
# 导入表单处理方法
from werkzeug.security import check_password_hash, generate_password_hash

from ..cLass import UserClass,MycollectClass
from . import bp_auth

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
    session["user_id"] = 9
    # basedir = os.path.abspath(os.path.dirname(__file__))
    # maindir = os.path.dirname(basedir)
    # pdir = os.path.dirname(maindir)
    # print(maindir)
    #print(os.path.abspath(os.path.dirname(__file__)))
    #return send_from_directory(pdir+'/projectfile/100/11',filename='in.zip', as_attachment=True)
    # user=UserClass("asdf")
    # print(user.getpath())
    #return redirect(url_for('auth.login'))
    #return send_file('index.html')
    return redirect(url_for('project.homepage'))

@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        print(email)
        print(password)
        # #whether it is publicproject/ administor
        # if userID == 'admin' and password=='a':
        #     session.clear()
        #     session["user_id"] = userID
        #     return redirect(url_for('publicproject.homepage'))
        newuser=UserClass(email)
        error = None
        error = newuser.check_user(password)
        if error is None:
            # store the wechat id in a new session and return to the index
            session.clear()
            # user = User.query.filter(User.email == email).first()
            session["user_id"] = newuser.getid()
            print(session["user_id"])
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
        newuser = UserClass(email)
        '''
        如果邮箱已存在
        '''
        if newuser.is_exit():
            error = "User {0} is already registered.".format(email)
            flash(f'Your account has been created!', 'success')
            print("no")

        if error is None:
            newuser.register(name,password)
            newuser.mkdir()
            return redirect(url_for("auth.login"))
    return render_template('auth/page-register.html')


@bp_auth.route('/forgot', methods=['GET', 'POST'])
def forgot():
    if request.method == "POST":
        email = request.form["email"]
        user = UserClass(email)
        user.sendemail()
        return redirect(url_for("auth.login"))

    return render_template('auth/pages-forget.html')



@bp_auth.route('/user/profile', methods=['GET', 'POST'])
def profile():
    user = UserClass.getfromid(session["user_id"])
    userinfo=user.myprofile()

    return render_template('auth/profile.html',user=userinfo)

@bp_auth.route('/user/mycollect', methods=['GET', 'POST'])
def mycollect():
    mycollect = MycollectClass()
    project=mycollect.mycollect(session["user_id"])

    return render_template('project/mycollect.html',projects=project)

# smtpserver = "smtp.qq.com"
# smtpport = 465
# from_mail = "919769592@qq.com"
# to_mail = [email]
# password = "njcaytofvudobfij"  # 16位授权码
#
# subject = "test report"
# from_name = "AFL测试平台"


# if User.query.filter(User.email == email).first() is not None:
#     error = "User {0} is already registered.".format(email)
#     flash(f'Your account has been created!', 'success')
#     print("no")
#
# if error is None:
#     db.session.add(User(name=name, email=email, password=generate_password_hash(password)))
#     db.session.commit()
#     print("here?")
#     return redirect(url_for("auth.login"))
