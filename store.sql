DROP TABLE IF EXISTS `emp`;
CREATE TABLE `emp` (
  `eno` int(5),
  `ename` varchar(20),
  `sal` int(10)
);

INSERT INTO `emp` VALUES
(1,'Aryan',99999),
(2,'Bhagath',30000),
(3,'Chinmay',70000);

DROP TABLE IF EXISTS `item`;
CREATE TABLE `item` (
  `itemno` int(5),
  `itemname` varchar(20),
  `price` float 
) ;

INSERT INTO `item` VALUES
(101,'Apple',10),
(102,'Banana',20),
(103,'Pen',40);
