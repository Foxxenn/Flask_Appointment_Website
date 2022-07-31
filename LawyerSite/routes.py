from LawyerSite import app
from flask import render_template, url_for, redirect, flash, request, session
from jinja2 import Environment, FileSystemLoader
from LawyerSite.forms import AppointmentForm, RegistrationForm, LoginForm, DateForm, addLawyer, adminForm, emailForm
from datetime import datetime
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="Posture1", database="mydb")
mycursor = mydb.cursor()

"""
Team 5 Lawyer Appointmnet Software
2021 Software Enginering CMP 408
By:
Python/HTML/MySQL Joe Garcia
HTML/CSS Roy Acevedo
MySQL Tyrell Whitfeild
Python/General Atm Mustafa


To run this program you need MySQL to be connected to a server, then input your personal password for MySQL in line 7:
mydb = mysql.connector.connect(host="localhost",user="root",passwd="<yourpassword>", database="mydb")

then add: `clientpics`  to the `Clients` table in position one in MySQL if not already added. You can check by running the Clients Table 
and if there is no `clientpics` near the top add it.

  `idAppointments` INT NOT NULL,
  `startTime` DATETIME NULL,       <<<------ delete time  DATETIME NULL and put DATE NULL
  `endTime` DATETIME NULL,

Please note the MySql database is empty.

"""


@app.route('/')
@app.route('/home')
def homepage():
    return render_template('homepage.html', title='Homepage')



@app.route('/addl', methods=['GET', 'POST'])    ### Add a laywer website page
def add_lawyer():
    form = addLawyer()                          ### Add the addLawyer() form from python
    if form.validate_on_submit():
        name_entered = form.username.data

        mycursor.execute("SELECT * FROM `Admin` ")
        myresult = mycursor.fetchall()
        admin_name = []
        for row in myresult:
            foundName= (str(row[0]))
            admin_name.append(foundName)
        


        mycursor.execute("SELECT * FROM `Lawyer` ")   ###retreive the lawyer datebase table
        myresult = mycursor.fetchall()

        for row in myresult:                            ###Look through every row in the lawyer database
            if row[0] == name_entered:
                flash(f'Lawyer Already Exists for {form.username.data}', category='danger')
                return render_template('add_lawyer.html',title='Addl', form= form)

        result=request.form
        sqlFormula = "INSERT INTO `Lawyer`(`lawyerUserName`,`lawyerPass`,`lawyerFName`,`lawyerMInt`,`lawyerLName`,`lawyerEmail`,`lawyerAddress`,`lawyerHomePhone`,`lawyerCellPhone`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"  ###add my MySql code in Lawyer Table
        lawyer1 = (result.get('username'), result.get('confirm_password'),result.get('fname'),'A',result.get('lname'),result.get('email'),'6','7','8')
        mycursor.execute(sqlFormula, lawyer1)
        mydb.commit()
        flash(f'Account Created Successfully for {form.username.data}',category='success')
        print("Im in addLawyer form successful")
        return redirect('admin/' + admin_name[0])
  
    return render_template('add_lawyer.html', title="Addl", form= form)   ##add a form to the addlawyer page that will take the data




@app.route('/admin/<name_entered>',methods= ['GET','POST'])  ### add an admin page with account name
def admin(name_entered):
    form = adminForm()
    print('Admin')
    mycursor.execute("SELECT * FROM `Appointments` ")   ###go into my appointments database
    myresult = mycursor.fetchall()
    formatted_result= []
    print('Admin2')
    for row in myresult:
        date_time= row[1].strftime("%m/%d/%Y")         ### make sure the appointment time is pretty 
        newresult = (str(row[0])+" ID "+row[3]+' with '+row[4]+' at '+ date_time)
        #print(row)
        formatted_result.append(newresult)

    print()
    if form.validate_on_submit():
        print('Did I validate')
        print('Admin1')
        add = form.add.data
        delete = form.delete.data
        delete_forever = str(delete)
    
        
        sqlFormula = "DELETE FROM `Appointments` where `idAppointments`= '"+ delete_forever+"' "  ####Delete from MySQL from appointments
        mycursor.execute(sqlFormula)
        mydb.commit()
        flash(f'Appointment Deleted Successfully', category='success')


        mycursor.execute("SELECT * FROM `Appointments` ")       ####go into my appointments database
        myresult = mycursor.fetchall()
        formatted_result= []
        print('Admin2')
        for row in myresult:
            date_time= row[1].strftime("%m/%d/%Y")              ###make datatime look pretty 
            newresult = (str(row[0])+" ID "+row[3]+' with '+row[4]+' at '+ date_time)
            formatted_result.append(newresult)
            
        return render_template('admin.html', user_name= name_entered, form= form,appointments_list= formatted_result, add=add, delete=delete)
    return render_template('admin.html', user_name= name_entered, form= form,appointments_list= formatted_result)


@app.route('/accountl/<name_entered>', methods= ['GET','POST'])  #### add an accountl page with account name
def account_lawyer(name_entered):
    form= AppointmentForm()
    mycursor.execute("SELECT * FROM `Case Loads` ")
    myresult= mycursor.fetchall()
    cases= myresult
    print(cases)
    cases_won= []
    for row in cases:
        newresult = ("Cases Won: "+str(row[1])+ " Cases Lost: "+ str(row[2]))
        if row[0] == name_entered:
            cases_won.append(newresult)


    mycursor.execute("SELECT * FROM `Appointments` ")
    myresult = mycursor.fetchall()
    formatted_result = []
    print(formatted_result)
    for row in myresult:
        date_time= row[1].strftime("%m/%d/%Y")
        newresult = (str(row[0])+" ID "+row[3]+' with '+row[4]+' at '+ date_time)
        if row[4] == name_entered:
            formatted_result.append(newresult)
    print('form gotten')
    if form.validate_on_submit():
        delete = form.delete.data
        delete_forever = str(delete)
        sqlFormula = "DELETE FROM `Appointments` where `idAppointments`= '"+ delete_forever+"' "   ###delete an appointment
        mycursor.execute(sqlFormula)
        mydb.commit()
        flash(f'Appointment Deleted Successfully', category='success')
        mycursor.execute("SELECT * FROM `Appointments` ")
        myresult = mycursor.fetchall()
        formatted_result = []
        print(formatted_result)
        for row in myresult:
            date_time= row[1].strftime("%m/%d/%Y")
            newresult = (str(row[0])+" ID "+row[3]+' with '+row[4]+' at '+ date_time)
            if row[4] == name_entered:
                formatted_result.append(newresult)
        print('form gotten')
        return render_template('account_lawyer.html', user_name= name_entered, form= form,appointments_list= formatted_result,cases_won = cases_won)  ###had a bunch of forms and vaireables that flask must use to transport to another page

    return render_template('account_lawyer.html', user_name= name_entered, form= form,appointments_list= formatted_result, cases_won = cases_won)


@app.route('/about')      ###add an about page
def about():
    apicture = 'Default.jpg'

    return render_template('about.html', title='About', picture = apicture)

@app.route('/email')       ### add an email page
def email():
    form = emailForm()
    return render_template('email.html', title="Email_Us", form= form)

@app.route('/account', methods=['GET','POST'])  ## add an account page
def account():
    return render_template('account.html',title='Account')



@app.route('/account/<name_entered>', methods=['GET','POST'])
def accountPost(name_entered):
    form= DateForm()

    mycursor.execute("SELECT * FROM `Appointments` ")
    myresult = mycursor.fetchall()
    formatted_result= []
    for row in myresult:  # myresult is all appointments
        date_time= row[1].strftime("%m/%d/%Y")
        newresult = (row[3]+' with '+row[4]+' at '+ date_time)
        if row[3] == name_entered:
            formatted_result.append(newresult)
    print('In account_user.')
    print(name_entered)
    print('appointments for this use ', formatted_result)

    if form.validate_on_submit():
        print('In account_user Validate Form.')
    
        chosen = request.form.getlist('lchoices')  # chosen is which lawyer was chosen by client
        print('chosen in account_user', chosen)
        session['startdate'] = form.startdate.data
        startdate = session['startdate']
        print(type(startdate))
        mycursor.execute("SELECT * FROM `Appointments` ")
        myresult = mycursor.fetchall()
        for row in myresult:    # myresult is all appointments
            print(row)
            print('row1 ', row[1], '  ', startdate)
            print(row[3], '  ', name_entered)
            print(row[4], '  ', chosen[0])
            if (row[1] == startdate and row[3] == name_entered  and row[4] == chosen[0]):
                flash(f'Appointment Already Exists', category='danger')
                print("Danger!")
                mycursor.execute("SELECT * FROM `Appointments` ")
                myresult = mycursor.fetchall()
                formatted_result= []
                for row in myresult:
                    date_time= row[1].strftime("%m/%d/%Y")
                    newresult = (row[3]+' with '+row[4]+' at '+ date_time)
                    if row[3] == name_entered:

                        formatted_result.append(newresult)
                return render_template('account_user.html', user_name= name_entered, form= form,appointments_list = formatted_result)

        print("all good, no such appointment already exists")
        test = 1
        found_match = True
        while(found_match == True):
            found_match = False
            for row in myresult:
                if row[0]== test:
                    test= test+1
                    found_match = True
                    break

        newappid= test
        sqlFormula = "INSERT INTO `Appointments`(`idAppointments`,`startTime`,`clientUserName`, `employeeUserName`) VALUES(%s,%s,%s,%s)"
        appoint1=(newappid,startdate, name_entered, chosen[0] )
        mycursor.execute(sqlFormula,appoint1)
        mydb.commit()
        
       
        mycursor.execute("SELECT * FROM `Appointments` ") ## access to Appointments Data
        myresult = mycursor.fetchall()
        formatted_result= []
        for row in myresult:
            
            date_time= row[1].strftime("%m/%d/%Y")
            newresult = (row[3]+' with '+row[4]+' at '+ date_time)
            if row[3] == name_entered:
                

                formatted_result.append(newresult)
        print("result after appointment was created", formatted_result)

        flash(f'Appointment Created Successfully',category='success')
 #          file_loader = FileSystemLoader('templates')
 #          env= Environment(loader= file_loader)

        return render_template('account_user.html', user_name= name_entered, form= form, appointments_list = formatted_result)

    return render_template('account_user.html', user_name= name_entered, form= form,appointments_list = formatted_result)




@app.route('/register',methods=['POST','GET'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():

        name_entered = form.username.data

        mycursor.execute("SELECT * FROM `Client` ") ###Access to Client data
        myresult = mycursor.fetchall()
        whether_found = False
        for row in myresult:                  ####checks to see whether client name has been made
            if row[1] == name_entered:
                whether_found = True
                flash(f'Login Already Exists for {form.username.data}', category='danger')
                return render_template('register.html',title='signup', form= form)

        result=request.form
        sqlFormula = "INSERT INTO `Client`(`clientpics`,`clientUserName`, `clientPass`, `clientFName`,  `clientMInt`, `clientLName`, `clientEmail`, `clientAddress`,`clientHomePhone`, `clientCellPhone`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        client1 = ('Default.jpeg',result.get('username'), result.get('confirm_password'),result.get('fname'),'2',result.get('lname'),result.get('email'),'4','5','6')
        mycursor.execute(sqlFormula, client1)
        mydb.commit()

        
        flash(f'Account Created Successfully for {form.username.data}',category='success')
        print("Im in registration form successful")

     #   sqlFormula = "INSERT INTO `Lawyer`(`lawyerUserName`,`lawyerPass`,`lawyerFName`,`lawyerMInt`,`lawyerLName`,`lawyerEmail`,`lawyerAddress`,`lawyerHomePhone`,`lawyerCellPhone`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
     #   lawyer1 = (result.get('username'), result.get('confirm_password'),'2','A','4',result.get('email'),'6','7','8')
     #   mycursor.execute(sqlFormula, lawyer1)
     #   mydb.commit()
     #   flash(f'Account Created Successfully for {form.username.data}',category='success')
     #   print("Im in registration form successful")

     #   print("the user is ", result.get('username'))
     #   result.get('confirm_password')
        return redirect('account/' + name_entered)
    return render_template('register.html',title='signup', form= form)

@app.route('/staff')
def staff():
    return render_template('staff.html', title='Lawyers')     


@app.route('/login', methods=['POST','GET'])
def login():
    form= LoginForm()

    if form.validate_on_submit():
        chosen = request.form.getlist('choices')
     #   print('chosen ')
       # print()
     #   print(chosen)

        name_entered = form.username.data
        pass_entered = form.password.data
        print(name_entered)
        print(pass_entered)
   
        if chosen== ['1']:
            mycursor.execute("SELECT * FROM `Client` ")
            myresult = mycursor.fetchall()
            whether_found = False
            for row in myresult:
                print(row)
                print (type(row))

                if row[1] == name_entered and row[2] == pass_entered:
                    whether_found = True
                    flash(f'Login successful for {form.username.data}', category='success')
                    print('account/'+ name_entered)
                    return redirect('account/' + name_entered)

            if whether_found == False:
                flash(f'Login unsuccessful for {form.username.data}', category='danger')
                print("In Client")


        elif chosen == ['4']:
            mycursor.execute("SELECT * FROM `Admin` ")
            myresult = mycursor.fetchall()
            whether_found = False
            for row in myresult:
                print(row)
                print (type(row))

                if row[0] == name_entered and row[1] == pass_entered:
                    whether_found = True
                    flash(f'Login successful for {form.username.data}', category='success')
                    return redirect('admin/' + name_entered)

            if whether_found == False:
                flash(f'Login unsuccessful for {form.username.data}', category='danger')
                print("In Admin")

        else:
            mycursor.execute("SELECT * FROM `Lawyer` ")   ###retreive the lawyer datebase table
            myresult = mycursor.fetchall()
            whether_found = False
            for row in myresult:
                print(row)
                print (type(row))

                if row[0] == name_entered and row[1] == pass_entered:
                    whether_found = True
                    flash(f'Login successful for {form.username.data}', category='success')
                    print('in lawyer')
                    return redirect('accountl/'+ name_entered)
                

            if whether_found == False:
                flash(f'Login unsuccessful for {form.username.data}', category='danger')
                print("In Lawyer")

 #       if form.username.data== 'Joe12' and form.password.data== '123456':
   #         flash(f'Login successful for {form.username.data}', category='success')
  #          print("hello")
  #          return redirect(url_for('index'))
    #    else:
   #         flash(f'Login unsuccessful for {form.username.data}', category='danger')
   #         print("hello2")
    return render_template('login.html',title='login',form= form)





#lawyer1 = ('Pythonjoe3','1','2','A','4','5','6','7','8')

