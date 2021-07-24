-- MySQL dump 10.13  Distrib 8.0.25, for Linux (x86_64)
--
-- Host: localhost    Database: employee
-- ------------------------------------------------------
-- Server version	8.0.25-0ubuntu0.20.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `department_id` int NOT NULL,
  `dept_name` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (101,'HR'),(102,'Engineering'),(103,'Finance');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `emp_data`
--

DROP TABLE IF EXISTS `emp_data`;
/*!50001 DROP VIEW IF EXISTS `emp_data`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `emp_data` AS SELECT 
 1 AS `name`,
 1 AS `salary`,
 1 AS `dept_name`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `emp_info`
--

DROP TABLE IF EXISTS `emp_info`;
/*!50001 DROP VIEW IF EXISTS `emp_info`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `emp_info` AS SELECT 
 1 AS `id`,
 1 AS `name`,
 1 AS `salary`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `emp_sales`
--

DROP TABLE IF EXISTS `emp_sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `emp_sales` (
  `id` int NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `year` int NOT NULL,
  `country` varchar(20) DEFAULT NULL,
  `product` varchar(45) DEFAULT NULL,
  `sale` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emp_sales`
--

LOCK TABLES `emp_sales` WRITE;
/*!40000 ALTER TABLE `emp_sales` DISABLE KEYS */;
INSERT INTO `emp_sales` VALUES (1,'Amar',2019,'India','iphone10',40000),(2,'Sagar',2021,'US','iphone12',80000),(3,'Nishad',2018,'US','iphone8',30000),(4,'Mayur',2020,'India','iphone11',50000),(5,'Sanket',2020,'UK','iphone11',50000),(6,'Swaraj',2021,'UK','iphone12',80000);
/*!40000 ALTER TABLE `emp_sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_details`
--

DROP TABLE IF EXISTS `employee_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_details` (
  `id` int NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `department_id` int DEFAULT NULL,
  `salary` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_details`
--

LOCK TABLES `employee_details` WRITE;
/*!40000 ALTER TABLE `employee_details` DISABLE KEYS */;
INSERT INTO `employee_details` VALUES (1,'Amar',101,30000),(2,'Sagar',102,40000),(3,'Mayur',101,40000),(4,'Sanket',105,50000),(5,'Swaraj',101,40000);
/*!40000 ALTER TABLE `employee_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `us_info`
--

DROP TABLE IF EXISTS `us_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `us_info` (
  `rank_id` int NOT NULL,
  `state_name` varchar(20) DEFAULT NULL,
  `postal` varchar(20) DEFAULT NULL,
  `population` int DEFAULT NULL,
  PRIMARY KEY (`rank_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `us_info`
--

LOCK TABLES `us_info` WRITE;
/*!40000 ALTER TABLE `us_info` DISABLE KEYS */;
INSERT INTO `us_info` VALUES (1,'Alabama','AL',4849377),(2,'Alaska','AK',736732),(3,'Arizona','AZ',6731484),(4,'Arkansas','AR',2966369),(5,'California','CA',38802500),(6,'Colorado','CO',5355866),(7,'Connecticut','CT',3596677),(8,'Delaware','DE',935614),(9,'District of Columbia','DC',658893),(10,'Florida','FL',19893297),(11,'Georgia','GA',10097343),(12,'Hawaii','HI',1419561),(13,'Idaho','ID',1634464),(14,'Illinois','IL',12880580),(15,'Indiana','IN',6596855),(16,'Iowa','IA',3107126),(17,'Kansas','KS',2904021),(18,'Kentucky','KY',4413457),(19,'Louisiana','LA',4649676),(20,'Maine','ME',1330089),(21,'Maryland','MD',5976407),(22,'Massachusetts','MA',6745408),(23,'Michigan','MI',9909877),(24,'Minnesota','MN',5457173),(25,'Mississippi','MS',2994079),(26,'Missouri','MO',6063589),(27,'Montana','MT',1023579),(28,'Nebraska','NE',1881503),(29,'Nevada','NV',2839098),(30,'New Hampshire','NH',1326813),(31,'New Jersey','NJ',8938175),(32,'New Mexico','NM',2085572),(33,'New York','NY',19746227),(34,'North Carolina','NC',9943964),(35,'North Dakota','ND',739482),(36,'Ohio','OH',11594163),(37,'Oklahoma','OK',3878051),(38,'Oregon','OR',3970239),(39,'Pennsylvania','PA',12787209),(40,'Puerto Rico','PR',3548397),(41,'Rhode Island','RI',1055173),(42,'South Carolina','SC',4832482),(43,'South Dakota','SD',853175),(44,'Tennessee','TN',6549352),(45,'Texas','TX',26956958),(46,'Utah','UT',2942902),(47,'Vermont','VT',626562),(48,'Virginia','VA',8326289),(49,'Washington','WA',7061530),(50,'West Virginia','WV',1850326),(51,'Wisconsin','WI',5757564),(52,'Wyoming','WY',584153);
/*!40000 ALTER TABLE `us_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `emp_data`
--

/*!50001 DROP VIEW IF EXISTS `emp_data`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `emp_data` AS select `employee_details`.`name` AS `name`,`employee_details`.`salary` AS `salary`,`department`.`dept_name` AS `dept_name` from (`employee_details` join `department` on((`employee_details`.`department_id` = `department`.`department_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `emp_info`
--

/*!50001 DROP VIEW IF EXISTS `emp_info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `emp_info` AS select `employee_details`.`id` AS `id`,`employee_details`.`name` AS `name`,`employee_details`.`salary` AS `salary` from `employee_details` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-24  8:57:13
