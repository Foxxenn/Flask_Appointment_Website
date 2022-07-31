# Flask_Appointment_Website
A project for school that took a website information that a user entered into MySql.

To run this program you need MySQL to be connected to a server, then input your personal password for MySQL in line 7:
mydb = mysql.connector.connect(host="localhost",user="root",passwd="<yourpassword>", database="mydb")
then add: `clientpics`  to the `Clients` table in position one in MySQL if not already added. You can check by running the Clients Table 
and if there is no `clientpics` near the top add it.
  `idAppointments` INT NOT NULL,
  `startTime` DATETIME NULL,       <<<------ delete time  DATETIME NULL and put DATE NULL
  `endTime` DATETIME NULL,
Please note the MySql database is empty.
