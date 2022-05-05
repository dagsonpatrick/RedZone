-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: redzone
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `api_eventoredzone`
--

DROP TABLE IF EXISTS `api_eventoredzone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `api_eventoredzone` (
  `id` int NOT NULL AUTO_INCREMENT,
  `portal` varchar(15) NOT NULL,
  `sentido` varchar(15) NOT NULL,
  `temperature` int NOT NULL,
  `battery` int NOT NULL,
  `status` int NOT NULL,
  `timestamp` datetime(6) DEFAULT NULL,
  `tag_id` bigint NOT NULL,
  `collaborator_id` bigint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `api_eventoredzone_tag_id_e93d934e_fk_tag_tag_id` (`tag_id`),
  KEY `api_eventoredzone_collaborator_id_55dee81a_fk_collabora` (`collaborator_id`),
  CONSTRAINT `api_eventoredzone_collaborator_id_55dee81a_fk_collabora` FOREIGN KEY (`collaborator_id`) REFERENCES `collaborator_collaborator` (`id`),
  CONSTRAINT `api_eventoredzone_tag_id_e93d934e_fk_tag_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `tag_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `api_eventoredzone`
--

LOCK TABLES `api_eventoredzone` WRITE;
/*!40000 ALTER TABLE `api_eventoredzone` DISABLE KEYS */;
INSERT INTO `api_eventoredzone` VALUES (2,'01','Entrou',23,59,1,'2020-04-30 20:01:18.539000',2,2),(3,'01','Entrou',20,59,1,'2020-04-30 20:01:18.539000',1,1),(4,'01','Entrou',24,80,1,'2020-04-30 20:01:18.539000',3,3);
/*!40000 ALTER TABLE `api_eventoredzone` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-04 16:54:37
