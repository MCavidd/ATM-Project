CREATE DATABASE IF NOT EXISTS atm ;
USE atm;

-- atm.delete2 definition

CREATE TABLE IF NOT EXISTS`delete2` (
  `id` int NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Surname` varchar(100) NOT NULL,
  `cardnum` varchar(100) NOT NULL,
  `pin` varchar(100) NOT NULL,
  `balance` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS `people` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Surname` varchar(100) NOT NULL,
  `cardnum` varchar(100) NOT NULL,
  `pin` varchar(100) NOT NULL,
  `balance` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
