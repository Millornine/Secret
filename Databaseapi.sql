-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               8.0.17 - MySQL Community Server - GPL
-- Server OS:                    Win64
-- HeidiSQL Version:             12.7.0.6850
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for senior
CREATE DATABASE IF NOT EXISTS `senior` /*!40100 DEFAULT CHARACTER SET tis620 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `senior`;

-- Dumping structure for table senior.course
CREATE TABLE IF NOT EXISTS `course` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT,
  `c_name` varchar(120) NOT NULL DEFAULT '',
  `c_description` varchar(255) NOT NULL DEFAULT '',
  `c_price` decimal(20,2) NOT NULL DEFAULT '0.00',
  PRIMARY KEY (`c_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=tis620;

-- Dumping data for table senior.course: ~0 rows (approximately)
REPLACE INTO `course` (`c_id`, `c_name`, `c_description`, `c_price`) VALUES
	(3, 'computer system', 'computer system v2.0.1', 12000.00);

-- Dumping structure for table senior.enroll
CREATE TABLE IF NOT EXISTS `enroll` (
  `cer_id` int(11) NOT NULL AUTO_INCREMENT,
  `m_id` int(11) NOT NULL DEFAULT '0',
  `c_id` int(11) NOT NULL DEFAULT '0',
  `cer_start` datetime NOT NULL,
  `cer_expire` datetime NOT NULL,
  PRIMARY KEY (`cer_id`),
  KEY `FK__member` (`m_id`),
  KEY `FK__course` (`c_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=tis620;

-- Dumping data for table senior.enroll: ~2 rows (approximately)
REPLACE INTO `enroll` (`cer_id`, `m_id`, `c_id`, `cer_start`, `cer_expire`) VALUES
	(4, 4, 3, '2024-08-16 10:13:40', '2024-08-16 10:13:40'),
	(5, 5, 3, '2024-08-15 16:06:44', '2024-08-20 16:06:44');

-- Dumping structure for table senior.member
CREATE TABLE IF NOT EXISTS `member` (
  `m_id` int(11) NOT NULL AUTO_INCREMENT,
  `m_email` varchar(120) NOT NULL DEFAULT '',
  `m_password` varchar(120) NOT NULL DEFAULT '',
  `m_name` varchar(120) NOT NULL DEFAULT '',
  PRIMARY KEY (`m_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=tis620;

-- Dumping data for table senior.member: ~0 rows (approximately)
REPLACE INTO `member` (`m_id`, `m_email`, `m_password`, `m_name`) VALUES
	(5, 'test01@test01.com', '123456', 'test test');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
