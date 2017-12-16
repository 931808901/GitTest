

# 创建数据库
CREATE DATABASE china CHARACTER SET 'utf8' COLLATE 'utf8_general_ci';

CREATE TABLE mytest(
	id INTEGER PRIMARY KEY auto_increment,
	name VARCHAR(20),
	age INTEGER,
	birthday datetime
);

INSERT into mytest(name,age) VALUES ("晁盖",30);

DELETE from mytest where name="chaogai";

update mytest set birthday=19700101000001;

select * from mytest;


# 查询宝安区的城市ID
select CityID from t_district where DisName = "宝安区";

# 从城市表中查询城市ID=200的记录
select * from t_city where CityID = 200;

# 查询宝安区所属的城市信息
select ProID from t_city where CityID = (select CityID from t_district where DisName = "宝安区");

# 查询宝安区所属的省份信息
select * from t_province where ProID = (select ProID from t_city where CityID = (select CityID from t_district where DisName = "宝安区"));


select ProID,ProRemark from t_province where ProName = "江西省";

select * from t_province where ProName like "%西省";

select * from t_province where ProName like "%西%";

select * from t_province where ProName like "%西省" or ProName like "%东省";

select ProName from t_province where ProName like "%西省" union select CityName from t_city where CityName like "%西市";

select * from t_province WHERE ProID = (select ProID from t_city where CityName = "鸡西市");


# 默认升序
select * from t_city ORDER BY CityID;

# 使用CityID的降序排列
select * from t_city ORDER BY CityID DESC;

# 使用CityID的升序排列
select * from t_city ORDER BY CityName ASC;

#江西省所有城市按城市ID升序
select *
from t_city
where ProID = (SELECT ProID FROM t_province WHERE ProName = "江西省")
ORDER BY CityID;

# 所有名称不带省字的省级行政区，按省份ID升序
SELECT *
from t_province
WHERE ProName not LIKE "%省"
ORDER BY ProID ASC;

# 所有名称不带“区县”二字的区县级行政区
SELECT *
from t_district
WHERE (DisName not LIKE "%区" ) and (DisName not LIKE "%县" );


# 所有Id不在【非区县结果集】中的记录
select * from t_district WHERE Id not in
(
SELECT Id from t_district
WHERE (DisName not LIKE "%区" ) and (DisName not LIKE "%县" )
);

# 所有某州市且在【国家重点发展城市名单】
SELECT * from t_city WHERE (CityName like "%州市") and CityName in
("张家口市","赣州市","上饶市","九江市","鹰潭市","丹东市","抚州市");

#  查询江西省所有【X州市】
select * from t_city where CityName like "%州市" and ProID = (select ProID from t_province where ProName="江西省");

#  查询江西省有多少个【X州市】
select count(CityID) from t_city where CityName like "%州市" and ProID = (select ProID from t_province where ProName="江西省");

# 江西一共有多少个地级市
select count(CityID)
from t_city
WHERE ProID = (SELECT ProID from t_province where ProName="广东省")

# 查询所有省份分别有多少地级市
select ProID as 省ID,count(CityID) as 地级市数量
from t_city
GROUP BY ProID



# 江西省的各市分别有多少个区县
# 全国所有地级市分别有多少个区县
select CityID as 城市ID,count(DisName) as 区县数量
from t_district
GROUP BY CityID
# 城市ID位于江西城市ID的集合中
having CityID IN
(
#查询江西所有的城市ID
select CityID FROM t_city where ProID=(select ProID from t_province where ProName="江西省")
)

# 查询全国每个地级市分别有多少区县
SELECT CityID,count(DisName)
from t_district
WHERE TRUE
GROUP BY CityID
HAVING CityID IN
(
# 江西省所有城市ID
select CityID
from t_city
WHERE ProID = (select ProID from t_province WHERE ProName = "江西省")
)


#
select max(CitySort)
from t_city
WHERE ProID = (select ProID from t_province WHERE ProName = "江西省")

# 中国各省分别有多少个地级市
SELECT ProID,avg(CitySort)
from t_city
GROUP BY ProID

# 所有X州市的人口
select CityName,CitySort
from t_city
WHERE CityName like "%州市"

# 所有X州市的平均人口
select AVG(CitySort)
from t_city
WHERE CityName like "%州市"

# 中国一共有多少个“州”
select count(*)
from t_city
WHERE CityName like "%州市"

#求各省分别有多少地级市（省名称，地级市数量）
select ProName,count(CityID) as 城市数量
from t_province JOIN t_city
ON t_city.ProID = t_province.ProID
GROUP BY t_city.ProID
ORDER BY 城市数量 DESC;

#求各省分别有多少地级市（省名称，地级市数量）
select ProName as 省份,count(CityID) as 城市数量
from t_province as p JOIN t_city as c
ON c.ProID = p.ProID
GROUP BY c.ProID
ORDER BY 城市数量 DESC;

#求【江西所有城市】和【湖北所有城市】中人口最多的城市，以及所属的省ID，及该城人口
select ProID,CityName
