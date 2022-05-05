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
-- Table structure for table `accounts_usuario_acesso`
--

DROP TABLE IF EXISTS `accounts_usuario_acesso`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `accounts_usuario_acesso` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date_login` datetime(6) NOT NULL,
  `date_logout` datetime(6) DEFAULT NULL,
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `accounts_usuario_ace_usuario_id_a52f55a8_fk_accounts_` (`usuario_id`),
  CONSTRAINT `accounts_usuario_ace_usuario_id_a52f55a8_fk_accounts_` FOREIGN KEY (`usuario_id`) REFERENCES `accounts_usuario` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_usuario_acesso`
--

LOCK TABLES `accounts_usuario_acesso` WRITE;
/*!40000 ALTER TABLE `accounts_usuario_acesso` DISABLE KEYS */;
INSERT INTO `accounts_usuario_acesso` VALUES (1,'2022-05-04 13:36:35.487671',NULL,1),(2,'2022-05-04 13:36:51.589291',NULL,1),(4,'2022-05-04 13:43:30.422691',NULL,3),(5,'2022-05-04 13:47:46.181205',NULL,1),(6,'2022-05-04 14:32:25.662622',NULL,1),(7,'2022-05-04 15:27:34.420410',NULL,3),(8,'2022-05-04 18:11:33.904508',NULL,1);
/*!40000 ALTER TABLE `accounts_usuario_acesso` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-04 16:54:41
