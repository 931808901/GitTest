CREATE DATABASE mynews;

#文章表（自增长主键ID，标题，日期，媒体，外键作者ID）
CREATE TABLE t_articles(
id INT PRIMARY KEY AUTO_INCREMENT,
title VARCHAR(50) UNIQUE,#唯一约束：下次插入title相同的记录时将无法插入
publish_time DATETIME,
media VARCHAR(20),
author_id INT
);

# 修改文章表，为title键增加唯一约束
ALTER TABLE t_article ADD UNIQUE (title);

#记者表（自增长ID，姓名，邮箱、媒体单位ID）
CREATE TABLE t_author(
id INT PRIMARY KEY AUTO_INCREMENT,
NAME VARCHAR(20) UNIQUE,#唯一约束：下次插入姓名相同的作者记录时将无法插入
email VARCHAR(50),
media_id INT
); 

#修改作者表，添加姓名字段
ALTER TABLE t_author ADD COLUMN(
NAME VARCHAR(20)
);

#创建媒体表:name字段唯一，无法插入name相同的记录
CREATE TABLE t_media(
id INT PRIMARY KEY AUTO_INCREMENT,
NAME VARCHAR(20) UNIQUE#唯一约束：下次插入名称相同的媒体记录时将无法插入
);

#查询某作者的全部文章
SELECT a.`title` 
FROM t_article a JOIN t_author b ON a.`author_id`=b.id
WHERE b.name LIKE '李天奕%';


