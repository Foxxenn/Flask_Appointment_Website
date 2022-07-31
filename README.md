# Flask_Appointment_Website
A project for my software engineering class that took a website we made for a law firm, and collected information that a user entered into MySql. We made the website accessable to different Lawyers working at the firm, and also for miscl. users.

To run this program you need MySQL to be connected to a server, then input your personal password for MySQL in line 7:

mydb = mysql.connector.connect(host="localhost",user="root",passwd="<yourpassword>", database="mydb")

Then add: `clientpics`  to the `Clients` table in position one in MySQL if not already added. You can check by running the Clients Table 
and if there is no `clientpics` near the top add it.
 
  `idAppointments` INT NOT NULL,
  `startTime` DATETIME NULL,       <<<------ delete time  DATETIME NULL and put DATE NULL
  `endTime` DATETIME NULL,
                                            
## Please note the MySql database is empty.
