create database flask_api;
use flask_api;

GRANT ALL PRIVILEGES ON flask_api.* TO 'root'@'localhost';

CREATE TABLE `user_table` (
  `user_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(100) DEFAULT NULL,
  `user_email` varchar(100) DEFAULT NULL,
  `user_password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
)AUTO_INCREMENT=1001 DEFAULT CHARSET=utf8;


INSERT INTO `flask_api`.`user_table`
(`user_name`,
`user_email`,
`user_password`)
VALUES
("Sanchit","sanchit@hydpy.org","12345"),
("Ram","ram@hydpy.org","12345"),
("Mani","mani@hydpy.org","12345"),
("Chirag","chirag@hydpy.org","12345"),
("Ananyo","ananyo@hydpy.org","12345"),
("Nithin","nithin@hydpy.org","12345"),
("Prudhvi","prudhvi@hydpy.org","12345"),
("divya","divya@hydpy.org","12345"),
("praneeth","praneeth@hydpy.org","12345"),
("bharath","bharath@hydpy.org","12345"),
("nivesh","nivesh@hydpy.org","12345"),
("jatin","jatin@hydpy.org","12345"),
("abhinay","abhinay@hydpy.org","12345"),
("gokul","gokul@hydpy.org","12345"),
("mohinder","mohinder@hydpy.org","12345"),
("gauri","gauri@hydpy.org","12345"),
("kanchan","kanchan@hydpy.org","12345");