create database Railway;

use Railway;
create table passengers(
	pname varchar(60),
    age varchar(60),
    traino varchar(60),
    noof varchar(60),
    cls varchar(60),
    destination varchar(60),
    amt varchar(60),
    status varchar(60),
    pnrno varchar(60)
    );
    
    
create table trainsdetail(
	tname varchar(60),
    tnum varchar(60),
    source varchar(60),
    destination varchar(60),
    fare varchar(60),
    ac1 varchar(60),
    ac2 varchar(60),
    slp varchar(60)
    );
    

insert into passengers values('Ankit Khurana','47','4347','1','AC1','GOA','3000','conf','G1001');
insert into passengers values('Mahinder Kapoor','54','5353','2','AC2','JAMMU','1000','conf','G1002');

insert into trainsdetail values('Goa Express','4347','Delhi','Goa','5000','23','34','65');
insert into trainsdetail values('Jammu Tavi','5353','Delhi','Jammu','6000','23','26','54');


select * from passengers;
select * from trainsdetail;

-- Delete from passengers where pname='sid';
-- set sql_safe_updates=0;