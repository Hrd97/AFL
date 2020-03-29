from flask import render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash

import app
from . import bp_users
import datetime
from ..model import db, User, Project


@bp_users.route('/users/homepage', methods=['GET', 'POST'])
def homepage():
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    print("here111")
    print(session["user_id"])
    user = User.query.filter(User.id == session["user_id"]).first()
    projects = Project.query.filter(User.id == session["user_id"]).all()

    return render_template('project.html', projects=projects)
    # if user.position=='Leader':
    #     return render_template('users/index_leader.html', reservations=reservations, user=user, notice=notice)
    # else:
    #     return render_template('users/login.html', reservations=reservations, user=user, notice=notice)


@bp_users.route('/users/new', methods=['POST'])
def newproject():
    return redirect(url_for('users.homepage'))




@bp_users.route('/users/run', methods=['POST'])
def run():
    return redirect(url_for('users.homepage'))
#
# @bp_doctor.route('/users/homepageLeader')
# def homepageleader():
#     dt = datetime.datetime.now().strftime("%Y-%m-%d")
#     reservations = Reservation.query.filter(Reservation.doctor_ID == session["user_id"],
#                                             Reservation.reservationDate == dt).all()
#     user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
#     return render_template('users/index_leader.html', reservations=reservations, user=user)
#
#
# @bp_doctor.route('/users/profile', methods=['GET', 'POST'])
# def profile():
#     if request.method == 'POST':
#         name = request.form['name']
#         email = request.form['email']
#         phone = request.form['phone']
#         officno = request.form['officeno']
#         password = request.form['password']
#         print("here")
#         user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
#         user.name = name
#         user.phoneNumber = phone
#         user.officeNo = officno
#         if password != '':
#             user.password = generate_password_hash(password)
#         user.email = email
#         db.session.commit()
#         return redirect(url_for('users.profile'))
#
#     user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
#     print(user.name)
#     return render_template('users/profile.html', user=user)
#
#
# @bp_doctor.route('/users/mySchedule')
# def myschedule():
#     dt = datetime.datetime.now().strftime("%Y-%m-%d")
#     scheduleInfo = Schedule.query.filter(Schedule.staff_ID == session["user_id"], Schedule.date >= dt).all()
#     user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
#     for schedule in scheduleInfo :
#         print(schedule)
#     return render_template('users/schedule.html', scheduleInfo=scheduleInfo, user=user)
#
#
# @bp_doctor.route('/users/schedule')
# def schedule():
#     user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
#
#     doctorlist = MedicalStaff.query.filter(MedicalStaff.StaffID.like('%' + user.StaffID[0] + '%'),
#                                            MedicalStaff.department_ID == user.department_ID).all()
#
#     print(doctorlist)
#     dateInfo = []
#     now = datetime.date.today()
#     dateInfo.append(now)
#     one = datetime.timedelta(days=1)
#     one_days = now + one
#     dateInfo.append(one_days)
#     two = datetime.timedelta(days=2)
#     two_days = now + two
#     dateInfo.append(two_days)
#     three = datetime.timedelta(days=3)
#     three_days = now + three
#     dateInfo.append(three_days)
#     four = datetime.timedelta(days=4)
#     four_days = now + four
#     dateInfo.append(four_days)
#     fix = datetime.timedelta(days=5)
#     fix_days = now + fix
#     dateInfo.append(fix_days)
#     six = datetime.timedelta(days=6)
#     six_days = now + six
#     dateInfo.append(six_days)
#
#     return render_template('users/schedule_leader.html', dateInfo=dateInfo, user=user, doctorlist=doctorlist)
#
#
# @bp_doctor.route('/users/scheduling')
# def scheduling():
#     return redirect(url_for({{'users.schedule'}}))
#
#
# @bp_doctor.route('/users/reservationCheck', methods=['GET', 'POST'])
# def reservationcheck():
#     dt = datetime.datetime.now().strftime("%Y-%m-%d")
#     reservationCheck = Reservation.query.filter_by(doctor_ID=session["user_id"], reservationDate=dt).all()
#     medicineInfo = Medicine.query.all()
#     user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
#     return render_template('users/reservationChecklist.html',
#                            reservationCheck=reservationCheck, medicineInfo=medicineInfo, user=user)
#
#
# @bp_doctor.route('/users/checkcondition', methods=['GET', 'POST'])
# def checkcondition():
#     data = request.get_json()
#     print(request.get_json())
#     patientid = data['patientid']
#     conditions = Nursing.query.filter(Nursing.id == patientid).all()
#
#     conditiondict = {}
#     i = 0
#     print(conditions)
#     for condition in conditions:
#         conditiondict[i] = condition.to_json()
#         i = i + 1
#     return conditiondict
#
#
# @bp_doctor.route('/users/inpatientList')
# def inpatientlist():
#     inpatientList = Hospitalization.query.filter_by(doctor_ID=session["user_id"]).all()
#     medicineInfo = Medicine.query.all()
#     user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
#     return render_template('users/inpatientList.html',
#                            inpatientList=inpatientList, medicineInfo=medicineInfo, user=user)
#
#
# @bp_doctor.route('/users/reservationCheck/diagnose', methods=['GET', 'POST'])
# def diagnose():
#     print(request.form)
#     diagnose = request.form['dia_desc']
#     rid = request.form['dia-rid']
#     dt = datetime.datetime.now().strftime("%Y-%m-%d")
#     reservation = Reservation.query.filter(Reservation.reservationID == rid).first()
#     reservation.description = diagnose
#     db.session.commit()
#
#     reservationCheck = Reservation.query.filter_by(doctor_ID=session["user_id"], reservationDate=dt).all()
#     medicineInfo = Medicine.query.all()
#     user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
#     return render_template('users/reservationChecklist.html',
#                            reservationCheck=reservationCheck, medicineInfo=medicineInfo, user=user)
#
#
# @bp_doctor.route('/users/reservationCheck/inpatient', methods=['GET', 'POST'])
# def inpatient():
#     if request.method == "POST":
#         pname = request.form['in-name']
#         date = request.form['in-date']
#         patientID = int(request.form['patientid'])
#         print(patientID)
#         print(date)
#         print(pname)
#         db.session.add(Hospitalization(id=patientID, startDate=date, doctor_ID=session["user_id"]))
#         db.session.commit()
#
#     # reservationCheck = Reservation.query.filter_by(doctor_ID= session["user_id"]).all()
#     # medicineInfo = Medicine.query.all()
#     # user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
#     # return render_template('users/reservationChecklist.html',
#     #                        reservationCheck=reservationCheck, medicineInfo=medicineInfo, user=user)
#     return redirect(url_for('users.reservationcheck'))
#
#
# @bp_doctor.route('/users/reservationCheck/prescribe', methods=['GET', 'POST'])
# def prescribe():
#     data = request.get_json()
#     # print('here')
#     # print(request.get_json())
#
#     patientid = data['pid']
#     mids = data['mid']
#     mquantity = data['mquantity']
#
#     # print(patientid)
#     # print(mids)
#     # print(type(mids))
#     # print(mquantity)
#
#     presID = createID()
#     dt = datetime.datetime.now().strftime("%Y-%m-%d")
#
#     # print(presID)
#     # print(dt)
#
#     db.session.add(Prescription(prescriptionID=presID, id=patientid, doctor_ID=session["user_id"],
#                                 prescriptionDate=dt,
#                                 paymentStatues='n', giveStatues='n'))
#     db.session.commit()
#
#     for i in range(len(mids)):
#         db.session.add(Prescription_Detail(prescriptionID=presID, medicine_ID=mids[i], quantity=int(mquantity[i])))
#         db.session.commit()
#
#     reservationCheck = Reservation.query.filter_by(doctor_ID=session["user_id"]).all()
#     medicineInfo = Medicine.query.all()
#     user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
#     return render_template('users/reservationChecklist.html',
#                            reservationCheck=reservationCheck, medicineInfo=medicineInfo, user=user)
#
#
# @bp_doctor.route('/users/reservationCheck/searchdate', methods=['POST'])
# def searchdate():
#     dt = request.form['sdate']
#     user = MedicalStaff.query.filter(MedicalStaff.StaffID == session["user_id"]).first()
#     if dt == '':
#         reservationCheck = Reservation.query.filter_by(doctor_ID=session["user_id"]).all()
#         medicineInfo = Medicine.query.all()
#         return render_template('users/reservationChecklist.html',
#                                reservationCheck=reservationCheck, medicineInfo=medicineInfo, user=user)
#
#     reservationCheck = Reservation.query.filter_by(doctor_ID=session["user_id"], reservationDate=dt).all()
#     medicineInfo = Medicine.query.all()
#     return render_template('users/reservationChecklist.html',
#                            reservationCheck=reservationCheck, medicineInfo=medicineInfo, user=user)
#
#
# @bp_doctor.route('/users/reservationCheck/addschdule', methods=['POST'])
# def addschedule():
#     data = request.get_json()
#     print(request.get_json())
#     doctorlist = data['doctorlist']
#     date = data['date']
#     tag = data['time'][1]
#     if tag == ':':
#         time = data['time'][0]
#     else:
#         time = data['time'][0:2]
#
#     # 1 代表有安排
#     for doctor in doctorlist:
#         schedule = Schedule.query.filter(Schedule.staff_ID == doctor, Schedule.date == date).first()
#         if schedule is None:
#             if time in 'timeInterval8':
#                 db.session.add(Schedule(staff_ID=doctor, date=date, timeInterval8='1' ))
#                 db.session.commit()
#             elif time in 'timeInterval9':
#                 db.session.add(Schedule(staff_ID=doctor, date=date, timeInterval9='1'))
#                 db.session.commit()
#             elif time in 'timeInterval10':
#                 db.session.add(Schedule(staff_ID=doctor, date=date, timeInterval10='1'))
#                 db.session.commit()
#             elif time in 'timeInterval11':
#                 db.session.add(Schedule(staff_ID=doctor, date=date, timeInterval11='1'))
#                 db.session.commit()
#             elif time in 'timeInterval14':
#                 db.session.add(Schedule(staff_ID=doctor, date=date, timeInterval14='1'))
#                 db.session.commit()
#             elif time in 'timeInterval15':
#                 db.session.add(Schedule(staff_ID=doctor, date=date, timeInterval15='1'))
#                 db.session.commit()
#             elif time in 'timeInterval16':
#                 db.session.add(Schedule(staff_ID=doctor, date=date, timeInterval6='1'))
#                 db.session.commit()
#             elif time in 'timeInterval17':
#                 db.session.add(Schedule(staff_ID=doctor, date=date, timeInterval17='1'))
#                 db.session.commit()
#         else:
#             if time in 'timeInterval8':
#                 schedule.timeInterval8 = '1'
#                 db.session.commit()
#             elif time in 'timeInterval9':
#                 schedule.timeInterval9 = '1'
#                 db.session.commit()
#             elif time in 'timeInterval10':
#                 schedule.timeInterval10 = '1'
#                 db.session.commit()
#             elif time in 'timeInterval11':
#                 schedule.timeInterval11 = '1'
#                 db.session.commit()
#             elif time in 'timeInterval14':
#                 schedule.timeInterval14 = '1'
#                 db.session.commit()
#             elif time in 'timeInterval15':
#                 schedule.timeInterval15 = '1'
#                 db.session.commit()
#             elif time in 'timeInterval16':
#                 schedule.timeInterval16 = '1'
#                 db.session.commit()
#             elif time in 'timeInterval17':
#                 schedule.timeInterval17 = '1'
#                 db.session.commit()
#
#     return "ok"
#
# def createID():
#     prescriptionID = Prescription.query.order_by(
#         Prescription.prescriptionID.desc()).first()
#     if prescriptionID is None:
#         return '00001'
#     print(prescriptionID)
#     id = prescriptionID.prescriptionID[:]
#     for i in range(1, 10000):
#         newid = ("{:0>5d}".format(i))
#         if id == newid:
#             newid = ("{:0>5d}".format(i + 1))
#             break
#
#     return newid
