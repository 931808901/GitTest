# 登录数据库
mysql -u root -p

# 查看所有数据库
show databases;

# 创建数据库
create database python1702;

# 删除数据库
drop database python1702;

# 切换到数据库
use python1702;

# 查看所有数据表
show tables;

# 建表
create table t_student(id int primary key auto_increment,name varchar(20),age int);

# 增加一条记录
insert into t_student(name,age) values('张三',20);

# 删除一条记录
delete from t_student where name='张三';

# 修改记录
update t_student set name='张三丰' where name='张三';

# 查询所有表记录
select * from t_student;