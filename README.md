# Flask_Appointment_Website
A project for my software engineering class.  We made a website for a (fictional) law firm; users enter information on the website, and the information is then saved into a database which is queried using MySQL.  We made the website accessable to different lawyers working at the firm, users, and administrators.

To run this program, you need MySQL to be connected to a server, then input your personal password for MySQL in line 7:

mydb = mysql.connector.connect(host="localhost",user="root",passwd="<yourpassword>", database="mydb")

Then add: `clientpics`  to the `Clients` table in position 1 in MySQL if not already added. You can check by running the Clients Table 
and if there is no `clientpics` near the top add it.
 
  `idAppointments` INT NOT NULL,
  `startTime` DATETIME NULL,       <<<------ delete time  DATETIME NULL and put DATE NULL
  `endTime` DATETIME NULL,
                                            
## Please note the MySQL database is currently empty.
