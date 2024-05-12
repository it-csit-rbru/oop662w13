-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 12, 2024 at 04:14 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `oopdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `comic`
--

CREATE TABLE `comic` (
  `cmn_id` int(10) NOT NULL,
  `cmn_name_th` varchar(200) NOT NULL,
  `cmn_name_jpen` varchar(200) NOT NULL,
  `cmn_pub_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `comic`
--

INSERT INTO `comic` (`cmn_id`, `cmn_name_th`, `cmn_name_jpen`, `cmn_pub_id`) VALUES
(1, 'ดันดาดัน', 'DanDaDan', 1);

-- --------------------------------------------------------

--
-- Table structure for table `comic_volume`
--

CREATE TABLE `comic_volume` (
  `cmv_id` int(11) NOT NULL,
  `cmv_cmn_id` int(11) NOT NULL,
  `cmv_vol` int(11) NOT NULL,
  `cmv_isbn` int(11) NOT NULL,
  `cmv_price` int(11) NOT NULL,
  `cmv_date` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `publisher`
--

CREATE TABLE `publisher` (
  `pub_id` int(10) NOT NULL,
  `pub_name` varchar(100) NOT NULL,
  `pub_address` varchar(300) NOT NULL,
  `pub_phone` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `publisher`
--

INSERT INTO `publisher` (`pub_id`, `pub_name`, `pub_address`, `pub_phone`) VALUES
(1, 'สยามอินเตอร์คอมิกส์', '459 ซ.พิบูลอุปถัมภ์ ลาดพร้าว 46 แขงสามเสนนอก เขตห้วยขวาง กรุงเทพฯ 10310', '026943010 ต่อ 1506-1507,1521-1523'),
(2, 'เอ บุ๊ค บาย เอจี กรุ๊ป', '29/463 หมู่ 9 ตำบล บางพูด อำเภอ ปากเกร็ด จังหวัด นนทบุรี 11210', '029841112'),
(3, 'เด๊กซ์เพรส', '19 สวนสน 9 ถนนรามคำแหง 60 แขวงหัวหมาก เขตบางกะปิ กรุงเทพมหานคร 10240', '027356830'),
(7, 'RBRU', 'RBRU', '039471058'),
(8, 'RBRU', 'RBRU', '039471058');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comic`
--
ALTER TABLE `comic`
  ADD PRIMARY KEY (`cmn_id`),
  ADD KEY `cmn_pub_id` (`cmn_pub_id`);

--
-- Indexes for table `comic_volume`
--
ALTER TABLE `comic_volume`
  ADD PRIMARY KEY (`cmv_id`);

--
-- Indexes for table `publisher`
--
ALTER TABLE `publisher`
  ADD PRIMARY KEY (`pub_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comic`
--
ALTER TABLE `comic`
  MODIFY `cmn_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `comic_volume`
--
ALTER TABLE `comic_volume`
  MODIFY `cmv_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `publisher`
--
ALTER TABLE `publisher`
  MODIFY `pub_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `comic`
--
ALTER TABLE `comic`
  ADD CONSTRAINT `omn_publisher` FOREIGN KEY (`cmn_pub_id`) REFERENCES `publisher` (`pub_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
