import datetime

from werkzeug.security import check_password_hash,generate_password_hash
from .model import db,User,Project,Collect,Comment,Like
import random
import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
dt = datetime.datetime.now().strftime("%Y-%m-%d")
dtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
class UserClass:
    def __init__(self, email):
        self.email = email

    @classmethod
    def getfromid(cls,id):
        user = User.query.filter(User.id == id).first()
        cls.id=id
        return cls(user.email)

    def check_user(self, password):
        error = None
        user = User.query.filter(User.email == self.email).first()
        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user.password, password):
            error = "Incorrect password."

        print(error)
        return error

    def is_exit(self):
        if User.query.filter(User.email == self.email).first() is not None:
            return True
        else:
            return False

    def register(self,name,password):
        db.session.add(User(name=name, email=self.email, password=generate_password_hash(password)))
        db.session.commit()

        return None

    def getid(self):
        user = User.query.filter(User.email == self.email).first()
        print(user.id)
        return user.id
    '''
    获取到app的路径 即/Users/darihan/Desktop/AFL/app
    '''
    def getpath(self):
        return os.path.abspath(os.path.dirname(__file__))

    def mkdir(self):
        projctpath = os.path.dirname(self.getpath()) + '/projectfile' + '/' + str(self.getid())
        print(projctpath)
        if not os.path.isdir(projctpath):
            os.mkdir(projctpath)
        return 0

    def sendemail(self):
        newpassword=self.resetpassword()
        msg_from = '919769592@qq.com'  # 发送方邮箱
        passwd = 'njcaytofvudobfij'  # 填入发送方邮箱的授权码
        msg_to = self.email  # 收件人邮箱

        subject = "重置密码,登陆后请修改新密码"  # 主题
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

        return 0

    def resetpassword(self):
        resetpassword=random.randint(0,99999)
        resetpassword=str(resetpassword)
        user = User.query.filter(User.email == self.email).first()
        user.password=generate_password_hash(resetpassword)
        db.session.commit()
        return resetpassword

    def myproject(self,id):
        return Project.query.filter(Project.userid == id).all()

    def publicproject(self):
        return Project.query.filter(Project.visibility == '1').all()


    def myprofile(self):
        return User.query.filter(User.id == self.id).first()



class ProjectClass:
    def __init__(self, name,userid):
        self.projectname = name
        self.userid=userid

    @classmethod
    def getfromid(cls,id):
        cls.id=id
        project = Project.query.filter(Project.id == id).first()
        return cls(project.name, project.userid)
    '''
    获取到app的路径 即/Users/darihan/Desktop/AFL
    '''
    def getbasepath(self):
        return os.path.dirname(os.path.abspath(os.path.dirname(__file__)))

    '''
    获取到app的路径 即/Users/darihan/Desktop/AFL/projectfile/1/pname
    '''
    def getprojectpath(self):
        basepath = self.getbasepath()
        print(self.projectname)
        project_path = basepath + "/projectfile/" + str(self.userid) + "/" + self.projectname  # 保存路径
        print('projectpath::' + project_path)
        return project_path

    '''
    保存到数据库
    '''
    def newproject(self, pfilefilename):

        filedir = self.getprojectpath() + "/" + pfilefilename[:-4]
        db.session.add(Project(name=self.projectname, userid=self.userid,
                               status="initial", visibility=0,
                               path=filedir,
                               uploadtime=dt))
        db.session.commit()
        return

    '''
    保存项目文件到本地并解压。
    '''
    def saveprojectfile(self,pfile):
        zipfile_path = self.getprojectpath() + "/" + pfile.filename  # 保存路径
        pfile.save(zipfile_path)

        os.system('unzip -d ' + self.getprojectpath() + ' ' + zipfile_path)


        outpath = self.getprojectpath() + "/afl-out"

        # os.mkdir(inpath)   初始测试用例由用户上传时完成创建
        os.mkdir(outpath)

        return 1

    '''运行项目'''
    def runproject(self,execName,parameter,compiler,makefile,read):

        scriptPath = self.getbasepath() + "/script"

        print(scriptPath)
        os.system('bash ' + scriptPath + '/test.sh')
        # if compiler == 'option1' and makefile == 'option1' and read == 'option1':
        #     os.system('bash ' + scriptPath + '/execafl-a.sh ' + execName + ' ' + parameter)
        # elif compiler == 'option1' and makefile == 'option1' and read == 'option2':
        #     os.system('bash ' + scriptPath + '/execafl-a.sh ' + execName + ' ' + parameter + ' ' + '@@')
        # elif compiler == 'option1' and makefile == 'option2' and read == 'option1':
        #     os.system('bash ' + scriptPath + '/execafl-a.sh ' + execName + ' ' + parameter)
        # elif compiler == 'option1' and makefile == 'option2' and read == 'option2':
        #     os.system('bash ' + scriptPath + '/execafl-a.sh ' + execName + ' ' + parameter + ' ' + '@@')
        # elif compiler == 'option2' and makefile == 'option1' and read == 'option1':
        #     os.system('bash ' + scriptPath + '/execafl-b.sh ' + execName + ' ' + parameter)
        # elif compiler == 'option2' and makefile == 'option1' and read == 'option2':
        #     os.system('bash ' + scriptPath + '/execafl-b.sh ' + execName + ' ' + parameter + ' ' + '@@')
        # elif compiler == 'option2' and makefile == 'option2' and read == 'option1':
        #     os.system('bash ' + scriptPath + '/execafl-b.sh ' + execName + ' ' + parameter)
        # elif compiler == 'option2' and makefile == 'option2' and read == 'option2':
        #     os.system('bash ' + scriptPath + '/execafl-b.sh ' + execName + ' ' + parameter + ' ' + '@@')

        project = Project.query.filter(Project.name == self.projectname, User.id == self.userid).first()

        project.status='runinng'
        db.session.commit()

        return 0


    '''上传测试用例'''
    def uploadtesttfile(self,pfile):
        '''
        保存zip文件
        '''
        pzipfileName = pfile.filename

        project = Project.query.filter(Project.name == self.projectname, User.id == self.userid).first()
        zipfile_path = os.path.dirname(project.path) + "/" + pzipfileName  # 保存路径

        pfile.save(zipfile_path)
        '''
        解压部分
        '''
        os.system('unzip -d ' + os.path.dirname(project.path) + ' ' + zipfile_path)
        return


    def getprojectfile(self):
        return


    def createprojectdir(self):
        print("项目目录" + self.getprojectpath())
        os.mkdir(self.getprojectpath())
        return


    def refreshproject(self,path):
        print(path)
        print('here')
        file_path = path+'/afl-out/fuzzer_stats'
        statdict={}
        with open(file_path, encoding='utf-8') as file_obj:
            line = file_obj.readline()
            while line != '':
                # print(line)
                x = line.split(':', 1);  # 以空格为分隔符，分隔成两个
                statdict[x[0].rstrip()] = x[1].rstrip("\n").strip()
                line = file_obj.readline()

        return statdict


    def getproject(self):
        return Project.query.filter(Project.userid == self.userid,
                                    Project.name==self.projectname).first()

    def desc(self,content,id):
        project = Project.query.filter(Project.id == id).first()
        project.description=content
        db.session.commit()
        return 1

    def addcomment(self):
        project = Project.query.filter(Project.id == self.id).first()
        project.comment+=1
        db.session.commit()
        return 1


class CommentClass:
    def __init__(self, pid):
        self.pid = pid

    def getComment(self):
        comments=Comment.query.filter(Comment.projectid == self.pid).all()
        return comments

    def savecomment(self, username, content, repliedname):
        db.session.add(Comment(projectid=self.pid, username=username,
                               time=dtime, content=content,
                               repliedname=repliedname,
                               star=0))
        db.session.commit()

        comments = Comment.query.filter(Comment.projectid == self.pid,Comment.username==username,Comment.content==content).first()
        return comments.id

    def split(self,content):
        replied=''
        comment=''
        print('split')
        print(content)
        print(content[0:4])
        if content[0:5]== 'reply' and ':' in content:
            tmp=content.split(':', 1)[0]
            comment=content.split(':', 1)[1]
            replied=tmp.split(' ',1)[1]
        else:
            comment=content
        return replied,comment


    def addstar(self,commentid,add):
        comment = Comment.query.filter(Comment.projectid == self.pid,Comment.id==commentid).first()
        comment.star+=add
        db.session.commit()
        return 1


class MycollectClass:
    def mycollect(self,userid):
        mycollect=Collect.query.filter(Collect.id == userid).all()
        return mycollect

    def addcollect(self,userid,projetid):
        mycollect=Collect.query.filter(Collect.id == userid).all()
        return 1

    def deletecollect(self,userid,projetid):
        mycollect=Collect.query.filter(Collect.id == userid).all()
        return 1

class LikeClass:
    def like(self, commentid, userid, projectid,add):
        if add == 1:
            db.session.add(Like(commentid=commentid, userid=userid,projectid=projectid))
            db.session.commit()
        else:
            like = Like.query.filter(Like.commentid == commentid, Like.userid == userid,Like.projectid==projectid).first()
            db.session.delete(like)
            db.session.commit()
        return 1

    def getlike(self, projectid,userid):
        likes = Like.query.filter(Like.projectid == projectid,Like.userid==userid).all()
        return likes
