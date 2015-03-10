-- phpMyAdmin SQL Dump
-- version 4.2.8
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2015-03-10 13:44:17
-- 服务器版本： 5.5.38-0ubuntu0.12.04.1
-- PHP Version: 5.3.10-1ubuntu3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `product`
--

-- --------------------------------------------------------

--
-- 表的结构 `devices`
--

CREATE TABLE IF NOT EXISTS `devices` (
`id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL,
  `user` varchar(255) NOT NULL,
  `bindusers` varchar(255) NOT NULL,
  `groups` varchar(255) NOT NULL,
  `data` varchar(255) NOT NULL,
  `pos` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `lasttime` datetime NOT NULL,
  `seedid` varchar(255) NOT NULL
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `devices`
--

INSERT INTO `devices` (`id`, `name`, `brand`, `user`, `bindusers`, `groups`, `data`, `pos`, `status`, `lasttime`, `seedid`) VALUES
(15, '玉米种子', '隆兴集团', '', '', '', '', '产品已销售', 0, '2014-09-25 15:32:03', '20140924001'),
(16, '小麦种子', '隆兴集团', '', '', '', '', '产品已生产', 0, '2014-11-18 17:41:14', '20140924002');

-- --------------------------------------------------------

--
-- 表的结构 `deviceuser`
--

CREATE TABLE IF NOT EXISTS `deviceuser` (
`id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `deviceuser`
--

INSERT INTO `deviceuser` (`id`, `name`) VALUES
(1, '测试用户1'),
(2, '测试用户2');

-- --------------------------------------------------------

--
-- 表的结构 `functions`
--

CREATE TABLE IF NOT EXISTS `functions` (
`id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `functions`
--

INSERT INTO `functions` (`id`, `name`, `url`) VALUES
(1, '欢迎页面', 'welcome'),
(2, '产品信息查看', 'view'),
(3, '产品管理', 'manage'),
(5, '密码管理', 'changepasswd'),
(6, '下载APP', '../static/zlwscanner.apk'),
(7, '帮助手册', '../static/seed-manual.pdf');

-- --------------------------------------------------------

--
-- 表的结构 `groups`
--

CREATE TABLE IF NOT EXISTS `groups` (
`id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `groups`
--

INSERT INTO `groups` (`id`, `name`) VALUES
(1, '测试群组1'),
(2, '测试群组2');

-- --------------------------------------------------------

--
-- 表的结构 `hispos`
--

CREATE TABLE IF NOT EXISTS `hispos` (
`id` int(11) NOT NULL,
  `deviceid` int(11) NOT NULL,
  `pos` varchar(255) NOT NULL,
  `time` datetime NOT NULL,
  `seedid` varchar(255) NOT NULL,
  `brand` varchar(255) NOT NULL
) ENGINE=MyISAM AUTO_INCREMENT=337 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `hispos`
--

INSERT INTO `hispos` (`id`, `deviceid`, `pos`, `time`, `seedid`, `brand`) VALUES
(336, 16, '产品已生产', '2014-11-18 17:41:14', '20140924002', '隆兴集团'),
(334, 16, '产品已生产', '2014-11-18 17:41:08', '20140924002', '隆兴集团'),
(335, 16, '产品已生产', '2014-11-18 17:41:13', '20140924002', '隆兴集团'),
(333, 16, '产品已销售', '2014-10-20 19:56:43', '20140924002', '隆兴集团'),
(332, 16, '产品已生产', '2014-10-20 17:21:22', '20140924002', '隆兴集团'),
(331, 16, '产品已生产', '2014-10-20 17:13:18', '20140924002', '隆兴集团'),
(330, 16, '产品已生产', '2014-10-20 17:06:16', '20140924002', '隆兴集团'),
(329, 16, '产品已生产', '2014-10-20 17:06:13', '20140924002', '隆兴集团'),
(327, 16, '产品已生产', '2014-10-20 17:05:30', '20140924002', '隆兴集团'),
(328, 16, '产品已生产', '2014-10-20 17:05:33', '20140924002', '隆兴集团'),
(323, 15, '产品已销售', '2014-09-25 15:32:03', '20140924001', '隆兴集团'),
(322, 15, '产品已销售', '2014-09-25 15:24:40', '20140924001', '隆兴集团'),
(326, 16, '产品已生产', '2014-10-20 11:02:46', '20140924002', '隆兴集团 '),
(321, 15, '产品已生产', '2014-09-25 15:24:19', '20140924001', '隆兴集团'),
(318, 15, '产品信息创建', '2014-09-24 18:12:15', '20140924001', '隆兴集团'),
(319, 16, '产品信息创建', '2014-09-24 18:12:28', '20140924002', '隆兴集团');

-- --------------------------------------------------------

--
-- 表的结构 `sessions`
--

CREATE TABLE IF NOT EXISTS `sessions` (
  `session_id` char(128) NOT NULL,
  `atime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `data` text
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `sessions`
--

INSERT INTO `sessions` (`session_id`, `atime`, `data`) VALUES
('d06f138dda3ab94f09a43085c0152595c8b2b89c', '2015-02-10 00:25:40', 'KGRwMQpTJ3VzZXJuYW1lJwpwMgpJMApzUydpcCcKcDMKVjIyMi4xODYuMTI4LjUyCnA0CnNTJ2xv\nZ2luJwpwNQpJMDAKc1Mnc2Vzc2lvbl9pZCcKcDYKUydkMDZmMTM4ZGRhM2FiOTRmMDlhNDMwODVj\nMDE1MjU5NWM4YjJiODljJwpwNwpzLg==\n'),
('92836473f682f661f88df4daeabd444f7b71263c', '2015-02-09 23:58:00', 'KGRwMQpTJ3VzZXJuYW1lJwpwMgpJMApzUydpcCcKcDMKVjIyMi4xODYuMTI4LjU1CnA0CnNTJ2xv\nZ2luJwpwNQpJMDAKc1Mnc2Vzc2lvbl9pZCcKcDYKUyc5MjgzNjQ3M2Y2ODJmNjYxZjg4ZGY0ZGFl\nYWJkNDQ0ZjdiNzEyNjNjJwpwNwpzLg==\n'),
('c36aaeb7f564401bd684530a2a4bd30b8af44c63', '2015-02-10 00:25:39', 'KGRwMQpTJ3VzZXJuYW1lJwpwMgpJMApzUydpcCcKcDMKVjIyMi4xODYuMTI4LjU1CnA0CnNTJ2xv\nZ2luJwpwNQpJMDAKc1Mnc2Vzc2lvbl9pZCcKcDYKUydjMzZhYWViN2Y1NjQ0MDFiZDY4NDUzMGEy\nYTRiZDMwYjhhZjQ0YzYzJwpwNwpzLg==\n');

-- --------------------------------------------------------

--
-- 表的结构 `status`
--

CREATE TABLE IF NOT EXISTS `status` (
  `id` int(11) NOT NULL,
  `statusname` varchar(255) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `status`
--

INSERT INTO `status` (`id`, `statusname`) VALUES
(1, '产品已销售'),
(0, '产品已生产');

-- --------------------------------------------------------

--
-- 表的结构 `type`
--

CREATE TABLE IF NOT EXISTS `type` (
`id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `type`
--

INSERT INTO `type` (`id`, `name`) VALUES
(1, '测试类型1'),
(2, '测试类型2');

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE IF NOT EXISTS `user` (
`id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `registertime` datetime NOT NULL COMMENT '注册时间',
  `lasttime` datetime NOT NULL COMMENT '最后登录时间',
  `admin` int(11) NOT NULL DEFAULT '0'
) ENGINE=MyISAM AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `name`, `registertime`, `lasttime`, `admin`) VALUES
(29, 'ch', 'iG%L&$C7E!OQWf91e067c94e26ff759272fd5380bcd6577538fb1b93d4bb87c30efa219df7bab', '陈欢', '2013-12-30 20:46:37', '2014-05-13 18:04:02', 0),
(30, '13312311231', 'bd9sG#y~eOjHfb5b8463f7ecf7247f2cb2286670fc30275adf46015521080dd072e8e417db478', 'aegftqwet4g', '2013-12-31 10:49:45', '2013-12-31 10:49:45', 0),
(31, 'test', 'Ptdh*HZq@J&1V250096d377a075cc90ea42232b128184b1e377d9f8d146fd5cc0ba9eb4686271', 'test', '2014-01-14 18:13:08', '2014-12-09 16:02:27', 0),
(32, 'test1', '~B!F*Z%KJW7q39aa32847f979c27a674a7edad9305bf92fd34cc3047670855ad39b5fa8593f2f', 'test', '2014-03-16 15:16:52', '2014-03-16 15:16:52', 0),
(33, 'yxxone', 'nl!bNOpcUX%fYbb9e87846badd877dbf8725380e856d3aa786972b65d6fb32bef6c55b825a772', '111111', '2014-03-18 14:47:21', '2014-03-18 14:47:21', 0),
(34, '又要注册', '%VILApdbcU98lab7ef5537ab08a80fd785e6df3cfc5ec6cef585d63708161fdcca3dd2b466def', '管你屁事', '2014-04-02 10:30:05', '2014-04-02 10:30:05', 0),
(35, 'yxx', '$XiHn9yDL4%Jvfd998fad60bd93d4a1f9168634e2939409a4c6ac3c0a1f231fc60d8786f518da', 'yxx', '2014-04-21 12:47:40', '2014-10-20 19:59:10', 0),
(36, 'zhstep', 'gG3WzCA$Rm9Q&cfa4f5897210240bf15bb31d7190ee73e7f25d7baeb0d3c50568d373ac2b3a4f', '周浩', '2014-04-21 13:17:56', '2014-04-21 13:17:56', 0),
(37, 'yxxoone2', 'o%F1iyNVPwQ2!21bb81700e28f10f09efe59ac1b3cbc6f3db79b7c5294d30feab641eede47124', '我不是欢哥', '2014-05-13 17:14:33', '2014-05-13 17:14:33', 0),
(38, 'yxxone3', 'dR3x!ecwah&pk2b2a49f540a70ba10c879f4b55af1b202282b46844957b33b169aec731252803', 'yxx', '2014-05-14 17:56:04', '2014-08-09 16:09:15', 0),
(39, 'zlw', 'NwAhRplyxDoiU218a441a7eee61c206b4a9d5964bde6f38b41e7c3459c368cc824aaa0213226a', '种联网平台用户', '2014-07-15 14:37:23', '2014-11-13 15:36:03', 0),
(40, 'shilei', 'PUbS2mXE@c6B!cee52e00af0ee05feb5c1e2e5b72cdd249be44327cb2d0e66b5cc999b406840b', '石磊', '2014-11-18 15:58:23', '2014-11-20 16:05:12', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `devices`
--
ALTER TABLE `devices`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `deviceuser`
--
ALTER TABLE `deviceuser`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `functions`
--
ALTER TABLE `functions`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `groups`
--
ALTER TABLE `groups`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hispos`
--
ALTER TABLE `hispos`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
 ADD UNIQUE KEY `session_id` (`session_id`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
 ADD KEY `id` (`id`);

--
-- Indexes for table `type`
--
ALTER TABLE `type`
 ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
 ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `devices`
--
ALTER TABLE `devices`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=20;
--
-- AUTO_INCREMENT for table `deviceuser`
--
ALTER TABLE `deviceuser`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `functions`
--
ALTER TABLE `functions`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `groups`
--
ALTER TABLE `groups`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `hispos`
--
ALTER TABLE `hispos`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=337;
--
-- AUTO_INCREMENT for table `type`
--
ALTER TABLE `type`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=41;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
