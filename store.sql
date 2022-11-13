--
-- Table structure for table `emp`
--

DROP TABLE IF EXISTS `emp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emp` (
  `eno` int(5) DEFAULT NULL,
  `ename` varchar(20) DEFAULT NULL,
  `sal` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp`
--

LOCK TABLES `emp` WRITE;
/*!40000 ALTER TABLE `emp` DISABLE KEYS */;
INSERT INTO `emp` VALUES
(1,'Aryan',99999),
(2,'Bhagath',30000),
(3,'Chinmay',70000);
/*!40000 ALTER TABLE `emp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `item`
--

DROP TABLE IF EXISTS `item`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `item` (
  `itemno` int(5) DEFAULT NULL,
  `itemname` varchar(20) DEFAULT NULL,
  `price` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `item`
--

LOCK TABLES `item` WRITE;
/*!40000 ALTER TABLE `item` DISABLE KEYS */;
INSERT INTO `item` VALUES
(101,'Apple',10),
(102,'Banana',20),
(103,'Pen',40);
/*!40000 ALTER TABLE `item` ENABLE KEYS */;
UNLOCK TABLES;

