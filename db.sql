-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema les
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema les
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `les` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `les` ;

-- -----------------------------------------------------
-- Table `les`.`utilizador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`utilizador` (
  `idutilizador` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `telefone` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `userName` VARCHAR(45) NOT NULL,
  `validada` TINYINT NOT NULL DEFAULT '0',
  PRIMARY KEY (`idutilizador`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `telefone_UNIQUE` (`telefone` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 15
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`administrador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`administrador` (
  `Utilizador_idutilizador` INT NOT NULL,
  PRIMARY KEY (`Utilizador_idutilizador`),
  CONSTRAINT `fk_Administrador_Utilizador`
    FOREIGN KEY (`Utilizador_idutilizador`)
    REFERENCES `les`.`utilizador` (`idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`campus`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`campus` (
  `idCampus` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCampus`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`espaco`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`espaco` (
  `idespaco` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `campus_idCampus` INT NOT NULL,
  PRIMARY KEY (`idespaco`),
  INDEX `fk_espaco_campus1_idx` (`campus_idCampus` ASC) VISIBLE,
  CONSTRAINT `fk_espaco_campus1`
    FOREIGN KEY (`campus_idCampus`)
    REFERENCES `les`.`campus` (`idCampus`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`anfiteatro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`anfiteatro` (
  `edificio` VARCHAR(45) NOT NULL,
  `andar` VARCHAR(45) NOT NULL,
  `espaco_idespaco` INT NOT NULL,
  PRIMARY KEY (`espaco_idespaco`),
  INDEX `fk_anfiteatro_espaco_id` (`espaco_idespaco` ASC) VISIBLE,
  CONSTRAINT `fk_anfiteatro_espaco`
    FOREIGN KEY (`espaco_idespaco`)
    REFERENCES `les`.`espaco` (`idespaco`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`arlivre`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`arlivre` (
  `descricao` VARCHAR(45) NOT NULL,
  `espaco_idespaco` INT NOT NULL,
  PRIMARY KEY (`espaco_idespaco`),
  INDEX `fk_arlivre_espaco_id` (`espaco_idespaco` ASC) VISIBLE,
  CONSTRAINT `fk_arlivre_espaco`
    FOREIGN KEY (`espaco_idespaco`)
    REFERENCES `les`.`espaco` (`idespaco`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`unidade_organica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`unidade_organica` (
  `idUO` INT NOT NULL AUTO_INCREMENT,
  `sigla` VARCHAR(5) NOT NULL,
  `Campus_idCampus` INT NOT NULL,
  PRIMARY KEY (`idUO`),
  INDEX `fk_unidade_organica_Campus_id` (`Campus_idCampus` ASC) VISIBLE,
  CONSTRAINT `fk_unidade_organica_Campus`
    FOREIGN KEY (`Campus_idCampus`)
    REFERENCES `les`.`campus` (`idCampus`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`departamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`departamento` (
  `idDepartamento` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `unidade_organica_idUO` INT NOT NULL,
  PRIMARY KEY (`idDepartamento`),
  INDEX `fk_Departamento_unidade_organica_id` (`unidade_organica_idUO` ASC) VISIBLE,
  CONSTRAINT `fk_Departamento_unidade_organica`
    FOREIGN KEY (`unidade_organica_idUO`)
    REFERENCES `les`.`unidade_organica` (`idUO`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`professor_universitario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`professor_universitario` (
  `Utilizador_idutilizador` INT NOT NULL,
  `departamento_idDepartamento` INT NOT NULL,
  PRIMARY KEY (`Utilizador_idutilizador`),
  INDEX `fk_professor_universitario_departamento1_idx` (`departamento_idDepartamento` ASC) VISIBLE,
  CONSTRAINT `fk_professor_universitario_departamento1`
    FOREIGN KEY (`departamento_idDepartamento`)
    REFERENCES `les`.`departamento` (`idDepartamento`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_professor_universitario_Utilizador`
    FOREIGN KEY (`Utilizador_idutilizador`)
    REFERENCES `les`.`utilizador` (`idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`atividade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`atividade` (
  `idAtividade` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(45) NOT NULL,
  `capacidade` INT NOT NULL,
  `publico_alvo` VARCHAR(45) NOT NULL,
  `duracao` FLOAT NOT NULL,
  `descricao` VARCHAR(250) NOT NULL,
  `validada` TINYINT NOT NULL DEFAULT '0',
  `professor_universitario_Utilizador_idutilizador` INT NOT NULL,
  `unidade_organica_idUO` INT NOT NULL,
  `Departamento_idDepartamento` INT NOT NULL,
  `espaco_idespaco` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idAtividade`),
  INDEX `fk_Atividade_professor_universitario_id` (`professor_universitario_Utilizador_idutilizador` ASC) VISIBLE,
  INDEX `fk_Atividade_unidade_organica_id` (`unidade_organica_idUO` ASC) VISIBLE,
  INDEX `fk_Atividade_Departamento_id` (`Departamento_idDepartamento` ASC) VISIBLE,
  INDEX `fk_atividade_espaco1_idx` (`espaco_idespaco` ASC) VISIBLE,
  CONSTRAINT `fk_Atividade_Departamento`
    FOREIGN KEY (`Departamento_idDepartamento`)
    REFERENCES `les`.`departamento` (`idDepartamento`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_atividade_espaco`
    FOREIGN KEY (`espaco_idespaco`)
    REFERENCES `les`.`espaco` (`idespaco`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Atividade_professor_universitario`
    FOREIGN KEY (`professor_universitario_Utilizador_idutilizador`)
    REFERENCES `les`.`professor_universitario` (`Utilizador_idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Atividade_unidade_organica`
    FOREIGN KEY (`unidade_organica_idUO`)
    REFERENCES `les`.`unidade_organica` (`idUO`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`material` (
  `idMaterial` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idMaterial`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`atividade_has_material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`atividade_has_material` (
  `Atividade_idAtividade` INT NOT NULL,
  `Material_idMaterial` INT NOT NULL,
  PRIMARY KEY (`Atividade_idAtividade`, `Material_idMaterial`),
  INDEX `fk_Atividade_has_Material_Material_id` (`Material_idMaterial` ASC) VISIBLE,
  INDEX `fk_Atividade_has_Material_Atividade_id` (`Atividade_idAtividade` ASC) VISIBLE,
  CONSTRAINT `fk_Atividade_has_Material_Atividade`
    FOREIGN KEY (`Atividade_idAtividade`)
    REFERENCES `les`.`atividade` (`idAtividade`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Atividade_has_Material_Material`
    FOREIGN KEY (`Material_idMaterial`)
    REFERENCES `les`.`material` (`idMaterial`)
    ON DELETE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`auth_group`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`auth_group` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name` (`name` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`django_content_type`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`django_content_type` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `app_label` VARCHAR(100) NOT NULL,
  `model` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label` ASC, `model` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 333
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`auth_permission`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`auth_permission` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `content_type_id` INT NOT NULL,
  `codename` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id` ASC, `codename` ASC) VISIBLE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `les`.`django_content_type` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 1329
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`auth_group_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`auth_group_permissions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `group_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id` ASC, `permission_id` ASC) VISIBLE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id` ASC) VISIBLE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `les`.`auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `les`.`auth_group` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`auth_user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`auth_user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `password` VARCHAR(128) NOT NULL,
  `last_login` DATETIME(6) NULL DEFAULT NULL,
  `is_superuser` TINYINT(1) NOT NULL,
  `username` VARCHAR(150) NOT NULL,
  `first_name` VARCHAR(30) NOT NULL,
  `last_name` VARCHAR(150) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `is_staff` TINYINT(1) NOT NULL,
  `is_active` TINYINT(1) NOT NULL,
  `date_joined` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `username` (`username` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`auth_user_groups`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`auth_user_groups` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `group_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id` ASC, `group_id` ASC) VISIBLE,
  INDEX `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id` ASC) VISIBLE,
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id`
    FOREIGN KEY (`group_id`)
    REFERENCES `les`.`auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `les`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`auth_user_user_permissions`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`auth_user_user_permissions` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id` ASC, `permission_id` ASC) VISIBLE,
  INDEX `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id` ASC) VISIBLE,
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm`
    FOREIGN KEY (`permission_id`)
    REFERENCES `les`.`auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `les`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`dia_aberto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`dia_aberto` (
  `ano` YEAR NOT NULL,
  `descricao` VARCHAR(120) NULL DEFAULT NULL,
  `datainscricao` DATE NOT NULL,
  `emailDiaAberto` VARCHAR(120) NOT NULL,
  `enderecoPaginaWeb` VARCHAR(60) NOT NULL,
  `dataDiainscricaoAtividadesInicio` DATE NOT NULL,
  `dataDiaAbertoInicio` DATE NOT NULL,
  `dataInscricaoAtividadesfim` DATE NOT NULL,
  `dataDiaAbertofim` DATE NOT NULL,
  `dataPropostaAtividadeInicio` DATE NOT NULL,
  `dataPropostaAtividadesFim` DATE NOT NULL,
  `Utilizador_idutilizador` INT NOT NULL,
  `Administrador_Utilizador_idutilizador` INT NOT NULL,
  PRIMARY KEY (`ano`),
  INDEX `fk_dia_aberto_Utilizador_id` (`Utilizador_idutilizador` ASC) VISIBLE,
  INDEX `fk_dia_aberto_Administrador_id` (`Administrador_Utilizador_idutilizador` ASC) VISIBLE,
  CONSTRAINT `fk_dia_aberto_Administrador`
    FOREIGN KEY (`Administrador_Utilizador_idutilizador`)
    REFERENCES `les`.`administrador` (`Utilizador_idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_dia_aberto_Utilizador`
    FOREIGN KEY (`Utilizador_idutilizador`)
    REFERENCES `les`.`utilizador` (`idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`colaborador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`colaborador` (
  `curso` VARCHAR(45) NOT NULL,
  `preferencia` VARCHAR(45) NULL DEFAULT NULL,
  `Utilizador_idutilizador` INT NOT NULL,
  `dia_aberto_ano` YEAR NOT NULL,
  PRIMARY KEY (`Utilizador_idutilizador`),
  INDEX `fk_colaborador_dia_aberto_id` (`dia_aberto_ano` ASC) VISIBLE,
  CONSTRAINT `fk_colaborador_dia_aberto`
    FOREIGN KEY (`dia_aberto_ano`)
    REFERENCES `les`.`dia_aberto` (`ano`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_colaborador_Utilizador`
    FOREIGN KEY (`Utilizador_idutilizador`)
    REFERENCES `les`.`utilizador` (`idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`dia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`dia` (
  `dia` DATE NOT NULL,
  PRIMARY KEY (`dia`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`horario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`horario` (
  `hora` TIME NOT NULL,
  PRIMARY KEY (`hora`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`horario_has_dia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`horario_has_dia` (
  `horario_hora` TIME NOT NULL,
  `Dia_dia` DATE NOT NULL,
  `id_dia_hora` INT NOT NULL,
  PRIMARY KEY (`id_dia_hora`),
  INDEX `fk_horario_has_Dia_Dia1_idx` (`Dia_dia` ASC) VISIBLE,
  INDEX `fk_horario_has_Dia_horario1_idx` (`horario_hora` ASC) VISIBLE,
  CONSTRAINT `fk_horario_has_Dia_Dia`
    FOREIGN KEY (`Dia_dia`)
    REFERENCES `les`.`dia` (`dia`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_horario_has_Dia_horario`
    FOREIGN KEY (`horario_hora`)
    REFERENCES `les`.`horario` (`hora`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`colaborador_has_horario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`colaborador_has_horario` (
  `colaborador_Utilizador_idutilizador` INT NOT NULL,
  `horario_has_dia_id_dia_hora` INT NOT NULL,
  INDEX `fk_colaborador_has_Horario_colaborador_id` (`colaborador_Utilizador_idutilizador` ASC) VISIBLE,
  INDEX `fk_colaborador_has_horario_horario_has_dia1_idx` (`horario_has_dia_id_dia_hora` ASC) VISIBLE,
  CONSTRAINT `fk_colaborador_has_Horario_colaborador`
    FOREIGN KEY (`colaborador_Utilizador_idutilizador`)
    REFERENCES `les`.`colaborador` (`Utilizador_idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_colaborador_has_horario_horario_has_dia1`
    FOREIGN KEY (`horario_has_dia_id_dia_hora`)
    REFERENCES `les`.`horario_has_dia` (`id_dia_hora`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`colaborador_has_unidade_organica`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`colaborador_has_unidade_organica` (
  `colaborador_Utilizador_idutilizador` INT NOT NULL,
  `unidade_organica_idUO` INT NOT NULL,
  INDEX `fk_colaborador_has_unidade_organica_unidade_organica_id` (`unidade_organica_idUO` ASC) VISIBLE,
  INDEX `fk_colaborador_has_unidade_organica_colaborador_id` (`colaborador_Utilizador_idutilizador` ASC) VISIBLE,
  CONSTRAINT `fk_colaborador_has_unidade_organica_colaborador`
    FOREIGN KEY (`colaborador_Utilizador_idutilizador`)
    REFERENCES `les`.`colaborador` (`Utilizador_idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_colaborador_has_unidade_organica_unidade_Organica`
    FOREIGN KEY (`unidade_organica_idUO`)
    REFERENCES `les`.`unidade_organica` (`idUO`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`coordenador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`coordenador` (
  `Utilizador_idutilizador` INT NOT NULL,
  `unidade_organica_idUO` INT NOT NULL,
  PRIMARY KEY (`Utilizador_idutilizador`),
  INDEX `fk_Coordenador_unidade_organica_id` (`unidade_organica_idUO` ASC) VISIBLE,
  CONSTRAINT `fk_Coordenador_unidade_organica`
    FOREIGN KEY (`unidade_organica_idUO`)
    REFERENCES `les`.`unidade_organica` (`idUO`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Coordenador_Utilizador`
    FOREIGN KEY (`Utilizador_idutilizador`)
    REFERENCES `les`.`utilizador` (`idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`coordenador_has_departamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`coordenador_has_departamento` (
  `Coordenador_Utilizador_idutilizador` INT NOT NULL,
  `Departamento_idDepartamento` INT NOT NULL,
  PRIMARY KEY (`Coordenador_Utilizador_idutilizador`, `Departamento_idDepartamento`),
  INDEX `fk_Coordenador_has_Departamento_Departamento_id` (`Departamento_idDepartamento` ASC) VISIBLE,
  INDEX `fk_Coordenador_has_Departamento_Coordenador_id` (`Coordenador_Utilizador_idutilizador` ASC) VISIBLE,
  CONSTRAINT `fk_Coordenador_has_Departamento_Coordenador`
    FOREIGN KEY (`Coordenador_Utilizador_idutilizador`)
    REFERENCES `les`.`coordenador` (`Utilizador_idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Coordenador_has_Departamento_Departamento`
    FOREIGN KEY (`Departamento_idDepartamento`)
    REFERENCES `les`.`departamento` (`idDepartamento`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`Paragem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`Paragem` (
  `paragem` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`paragem`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`django_admin_log`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`django_admin_log` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `action_time` DATETIME(6) NOT NULL,
  `object_id` LONGTEXT NULL DEFAULT NULL,
  `object_repr` VARCHAR(200) NOT NULL,
  `action_flag` SMALLINT UNSIGNED NOT NULL,
  `change_message` LONGTEXT NOT NULL,
  `content_type_id` INT NULL DEFAULT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id` ASC) VISIBLE,
  INDEX `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id` ASC) VISIBLE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co`
    FOREIGN KEY (`content_type_id`)
    REFERENCES `les`.`django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id`
    FOREIGN KEY (`user_id`)
    REFERENCES `les`.`auth_user` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`django_migrations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`django_migrations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `app` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `applied` DATETIME(6) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 60
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`django_session`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`django_session` (
  `session_key` VARCHAR(40) NOT NULL,
  `session_data` LONGTEXT NOT NULL,
  `expire_date` DATETIME(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  INDEX `django_session_expire_date_a5c62663` (`expire_date` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`escola`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`escola` (
  `idescola` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `local` VARCHAR(45) NOT NULL,
  `telefone` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`idescola`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`idioma`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`idioma` (
  `nome` VARCHAR(24) NOT NULL,
  `sigla` VARCHAR(45) NOT NULL,
  `Administrador_Utilizador_idutilizador` INT NOT NULL,
  PRIMARY KEY (`nome`),
  UNIQUE INDEX `sigla_UNIQUE` (`sigla` ASC) VISIBLE,
  INDEX `fk_idioma_Administrador_id` (`Administrador_Utilizador_idutilizador` ASC) VISIBLE,
  CONSTRAINT `fk_idioma_Administrador`
    FOREIGN KEY (`Administrador_Utilizador_idutilizador`)
    REFERENCES `les`.`administrador` (`Utilizador_idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`inscricao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`inscricao` (
  `idinscricao` INT NOT NULL AUTO_INCREMENT,
  `ano` YEAR NOT NULL,
  `local` VARCHAR(45) NOT NULL,
  `nparticipantes` INT NOT NULL,
  `areacientifica` VARCHAR(45) NOT NULL,
  `transporte` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`idinscricao`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`participante`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`participante` (
  `Utilizador_idutilizador` INT NOT NULL,
  PRIMARY KEY (`Utilizador_idutilizador`),
  CONSTRAINT `fk_Participante_Utilizador`
    FOREIGN KEY (`Utilizador_idutilizador`)
    REFERENCES `les`.`utilizador` (`idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`inscricao_coletiva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`inscricao_coletiva` (
  `nresponsaveis` INT NOT NULL,
  `turma` CHAR(1) NOT NULL,
  `Participante_Utilizador_idutilizador` INT NOT NULL,
  `escola_idescola` INT NOT NULL,
  `inscricao_idinscricao` INT NOT NULL,
  `telefone` INT NOT NULL,
  PRIMARY KEY (`inscricao_idinscricao`),
  INDEX `fk_inscricao_coletiva_Participante_id` (`Participante_Utilizador_idutilizador` ASC) VISIBLE,
  INDEX `fk_inscricao_coletiva_escola_id` (`escola_idescola` ASC) VISIBLE,
  INDEX `fk_inscricao_coletiva_inscricao_id` (`inscricao_idinscricao` ASC) VISIBLE,
  CONSTRAINT `fk_inscricao_coletiva_escola`
    FOREIGN KEY (`escola_idescola`)
    REFERENCES `les`.`escola` (`idescola`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_inscricao_coletiva_inscricao`
    FOREIGN KEY (`inscricao_idinscricao`)
    REFERENCES `les`.`inscricao` (`idinscricao`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_inscricao_coletiva_Participante`
    FOREIGN KEY (`Participante_Utilizador_idutilizador`)
    REFERENCES `les`.`participante` (`Utilizador_idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`menu`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`menu` (
  `idMenu` INT NOT NULL AUTO_INCREMENT,
  `precoAluno` FLOAT NOT NULL,
  `PrecoProfessor` FLOAT NOT NULL,
  `tipo` VARCHAR(45) NOT NULL,
  `menu` VARCHAR(45) NOT NULL,
  `Administrador_Utilizador_idutilizador` INT NOT NULL,
  `Campus_idCampus` INT NOT NULL,
  `horario_has_dia_id_dia_hora` INT NOT NULL,
  PRIMARY KEY (`idMenu`),
  INDEX `fk_Menu_Administrador_id` (`Administrador_Utilizador_idutilizador` ASC) VISIBLE,
  INDEX `fk_Menu_Campus_id` (`Campus_idCampus` ASC) VISIBLE,
  INDEX `fk_menu_horario_has_dia1_idx` (`horario_has_dia_id_dia_hora` ASC) VISIBLE,
  CONSTRAINT `fk_Menu_Administrador`
    FOREIGN KEY (`Administrador_Utilizador_idutilizador`)
    REFERENCES `les`.`administrador` (`Utilizador_idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Menu_Campus`
    FOREIGN KEY (`Campus_idCampus`)
    REFERENCES `les`.`campus` (`idCampus`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_menu_horario_has_dia1`
    FOREIGN KEY (`horario_has_dia_id_dia_hora`)
    REFERENCES `les`.`horario_has_dia` (`id_dia_hora`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`prato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`prato` (
  `idPrato` INT NOT NULL AUTO_INCREMENT,
  `nralomocosdisponiveis` INT NOT NULL,
  `descricao` VARCHAR(125) NOT NULL,
  `Menu_idMenu` INT NOT NULL,
  PRIMARY KEY (`idPrato`),
  INDEX `fk_Prato_Menu_id` (`Menu_idMenu` ASC) VISIBLE,
  CONSTRAINT `fk_Prato_Menu`
    FOREIGN KEY (`Menu_idMenu`)
    REFERENCES `les`.`menu` (`idMenu`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`inscricao_has_prato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`inscricao_has_prato` (
  `inscricao_idinscricao` INT NOT NULL,
  `Prato_idPrato` INT NOT NULL,
  INDEX `fk_inscricao_has_Prato_Prato_id` (`Prato_idPrato` ASC) VISIBLE,
  INDEX `fk_inscricao_has_Prato_inscricao_id` (`inscricao_idinscricao` ASC) VISIBLE,
  CONSTRAINT `fk_inscricao_has_Prato_inscricao`
    FOREIGN KEY (`inscricao_idinscricao`)
    REFERENCES `les`.`inscricao` (`idinscricao`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_inscricao_has_Prato_Prato`
    FOREIGN KEY (`Prato_idPrato`)
    REFERENCES `les`.`prato` (`idPrato`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`sessao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`sessao` (
  `idsessao` INT NOT NULL AUTO_INCREMENT,
  `nrinscritos` INT NOT NULL DEFAULT '0',
  `vagas` INT NOT NULL DEFAULT '0',
  `Atividade_idAtividade` INT NOT NULL,
  `horario_has_dia_id_dia_hora` INT NOT NULL,
  PRIMARY KEY (`idsessao`),
  INDEX `fk_sessao_Atividade_id` (`Atividade_idAtividade` ASC) VISIBLE,
  INDEX `fk_sessao_horario_has_dia1_idx` (`horario_has_dia_id_dia_hora` ASC) VISIBLE,
  CONSTRAINT `fk_sessao_Atividade`
    FOREIGN KEY (`Atividade_idAtividade`)
    REFERENCES `les`.`atividade` (`idAtividade`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_sessao_horario_has_dia1`
    FOREIGN KEY (`horario_has_dia_id_dia_hora`)
    REFERENCES `les`.`horario_has_dia` (`id_dia_hora`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`inscricao_has_sessao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`inscricao_has_sessao` (
  `inscricao_idinscricao` INT NOT NULL,
  `sessao_idsessao` INT NOT NULL,
  INDEX `fk_inscricao_has_sessao_sessao_id` (`sessao_idsessao` ASC) VISIBLE,
  INDEX `fk_inscricao_has_sessao_inscricao_id` (`inscricao_idinscricao` ASC) VISIBLE,
  CONSTRAINT `fk_inscricao_has_sessao_inscricao`
    FOREIGN KEY (`inscricao_idinscricao`)
    REFERENCES `les`.`inscricao` (`idinscricao`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_inscricao_has_sessao_sessao`
    FOREIGN KEY (`sessao_idsessao`)
    REFERENCES `les`.`sessao` (`idsessao`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`inscricao_individual`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`inscricao_individual` (
  `nracompanhades` INT(10) UNSIGNED ZEROFILL NOT NULL,
  `Participante_Utilizador_idutilizador` INT NOT NULL,
  `inscricao_idinscricao` INT NOT NULL,
  PRIMARY KEY (`inscricao_idinscricao`),
  INDEX `fk_inscricao_individual_Participante_id` (`Participante_Utilizador_idutilizador` ASC) VISIBLE,
  INDEX `fk_inscricao_individual_inscricao_id` (`inscricao_idinscricao` ASC) VISIBLE,
  CONSTRAINT `fk_inscricao_individual_inscricao`
    FOREIGN KEY (`inscricao_idinscricao`)
    REFERENCES `les`.`inscricao` (`idinscricao`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_inscricao_individual_Participante`
    FOREIGN KEY (`Participante_Utilizador_idutilizador`)
    REFERENCES `les`.`participante` (`Utilizador_idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`notificacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`notificacao` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(45) NOT NULL,
  `criadoem` DATETIME(6) NOT NULL,
  `idutilizadorenvia` INT NOT NULL,
  `utilizadorrecebe` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`responsaveis`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`responsaveis` (
  `idresponsavel` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `telefone` VARCHAR(45) NOT NULL,
  `idInscricao` INT NOT NULL,
  PRIMARY KEY (`idresponsavel`),
  INDEX `fk_Responsáveis_Inscricao` (`idInscricao` ASC) VISIBLE,
  CONSTRAINT `fk_Responsáveis_Inscricao`
    FOREIGN KEY (`idInscricao`)
    REFERENCES `les`.`inscricao` (`idinscricao`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`sala`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`sala` (
  `edificio` VARCHAR(45) NOT NULL,
  `andar` VARCHAR(45) NOT NULL,
  `gabinete` VARCHAR(45) NULL DEFAULT NULL,
  `espaco_idespaco` INT NOT NULL,
  PRIMARY KEY (`espaco_idespaco`),
  INDEX `fk_sala_espaco_id` (`espaco_idespaco` ASC) VISIBLE,
  CONSTRAINT `fk_sala_espaco`
    FOREIGN KEY (`espaco_idespaco`)
    REFERENCES `les`.`espaco` (`idespaco`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`tarefa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`tarefa` (
  `idtarefa` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `concluida` TINYINT NOT NULL,
  `Coordenador_Utilizador_idutilizador` INT NOT NULL,
  `colaborador_Utilizador_idutilizador` INT NOT NULL,
  `Atividade_idAtividade` INT NOT NULL,
  PRIMARY KEY (`idtarefa`),
  INDEX `fk_tarefa_Coordenador_id` (`Coordenador_Utilizador_idutilizador` ASC) VISIBLE,
  INDEX `fk_tarefa_colaborador_id` (`colaborador_Utilizador_idutilizador` ASC) VISIBLE,
  INDEX `fk_tarefa_Atividade_id` (`Atividade_idAtividade` ASC) VISIBLE,
  CONSTRAINT `fk_tarefa_Atividade`
    FOREIGN KEY (`Atividade_idAtividade`)
    REFERENCES `les`.`atividade` (`idAtividade`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_tarefa_colaborador`
    FOREIGN KEY (`colaborador_Utilizador_idutilizador`)
    REFERENCES `les`.`colaborador` (`Utilizador_idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_tarefa_Coordenador`
    FOREIGN KEY (`Coordenador_Utilizador_idutilizador`)
    REFERENCES `les`.`coordenador` (`Utilizador_idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`transporte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`transporte` (
  `idtransporte` INT NOT NULL AUTO_INCREMENT,
  `capacidade` INT NOT NULL,
  `identificacao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idtransporte`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`transporte_has_horario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`transporte_has_horario` (
  `transporte_idtransporte` INT NOT NULL,
  `horario_has_dia_id_dia_hora` INT NOT NULL,
  `vagas` INT NOT NULL,
  `id_transporte_has_horario` INT NOT NULL,
  `destino` VARCHAR(45) NOT NULL,
  `origem` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_transporte_has_horario`),
  INDEX `fk_transporte_has_Horario_transporte_id` (`transporte_idtransporte` ASC) VISIBLE,
  INDEX `fk_transporte_has_horario_horario_has_dia1_idx` (`horario_has_dia_id_dia_hora` ASC) VISIBLE,
  INDEX `fk_transporte_has_horario_Paragem1_idx` (`destino` ASC) VISIBLE,
  INDEX `fk_transporte_has_horario_Paragem2_idx` (`origem` ASC) VISIBLE,
  CONSTRAINT `fk_transporte_has_horario_horario_has_dia1`
    FOREIGN KEY (`horario_has_dia_id_dia_hora`)
    REFERENCES `les`.`horario_has_dia` (`id_dia_hora`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_transporte_has_Horario_transporte`
    FOREIGN KEY (`transporte_idtransporte`)
    REFERENCES `les`.`transporte` (`idtransporte`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_transporte_has_horario_Paragem1`
    FOREIGN KEY (`destino`)
    REFERENCES `les`.`Paragem` (`paragem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_transporte_has_horario_Paragem2`
    FOREIGN KEY (`origem`)
    REFERENCES `les`.`Paragem` (`paragem`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`transporte_has_inscricao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`transporte_has_inscricao` (
  `inscricao_idinscricao` INT NOT NULL,
  `transporte_has_horario_id_transporte_has_horario` INT NOT NULL,
  INDEX `fk_transporte_has_inscricao_inscricao_id` (`inscricao_idinscricao` ASC) VISIBLE,
  INDEX `fk_transporte_has_inscricao_transporte_has_horario1_idx` (`transporte_has_horario_id_transporte_has_horario` ASC) VISIBLE,
  CONSTRAINT `fk_transporte_has_inscricao_inscricao`
    FOREIGN KEY (`inscricao_idinscricao`)
    REFERENCES `les`.`inscricao` (`idinscricao`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_transporte_has_inscricao_transporte_has_horario1`
    FOREIGN KEY (`transporte_has_horario_id_transporte_has_horario`)
    REFERENCES `les`.`transporte_has_horario` (`id_transporte_has_horario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`transporte_pessoal`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`transporte_pessoal` (
  `transporte_idtransporte` INT NOT NULL,
  PRIMARY KEY (`transporte_idtransporte`),
  CONSTRAINT `fk_Transporte_pessoal_transporte`
    FOREIGN KEY (`transporte_idtransporte`)
    REFERENCES `les`.`transporte` (`idtransporte`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`transporte_universitario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`transporte_universitario` (
  `capacidade` INT NOT NULL,
  `transporte_idtransporte` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`transporte_idtransporte`),
  CONSTRAINT `fk_transporte Universitario_transporte`
    FOREIGN KEY (`transporte_idtransporte`)
    REFERENCES `les`.`transporte` (`idtransporte`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`utilizador_has_notificacao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`utilizador_has_notificacao` (
  `Utilizador_idutilizador` INT NOT NULL,
  `notificacao_id` INT NOT NULL,
  INDEX `fk_Utilizador_has_notificacao_notificacao_id` (`notificacao_id` ASC) VISIBLE,
  INDEX `fk_Utilizador_has_notificacao_Utilizador_id` (`Utilizador_idutilizador` ASC) VISIBLE,
  CONSTRAINT `fk_Utilizador_has_notificacao_notificacao`
    FOREIGN KEY (`notificacao_id`)
    REFERENCES `les`.`notificacao` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Utilizador_has_notificacao_Utilizador`
    FOREIGN KEY (`Utilizador_idutilizador`)
    REFERENCES `les`.`utilizador` (`idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
