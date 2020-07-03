-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 02, 2020 at 09:34 PM
-- Server version: 8.0.20-0ubuntu0.20.04.1
-- PHP Version: 7.4.3

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

--
-- Dumping data for table `administrador`
--

INSERT INTO `administrador` (`Utilizador_idutilizador`) VALUES
(1002);

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
  `espaco_idespaco` int DEFAULT NULL,
  `tematica` varchar(250) DEFAULT NULL,
  `nrColaborador` varchar(45) DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `atividade`
--

INSERT INTO `atividade` (`idAtividade`, `titulo`, `capacidade`, `publico_alvo`, `duracao`, `descricao`, `validada`, `professor_universitario_Utilizador_idutilizador`, `unidade_organica_idUO`, `Departamento_idDepartamento`, `espaco_idespaco`, `tematica`, `nrColaborador`) VALUES
(6, 'Brincar Com Números', 20, 'Estudantes', 30, 'brincadeirinha', 1, 1005, 9, 5, 8, 'tema', '2'),
(7, 'Matemática com o Rafa', 20, 'lei estudantes', 30, 'uma porcaria', 1, 1005, 9, 6, 8, 'chumbar', '3');

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
  `nome` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `campus`
--

INSERT INTO `campus` (`idCampus`, `nome`) VALUES
(4, 'Gambelas'),
(5, 'Penha');

-- --------------------------------------------------------

--
-- Table structure for table `colaborador`
--

CREATE TABLE `colaborador` (
  `Utilizador_idutilizador` int NOT NULL,
  `curso_idcurso` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `colaborador`
--

INSERT INTO `colaborador` (`Utilizador_idutilizador`, `curso_idcurso`) VALUES
(1010, 6),
(1011, 6),
(1012, 6);

-- --------------------------------------------------------

--
-- Table structure for table `colaborador_has_horario`
--

CREATE TABLE `colaborador_has_horario` (
  `colaborador_Utilizador_idutilizador` int NOT NULL,
  `horario_has_dia_id_dia_hora` int NOT NULL,
  `colaborador_has_horario_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `colaborador_has_unidade_organica`
--

CREATE TABLE `colaborador_has_unidade_organica` (
  `colaborador_Utilizador_idutilizador` int NOT NULL,
  `unidade_organica_idUO` int NOT NULL,
  `colaborador_has_unidade_organica_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `coordenador`
--

CREATE TABLE `coordenador` (
  `Utilizador_idutilizador` int NOT NULL,
  `unidade_organica_idUO` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `coordenador`
--

INSERT INTO `coordenador` (`Utilizador_idutilizador`, `unidade_organica_idUO`) VALUES
(1004, 9);

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
-- Table structure for table `curso`
--

CREATE TABLE `curso` (
  `idcurso` int NOT NULL,
  `unidade_organica_idUO` int NOT NULL,
  `nome` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `curso`
--

INSERT INTO `curso` (`idcurso`, `unidade_organica_idUO`, `nome`) VALUES
(6, 9, 'LEI'),
(7, 11, 'Gestão');

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
(5, 'DEEI', 9),
(6, 'DAH', 10);

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
('2020-07-27'),
('2020-07-28'),
('2020-07-29');

-- --------------------------------------------------------

--
-- Table structure for table `dia_aberto`
--

CREATE TABLE `dia_aberto` (
  `ano` year NOT NULL,
  `descricao` varchar(120) DEFAULT NULL,
  `emailDiaAberto` varchar(120) NOT NULL,
  `enderecoPaginaWeb` varchar(60) NOT NULL,
  `dataDiaAbertoInicio` date NOT NULL,
  `dataDiaAbertofim` date NOT NULL,
  `datainscricaonasatividadesinicio` date NOT NULL,
  `datainscricaonasatividadesfim` date NOT NULL,
  `dataPropostaAtividadeInicio` date NOT NULL,
  `dataPropostaAtividadesFim` date NOT NULL,
  `preco_almoco_estudante` float NOT NULL DEFAULT '0',
  `preco_almoco_professor` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `dia_aberto`
--

INSERT INTO `dia_aberto` (`ano`, `descricao`, `emailDiaAberto`, `enderecoPaginaWeb`, `dataDiaAbertoInicio`, `dataDiaAbertofim`, `datainscricaonasatividadesinicio`, `datainscricaonasatividadesfim`, `dataPropostaAtividadeInicio`, `dataPropostaAtividadesFim`, `preco_almoco_estudante`, `preco_almoco_professor`) VALUES
(2020, 'é agora mesmo', 'guilhas24@gmail.com', 'http://www.viviana.com', '2020-07-27', '2020-07-29', '2020-07-01', '2020-07-04', '2020-07-13', '2020-07-16', 2.8, 4.2);

-- --------------------------------------------------------

--
-- Table structure for table `disponibilidade`
--

CREATE TABLE `disponibilidade` (
  `colaborador_Utilizador_idutilizador` int NOT NULL,
  `dia_dia` date NOT NULL,
  `horario_hora` time NOT NULL,
  `horario_hora1` time NOT NULL,
  `tipo_de_tarefa` varchar(45) NOT NULL,
  `disponibilidade_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `disponibilidade`
--

INSERT INTO `disponibilidade` (`colaborador_Utilizador_idutilizador`, `dia_dia`, `horario_hora`, `horario_hora1`, `tipo_de_tarefa`, `disponibilidade_id`) VALUES
(1010, '2020-07-27', '08:00:00', '23:00:00', 'Sem preferência', 3),
(1011, '2020-07-27', '08:00:00', '23:00:00', 'Sem preferência', 4);

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
(3, 'Escola Secundária Tavira', 'Tavira', '922345678', 'tavira@tavira.com'),
(4, 'Escola Faro', 'Faro', '978878878', 'faro@faro.com'),
(5, 'Escola do Alentejo', 'Alentejo', '987234596', 'alentejo@alentejo.com');

-- --------------------------------------------------------

--
-- Table structure for table `espaco`
--

CREATE TABLE `espaco` (
  `idespaco` int NOT NULL,
  `nome` varchar(255) NOT NULL,
  `campus_idCampus` int NOT NULL,
  `img` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `espaco`
--

INSERT INTO `espaco` (`idespaco`, `nome`, `campus_idCampus`, `img`) VALUES
(7, 'Sala 1.21', 5, 'images/QspcR_ye_400x400.jpg'),
(8, 'A', 4, 'images/QspcR_ye_400x400_jzTYYPT.jpg');

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
('08:00:00'),
('08:15:00'),
('08:30:00'),
('08:45:00'),
('09:00:00'),
('09:15:00'),
('09:30:00'),
('09:45:00'),
('10:00:00'),
('10:30:00'),
('11:00:00'),
('11:30:00'),
('12:00:00'),
('12:30:00'),
('13:00:00'),
('13:30:00'),
('14:00:00'),
('14:30:00'),
('15:00:00'),
('15:30:00'),
('16:00:00'),
('16:30:00'),
('17:00:00'),
('17:30:00'),
('18:00:00'),
('18:30:00'),
('19:00:00'),
('19:30:00'),
('20:00:00'),
('20:30:00'),
('21:00:00'),
('21:30:00'),
('22:00:00'),
('22:30:00'),
('23:00:00');

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
('09:30:00', '2020-07-27', 5),
('10:00:00', '2020-07-27', 6),
('10:30:00', '2020-07-27', 7),
('11:00:00', '2020-07-27', 8),
('11:30:00', '2020-07-27', 9),
('12:00:00', '2020-07-27', 10),
('12:30:00', '2020-07-27', 11),
('13:00:00', '2020-07-27', 12),
('13:30:00', '2020-07-27', 13),
('14:00:00', '2020-07-27', 14),
('14:30:00', '2020-07-27', 15),
('15:00:00', '2020-07-27', 16),
('15:30:00', '2020-07-27', 17),
('16:00:00', '2020-07-27', 18),
('16:30:00', '2020-07-27', 19),
('17:00:00', '2020-07-27', 20),
('17:30:00', '2020-07-27', 21),
('18:00:00', '2020-07-27', 22),
('18:30:00', '2020-07-27', 23),
('19:00:00', '2020-07-27', 24),
('19:30:00', '2020-07-27', 25),
('20:00:00', '2020-07-27', 26),
('20:30:00', '2020-07-27', 27),
('21:00:00', '2020-07-27', 28),
('21:30:00', '2020-07-27', 29),
('22:00:00', '2020-07-27', 30),
('22:30:00', '2020-07-27', 31),
('23:00:00', '2020-07-27', 32),
('09:30:00', '2020-07-28', 33),
('10:00:00', '2020-07-28', 34),
('10:30:00', '2020-07-28', 35),
('11:00:00', '2020-07-28', 36),
('11:30:00', '2020-07-28', 37),
('12:00:00', '2020-07-28', 38),
('12:30:00', '2020-07-28', 39),
('13:00:00', '2020-07-28', 40),
('13:30:00', '2020-07-28', 41),
('14:00:00', '2020-07-28', 42),
('14:30:00', '2020-07-28', 43),
('15:00:00', '2020-07-28', 44),
('15:30:00', '2020-07-28', 45),
('16:00:00', '2020-07-28', 46),
('16:30:00', '2020-07-28', 47),
('17:00:00', '2020-07-28', 48),
('17:30:00', '2020-07-28', 49),
('18:00:00', '2020-07-28', 50),
('18:30:00', '2020-07-28', 51),
('19:00:00', '2020-07-28', 52),
('19:30:00', '2020-07-28', 53),
('20:00:00', '2020-07-28', 54),
('20:30:00', '2020-07-28', 55),
('21:00:00', '2020-07-28', 56),
('21:30:00', '2020-07-28', 57),
('22:00:00', '2020-07-28', 58),
('22:30:00', '2020-07-28', 59),
('23:00:00', '2020-07-28', 60),
('09:30:00', '2020-07-29', 61),
('10:00:00', '2020-07-29', 62),
('10:30:00', '2020-07-29', 63),
('11:00:00', '2020-07-29', 64),
('11:30:00', '2020-07-29', 65),
('12:00:00', '2020-07-29', 66),
('12:30:00', '2020-07-29', 67),
('13:00:00', '2020-07-29', 68),
('13:30:00', '2020-07-29', 69),
('14:00:00', '2020-07-29', 70),
('14:30:00', '2020-07-29', 71),
('15:00:00', '2020-07-29', 72),
('15:30:00', '2020-07-29', 73),
('16:00:00', '2020-07-29', 74),
('16:30:00', '2020-07-29', 75),
('17:00:00', '2020-07-29', 76),
('17:30:00', '2020-07-29', 77),
('18:00:00', '2020-07-29', 78),
('18:30:00', '2020-07-29', 79),
('19:00:00', '2020-07-29', 80),
('19:30:00', '2020-07-29', 81),
('20:00:00', '2020-07-29', 82),
('20:30:00', '2020-07-29', 83),
('21:00:00', '2020-07-29', 84),
('21:30:00', '2020-07-29', 85),
('22:00:00', '2020-07-29', 86),
('22:30:00', '2020-07-29', 87),
('23:00:00', '2020-07-29', 88),
('10:30:00', '2020-07-27', 89),
('08:00:00', '2020-07-27', 90),
('08:15:00', '2020-07-27', 91),
('08:30:00', '2020-07-27', 92),
('08:45:00', '2020-07-27', 93),
('09:00:00', '2020-07-27', 94),
('09:15:00', '2020-07-27', 95),
('09:45:00', '2020-07-27', 96),
('08:00:00', '2020-07-28', 97),
('08:15:00', '2020-07-28', 98),
('08:30:00', '2020-07-28', 99),
('08:45:00', '2020-07-28', 100),
('09:00:00', '2020-07-28', 101),
('09:15:00', '2020-07-28', 102),
('09:45:00', '2020-07-28', 103),
('08:00:00', '2020-07-29', 104),
('08:15:00', '2020-07-29', 105),
('08:30:00', '2020-07-29', 106),
('08:45:00', '2020-07-29', 107),
('09:00:00', '2020-07-29', 108),
('09:15:00', '2020-07-29', 109),
('09:45:00', '2020-07-29', 110);

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
  `ano` int NOT NULL,
  `local` varchar(255) NOT NULL,
  `areacientifica` varchar(255) NOT NULL,
  `transporte` tinyint(1) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `inscricao`
--

INSERT INTO `inscricao` (`idinscricao`, `ano`, `local`, `areacientifica`, `transporte`) VALUES
(3, 12, 'Tavira', 'Artes', 0),
(4, 12, 'Faro', 'Ciências', 0),
(5, 12, 'Alentejo', 'Ciências', 0);

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
(1, 'B', 1007, 3, 14, 3),
(1, 'A', 1008, 4, 13, 4),
(2, 'B', 1009, 5, 10, 5);

-- --------------------------------------------------------

--
-- Table structure for table `inscricao_has_prato`
--

CREATE TABLE `inscricao_has_prato` (
  `inscricao_idinscricao` int NOT NULL,
  `Prato_idPrato` int NOT NULL,
  `inscricao_has_prato_id` int NOT NULL,
  `nralmocos` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `inscricao_has_prato`
--

INSERT INTO `inscricao_has_prato` (`inscricao_idinscricao`, `Prato_idPrato`, `inscricao_has_prato_id`, `nralmocos`) VALUES
(3, 24, 1, 14),
(4, 24, 2, 13),
(5, 24, 3, 10);

-- --------------------------------------------------------

--
-- Table structure for table `inscricao_has_sessao`
--

CREATE TABLE `inscricao_has_sessao` (
  `inscricao_idinscricao` int NOT NULL,
  `sessao_idsessao` int NOT NULL,
  `inscricao_has_sessao_id` int NOT NULL,
  `nr_inscritos` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `inscricao_has_sessao`
--

INSERT INTO `inscricao_has_sessao` (`inscricao_idinscricao`, `sessao_idsessao`, `inscricao_has_sessao_id`, `nr_inscritos`) VALUES
(3, 5, 4, 6),
(3, 6, 5, 8),
(4, 5, 6, 2),
(4, 6, 7, 11),
(5, 5, 8, 9),
(5, 6, 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `inscricao_individual`
--

CREATE TABLE `inscricao_individual` (
  `nracompanhantes` int(10) UNSIGNED ZEROFILL NOT NULL,
  `Participante_Utilizador_idutilizador` int NOT NULL,
  `inscricao_idinscricao` int NOT NULL,
  `telefone` int NOT NULL
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
  `menu` varchar(45) NOT NULL,
  `descricao` varchar(125) DEFAULT NULL,
  `Campus_idCampus` int NOT NULL,
  `horario_has_dia_id_dia_hora` int NOT NULL,
  `nralmocosdisponiveis` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`idMenu`, `menu`, `descricao`, `Campus_idCampus`, `horario_has_dia_id_dia_hora`, `nralmocosdisponiveis`) VALUES
(14, 'Menu do dia 27', 'sopa de legumes\r\nsobremesa cenoura', 5, 10, 463);

-- --------------------------------------------------------

--
-- Table structure for table `notificacao`
--

CREATE TABLE `notificacao` (
  `id` int NOT NULL,
  `descricao` varchar(255) NOT NULL,
  `criadoem` datetime(6) NOT NULL,
  `idutilizadorenvia` int NOT NULL,
  `utilizadorrecebe` int NOT NULL,
  `assunto` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `notificacao`
--

INSERT INTO `notificacao` (`id`, `descricao`, `criadoem`, `idutilizadorenvia`, `utilizadorrecebe`, `assunto`) VALUES
(46, 'Seja bem-vindo ao site do dia aberto', '2020-07-02 16:43:55.935515', -1, 1003, 'Bem-vindo'),
(47, 'Seja bem-vindo ao site do dia aberto', '2020-07-02 16:44:56.197261', -1, 1004, 'Bem-vindo'),
(48, 'Seja bem-vindo ao site do dia aberto', '2020-07-02 16:46:05.667510', -1, 1005, 'Bem-vindo'),
(49, 'Seja bem-vindo ao site do dia aberto', '2020-07-02 16:46:39.169280', -1, 1006, 'Bem-vindo'),
(50, 'Seja bem-vindo ao site do dia aberto', '2020-07-02 16:46:39.182245', -1, 1006, 'Bem-vindo'),
(51, 'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.', '2020-07-02 16:47:00.415221', 1002, 1005, 'Alteração de dados no perfil'),
(52, 'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.', '2020-07-02 16:47:21.600009', 1002, 1005, 'Alteração de dados no perfil'),
(53, 'Seja bem-vindo ao site do dia aberto', '2020-07-02 16:48:24.907746', -1, 1007, 'Bem-vindo'),
(54, 'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.', '2020-07-02 16:49:50.598228', 1002, 1007, 'Alteração de dados no perfil'),
(55, 'Nova inscrição de 6 pessoa(s) registada na atividade Brincar Com Números na sessão das 09:30:00.\nExistem ainda 20 lugares disponiveis.', '2020-07-02 17:10:31.106664', 1007, 1005, 'Nova Inscrição'),
(56, 'Nova inscrição de 8 pessoa(s) registada na atividade Matemática com o Rafa na sessão das 10:00:00.\nExistem ainda 20 lugares disponiveis.', '2020-07-02 17:10:31.126627', 1007, 1005, 'Nova Inscrição'),
(57, 'Seja bem-vindo ao site do dia aberto', '2020-07-02 17:12:35.431696', -1, 1008, 'Bem-vindo'),
(58, 'Nova inscrição de 2 pessoa(s) registada na atividade Brincar Com Números na sessão das 09:30:00.\nExistem ainda 14 lugares disponiveis.', '2020-07-02 17:14:26.763385', 1008, 1005, 'Nova Inscrição'),
(59, 'Nova inscrição de 11 pessoa(s) registada na atividade Matemática com o Rafa na sessão das 10:00:00.\nExistem ainda 12 lugares disponiveis.', '2020-07-02 17:14:26.775353', 1008, 1005, 'Nova Inscrição'),
(60, 'Seja bem-vindo ao site do dia aberto', '2020-07-02 17:15:42.437086', -1, 1009, 'Bem-vindo'),
(61, 'Nova inscrição de 9 pessoa(s) registada na atividade Brincar Com Números na sessão das 09:30:00.\nExistem ainda 12 lugares disponiveis.', '2020-07-02 17:17:23.654786', 1009, 1005, 'Nova Inscrição'),
(62, 'Nova inscrição de 1 pessoa(s) registada na atividade Matemática com o Rafa na sessão das 10:00:00.\nExistem ainda 1 lugares disponiveis.', '2020-07-02 17:17:23.666755', 1009, 1005, 'Nova Inscrição'),
(63, 'Seja bem-vindo ao site do dia aberto', '2020-07-02 17:22:28.231747', -1, 1010, 'Bem-vindo'),
(64, 'Seja bem-vindo ao site do dia aberto', '2020-07-02 17:27:30.171184', -1, 1011, 'Bem-vindo'),
(65, 'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.', '2020-07-02 17:48:34.561469', 1002, 1010, 'Alteração de dados no perfil'),
(66, 'Foi atribuido uma Nova Tarefa', '2020-07-02 17:50:54.431862', 1004, 1010, 'Tarefa'),
(67, 'Foi atribuido uma Nova Tarefa', '2020-07-02 17:51:34.395226', 1004, 1011, 'Tarefa'),
(68, 'Foi atribuido uma Nova Tarefa', '2020-07-02 17:53:17.006383', 1004, 1011, 'Tarefa'),
(69, 'Foi atribuido uma Nova Tarefa', '2020-07-02 17:58:41.995776', 1004, 1010, 'Tarefa'),
(70, 'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.', '2020-07-02 18:20:46.653293', -1, 1002, 'Alteração de dados no perfil'),
(71, 'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.', '2020-07-02 18:21:03.130196', -1, 1002, 'Alteração de dados no perfil'),
(72, 'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.', '2020-07-02 18:30:59.309272', -1, 1002, 'Alteração de dados no perfil'),
(73, 'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.', '2020-07-02 19:04:44.628093', -1, 1002, 'Alteração de dados no perfil'),
(74, 'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.', '2020-07-02 19:12:18.344080', -1, 1002, 'Alteração de dados no perfil'),
(75, 'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.', '2020-07-02 19:17:06.674064', -1, 1011, 'Alteração de dados no perfil'),
(76, 'Seja bem-vindo ao site do dia aberto', '2020-07-02 19:25:16.735821', -1, 1013, 'Bem-vindo'),
(77, 'Seja bem-vindo ao site do dia aberto', '2020-07-02 19:27:41.233163', -1, 1013, 'Bem-vindo');

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
('Penha'),
('Terminal');

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
(1007),
(1008),
(1009);

-- --------------------------------------------------------

--
-- Table structure for table `prato`
--

CREATE TABLE `prato` (
  `idPrato` int NOT NULL,
  `tipo` varchar(45) NOT NULL,
  `descricao` varchar(125) NOT NULL,
  `nralmocos` int DEFAULT NULL,
  `menu_idMenu` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `prato`
--

INSERT INTO `prato` (`idPrato`, `tipo`, `descricao`, `nralmocos`, `menu_idMenu`) VALUES
(24, 'Carne', 'vitela cozida', 37, 14),
(26, 'Peixe', 'douradinhos', 0, 14),
(28, 'Vegetariano', 'relva doce', 0, 14);

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
(1005, 5),
(1014, 6);

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
(3, 'eu', 'guilhas24@gmail.com', '980090090', 3),
(4, 'eu', 'vasco@mail.com', '909909902', 4),
(5, 'eu', 'a@a.com', '982234569', 5),
(6, 'tu', 'tu@tu.com', '090898716', 5);

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
  `capacidade` int NOT NULL DEFAULT '0',
  `Atividade_idAtividade` int NOT NULL,
  `horario_has_dia_id_dia_hora` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `sessao`
--

INSERT INTO `sessao` (`idsessao`, `nrinscritos`, `capacidade`, `Atividade_idAtividade`, `horario_has_dia_id_dia_hora`) VALUES
(5, 17, 20, 6, 5),
(6, 20, 20, 7, 6);

-- --------------------------------------------------------

--
-- Table structure for table `sessao_has_horario_has_dia`
--

CREATE TABLE `sessao_has_horario_has_dia` (
  `sessao_idsessao` int NOT NULL,
  `horario_has_dia_id_dia_hora` int NOT NULL,
  `sessao_has_horario_has_dia_id` int NOT NULL
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
  `colaborador_Utilizador_idutilizador` int DEFAULT NULL,
  `hora_inicio` time DEFAULT NULL,
  `dia_dia` date DEFAULT NULL,
  `sessao_idsessao` int DEFAULT NULL,
  `buscar` int DEFAULT NULL,
  `levar` int DEFAULT NULL,
  `inscricao_coletiva_inscricao_idinscricao` int DEFAULT NULL
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

--
-- Dumping data for table `transporte`
--

INSERT INTO `transporte` (`idtransporte`, `capacidade`, `identificacao`) VALUES
(2, 98, 'Próximo 20'),
(3, 95, 'Próximo 20');

-- --------------------------------------------------------

--
-- Table structure for table `transporte_has_horario`
--

CREATE TABLE `transporte_has_horario` (
  `transporte_idtransporte` int NOT NULL,
  `id_transporte_has_horario` int NOT NULL,
  `origem` varchar(45) NOT NULL,
  `destino` varchar(45) NOT NULL,
  `horario_has_dia_id_dia_hora` int NOT NULL,
  `n_passageiros` int DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `transporte_has_horario`
--

INSERT INTO `transporte_has_horario` (`transporte_idtransporte`, `id_transporte_has_horario`, `origem`, `destino`, `horario_has_dia_id_dia_hora`, `n_passageiros`) VALUES
(3, 1, 'Terminal', 'Penha', 95, 24);

-- --------------------------------------------------------

--
-- Table structure for table `transporte_has_inscricao`
--

CREATE TABLE `transporte_has_inscricao` (
  `inscricao_idinscricao` int NOT NULL,
  `transporte_has_inscricao_id` int NOT NULL,
  `transporte_has_horario_id_transporte_has_horario` int NOT NULL,
  `n_passageiros` int DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `transporte_has_inscricao`
--

INSERT INTO `transporte_has_inscricao` (`inscricao_idinscricao`, `transporte_has_inscricao_id`, `transporte_has_horario_id_transporte_has_horario`, `n_passageiros`) VALUES
(3, 1, 1, 14),
(5, 2, 1, 10);

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
  `sigla` varchar(255) NOT NULL,
  `Campus_idCampus` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `unidade_organica`
--

INSERT INTO `unidade_organica` (`idUO`, `sigla`, `Campus_idCampus`) VALUES
(9, 'FCT', 4),
(10, 'FCHS', 4),
(11, 'ESGHT', 5);

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
  `validada` tinyint NOT NULL DEFAULT '0',
  `remember_me` varchar(255) DEFAULT NULL,
  `dia_aberto_ano` year DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `utilizador`
--

INSERT INTO `utilizador` (`idutilizador`, `nome`, `email`, `telefone`, `password`, `validada`, `remember_me`, `dia_aberto_ano`) VALUES
(1002, 'Admin', 'admin@admin.com', '987789987', '03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7', 4, NULL, 2020),
(1004, 'cordenador', 'cordenador@cord.com', '987789010', '03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7', 2, NULL, 2020),
(1005, 'prof', 'prof@uni.com', '967109177', '03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7', 3, NULL, 2020),
(1007, 'Vasco', 'gui24@gmail.com', '987090111', '03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7', 0, NULL, 2020),
(1008, 'vasco', 'vasco@gmail.com', '909909909', '03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7', 0, NULL, 2020),
(1009, 'participante', 'v@v.com', '123123123', '03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7', 0, NULL, 2020),
(1010, 'Antonio Costa', 'co@co.com', '123456789', 'e3c5bd099032e227ead7c99cf6768150ddf071f939e1a669edadf409670a8ec2', 1, NULL, 2020),
(1011, 'Miguel Carlos', 'miguelinho@carlos.com', '978090123', '03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7', 1, NULL, 2020),
(1012, 'Guilherme Sousa Correia', 'kkk@u.com', '741852933', '7bd0854665d161be3d4504443e438c409ea9db07156fdbc3d5d143bc72ff4c39', 5, NULL, 2020),
(1014, 'Guilherme Sousa Correia', 'guilhas24@gmail.com', '123456789', '7bd0854665d161be3d4504443e438c409ea9db07156fdbc3d5d143bc72ff4c39', 5, NULL, 2020);

-- --------------------------------------------------------

--
-- Table structure for table `utilizador_has_notificacao`
--

CREATE TABLE `utilizador_has_notificacao` (
  `Utilizador_idutilizador` int NOT NULL,
  `notificacao_id` int NOT NULL,
  `utilizador_has_notificacao_id` int NOT NULL,
  `estado` tinyint NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `utilizador_has_notificacao`
--

INSERT INTO `utilizador_has_notificacao` (`Utilizador_idutilizador`, `notificacao_id`, `utilizador_has_notificacao_id`, `estado`) VALUES
(1004, 47, 85, 0),
(1005, 48, 86, 0),
(1005, 51, 89, 0),
(1002, 51, 90, 0),
(1005, 52, 91, 0),
(1002, 52, 92, 0),
(1007, 53, 93, 1),
(1007, 54, 94, 1),
(1002, 54, 95, 1),
(1005, 55, 96, 0),
(1007, 55, 97, 0),
(1005, 56, 98, 0),
(1007, 56, 99, 0),
(1008, 57, 100, 0),
(1005, 58, 101, 0),
(1008, 58, 102, 0),
(1005, 59, 103, 0),
(1008, 59, 104, 0),
(1009, 60, 105, 0),
(1005, 61, 106, 0),
(1009, 61, 107, 0),
(1005, 62, 108, 0),
(1009, 62, 109, 0),
(1010, 63, 110, 0),
(1011, 64, 111, 0),
(1010, 65, 112, 0),
(1002, 65, 113, 0),
(1010, 66, 114, 0),
(1004, 66, 115, 0),
(1011, 67, 116, 1),
(1004, 67, 117, 1),
(1011, 68, 118, 1),
(1004, 68, 119, 1),
(1010, 69, 120, 0),
(1004, 69, 121, 0),
(1002, 70, 122, 0),
(1002, 71, 123, 0),
(1002, 72, 124, 0),
(1002, 73, 125, 1),
(1002, 74, 126, 0),
(1011, 75, 127, 0);

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
  ADD PRIMARY KEY (`idCampus`);

--
-- Indexes for table `colaborador`
--
ALTER TABLE `colaborador`
  ADD PRIMARY KEY (`Utilizador_idutilizador`),
  ADD KEY `fk_colaborador_curso1_idx` (`curso_idcurso`);

--
-- Indexes for table `colaborador_has_horario`
--
ALTER TABLE `colaborador_has_horario`
  ADD PRIMARY KEY (`colaborador_has_horario_id`),
  ADD KEY `fk_colaborador_has_Horario_colaborador_id` (`colaborador_Utilizador_idutilizador`),
  ADD KEY `fk_colaborador_has_horario_horario_has_dia1_idx` (`horario_has_dia_id_dia_hora`);

--
-- Indexes for table `colaborador_has_unidade_organica`
--
ALTER TABLE `colaborador_has_unidade_organica`
  ADD PRIMARY KEY (`colaborador_has_unidade_organica_id`),
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
  ADD PRIMARY KEY (`Coordenador_Utilizador_idutilizador`),
  ADD KEY `fk_Coordenador_has_Departamento_Departamento_id` (`Departamento_idDepartamento`),
  ADD KEY `fk_Coordenador_has_Departamento_Coordenador_id` (`Coordenador_Utilizador_idutilizador`);

--
-- Indexes for table `curso`
--
ALTER TABLE `curso`
  ADD PRIMARY KEY (`idcurso`),
  ADD KEY `fk_curso_unidade_organica1_idx` (`unidade_organica_idUO`);

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
  ADD PRIMARY KEY (`ano`);

--
-- Indexes for table `disponibilidade`
--
ALTER TABLE `disponibilidade`
  ADD PRIMARY KEY (`disponibilidade_id`),
  ADD KEY `fk_table1_colaborador1_idx` (`colaborador_Utilizador_idutilizador`),
  ADD KEY `fk_table1_dia1_idx` (`dia_dia`),
  ADD KEY `fk_table1_horario1_idx` (`horario_hora`),
  ADD KEY `fk_table1_horario2_idx` (`horario_hora1`);

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
  ADD PRIMARY KEY (`inscricao_has_prato_id`),
  ADD KEY `fk_inscricao_has_Prato_Prato_id` (`Prato_idPrato`),
  ADD KEY `fk_inscricao_has_Prato_inscricao_id` (`inscricao_idinscricao`);

--
-- Indexes for table `inscricao_has_sessao`
--
ALTER TABLE `inscricao_has_sessao`
  ADD PRIMARY KEY (`inscricao_has_sessao_id`),
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
  ADD KEY `fk_prato_menu1_idx` (`menu_idMenu`);

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
  ADD PRIMARY KEY (`sessao_has_horario_has_dia_id`),
  ADD KEY `fk_sessao_has_horario_has_dia_horario_has_dia1_idx` (`horario_has_dia_id_dia_hora`),
  ADD KEY `fk_sessao_has_horario_has_dia_sessao1_idx` (`sessao_idsessao`);

--
-- Indexes for table `tarefa`
--
ALTER TABLE `tarefa`
  ADD PRIMARY KEY (`idtarefa`),
  ADD KEY `fk_tarefa_Coordenador_id` (`Coordenador_Utilizador_idutilizador`),
  ADD KEY `fk_tarefa_colaborador_id` (`colaborador_Utilizador_idutilizador`),
  ADD KEY `fk_tarefa_dia1_idx` (`dia_dia`),
  ADD KEY `fk_tarefa_sessao1_idx` (`sessao_idsessao`),
  ADD KEY `fk_tarefa_espaco1_idx` (`buscar`),
  ADD KEY `fk_tarefa_espaco2_idx` (`levar`),
  ADD KEY `fk_tarefa_inscricao_coletiva1_idx` (`inscricao_coletiva_inscricao_idinscricao`);

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
  ADD KEY `fk_transporte_has_horario_paragem1_idx` (`origem`),
  ADD KEY `fk_transporte_has_horario_paragem2_idx` (`destino`),
  ADD KEY `fk_transporte_has_horario_horario_has_dia1_idx` (`horario_has_dia_id_dia_hora`);

--
-- Indexes for table `transporte_has_inscricao`
--
ALTER TABLE `transporte_has_inscricao`
  ADD PRIMARY KEY (`transporte_has_inscricao_id`),
  ADD KEY `fk_transporte_has_inscricao_inscricao_id` (`inscricao_idinscricao`),
  ADD KEY `fk_transporte_has_inscricao_transporte_has_horario1_idx` (`transporte_has_horario_id_transporte_has_horario`);

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
  ADD KEY `fk_utilizador_dia_aberto1_idx` (`dia_aberto_ano`);

--
-- Indexes for table `utilizador_has_notificacao`
--
ALTER TABLE `utilizador_has_notificacao`
  ADD PRIMARY KEY (`utilizador_has_notificacao_id`),
  ADD KEY `fk_Utilizador_has_notificacao_notificacao_id` (`notificacao_id`),
  ADD KEY `fk_Utilizador_has_notificacao_Utilizador_id` (`Utilizador_idutilizador`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `atividade`
--
ALTER TABLE `atividade`
  MODIFY `idAtividade` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

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
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5285;

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
  MODIFY `idCampus` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `colaborador_has_horario`
--
ALTER TABLE `colaborador_has_horario`
  MODIFY `colaborador_has_horario_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `colaborador_has_unidade_organica`
--
ALTER TABLE `colaborador_has_unidade_organica`
  MODIFY `colaborador_has_unidade_organica_id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `curso`
--
ALTER TABLE `curso`
  MODIFY `idcurso` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `departamento`
--
ALTER TABLE `departamento`
  MODIFY `idDepartamento` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `disponibilidade`
--
ALTER TABLE `disponibilidade`
  MODIFY `disponibilidade_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=39;

--
-- AUTO_INCREMENT for table `escola`
--
ALTER TABLE `escola`
  MODIFY `idescola` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `espaco`
--
ALTER TABLE `espaco`
  MODIFY `idespaco` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `horario_has_dia`
--
ALTER TABLE `horario_has_dia`
  MODIFY `id_dia_hora` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=111;

--
-- AUTO_INCREMENT for table `inscricao`
--
ALTER TABLE `inscricao`
  MODIFY `idinscricao` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `inscricao_has_prato`
--
ALTER TABLE `inscricao_has_prato`
  MODIFY `inscricao_has_prato_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `inscricao_has_sessao`
--
ALTER TABLE `inscricao_has_sessao`
  MODIFY `inscricao_has_sessao_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `material`
--
ALTER TABLE `material`
  MODIFY `idMaterial` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `menu`
--
ALTER TABLE `menu`
  MODIFY `idMenu` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `notificacao`
--
ALTER TABLE `notificacao`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=78;

--
-- AUTO_INCREMENT for table `prato`
--
ALTER TABLE `prato`
  MODIFY `idPrato` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `responsaveis`
--
ALTER TABLE `responsaveis`
  MODIFY `idresponsavel` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `sessao`
--
ALTER TABLE `sessao`
  MODIFY `idsessao` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `sessao_has_horario_has_dia`
--
ALTER TABLE `sessao_has_horario_has_dia`
  MODIFY `sessao_has_horario_has_dia_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `tarefa`
--
ALTER TABLE `tarefa`
  MODIFY `idtarefa` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `transporte`
--
ALTER TABLE `transporte`
  MODIFY `idtransporte` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `transporte_has_horario`
--
ALTER TABLE `transporte_has_horario`
  MODIFY `id_transporte_has_horario` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `transporte_has_inscricao`
--
ALTER TABLE `transporte_has_inscricao`
  MODIFY `transporte_has_inscricao_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `unidade_organica`
--
ALTER TABLE `unidade_organica`
  MODIFY `idUO` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `utilizador`
--
ALTER TABLE `utilizador`
  MODIFY `idutilizador` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1015;

--
-- AUTO_INCREMENT for table `utilizador_has_notificacao`
--
ALTER TABLE `utilizador_has_notificacao`
  MODIFY `utilizador_has_notificacao_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=128;

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
-- Constraints for table `colaborador`
--
ALTER TABLE `colaborador`
  ADD CONSTRAINT `fk_colaborador_curso1` FOREIGN KEY (`curso_idcurso`) REFERENCES `curso` (`idcurso`) ON DELETE CASCADE ON UPDATE CASCADE,
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
-- Constraints for table `curso`
--
ALTER TABLE `curso`
  ADD CONSTRAINT `fk_curso_unidade_organica1` FOREIGN KEY (`unidade_organica_idUO`) REFERENCES `unidade_organica` (`idUO`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `departamento`
--
ALTER TABLE `departamento`
  ADD CONSTRAINT `fk_Departamento_unidade_organica` FOREIGN KEY (`unidade_organica_idUO`) REFERENCES `unidade_organica` (`idUO`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `disponibilidade`
--
ALTER TABLE `disponibilidade`
  ADD CONSTRAINT `fk_table1_colaborador1` FOREIGN KEY (`colaborador_Utilizador_idutilizador`) REFERENCES `colaborador` (`Utilizador_idutilizador`),
  ADD CONSTRAINT `fk_table1_dia1` FOREIGN KEY (`dia_dia`) REFERENCES `dia` (`dia`),
  ADD CONSTRAINT `fk_table1_horario1` FOREIGN KEY (`horario_hora`) REFERENCES `horario` (`hora`),
  ADD CONSTRAINT `fk_table1_horario2` FOREIGN KEY (`horario_hora1`) REFERENCES `horario` (`hora`);

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
  ADD CONSTRAINT `fk_prato_menu1` FOREIGN KEY (`menu_idMenu`) REFERENCES `menu` (`idMenu`);

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
  ADD CONSTRAINT `fk_tarefa_colaborador` FOREIGN KEY (`colaborador_Utilizador_idutilizador`) REFERENCES `colaborador` (`Utilizador_idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_tarefa_Coordenador` FOREIGN KEY (`Coordenador_Utilizador_idutilizador`) REFERENCES `coordenador` (`Utilizador_idutilizador`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_tarefa_dia1` FOREIGN KEY (`dia_dia`) REFERENCES `dia` (`dia`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_tarefa_espaco1` FOREIGN KEY (`buscar`) REFERENCES `espaco` (`idespaco`),
  ADD CONSTRAINT `fk_tarefa_espaco2` FOREIGN KEY (`levar`) REFERENCES `espaco` (`idespaco`),
  ADD CONSTRAINT `fk_tarefa_inscricao_coletiva1` FOREIGN KEY (`inscricao_coletiva_inscricao_idinscricao`) REFERENCES `inscricao_coletiva` (`inscricao_idinscricao`),
  ADD CONSTRAINT `fk_tarefa_sessao1` FOREIGN KEY (`sessao_idsessao`) REFERENCES `sessao` (`idsessao`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `transporte_has_horario`
--
ALTER TABLE `transporte_has_horario`
  ADD CONSTRAINT `fk_transporte_has_horario_horario_has_dia1` FOREIGN KEY (`horario_has_dia_id_dia_hora`) REFERENCES `horario_has_dia` (`id_dia_hora`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_transporte_has_horario_paragem1` FOREIGN KEY (`origem`) REFERENCES `paragem` (`paragem`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_transporte_has_horario_paragem2` FOREIGN KEY (`destino`) REFERENCES `paragem` (`paragem`),
  ADD CONSTRAINT `fk_transporte_has_Horario_transporte` FOREIGN KEY (`transporte_idtransporte`) REFERENCES `transporte` (`idtransporte`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `transporte_has_inscricao`
--
ALTER TABLE `transporte_has_inscricao`
  ADD CONSTRAINT `fk_transporte_has_inscricao_inscricao` FOREIGN KEY (`inscricao_idinscricao`) REFERENCES `inscricao` (`idinscricao`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_transporte_has_inscricao_transporte_has_horario1` FOREIGN KEY (`transporte_has_horario_id_transporte_has_horario`) REFERENCES `transporte_has_horario` (`id_transporte_has_horario`) ON DELETE CASCADE ON UPDATE CASCADE;

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
-- Constraints for table `utilizador`
--
ALTER TABLE `utilizador`
  ADD CONSTRAINT `fk_utilizador_dia_aberto1` FOREIGN KEY (`dia_aberto_ano`) REFERENCES `dia_aberto` (`ano`);

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
