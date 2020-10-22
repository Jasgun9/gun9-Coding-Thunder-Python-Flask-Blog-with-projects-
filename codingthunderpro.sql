-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 22, 2020 at 11:05 AM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunderpro`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(50) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `email`, `phone_num`, `msg`, `date`) VALUES
(1, 'first post', 'firstpost@gmail.com', '123456789', 'first post', '2020-10-09 19:19:24'),
(2, 'this', 'this@gmail.com', '5555555555', 'Jasgun singh', '2020-10-10 14:54:37'),
(3, 'this', 'this@gmail.com', '5555555555', 'fhgj', '2020-10-10 15:36:43'),
(4, 'Js', 'js@gmail.com', '5555555555', 'Jssssss', '2020-10-10 18:14:42'),
(5, 'Js', 'js@gmail.com', '5555555555', 'Jsssssssssssssssssssss', '2020-10-10 18:26:55'),
(6, 'Js', 'js@gmail.com', '5555555555', 'Jsssssssssssssssssssss', '2020-10-10 18:50:40'),
(7, 'this', 'this@gmail.com', '5555555555', 'fggf', '2020-10-10 21:37:53');

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `sno` int(255) NOT NULL,
  `title` varchar(50) NOT NULL,
  `language` varchar(50) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `code` varchar(2000) NOT NULL,
  `date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`sno`, `title`, `language`, `slug`, `code`, `date`) VALUES
(1, 'java hello world program', 'java', 'java-hello-world', 'class HelloWorld {\r\n    public static void main(String[] args) {\r\n        System.out.println(\"Hello, World!\"); \r\n    }\r\n}', '2020-10-15 20:55:16'),
(2, 'python hello world program', 'python', 'python-hello-world', 'print(\"Hello world\")', '2020-10-15 00:00:00'),
(3, 'c hello world program', 'c', 'c-hello-world', '#include<stdio.h>\r\nint main{\r\n    printf(\"Hello world\");\r\n    return 0;\r\n}', '2020-10-15 00:00:00'),
(4, 'c++ hello world program', 'cpp', 'cpp-hello-world-program', '#include<iostream>\r\nusing namespace std;\r\nint main(){\r\n    cout<<\"Hello World\";\r\n    return 0;\r\n}', '2020-10-18 18:21:24'),
(5, 'javascript hello world program', 'javascript', 'javascript-hello-world-program', 'console.log(\"Hello world\")', '2020-10-18 18:26:01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `sno` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
