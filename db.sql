-- phpMyAdmin SQL Dump
-- version 4.9.4deb1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Mar 31, 2020 at 04:21 AM
-- Server version: 8.0.19-0ubuntu0.19.10.3
-- PHP Version: 7.3.11-0ubuntu0.19.10.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `les`
--

-- --------------------------------------------------------

--
-- Table structure for table `administrador`
--

CREATE TABLE `administrador` (
  `Utilizador_idutilizador` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `anfiteatro`
--

CREATE TABLE `anfiteatro` (
  `edificio` varchar(45) NOT NULL,
  `andar` varchar(45) NOT NULL,
  `espaco_idespaco` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `arlivre`
--

CREATE TABLE `arlivre` (
  `descricao` varchar(255) NOT NULL,
  `espaco_idespaco` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `atividade`
--

CREATE TABLE `atividade` (
  `idAtividade` int NOT NULL,
  `titulo` varchar(45) NOT NULL,
  `capacidade` int NOT NULL,
  `publico_alvo` varchar(45) NOT NULL,
  `duracao` float NOT NULL,
  `descricao` varchar(250) NOT NULL,
  `validada` tinyint NOT NULL DEFAULT '0',
  `professor_universitario_Utilizador_idutilizador` int NOT NULL,
  `unidade_organica_idUO` int NOT NULL,
  `Departamento_idDepartamento` int NOT NULL,
  `espaco_idespaco` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `atividade`
--

INSERT INTO `atividade` (`idAtividade`, `titulo`, `capacidade`, `publico_alvo`, `duracao`, `descricao`, `validada`, `professor_universitario_Utilizador_idutilizador`, `unidade_organica_idUO`, `Departamento_idDepartamento`, `espaco_idespaco`) VALUES
(3, 'dsfgh', 123, 'dfgdfg', 12, 'sddgdfg', 0, 1, 5, 4, 5);

-- --------------------------------------------------------

--
-- Table structure for table `atividade_has_material`
--

CREATE TABLE `atividade_has_material` (
  `Atividade_idAtividade` int NOT NULL,
  `Material_idMaterial` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `campus`
--

CREATE TABLE `campus` (
  `idCampus` int NOT NULL,
  `nome` varchar(255) NOT NULL,
  `paragem` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `campus`
--

INSERT INTO `campus` (`idCampus`, `nome`, `paragem`) VALUES
(21, 'Gambelas', 'Gambelas'),
(22, 'Penha', 'Penha');

-- --------------------------------------------------------

--
-- Table structure for table `colaborador`
--

CREATE TABLE `colaborador` (
  `curso` varchar(45) NOT NULL,
  `preferencia` varchar(255) DEFAULT NULL,
  `Utilizador_idutilizador` int NOT NULL,
  `dia_aberto_ano` year NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `colaborador_has_horario`
--

CREATE TABLE `colaborador_has_horario` (
  `colaborador_Utilizador_idutilizador` int NOT NULL,
  `horario_has_dia_id_dia_hora` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `colaborador_has_unidade_organica`
--

CREATE TABLE `colaborador_has_unidade_organica` (
  `colaborador_Utilizador_idutilizador` int NOT NULL,
  `unidade_organica_idUO` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `coordenador`
--

CREATE TABLE `coordenador` (
  `Utilizador_idutilizador` int NOT NULL,
  `unidade_organica_idUO` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `coordenador_has_departamento`
--

CREATE TABLE `coordenador_has_departamento` (
  `Coordenador_Utilizador_idutilizador` int NOT NULL,
  `Departamento_idDepartamento` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `departamento`
--

CREATE TABLE `departamento` (
  `idDepartamento` int NOT NULL,
  `nome` varchar(255) NOT NULL,
  `unidade_organica_idUO` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `departamento`
--

INSERT INTO `departamento` (`idDepartamento`, `nome`, `unidade_organica_idUO`) VALUES
(4, 'AD', 5),
(5, 'dasd', 6);

-- --------------------------------------------------------

--
-- Table structure for table `dia`
--

CREATE TABLE `dia` (
  `dia` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `dia`
--

INSERT INTO `dia` (`dia`) VALUES
('2020-03-17');

-- --------------------------------------------------------

--
-- Table structure for table `dia_aberto`
--

CREATE TABLE `dia_aberto` (
  `ano` year NOT NULL,
  `descricao` varchar(120) DEFAULT NULL,
  `datainscricao` date NOT NULL,
  `emailDiaAberto` varchar(120) NOT NULL,
  `enderecoPaginaWeb` varchar(60) NOT NULL,
  `dataDiainscricaoAtividadesInicio` date NOT NULL,
  `dataDiaAbertoInicio` date NOT NULL,
  `dataInscricaoAtividadesfim` date NOT NULL,
  `dataDiaAbertofim` date NOT NULL,
  `dataPropostaAtividadeInicio` date NOT NULL,
  `dataPropostaAtividadesFim` date NOT NULL,
  `Utilizador_idutilizador` int NOT NULL,
  `Administrador_Utilizador_idutilizador` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `escola`
--

CREATE TABLE `escola` (
  `idescola` int NOT NULL,
  `nome` varchar(255) NOT NULL,
  `local` varchar(45) NOT NULL,
  `telefone` varchar(45) NOT NULL,
  `email` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `escola`
--

INSERT INTO `escola` (`idescola`, `nome`, `local`, `telefone`, `email`) VALUES
(8, 'Miguel Martins', 'kljdflkjsldfj', '916069401', 'miguelmartins17@hotmail.com'),
(9, 'Miguel Martins', 'kljdflkjsldfj', '916069401', 'miguelmartins17@hotmail.com'),
(10, 'Miguel Martins', 'kljdflkjsldfj', '916069401', 'miguelmartins17@hotmail.com'),
(11, 'Miguel Martins', 'kljdflkjsldfj', '916069401', 'miguelmartins17@hotmail.com'),
(12, 'Miguel Martins', 'kljdflkjsldfj', '916069401', 'miguelmartins17@hotmail.com'),
(13, 'Miguel Martins', 'kljdflkjsldfj', '916069401', 'miguelmartins17@hotmail.com'),
(14, 'Miguel Martins', 'kljdflkjsldfj', '916069401', 'miguelmartins17@hotmail.com'),
(15, 'Miguel Martins', 'kljdflkjsldfj', '916069401', 'miguelmartins17@hotmail.com'),
(16, 'Miguel Martins', 'kljdflkjsldfj', '916069401', 'miguelmartins17@hotmail.com'),
(17, 'Miguel Martins', 'kljdflkjsldfj', '916069401', 'miguelmartins17@hotmail.com'),
(18, 'Miguel Martins', 'ksjdhfskjdfh', '916069401', 'miguelmartins17@hotmail.com'),
(19, 'Miguel Martins', 'ksjdhfskjdfh', '916069401', 'miguelmartins17@hotmail.com'),
(20, 'Miguel Martins', 'ksjdhfskjdfh', '916069401', 'miguelmartins17@hotmail.com'),
(21, 'Miguel Martins', 'ksjdhfskjdfh', '916069401', 'miguelmartins17@hotmail.com'),
(22, 'DownD .D', 'kljdflkjsldfj', '960319939', 'downnnd@gmail.com'),
(23, 'DownD .D', 'kljdflkjsldfj', '960319939', 'downnnd@gmail.com'),
(24, 'DownD .D', 'kljdflkjsldfj', '960319939', 'downnnd@gmail.com'),
(25, 'DownD .D', 'kljdflkjsldfj', '960319939', 'downnnd@gmail.com'),
(26, 'DownD .D', 'kljdflkjsldfj', '960319939', 'downnnd@gmail.com'),
(27, 'DownD .D', 'kljdflkjsldfj', '960319939', 'downnnd@gmail.com'),
(28, 'DownD .D', 'kljdflkjsldfj', '960319939', 'downnnd@gmail.com'),
(29, 'DownD .D', 'kljdflkjsldfj', '960319939', 'downnnd@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `espaco`
--

CREATE TABLE `espaco` (
  `idespaco` int NOT NULL,
  `nome` varchar(255) NOT NULL,
  `campus_idCampus` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `espaco`
--

INSERT INTO `espaco` (`idespaco`, `nome`, `campus_idCampus`) VALUES
(4, 'ssdf', 22),
(5, 'dsfsdf', 22);

-- --------------------------------------------------------

--
-- Table structure for table `horario`
--

CREATE TABLE `horario` (
  `hora` time NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `horario`
--

INSERT INTO `horario` (`hora`) VALUES
('11:34:22'),
('30:41:25');

-- --------------------------------------------------------

--
-- Table structure for table `horario_has_dia`
--

CREATE TABLE `horario_has_dia` (
  `horario_hora` time NOT NULL,
  `Dia_dia` date NOT NULL,
  `id_dia_hora` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `horario_has_dia`
--

INSERT INTO `horario_has_dia` (`horario_hora`, `Dia_dia`, `id_dia_hora`) VALUES
('11:34:22', '2020-03-17', 2);

-- --------------------------------------------------------

--
-- Table structure for table `idioma`
--

CREATE TABLE `idioma` (
  `nome` varchar(255) NOT NULL,
  `sigla` varchar(45) NOT NULL,
  `Administrador_Utilizador_idutilizador` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inscricao`
--

CREATE TABLE `inscricao` (
  `idinscricao` int NOT NULL,
  `ano` year NOT NULL,
  `local` varchar(255) NOT NULL,
  `areacientifica` varchar(255) NOT NULL,
  `transporte` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `inscricao`
--

INSERT INTO `inscricao` (`idinscricao`, `ano`, `local`, `areacientifica`, `transporte`) VALUES
(1, 2010, '10', 'ciencias', 1),
(2, 2010, '10', 'ciencias', 1),
(3, 2010, '10', 'ciencias', 1),
(4, 2010, '10', 'ciencias', 1),
(5, 2010, '10', 'ciencias', 1),
(6, 2010, '10', 'ciencias', 0),
(7, 2010, '10', 'ciencias', 0),
(8, 2010, '10', 'ciencias', 0),
(9, 2010, '10', 'ciencias', 0),
(10, 2010, '10', 'ciencias', 0),
(11, 2010, '10', 'ciencias', 0),
(12, 2010, '10', 'ciencias', 0),
(13, 2010, '10', 'ciencias', 1),
(14, 2010, '10', 'ciencias', 1),
(15, 2012, '1', 'klsjdlfksdf', 1),
(16, 2012, '1', 'Ciencias', 1),
(17, 2012, '1', 'Ciencias', 1),
(18, 2012, '1', 'Ciencias', 1),
(19, 2012, 'slkdfslkdfj', 'Ciencias', 1),
(20, 2012, 'slkdfslkdfj', 'Ciencias', 1),
(21, 2012, 'slkdfslkdfj', 'Ciencias', 1),
(22, 2012, 'slkdfslkdfj', 'Ciencias', 1),
(23, 2012, 'slkdfslkdfj', 'Ciencias', 1),
(24, 2012, 'slkdfslkdfj', 'Ciencias', 1),
(25, 2012, 'slkdfslkdfj', 'Ciencias', 1),
(26, 2012, 'slkdfslkdfj', 'Ciencias', 1);

-- --------------------------------------------------------

--
-- Table structure for table `inscricao_coletiva`
--

CREATE TABLE `inscricao_coletiva` (
  `nresponsaveis` int NOT NULL,
  `turma` char(1) NOT NULL,
  `Participante_Utilizador_idutilizador` int NOT NULL,
  `escola_idescola` int NOT NULL,
  `nparticipantes` int NOT NULL DEFAULT '1',
  `inscricao_idinscricao` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `inscricao_coletiva`
--

INSERT INTO `inscricao_coletiva` (`nresponsaveis`, `turma`, `Participante_Utilizador_idutilizador`, `escola_idescola`, `nparticipantes`, `inscricao_idinscricao`) VALUES
(2, 'A', 2, 13, 12, 10),
(2, 'A', 2, 14, 12, 11),
(2, 'A', 2, 15, 12, 12),
(2, 'A', 2, 16, 10, 13),
(2, 'A', 2, 17, 10, 14),
(3, 'A', 2, 18, 11, 15),
(3, 'a', 2, 19, 1, 16),
(3, 'a', 2, 20, 1, 17),
(3, 'a', 2, 21, 1, 18),
(1, 'A', 2, 22, 2, 19),
(1, 'A', 2, 23, 2, 20),
(1, 'A', 2, 24, 2, 21),
(1, 'A', 2, 25, 2, 22),
(1, 'A', 2, 26, 2, 23),
(1, 'A', 2, 27, 2, 24),
(1, 'A', 2, 28, 2, 25),
(1, 'A', 2, 29, 2, 26);

-- --------------------------------------------------------

--
-- Table structure for table `inscricao_has_prato`
--

CREATE TABLE `inscricao_has_prato` (
  `inscricao_idinscricao` int NOT NULL,
  `Prato_idPrato` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `inscricao_has_prato`
--

INSERT INTO `inscricao_has_prato` (`inscricao_idinscricao`, `Prato_idPrato`) VALUES
(20, 41),
(20, 42),
(20, 43),
(21, 44),
(21, 45),
(21, 46),
(22, 47),
(22, 48),
(22, 49),
(23, 50),
(23, 51),
(23, 52),
(24, 53),
(24, 54),
(24, 55),
(25, 56),
(25, 57),
(25, 58),
(26, 59),
(26, 60),
(26, 61);

-- --------------------------------------------------------

--
-- Table structure for table `inscricao_has_sessao`
--

CREATE TABLE `inscricao_has_sessao` (
  `id_IHS` int NOT NULL,
  `inscricao_idinscricao` int NOT NULL,
  `sessao_idsessao` int NOT NULL,
  `inscritos` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `inscricao_individual`
--

CREATE TABLE `inscricao_individual` (
  `nracompanhades` int(10) UNSIGNED ZEROFILL NOT NULL,
  `Participante_Utilizador_idutilizador` int NOT NULL,
  `inscricao_idinscricao` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `material`
--

CREATE TABLE `material` (
  `idMaterial` int NOT NULL,
  `descricao` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `idMenu` int NOT NULL,
  `precoAluno` float NOT NULL,
  `PrecoProfessor` float NOT NULL,
  `tipo` varchar(45) NOT NULL,
  `menu` varchar(45) NOT NULL,
  `Campus_idCampus` int NOT NULL,
  `horario_has_dia_id_dia_hora` int NOT NULL,
  `nralmoçosdisponiveis` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`idMenu`, `precoAluno`, `PrecoProfessor`, `tipo`, `menu`, `Campus_idCampus`, `horario_has_dia_id_dia_hora`, `nralmoçosdisponiveis`) VALUES
(5, 12, 123, 'Carne', '', 22, 2, 100),
(6, 123, 12, '123', '123', 21, 2, 123),
(7, 123, 12, 'Vegan', '123', 22, 2, 2);

-- --------------------------------------------------------

--
-- Table structure for table `notificacao`
--

CREATE TABLE `notificacao` (
  `id` int NOT NULL,
  `descricao` varchar(255) NOT NULL,
  `criadoem` datetime(6) NOT NULL,
  `idutilizadorenvia` int NOT NULL,
  `utilizadorrecebe` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `paragem`
--

CREATE TABLE `paragem` (
  `paragem` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `paragem`
--

INSERT INTO `paragem` (`paragem`) VALUES
('Gambelas'),
('kljdflkjsldfj'),
('Penha');

-- --------------------------------------------------------

--
-- Table structure for table `participante`
--

CREATE TABLE `participante` (
  `Utilizador_idutilizador` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `participante`
--

INSERT INTO `participante` (`Utilizador_idutilizador`) VALUES
(2);

-- --------------------------------------------------------

--
-- Table structure for table `prato`
--

CREATE TABLE `prato` (
  `idPrato` int NOT NULL,
  `nralmocos` int NOT NULL,
  `descricao` varchar(125) NOT NULL,
  `Menu_idMenu` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `prato`
--

INSERT INTO `prato` (`idPrato`, `nralmocos`, `descricao`, `Menu_idMenu`) VALUES
(41, 1, '', 6),
(42, 1, '', 5),
(43, 1, '', 7),
(44, 1, '', 6),
(45, 1, '', 5),
(46, 1, '', 7),
(47, 1, '', 6),
(48, 1, '', 5),
(49, 1, '', 7),
(50, 1, '', 6),
(51, 1, '', 5),
(52, 1, '', 7),
(53, 1, '', 6),
(54, 1, '', 5),
(55, 1, '', 7),
(56, 1, '', 6),
(57, 1, '', 5),
(58, 1, '', 7),
(59, 1, '', 6),
(60, 1, '', 5),
(61, 1, '', 7);

-- --------------------------------------------------------

--
-- Table structure for table `professor_universitario`
--

CREATE TABLE `professor_universitario` (
  `Utilizador_idutilizador` int NOT NULL,
  `departamento_idDepartamento` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `professor_universitario`
--

INSERT INTO `professor_universitario` (`Utilizador_idutilizador`, `departamento_idDepartamento`) VALUES
(2, 4),
(1, 5);

-- --------------------------------------------------------

--
-- Table structure for table `responsaveis`
--

CREATE TABLE `responsaveis` (
  `idresponsavel` int NOT NULL,
  `nome` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `telefone` varchar(45) NOT NULL,
  `idInscricao` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `responsaveis`
--

INSERT INTO `responsaveis` (`idresponsavel`, `nome`, `email`, `telefone`, `idInscricao`) VALUES
(1, 'Pedro', 'dsklfslkdfj@gmail.com', '', 18),
(2, 'klsdjfldskf', 'pedro@gmail.com', '', 18),
(3, 'DownD .D', 'downnnd@gmail.com', '', 18);

-- --------------------------------------------------------

--
-- Table structure for table `sala`
--

CREATE TABLE `sala` (
  `edificio` varchar(45) NOT NULL,
  `andar` varchar(45) NOT NULL,
  `gabinete` varchar(45) DEFAULT NULL,
  `espaco_idespaco` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `sessao`
--

CREATE TABLE `sessao` (
  `idsessao` int NOT NULL,
  `nrinscritos` int NOT NULL DEFAULT '0',
  `vagas` int NOT NULL DEFAULT '0',
  `Atividade_idAtividade` int NOT NULL,
  `horario_has_dia_id_dia_hora` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `sessao`
--

INSERT INTO `sessao` (`idsessao`, `nrinscritos`, `vagas`, `Atividade_idAtividade`, `horario_has_dia_id_dia_hora`) VALUES
(14, 1, 21, 3, 2),
(15, 12, 12, 3, 2);

-- --------------------------------------------------------

--
-- Table structure for table `sessao_has_horario_has_dia`
--

CREATE TABLE `sessao_has_horario_has_dia` (
  `sessao_idsessao` int NOT NULL,
  `horario_has_dia_id_dia_hora` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tarefa`
--

CREATE TABLE `tarefa` (
  `idtarefa` int NOT NULL,
  `nome` varchar(255) NOT NULL,
  `concluida` tinyint NOT NULL,
  `Coordenador_Utilizador_idutilizador` int NOT NULL,
  `colaborador_Utilizador_idutilizador` int NOT NULL,
  `Atividade_idAtividade` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `transporte`
--

CREATE TABLE `transporte` (
  `idtransporte` int NOT NULL,
  `capacidade` int NOT NULL,
  `identificacao` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `transporte_has_horario`
--

CREATE TABLE `transporte_has_horario` (
  `transporte_idtransporte` int DEFAULT NULL,
  `horario_has_dia_id_dia_hora` int NOT NULL,
  `nPessoas` int NOT NULL,
  `id_transporte_has_horario` int NOT NULLAUTO_INCREMENT,
  `destino` varchar(45) NOT NULL,
  `origem` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `transporte_has_inscricao`
--

CREATE TABLE `transporte_has_inscricao` (
  `inscricao_idinscricao` int NOT NULL,
  `partida` int NOT NULL,
  `chegada` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `transporte_pessoal`
--

CREATE TABLE `transporte_pessoal` (
  `transporte_idtransporte` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `transporte_universitario`
--

CREATE TABLE `transporte_universitario` (
  `capacidade` int NOT NULL,
  `transporte_idtransporte` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `unidade_organica`
--

CREATE TABLE `unidade_organica` (
  `idUO` int NOT NULL,
  `sigla` varchar(5) NOT NULL,
  `Campus_idCampus` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `unidade_organica`
--

INSERT INTO `unidade_organica` (`idUO`, `sigla`, `Campus_idCampus`) VALUES
(5, 'ASD', 21),
(6, 'DS', 22);

-- --------------------------------------------------------

--
-- Table structure for table `utilizador`
--

CREATE TABLE `utilizador` (
  `idutilizador` int NOT NULL,
  `nome` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `telefone` varchar(45) NOT NULL,
  `password` varchar(255) NOT NULL,
  `userName` varchar(255) NOT NULL,
  `validada` tinyint NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `utilizador`
--

INSERT INTO `utilizador` (`idutilizador`, `nome`, `email`, `telefone`, `password`, `userName`, `validada`) VALUES
(1, 'dsklfjsdlkfj', 'ksjdlfksjdlfjk@kjghdkfjgh.com', '987654', 'wertyuiojkwhf83ufn', 'kdsljfdfk', 1),
(2, 'jkewhrkwejhr', 'skjdfhksjdfh@gmail.vom', '09876578', 'ksdfskdjfhkjsdh', 'kjdsfhsjdkfhq', 0),
(3, 'sdfdsf', 'wersdsvsdsdv@gmaofk.smdm', '123456', 'sdfksldjfskljc', 'nada', 0);

-- --------------------------------------------------------

--
-- Table structure for table `utilizador_has_notificacao`
--

CREATE TABLE `utilizador_has_notificacao` (
  `Utilizador_idutilizador` int NOT NULL,
  `notificacao_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `administrador`
--
ALTER TABLE `administrador`
  ADD PRIMARY KEY (`Utilizador_idutilizador`);

--
-- Indexes for table `anfiteatro`
--
ALTER TABLE `anfiteatro`
  ADD PRIMARY KEY (`espaco_idespaco`),
  ADD KEY `fk_anfiteatro_espaco_id` (`espaco_idespaco`);

--
-- Indexes for table `arlivre`
--
ALTER TABLE `arlivre`
  ADD PRIMARY KEY (`espaco_idespaco`),
  ADD KEY `fk_arlivre_espaco_id` (`espaco_idespaco`);

--
-- Indexes for table `atividade`
--
ALTER TABLE `atividade`
  ADD PRIMARY KEY (`idAtividade`),
  ADD KEY `fk_Atividade_professor_universitario_id` (`professor_universitario_Utilizador_idutilizador`),
  ADD KEY `fk_Atividade_unidade_organica_id` (`unidade_organica_idUO`),
  ADD KEY `fk_Atividade_Departamento_id` (`Departamento_idDepartamento`),
  ADD KEY `fk_atividade_espaco1_idx` (`espaco_idespaco`);

--
-- Indexes for table `atividade_has_material`
--
ALTER TABLE `atividade_has_material`
  ADD PRIMARY KEY (`Atividade_idAtividade`,`Material_idMaterial`),
  ADD KEY `fk_Atividade_has_Material_Material_id` (`Material_idMaterial`),
  ADD KEY `fk_Atividade_has_Material_Atividade_id` (`Atividade_idAtividade`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `campus`
--
ALTER TABLE `campus`
  ADD PRIMARY KEY (`idCampus`),
  ADD KEY `paragem` (`paragem`);

--
-- Indexes for table `colaborador`
--
ALTER TABLE `colaborador`
  ADD PRIMARY KEY (`Utilizador_idutilizador`),
  ADD KEY `fk_colaborador_dia_aberto_id` (`dia_aberto_ano`);

--
-- Indexes for table `colaborador_has_horario`
--
ALTER TABLE `colaborador_has_horario`
  ADD KEY `fk_colaborador_has_Horario_colaborador_id` (`colaborador_Utilizador_idutilizador`),
  ADD KEY `fk_colaborador_has_horario_horario_has_dia1_idx` (`horario_has_dia_id_dia_hora`);

--
-- Indexes for table `colaborador_has_unidade_organica`
--
ALTER TABLE `colaborador_has_unidade_organica`
  ADD KEY `fk_colaborador_has_unidade_organica_unidade_organica_id` (`unidade_organica_idUO`),
  ADD KEY `fk_colaborador_has_unidade_organica_colaborador_id` (`colaborador_Utilizador_idutilizador`);

--
-- Indexes for table `coordenador`
--
ALTER TABLE `coordenador`
  ADD PRIMARY KEY (`Utilizador_idutilizador`),
  ADD KEY `fk_Coordenador_unidade_organica_id` (`unidade_organica_idUO`);

--
-- Indexes for table `coordenador_has_departamento`
--
ALTER TABLE `coordenador_has_departamento`
  ADD PRIMARY KEY (`Coordenador_Utilizador_idutilizador`,`Departamento_idDepartamento`),
  ADD KEY `fk_Coordenador_has_Departamento_Departamento_id` (`Departamento_idDepartamento`),
  ADD KEY `fk_Coordenador_has_Departamento_Coordenador_id` (`Coordenador_Utilizador_idutilizador`);

--
-- Indexes for table `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`idDepartamento`),
  ADD KEY `fk_Departamento_unidade_organica_id` (`unidade_organica_idUO`);

--
-- Indexes for table `dia`
--
ALTER TABLE `dia`
  ADD PRIMARY KEY (`dia`);

--
-- Indexes for table `dia_aberto`
--
ALTER TABLE `dia_aberto`
  ADD PRIMARY KEY (`ano`),
  ADD KEY `fk_dia_aberto_Utilizador_id` (`Utilizador_idutilizador`),
  ADD KEY `fk_dia_aberto_Administrador_id` (`Administrador_Utilizador_idutilizador`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `escola`
--
ALTER TABLE `escola`
  ADD PRIMARY KEY (`idescola`);

--
-- Indexes for table `espaco`
--
ALTER TABLE `espaco`
  ADD PRIMARY KEY (`idespaco`),
  ADD KEY `fk_espaco_campus1_idx` (`campus_idCampus`);

--
-- Indexes for table `horario`
--
ALTER TABLE `horario`
  ADD PRIMARY KEY (`hora`);

--
-- Indexes for table `horario_has_dia`
--
ALTER TABLE `horario_has_dia`
  ADD PRIMARY KEY (`id_dia_hora`),
  ADD KEY `fk_horario_has_Dia_Dia1_idx` (`Dia_dia`),
  ADD KEY `fk_horario_has_Dia_horario1_idx` (`horario_hora`);

--
-- Indexes for table `idioma`
--
ALTER TABLE `idioma`
  ADD PRIMARY KEY (`nome`),
  ADD UNIQUE KEY `sigla_UNIQUE` (`sigla`),
  ADD KEY `fk_idioma_Administrador_id` (`Administrador_Utilizador_idutilizador`);

--
-- Indexes for table `inscricao`
--
ALTER TABLE `inscricao`
  ADD PRIMARY KEY (`idinscricao`);

--
-- Indexes for table `inscricao_coletiva`
--
ALTER TABLE `inscricao_coletiva`
  ADD PRIMARY KEY (`inscricao_idinscricao`),
  ADD KEY `fk_inscricao_coletiva_Participante_id` (`Participante_Utilizador_idutilizador`),
  ADD KEY `fk_inscricao_coletiva_escola_id` (`escola_idescola`),
  ADD KEY `fk_inscricao_coletiva_inscricao_id` (`inscricao_idinscricao`);

--
-- Indexes for table `inscricao_has_prato`
--
ALTER TABLE `inscricao_has_prato`
  ADD KEY `fk_inscricao_has_Prato_Prato_id` (`Prato_idPrato`),
  ADD KEY `fk_inscricao_has_Prato_inscricao_id` (`inscricao_idinscricao`);

--
-- Indexes for table `inscricao_has_sessao`
--
ALTER TABLE `inscricao_has_sessao`
  ADD PRIMARY KEY (`id_IHS`),
  ADD KEY `fk_inscricao_has_sessao_sessao_id` (`sessao_idsessao`),
  ADD KEY `fk_inscricao_has_sessao_inscricao_id` (`inscricao_idinscricao`);

--
-- Indexes for table `inscricao_individual`
--
ALTER TABLE `inscricao_individual`
  ADD PRIMARY KEY (`inscricao_idinscricao`),
  ADD KEY `fk_inscricao_individual_Participante_id` (`Participante_Utilizador_idutilizador`),
  ADD KEY `fk_inscricao_individual_inscricao_id` (`inscricao_idinscricao`);

--
-- Indexes for table `material`
--
ALTER TABLE `material`
  ADD PRIMARY KEY (`idMaterial`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`idMenu`),
  ADD KEY `fk_Menu_Campus_id` (`Campus_idCampus`),
  ADD KEY `fk_menu_horario_has_dia1_idx` (`horario_has_dia_id_dia_hora`);

--
-- Indexes for table `notificacao`
--
ALTER TABLE `notificacao`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `paragem`
--
ALTER TABLE `paragem`
  ADD PRIMARY KEY (`paragem`);

--
-- Indexes for table `participante`
--
ALTER TABLE `participante`
  ADD PRIMARY KEY (`Utilizador_idutilizador`);

--
-- Indexes for table `prato`
--
ALTER TABLE `prato`
  ADD PRIMARY KEY (`idPrato`),
  ADD KEY `fk_Prato_Menu_id` (`Menu_idMenu`);

--
-- Indexes for table `professor_universitario`
--
ALTER TABLE `professor_universitario`
  ADD PRIMARY KEY (`Utilizador_idutilizador`),
  ADD KEY `fk_professor_universitario_departamento1_idx` (`departamento_idDepartamento`);

--
-- Indexes for table `responsaveis`
--
ALTER TABLE `responsaveis`
  ADD PRIMARY KEY (`idresponsavel`),
  ADD KEY `fk_Responsáveis_Inscricao` (`idInscricao`);

--
-- Indexes for table `sala`
--
ALTER TABLE `sala`
  ADD PRIMARY KEY (`espaco_idespaco`),
  ADD KEY `fk_sala_espaco_id` (`espaco_idespaco`);

--
-- Indexes for table `sessao`
--
ALTER TABLE `sessao`
  ADD PRIMARY KEY (`idsessao`),
  ADD KEY `fk_sessao_Atividade_id` (`Atividade_idAtividade`),
  ADD KEY `fk_sessao_horario_has_dia1_idx` (`horario_has_dia_id_dia_hora`);

--
-- Indexes for table `sessao_has_horario_has_dia`
--
ALTER TABLE `sessao_has_horario_has_dia`
  ADD KEY `fk_sessao_has_horario_has_dia_horario_has_dia1_idx` (`horario_has_dia_id_dia_hora`),
  ADD KEY `fk_sessao_has_horario_has_dia_sessao1_idx` (`sessao_idsessao`);

--
-- Indexes for table `tarefa`
--
ALTER TABLE `tarefa`
  ADD PRIMARY KEY (`idtarefa`),
  ADD KEY `fk_tarefa_Coordenador_id` (`Coordenador_Utilizador_idutilizador`),
  ADD KEY `fk_tarefa_colaborador_id` (`colaborador_Utilizador_idutilizador`),
  ADD KEY `fk_tarefa_Atividade_id` (`Atividade_idAtividade`);

--
-- Indexes for table `transporte`
--
ALTER TABLE `transporte`
  ADD PRIMARY KEY (`idtransporte`);

--
-- Indexes for table `transporte_has_horario`
--
ALTER TABLE `transporte_has_horario`
  ADD PRIMARY KEY (`id_transporte_has_horario`),
  ADD KEY `fk_transporte_has_Horario_transporte_id` (`transporte_idtransporte`),
  ADD KEY `fk_transporte_has_horario_horario_has_dia1_idx` (`horario_has_dia_id_dia_hora`),
  ADD KEY `fk_transporte_has_horario_paragem1_idx` (`destino`),
  ADD KEY `fk_transporte_has_horario_paragem2_idx` (`origem`);

--
-- Indexes for table `transporte_has_inscricao`
--
ALTER TABLE `transporte_has_inscricao`
  ADD KEY `fk_transporte_has_inscricao_inscricao_id` (`inscricao_idinscricao`),
  ADD KEY `fk_transporte_has_inscricao_transporte_has_horario1_idx` (`partida`),
  ADD KEY `fk_transporte_has_inscricao_transporte_has_horario2_idx` (`chegada`);

--
-- Indexes for table `transporte_pessoal`
--
ALTER TABLE `transporte_pessoal`
  ADD PRIMARY KEY (`transporte_idtransporte`);

--
-- Indexes for table `transporte_universitario`
--
ALTER TABLE `transporte_universitario`
  ADD PRIMARY KEY (`transporte_idtransporte`);

--
-- Indexes for table `unidade_organica`
--
ALTER TABLE `unidade_organica`
  ADD PRIMARY KEY (`idUO`),
  ADD KEY `fk_unidade_organica_Campus_id` (`Campus_idCampus`);

--
-- Indexes for table `utilizador`
--
ALTER TABLE `utilizador`
  ADD PRIMARY KEY (`idutilizador`),
  ADD UNIQUE KEY `email_UNIQUE` (`email`),
  ADD UNIQUE KEY `telefone_UNIQUE` (`telefone`);

--
-- Indexes for table `utilizador_has_notificacao`
--
ALTER TABLE `utilizador_has_notificacao`
  ADD KEY `fk_Utilizador_has_notificacao_notificacao_id` (`notificacao_id`),
  ADD KEY `fk_Utilizador_has_notificacao_Utilizador_id` (`Utilizador_idutilizador`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `atividade`
--
ALTER TABLE `atividade`
  MODIFY `idAtividade` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1329;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `campus`
--
ALTER TABLE `campus`
  MODIFY `idCampus` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `departamento`
--
ALTER TABLE `departamento`
  MODIFY `idDepartamento` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=333;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT for table `escola`
--
ALTER TABLE `escola`
  MODIFY `idescola` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `espaco`
--
ALTER TABLE `espaco`
  MODIFY `idespaco` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `inscricao`
--
ALTER TABLE `inscricao`
  MODIFY `idinscricao` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `inscricao_has_sessao`
--
ALTER TABLE `inscricao_has_sessao`
  MODIFY `id_IHS` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `material`
--
ALTER TABLE `material`
  MODIFY `idMaterial` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `menu`
--
ALTER TABLE `menu`
  MODIFY `idMenu` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `notificacao`
--
ALTER TABLE `notificacao`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `prato`
--
ALTER TABLE `prato`
  MODIFY `idPrato` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=62;

--
-- AUTO_INCREMENT for table `responsaveis`
--
ALTER TABLE `responsaveis`
  MODIFY `idresponsavel` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `sessao`
--
ALTER TABLE `sessao`
  MODIFY `idsessao` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `tarefa`
--
ALTER TABLE `tarefa`
  MODIFY `idtarefa` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transporte`
--
ALTER TABLE `transporte`
  MODIFY `idtransporte` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `transporte_universitario`
--
ALTER TABLE `transporte_universitario`
  MODIFY `transporte_idtransporte` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `unidade_organica`
--
ALTER TABLE `unidade_organica`
  MODIFY `idUO` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `utilizador`
--
ALTER TABLE `utilizador`
  MODIFY `idutilizador` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `administrador`
--
ALTER TABLE `administrador`
  ADD CONSTRAINT `fk_Administrador_Utilizador` FOREIGN KEY (`Utilizador_idutilizador`) REFERENCES `utilizador` (`idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `anfiteatro`
--
ALTER TABLE `anfiteatro`
  ADD CONSTRAINT `fk_anfiteatro_espaco` FOREIGN KEY (`espaco_idespaco`) REFERENCES `espaco` (`idespaco`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `arlivre`
--
ALTER TABLE `arlivre`
  ADD CONSTRAINT `fk_arlivre_espaco` FOREIGN KEY (`espaco_idespaco`) REFERENCES `espaco` (`idespaco`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `atividade`
--
ALTER TABLE `atividade`
  ADD CONSTRAINT `fk_Atividade_Departamento` FOREIGN KEY (`Departamento_idDepartamento`) REFERENCES `departamento` (`idDepartamento`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_atividade_espaco` FOREIGN KEY (`espaco_idespaco`) REFERENCES `espaco` (`idespaco`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Atividade_professor_universitario` FOREIGN KEY (`professor_universitario_Utilizador_idutilizador`) REFERENCES `professor_universitario` (`Utilizador_idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Atividade_unidade_organica` FOREIGN KEY (`unidade_organica_idUO`) REFERENCES `unidade_organica` (`idUO`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `atividade_has_material`
--
ALTER TABLE `atividade_has_material`
  ADD CONSTRAINT `fk_Atividade_has_Material_Atividade` FOREIGN KEY (`Atividade_idAtividade`) REFERENCES `atividade` (`idAtividade`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Atividade_has_Material_Material` FOREIGN KEY (`Material_idMaterial`) REFERENCES `material` (`idMaterial`) ON DELETE CASCADE;

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `campus`
--
ALTER TABLE `campus`
  ADD CONSTRAINT `campus_ibfk_1` FOREIGN KEY (`paragem`) REFERENCES `paragem` (`paragem`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `colaborador`
--
ALTER TABLE `colaborador`
  ADD CONSTRAINT `fk_colaborador_dia_aberto` FOREIGN KEY (`dia_aberto_ano`) REFERENCES `dia_aberto` (`ano`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_colaborador_Utilizador` FOREIGN KEY (`Utilizador_idutilizador`) REFERENCES `utilizador` (`idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `colaborador_has_horario`
--
ALTER TABLE `colaborador_has_horario`
  ADD CONSTRAINT `fk_colaborador_has_Horario_colaborador` FOREIGN KEY (`colaborador_Utilizador_idutilizador`) REFERENCES `colaborador` (`Utilizador_idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_colaborador_has_horario_horario_has_dia1` FOREIGN KEY (`horario_has_dia_id_dia_hora`) REFERENCES `horario_has_dia` (`id_dia_hora`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `colaborador_has_unidade_organica`
--
ALTER TABLE `colaborador_has_unidade_organica`
  ADD CONSTRAINT `fk_colaborador_has_unidade_organica_colaborador` FOREIGN KEY (`colaborador_Utilizador_idutilizador`) REFERENCES `colaborador` (`Utilizador_idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_colaborador_has_unidade_organica_unidade_Organica` FOREIGN KEY (`unidade_organica_idUO`) REFERENCES `unidade_organica` (`idUO`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `coordenador`
--
ALTER TABLE `coordenador`
  ADD CONSTRAINT `fk_Coordenador_unidade_organica` FOREIGN KEY (`unidade_organica_idUO`) REFERENCES `unidade_organica` (`idUO`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Coordenador_Utilizador` FOREIGN KEY (`Utilizador_idutilizador`) REFERENCES `utilizador` (`idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `coordenador_has_departamento`
--
ALTER TABLE `coordenador_has_departamento`
  ADD CONSTRAINT `fk_Coordenador_has_Departamento_Coordenador` FOREIGN KEY (`Coordenador_Utilizador_idutilizador`) REFERENCES `coordenador` (`Utilizador_idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Coordenador_has_Departamento_Departamento` FOREIGN KEY (`Departamento_idDepartamento`) REFERENCES `departamento` (`idDepartamento`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `departamento`
--
ALTER TABLE `departamento`
  ADD CONSTRAINT `fk_Departamento_unidade_organica` FOREIGN KEY (`unidade_organica_idUO`) REFERENCES `unidade_organica` (`idUO`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `dia_aberto`
--
ALTER TABLE `dia_aberto`
  ADD CONSTRAINT `fk_dia_aberto_Administrador` FOREIGN KEY (`Administrador_Utilizador_idutilizador`) REFERENCES `administrador` (`Utilizador_idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_dia_aberto_Utilizador` FOREIGN KEY (`Utilizador_idutilizador`) REFERENCES `utilizador` (`idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `espaco`
--
ALTER TABLE `espaco`
  ADD CONSTRAINT `fk_espaco_campus1` FOREIGN KEY (`campus_idCampus`) REFERENCES `campus` (`idCampus`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `horario_has_dia`
--
ALTER TABLE `horario_has_dia`
  ADD CONSTRAINT `fk_horario_has_Dia_Dia` FOREIGN KEY (`Dia_dia`) REFERENCES `dia` (`dia`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_horario_has_Dia_horario` FOREIGN KEY (`horario_hora`) REFERENCES `horario` (`hora`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `idioma`
--
ALTER TABLE `idioma`
  ADD CONSTRAINT `fk_idioma_Administrador` FOREIGN KEY (`Administrador_Utilizador_idutilizador`) REFERENCES `administrador` (`Utilizador_idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `inscricao_coletiva`
--
ALTER TABLE `inscricao_coletiva`
  ADD CONSTRAINT `fk_inscricao_coletiva_escola` FOREIGN KEY (`escola_idescola`) REFERENCES `escola` (`idescola`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_inscricao_coletiva_inscricao` FOREIGN KEY (`inscricao_idinscricao`) REFERENCES `inscricao` (`idinscricao`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_inscricao_coletiva_Participante` FOREIGN KEY (`Participante_Utilizador_idutilizador`) REFERENCES `participante` (`Utilizador_idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `inscricao_has_prato`
--
ALTER TABLE `inscricao_has_prato`
  ADD CONSTRAINT `fk_inscricao_has_Prato_inscricao` FOREIGN KEY (`inscricao_idinscricao`) REFERENCES `inscricao` (`idinscricao`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_inscricao_has_Prato_Prato` FOREIGN KEY (`Prato_idPrato`) REFERENCES `prato` (`idPrato`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `inscricao_has_sessao`
--
ALTER TABLE `inscricao_has_sessao`
  ADD CONSTRAINT `fk_inscricao_has_sessao_inscricao` FOREIGN KEY (`inscricao_idinscricao`) REFERENCES `inscricao` (`idinscricao`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_inscricao_has_sessao_sessao` FOREIGN KEY (`sessao_idsessao`) REFERENCES `sessao` (`idsessao`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `inscricao_individual`
--
ALTER TABLE `inscricao_individual`
  ADD CONSTRAINT `fk_inscricao_individual_inscricao` FOREIGN KEY (`inscricao_idinscricao`) REFERENCES `inscricao` (`idinscricao`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_inscricao_individual_Participante` FOREIGN KEY (`Participante_Utilizador_idutilizador`) REFERENCES `participante` (`Utilizador_idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `menu`
--
ALTER TABLE `menu`
  ADD CONSTRAINT `fk_Menu_Campus` FOREIGN KEY (`Campus_idCampus`) REFERENCES `campus` (`idCampus`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_menu_horario_has_dia1` FOREIGN KEY (`horario_has_dia_id_dia_hora`) REFERENCES `horario_has_dia` (`id_dia_hora`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `participante`
--
ALTER TABLE `participante`
  ADD CONSTRAINT `fk_Participante_Utilizador` FOREIGN KEY (`Utilizador_idutilizador`) REFERENCES `utilizador` (`idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `prato`
--
ALTER TABLE `prato`
  ADD CONSTRAINT `fk_Prato_Menu` FOREIGN KEY (`Menu_idMenu`) REFERENCES `menu` (`idMenu`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `professor_universitario`
--
ALTER TABLE `professor_universitario`
  ADD CONSTRAINT `fk_professor_universitario_departamento1` FOREIGN KEY (`departamento_idDepartamento`) REFERENCES `departamento` (`idDepartamento`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_professor_universitario_Utilizador` FOREIGN KEY (`Utilizador_idutilizador`) REFERENCES `utilizador` (`idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `responsaveis`
--
ALTER TABLE `responsaveis`
  ADD CONSTRAINT `fk_Responsáveis_Inscricao` FOREIGN KEY (`idInscricao`) REFERENCES `inscricao` (`idinscricao`);

--
-- Constraints for table `sala`
--
ALTER TABLE `sala`
  ADD CONSTRAINT `fk_sala_espaco` FOREIGN KEY (`espaco_idespaco`) REFERENCES `espaco` (`idespaco`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `sessao`
--
ALTER TABLE `sessao`
  ADD CONSTRAINT `fk_sessao_Atividade` FOREIGN KEY (`Atividade_idAtividade`) REFERENCES `atividade` (`idAtividade`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_sessao_horario_has_dia1` FOREIGN KEY (`horario_has_dia_id_dia_hora`) REFERENCES `horario_has_dia` (`id_dia_hora`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `sessao_has_horario_has_dia`
--
ALTER TABLE `sessao_has_horario_has_dia`
  ADD CONSTRAINT `fk_sessao_has_horario_has_dia_horario_has_dia1` FOREIGN KEY (`horario_has_dia_id_dia_hora`) REFERENCES `horario_has_dia` (`id_dia_hora`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_sessao_has_horario_has_dia_sessao1` FOREIGN KEY (`sessao_idsessao`) REFERENCES `sessao` (`idsessao`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `tarefa`
--
ALTER TABLE `tarefa`
  ADD CONSTRAINT `fk_tarefa_Atividade` FOREIGN KEY (`Atividade_idAtividade`) REFERENCES `atividade` (`idAtividade`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_tarefa_colaborador` FOREIGN KEY (`colaborador_Utilizador_idutilizador`) REFERENCES `colaborador` (`Utilizador_idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_tarefa_Coordenador` FOREIGN KEY (`Coordenador_Utilizador_idutilizador`) REFERENCES `coordenador` (`Utilizador_idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `transporte_has_horario`
--
ALTER TABLE `transporte_has_horario`
  ADD CONSTRAINT `fk_transporte_has_horario_horario_has_dia1` FOREIGN KEY (`horario_has_dia_id_dia_hora`) REFERENCES `horario_has_dia` (`id_dia_hora`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_transporte_has_horario_paragem1` FOREIGN KEY (`destino`) REFERENCES `paragem` (`paragem`),
  ADD CONSTRAINT `fk_transporte_has_horario_paragem2` FOREIGN KEY (`origem`) REFERENCES `paragem` (`paragem`),
  ADD CONSTRAINT `fk_transporte_has_Horario_transporte` FOREIGN KEY (`transporte_idtransporte`) REFERENCES `transporte` (`idtransporte`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `transporte_has_inscricao`
--
ALTER TABLE `transporte_has_inscricao`
  ADD CONSTRAINT `fk_transporte_has_inscricao_inscricao` FOREIGN KEY (`inscricao_idinscricao`) REFERENCES `inscricao` (`idinscricao`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_transporte_has_inscricao_transporte_has_horario1` FOREIGN KEY (`partida`) REFERENCES `transporte_has_horario` (`id_transporte_has_horario`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_transporte_has_inscricao_transporte_has_horario2` FOREIGN KEY (`chegada`) REFERENCES `transporte_has_horario` (`id_transporte_has_horario`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `transporte_pessoal`
--
ALTER TABLE `transporte_pessoal`
  ADD CONSTRAINT `fk_Transporte_pessoal_transporte` FOREIGN KEY (`transporte_idtransporte`) REFERENCES `transporte` (`idtransporte`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `transporte_universitario`
--
ALTER TABLE `transporte_universitario`
  ADD CONSTRAINT `fk_transporte Universitario_transporte` FOREIGN KEY (`transporte_idtransporte`) REFERENCES `transporte` (`idtransporte`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `unidade_organica`
--
ALTER TABLE `unidade_organica`
  ADD CONSTRAINT `fk_unidade_organica_Campus` FOREIGN KEY (`Campus_idCampus`) REFERENCES `campus` (`idCampus`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `utilizador_has_notificacao`
--
ALTER TABLE `utilizador_has_notificacao`
  ADD CONSTRAINT `fk_Utilizador_has_notificacao_notificacao` FOREIGN KEY (`notificacao_id`) REFERENCES `notificacao` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_Utilizador_has_notificacao_Utilizador` FOREIGN KEY (`Utilizador_idutilizador`) REFERENCES `utilizador` (`idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
