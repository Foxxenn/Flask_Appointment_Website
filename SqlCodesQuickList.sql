insert into `admin` values('123','123456','Joe');

insert into `employee` values('JoeTest','123456','Joe','I','Gar','J@g','12Walnut','12','12','a');

/*insert into `Lawyer`values('JoeTest','1','2','A','4','5','6','7','8');
*/

insert into `Lawyer`(`lawyerUserName`,`lawyerPass`,`lawyerFName`,`lawyerLName`) values('JoeTest2','1','2','3');

select * from `Lawyer`;
select * from `Senior Partner`;

 DELETE FROM `Lawyer` WHERE `lawyerUserName`= 'Pythonjoe3'; 

/*insert into `Lawyer`(`lawyerUserName`,`lawyerPass`,`lawyerFName`,`lawyerLName`,`lawyerEmail`) values ()
*/

insert into `Senior Partner`(`seniorUserName`,`seniorPass`,`seniorEmail`, `seniorFName` , `seniorLName`) values ('Rob100','sp0001','rober.morgan@email.com', 'Robert', 'Morgan');



select `employeeUserName` from `employee`;
select * from `Lawyer`;
select * from `Appointments`;
select * from `Fees`;
select * from `Client`;
select * from `employee`;
select * from `Case Loads`;
select * from `Admin`;


drop table `Client`;
drop table `Fees`;
drop table `Appointments`;
drop table `Lawyer`;

insert into `Client`(`clientPics`,`clientUserName`) values ('1','test');
insert into `Lawyer`(`lawyerUserName`,`lawyerPass`,`lawyerFName`,`lawyerLName`) values('Jennifer01','111111','Jennifer','Fernandez');
insert into `Appointments`(`idAppointments`,`startTime`,`clientUserName`, `employeeUserName`) values('12','2020-02-11','test','Jose01');
insert into `employee`(`employeeUserName`,`employeePass`, `employeeFName`, `employeeLName`,`employeeAssignedLawyer`) values ('Vera01','111111','Vera','Standhope','Jennifer01');
insert into `Admin`(`adminUserName`,`adminPass`,`adminEmail`) values ('Joseph01','222222','j@email.com');



delete from `employee`  where `employeeUserName`='Joe';
delete from `Lawyer` where `lawyerUserName`= 'test';
delete from `Appointments` where `employeeUserName`= 'Patrick01';
delete from `Admin` where `adminUserName`='Joseph';