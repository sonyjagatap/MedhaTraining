create table accounts (accountNO varchar(20) primary key not null,accounttype varchar(20)not null,financialinstitue varchar(20)not null);
insert into accounts (accountNO,accounttype,financialinstitue) values ("111","credit","chase");
insert into accounts (accountNo,accounttype,financialinstitue) values ("222","saving","bankofamerica");
insert into accounts (accountNo,accounttype,financialinstitue) values ("333","checking","bankofamerica");
select *from accounts;


create table transcationinfo (transcationID int primary key,accountNO varchar(20)not null,tdate date not null,description varchar(20) not null,amount int not null,transcationtype varchar(20) not null,location varchar(20));
insert into transcationinfo(transcationID,accountNO,tdate,description,amount,transcationtype,location) values ("1","111", "2014/12/5","costco","140","credit","fremont");
insert into transcationinfo(transcationID,accountNO,tdate,description,amount,transcationtype,location) values ("2","111", "2014/12/6","traderjoe","50","credit","fremont");
insert into transcationinfo(transcationID,accountNO,tdate,description,amount,transcationtype,location) values ("3","111", "2014/12/8","safeway","30","credit","fremont");
insert into transcationinfo(transcationID,accountNO,tdate,description,amount,transcationtype,location) values ("4","111", "2014/12/8","centurytheaters","60","credit","fremont");
insert into transcationinfo(transcationID,accountNO,tdate,description,amount,transcationtype,location) values ("5","111", "2014/12/13","traderjoe","35","credit","fremont");
insert into transcationinfo(transcationID,accountNO,tdate,description,amount,transcationtype,location) values ("6","111", "2014/12/15","costco","79","credit","fremont");
insert into transcationinfo(transcationID,accountNO,tdate,description,amount,transcationtype,location) values ("7","111", "2014/12/18","walmart","100","credit","fremont");
insert into transcationinfo(transcationID,accountNO,tdate,description,amount,transcationtype,location) values ("8","111", "2014/12/18","indiacashandcarry","100","credit","fremont");
select * from transcationinfo;


create table catagory (catagoryname varchar(20) not null,merchantname varchar(100) not null, location varchar(20));
insert into catagory (catagoryname,merchantname,location) values ("wholesale","costco","fremont");
insert into catagory (catagoryname,merchantname,location) values ("grocery","traderjoe,indiacashandcarry,safeway","fremont");
insert into catagory (catagoryname,merchantname,location) values ("entertainment","centurytheaters","fremont");
insert into catagory (catagoryname,merchantname,location) values ("deportmentalstore","walmart","fremont");
select *from catagory;

select * from transcationinfo where transcationId=3;
select * from transcationinfo where description like "costco";
select * from transcationinfo where description like "costco" and amount >100;
select * from transcationinfo where description like "traderjoe" and amount < 100; 
 
 