# -*- coding: utf-8 -*-
import datetime

from flask import render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash

from . import bp_hr
from ..model import MedicalStaff, Department, db, Post

@bp_hr.route('/testresult/homepage')
def homepage():
    #Patient.query.filter(Patient.phoneNumber == phoneNumber).first()
    #session['user_id'] = 'H004'
    notice = Post.query.all()
    user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
    return render_template('hrAdmin/login.html', user=user,notice=notice)

@bp_hr.route('/testresult/post',methods=['GET', 'POST'])
def post():
    user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        now = datetime.datetime.now()
        date=now.strftime('%Y-%m-%d')
        db.session.add(Post(postTitle=title, postContent=content,postDate=date))
        db.session.commit()
        return render_template('hrAdmin/post.html',user=user)
    return render_template('hrAdmin/post.html',user=user)

@bp_hr.route('/testresult/profile',methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        officno = request.form['officeno']
        password = request.form['password']
        print("here")
        user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
        user.name = name
        user.phoneNumber = phone
        user.officeNo = officno
        if password != '':
            user.password = generate_password_hash(password)
        user.email = email
        db.session.commit()
        return redirect(url_for('testresult.profile'))

    user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
    print(user.name)
    return render_template('hrAdmin/profile.html', user=user)

@bp_hr.route('/testresult/accountManage', methods=['GET', 'POST'])
def account():
    if request.method == "POST":
        print(request.form)
        if request.form['formtype'] == 'search':

            name = request.form['search_name']
            department = request.form['search_department']
            status = request.form['search_status']
            print(name)
            print(department)
            print(status)
            '''
            这搜索页面我真的是······
            '''
            if name == '' and department == 'All' and status == 'All':
                staffInfo = MedicalStaff.query.all()
                print("1")
            elif name == '' and department == 'All' and status != 'All':
                staffInfo = MedicalStaff.query.filter(MedicalStaff.status == status).all()
                print("2")
            elif name == '' and department != 'All' and status == 'All':
                departmentid = Department.query.filter(Department.departmentName.like(department)).first().department_ID
                staffInfo = MedicalStaff.query.filter(MedicalStaff.department_ID == departmentid).all()
                print("3")
            elif name == '' and department != 'All' and status != 'All':
                departmentid = Department.query.filter(Department.departmentName.like(department)).first().department_ID
                staffInfo = MedicalStaff.query.filter(MedicalStaff.department_ID == departmentid, MedicalStaff.status ==
                                                      status).all()
                print("4")
            elif name != '' and department == 'All' and status == 'All':
                staffInfo = MedicalStaff.query.filter(MedicalStaff.name.like('%'+name+'%')).all()
                print("5")
            elif name != '' and department == 'All' and status != 'All':
                staffInfo = MedicalStaff.query.filter(MedicalStaff.name.like(name),MedicalStaff.status == status).all()
                print("6")
            elif name != '' and department != 'All' and status == 'All':
                departmentid = Department.query.filter(Department.departmentName.like(department)).first().department_ID
                staffInfo = MedicalStaff.query.filter(MedicalStaff.name.like(name), MedicalStaff.department_ID ==
                                                      departmentid).all()
                print("7")
            elif name != '' and department != 'All' and status != 'All':
                departmentid = Department.query.filter(Department.departmentName.like(department)).first().department_ID
                staffInfo = MedicalStaff.query.filter(MedicalStaff.name.like(name),MedicalStaff.department_ID ==
                                                      departmentid, MedicalStaff.status == status).all()
                print("8")
            else:
                pass
            print("9")
            #return redirect(url_for('testresult.account', staffInfo=staffInfo))
            user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
            return render_template('hrAdmin/accountManage.html', staffInfo=staffInfo,user=user)
            print("10")

        elif request.form['formtype'] == 'modify':

            id=request.form['modify_id']
            name = request.form['modify_name']
            gender =request.form['modify_gender']
            status = request.form['modify_status']
            department = request.form['modify_department']
            phone = request.form['modify_phone']
            position = request.form['modify_position']

            departmentid = Department.query.filter(Department.departmentName.like(department)).first().department_ID
            staffInfo = MedicalStaff.query.filter(MedicalStaff.StaffID == id).first()
            dt = datetime.datetime.now().strftime("%Y-%m-%d")

            staffInfo.name = name
            staffInfo.gender = gender
            staffInfo.department_ID = departmentid
            staffInfo.phoneNumber = phone
            staffInfo.status = status
            staffInfo.position = position
            if status == 'Passive':
                staffInfo.retirementDate = dt
            db.session.commit()

        else:  # is formtype==add
            name = request.form['add_name']
            gender = request.form['add_gender']
            staffid=createID(request.form['add_type'])
            department = request.form['add_department']
            departmentid = Department.query.filter(Department.departmentName.like(department)).first().department_ID
            dt = datetime.datetime.now().strftime("%Y-%m-%d")
            phone = request.form['add_phone']
            position = request.form['add_position']
            db.session.add(MedicalStaff(StaffID=staffid, phoneNumber=phone, password=generate_password_hash('123456'),
                                        name=name, gender=gender, department_ID=departmentid, position=position
                                        , entryDay=dt, status='Active'))
            db.session.commit()

        staffInfo = MedicalStaff.query.all()
        user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
        return redirect(url_for('testresult.account', staffInfo=staffInfo, user=user))
        #return redirect(url_for('testresult.account'))
        #return render_template('hrAdmin/accountManage.html', staffInfo=staffInfo)

    #print(request.form['add_name'])
    # DoctorInfo = db.session.query(filter(MedicalStaff.StaffID.like('D%')).all()
    staffInfo= MedicalStaff.query.all()
    user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
    # for staff in staffInfo:
    #     if
    #     print(staff.department)
    # print(staffInfo)
    # print(staffInfo['position'])
    # print(type(staffInfo))
    # print(staffInfo[0])
    #print(staffInfo.name)
    return render_template('hrAdmin/accountManage.html', staffInfo=staffInfo,user=user)

def createID(stafftype):
    if stafftype[0]=='D':
        staffID = MedicalStaff.query.filter(MedicalStaff.StaffID.like('D%')).order_by(
            MedicalStaff.StaffID.desc()).first()
        if staffID is None:
            return 'D001'
    elif stafftype[0]=='N':
        staffID = MedicalStaff.query.filter(MedicalStaff.StaffID.like('N%')).order_by(
            MedicalStaff.StaffID.desc()).first()
        if staffID is None:
            return 'N001'
    elif stafftype[0]=='W':
        staffID = MedicalStaff.query.filter(MedicalStaff.StaffID.like('W%')).order_by(
            MedicalStaff.StaffID.desc()).first()
        if staffID is None:
            return 'W001'

    else:
        staffID = MedicalStaff.query.filter(MedicalStaff.StaffID.like('H%')).order_by(
            MedicalStaff.StaffID.desc()).first()
        if staffID is None:
            return 'H001'

    #
    # print(staffID.StaffID)
    # print(staffID.StaffID[1:])
    stafftype =staffID.StaffID[0]
    id = staffID.StaffID[1:]

    for i in range(1, 100):
        newid = ("{:0>3d}".format(i))
        if id == newid:
            newid = ("{:0>3d}".format(i+1))
            break
    # print(stafftype+newid)
    return stafftype+newid
    # for staff in staffID:
    #     print(staff.StaffID)

    # staffID1=MedicalStaff.query.filter(MedicalStaff.StaffID.like('D%')).order_by(MedicalStaff.StaffID.asc()).all()
    #
    # for staff in staffID1:
    #     print(staff.StaffID)


# @bp_auth.route('/register', methods=['GET', 'POST'])
# def register():
#
#     if request.method == "POST":
#         error = None
#         pName = request.form["name"]
#         print(pName)
#         password = request.form["password"]
#         print(password)
#
#         gender = request.form["gender"]
#         print(gender)
#
#         birthday = request.form["birthday"]
#         print(birthday)
#
#         phoneNumber = request.form["phonenumber"]
#         print(phoneNumber)
#
#         gender = 'm'
#
#         if Patient.query.filter(Patient.phoneNumber == phoneNumber).first() is not None:
#             error = "User {0} is already registered.".format(phoneNumber)
#
#         # patientID = db.Column(db.CHAR(4), primary_key=True)  # 每个用户记得添加用户组
#         # name = db.Column(db.CHAR(20))
#         # gender = db.Column(db.CHAR(1))
#         # birthDay = db.Column(db.DATE)
#         # phoneNumber = db.Column(db.CHAR(11))
#         # address = db.Column(db.CHAR(20))
#         # password = db.Column(db.VARCHAR(100))
#         if error is None:
#             db.session.add(Patient(patientID='0002', phoneNumber=phoneNumber, password=generate_password_hash(password),
#                            name=pName, gender=gender, birthDay=birthday))
#             db.session.commit()
#             redirect(url_for("auth.login"))
#     return render_template('auth/register.html')

