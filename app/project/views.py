from flask import render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash

import app
from . import bp_project
import datetime
from ..model import db, User, Project
from ..cLass import UserClass, ProjectClass
import os

basedir = os.path.abspath(os.path.dirname(__file__))
maindir = os.path.dirname(basedir)
projectdir= os.path.dirname(os.path.dirname(basedir))+"/projectfile"
dt = datetime.datetime.now().strftime("%Y-%m-%d")
@bp_project.route('/project/homepage', methods=['GET', 'POST'])
def homepage():
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    print(session["user_id"])

    user=UserClass.getfromid(session["user_id"])
    #print(user.email)
    #user = User.query.filter(User.id == session["user_id"]).first()
    projects=user.myproject(session["user_id"])
    #projects = Project.query.filter(Project.userid == session["user_id"]).all()

    return render_template('project/project.html', projects=projects)
    # if user.position=='Leader':
    #     return render_template('project/index_leader.html', reservations=reservations, user=user, notice=notice)
    # else:
    #     return render_template('project/login.html', reservations=reservations, user=user, notice=notice)

@bp_project.route('/project/new', methods=['POST'])
def newproject():

    projectName = request.form["pname"]
    pfile = request.files["pfile"]


    print("项目名"+projectName)
    print("基地址"+basedir)

    project=ProjectClass(projectName,session["user_id"])

    project.createprojectdir()

    project.saveprojectfile(pfile)

    project.newproject(pfile.filename)


    return redirect(url_for('project.homepage'))




@bp_project.route('/project/run', methods=['POST'])
def run():
    execName = request.form["exec"]
    parameter = request.form["parameter"]
    compiler = request.form["compiler"]
    makefile = request.form["makefile"]
    projectName = request.form["projectname"]
    read = request.form["read"]

    print(execName)
    print(parameter)

    print(compiler)
    print(makefile)
    print(read)

    pfile = request.files["file-input"]
    print(pfile)


    print(projectName)

    project = ProjectClass(projectName, session["user_id"])


    project.uploadtesttfile(pfile)

    project.runproject(execName,parameter,compiler,makefile,read)



    # print("基地址" + basedir)
    # print("项目目录" + projectdir)
    # scriptPath=os.path.dirname(projectdir)+"/script"
    # '''
    # 通过传参数去完成执行afl工具
    # '''

    return redirect(url_for('project.homepage'))




@bp_project.route('/project/refresh', methods=['POST'])
def refresh():
    data = request.get_json()
    #print(request.get_json())
    #print(data['projectname'])
    project = ProjectClass(data['projectname'], session["user_id"])
    return project.refreshproject(project.getprojectpath())
    # file_path = os.path.dirname(data['projectname']) +'/afl-out/fuzzer_stats'
    #
    # statdict = {}
    # with open(file_path, encoding='utf-8') as file_obj:
    #     line = file_obj.readline()
    #     while line != '':
    #         #print(line)
    #         x=line.split(':', 1);  # 以空格为分隔符，分隔成两个
    #         statdict[x[0].rstrip()] = x[1].rstrip("\n").strip()
    #         line = file_obj.readline()
    #
    # return statdict


@bp_project.route('/project/newproject', methods=['POST'])
def new():
    pname = request.form["pname"]
    print(pname)

    file_path = projectdir + "/" + str(session["user_id"]) + "/" + pname  # 保存路径
    print(file_path)
    os.mkdir(file_path)
    print("ok?")
    return redirect(url_for('project.homepage'))





'''
dashboard  这里需要改造。
'''
@bp_project.route('/project/dashboard', methods=['GET','POST'])
def dashboard():
    projectName = request.form["projectname"]
    print(projectName)
    project = ProjectClass(projectName, session["user_id"])
    return render_template('project/dashboard.html', project=project.getproject())


@bp_project.route('/project/result', methods=['GET', 'POST'])
def result():
    projectName = request.form["projectname"]
    print(projectName)
    project = ProjectClass(projectName, session["user_id"])
    return render_template('project/result.html', project=project.getproject())

@bp_project.route('/project/crashresult', methods=['GET', 'POST'])
def crashresult():
    projectName = request.form["projectname"]
    print(projectName)
    project = ProjectClass(projectName, session["user_id"])
    return render_template('project/result.html', project=project.getproject())

@bp_project.route('/project/pathresult', methods=['GET', 'POST'])
def pathresult():
    projectName = request.form["projectname"]
    print(projectName)
    project = ProjectClass(projectName, session["user_id"])
    return render_template('project/result.html', project=project.getproject())

@bp_project.route('/project/hangresult', methods=['GET', 'POST'])
def hangresult():
    projectName = request.form["projectname"]
    print(projectName)
    project = ProjectClass(projectName, session["user_id"])
    return render_template('project/result.html', project=project.getproject())

    # i = 0
    # print(prescription)
    # for medicine in prescription:
    #     medicinedict[i] = medicine.to_json()
    #     i = i + 100
    #
    # return medicinedict

    # project = Project.query.filter(Project.name == projectName, User.id == session["user_id"]).first()
    #
    # medicinedict = {}
    # i = 0
    # print(prescription)
    # for medicine in prescription:
    #     medicinedict[i] = medicine.to_json()
    #     i = i + 100

