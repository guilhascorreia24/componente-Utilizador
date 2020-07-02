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
-- Table `les`.`dia_aberto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`dia_aberto` (
  `ano` YEAR NOT NULL,
  `descricao` VARCHAR(120) NULL DEFAULT NULL,
  `emailDiaAberto` VARCHAR(120) NOT NULL,
  `enderecoPaginaWeb` VARCHAR(60) NOT NULL,
  `dataDiaAbertoInicio` DATE NOT NULL,
  `dataDiaAbertofim` DATE NOT NULL,
  `datainscricaonasatividadesinicio` DATE NOT NULL,
  `datainscricaonasatividadesfim` DATE NOT NULL,
  `dataPropostaAtividadeInicio` DATE NOT NULL,
  `dataPropostaAtividadesFim` DATE NOT NULL,
  `preco_almoco_estudante` FLOAT NOT NULL DEFAULT '0',
  `preco_almoco_professor` FLOAT NOT NULL,
  PRIMARY KEY (`ano`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`utilizador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`utilizador` (
  `idutilizador` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `telefone` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `validada` TINYINT NOT NULL DEFAULT '0',
  `remember_me` VARCHAR(255) NULL DEFAULT NULL,
  `dia_aberto_ano` YEAR NULL DEFAULT NULL,
  PRIMARY KEY (`idutilizador`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  INDEX `fk_utilizador_dia_aberto1_idx` (`dia_aberto_ano` ASC) VISIBLE,
  CONSTRAINT `fk_utilizador_dia_aberto1`
    FOREIGN KEY (`dia_aberto_ano`)
    REFERENCES `les`.`dia_aberto` (`ano`))
ENGINE = InnoDB
AUTO_INCREMENT = 1002
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
  `nome` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`idCampus`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`espaco`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`espaco` (
  `idespaco` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  `campus_idCampus` INT NOT NULL,
  `img` VARCHAR(100) NULL DEFAULT NULL,
  PRIMARY KEY (`idespaco`),
  INDEX `fk_espaco_campus1_idx` (`campus_idCampus` ASC) VISIBLE,
  CONSTRAINT `fk_espaco_campus1`
    FOREIGN KEY (`campus_idCampus`)
    REFERENCES `les`.`campus` (`idCampus`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 7
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
  `descricao` VARCHAR(255) NOT NULL,
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
  `sigla` VARCHAR(255) NOT NULL,
  `Campus_idCampus` INT NOT NULL,
  PRIMARY KEY (`idUO`),
  INDEX `fk_unidade_organica_Campus_id` (`Campus_idCampus` ASC) VISIBLE,
  CONSTRAINT `fk_unidade_organica_Campus`
    FOREIGN KEY (`Campus_idCampus`)
    REFERENCES `les`.`campus` (`idCampus`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`departamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`departamento` (
  `idDepartamento` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  `unidade_organica_idUO` INT NOT NULL,
  PRIMARY KEY (`idDepartamento`),
  INDEX `fk_Departamento_unidade_organica_id` (`unidade_organica_idUO` ASC) VISIBLE,
  CONSTRAINT `fk_Departamento_unidade_organica`
    FOREIGN KEY (`unidade_organica_idUO`)
    REFERENCES `les`.`unidade_organica` (`idUO`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 5
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
  `tematica` VARCHAR(250) NULL DEFAULT NULL,
  `nrColaborador` VARCHAR(45) NULL DEFAULT '0',
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
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`material`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`material` (
  `idMaterial` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(255) NOT NULL,
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
AUTO_INCREMENT = 5285
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
-- Table `les`.`curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`curso` (
  `idcurso` INT NOT NULL AUTO_INCREMENT,
  `unidade_organica_idUO` INT NOT NULL,
  `nome` VARCHAR(250) NOT NULL,
  PRIMARY KEY (`idcurso`),
  INDEX `fk_curso_unidade_organica1_idx` (`unidade_organica_idUO` ASC) VISIBLE,
  CONSTRAINT `fk_curso_unidade_organica1`
    FOREIGN KEY (`unidade_organica_idUO`)
    REFERENCES `les`.`unidade_organica` (`idUO`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 6
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`colaborador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`colaborador` (
  `Utilizador_idutilizador` INT NOT NULL,
  `curso_idcurso` INT NULL DEFAULT NULL,
  PRIMARY KEY (`Utilizador_idutilizador`),
  INDEX `fk_colaborador_curso1_idx` (`curso_idcurso` ASC) VISIBLE,
  CONSTRAINT `fk_colaborador_curso1`
    FOREIGN KEY (`curso_idcurso`)
    REFERENCES `les`.`curso` (`idcurso`)
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
  `id_dia_hora` INT NOT NULL AUTO_INCREMENT,
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
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`colaborador_has_horario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`colaborador_has_horario` (
  `colaborador_Utilizador_idutilizador` INT NOT NULL,
  `horario_has_dia_id_dia_hora` INT NOT NULL,
  `colaborador_has_horario_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`colaborador_has_horario_id`),
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
  `colaborador_has_unidade_organica_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`colaborador_has_unidade_organica_id`),
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
  PRIMARY KEY (`Coordenador_Utilizador_idutilizador`),
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
-- Table `les`.`disponibilidade`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`disponibilidade` (
  `colaborador_Utilizador_idutilizador` INT NOT NULL,
  `dia_dia` DATE NOT NULL,
  `horario_hora` TIME NOT NULL,
  `horario_hora1` TIME NOT NULL,
  `tipo_de_tarefa` VARCHAR(45) NOT NULL,
  `disponibilidade_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`disponibilidade_id`),
  INDEX `fk_table1_colaborador1_idx` (`colaborador_Utilizador_idutilizador` ASC) VISIBLE,
  INDEX `fk_table1_dia1_idx` (`dia_dia` ASC) VISIBLE,
  INDEX `fk_table1_horario1_idx` (`horario_hora` ASC) VISIBLE,
  INDEX `fk_table1_horario2_idx` (`horario_hora1` ASC) VISIBLE,
  CONSTRAINT `fk_table1_colaborador1`
    FOREIGN KEY (`colaborador_Utilizador_idutilizador`)
    REFERENCES `les`.`colaborador` (`Utilizador_idutilizador`),
  CONSTRAINT `fk_table1_dia1`
    FOREIGN KEY (`dia_dia`)
    REFERENCES `les`.`dia` (`dia`),
  CONSTRAINT `fk_table1_horario1`
    FOREIGN KEY (`horario_hora`)
    REFERENCES `les`.`horario` (`hora`),
  CONSTRAINT `fk_table1_horario2`
    FOREIGN KEY (`horario_hora1`)
    REFERENCES `les`.`horario` (`hora`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
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
AUTO_INCREMENT = 39
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
  `nome` VARCHAR(255) NOT NULL,
  `local` VARCHAR(45) NOT NULL,
  `telefone` VARCHAR(45) NOT NULL,
  `email` VARCHAR(255) NULL DEFAULT NULL,
  PRIMARY KEY (`idescola`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`idioma`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`idioma` (
  `nome` VARCHAR(255) NOT NULL,
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
  `ano` INT NOT NULL,
  `local` VARCHAR(255) NOT NULL,
  `areacientifica` VARCHAR(255) NOT NULL,
  `transporte` TINYINT(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`idinscricao`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
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
  `nparticipantes` INT NOT NULL DEFAULT '1',
  `inscricao_idinscricao` INT NOT NULL,
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
  `menu` VARCHAR(45) NOT NULL,
  `descricao` VARCHAR(125) NULL DEFAULT NULL,
  `Campus_idCampus` INT NOT NULL,
  `horario_has_dia_id_dia_hora` INT NOT NULL,
  `nralmocosdisponiveis` INT NOT NULL,
  PRIMARY KEY (`idMenu`),
  INDEX `fk_Menu_Campus_id` (`Campus_idCampus` ASC) VISIBLE,
  INDEX `fk_menu_horario_has_dia1_idx` (`horario_has_dia_id_dia_hora` ASC) VISIBLE,
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
AUTO_INCREMENT = 14
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`prato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`prato` (
  `idPrato` INT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45) NOT NULL,
  `descricao` VARCHAR(125) NOT NULL,
  `nralmocos` INT NULL DEFAULT NULL,
  `menu_idMenu` INT NOT NULL,
  PRIMARY KEY (`idPrato`),
  INDEX `fk_prato_menu1_idx` (`menu_idMenu` ASC) VISIBLE,
  CONSTRAINT `fk_prato_menu1`
    FOREIGN KEY (`menu_idMenu`)
    REFERENCES `les`.`menu` (`idMenu`))
ENGINE = InnoDB
AUTO_INCREMENT = 24
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`inscricao_has_prato`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`inscricao_has_prato` (
  `inscricao_idinscricao` INT NOT NULL,
  `Prato_idPrato` INT NOT NULL,
  `inscricao_has_prato_id` INT NOT NULL AUTO_INCREMENT,
  `nralmocos` INT NOT NULL,
  PRIMARY KEY (`inscricao_has_prato_id`),
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
  `capacidade` INT NOT NULL DEFAULT '0',
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
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`inscricao_has_sessao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`inscricao_has_sessao` (
  `inscricao_idinscricao` INT NOT NULL,
  `sessao_idsessao` INT NOT NULL,
  `inscricao_has_sessao_id` INT NOT NULL AUTO_INCREMENT,
  `nr_inscritos` INT NOT NULL,
  PRIMARY KEY (`inscricao_has_sessao_id`),
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
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`inscricao_individual`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`inscricao_individual` (
  `nracompanhantes` INT(10) UNSIGNED ZEROFILL NOT NULL,
  `Participante_Utilizador_idutilizador` INT NOT NULL,
  `inscricao_idinscricao` INT NOT NULL,
  `telefone` INT NOT NULL,
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
  `descricao` VARCHAR(255) NOT NULL,
  `criadoem` DATETIME(6) NOT NULL,
  `idutilizadorenvia` INT NOT NULL,
  `utilizadorrecebe` INT NOT NULL,
  `assunto` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 46
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`paragem`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`paragem` (
  `paragem` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`paragem`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`responsaveis`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`responsaveis` (
  `idresponsavel` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `telefone` VARCHAR(45) NOT NULL,
  `idInscricao` INT NOT NULL,
  PRIMARY KEY (`idresponsavel`),
  INDEX `fk_Responsáveis_Inscricao` (`idInscricao` ASC) VISIBLE,
  CONSTRAINT `fk_Responsáveis_Inscricao`
    FOREIGN KEY (`idInscricao`)
    REFERENCES `les`.`inscricao` (`idinscricao`))
ENGINE = InnoDB
AUTO_INCREMENT = 3
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
-- Table `les`.`sessao_has_horario_has_dia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`sessao_has_horario_has_dia` (
  `sessao_idsessao` INT NOT NULL,
  `horario_has_dia_id_dia_hora` INT NOT NULL,
  `sessao_has_horario_has_dia_id` INT NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`sessao_has_horario_has_dia_id`),
  INDEX `fk_sessao_has_horario_has_dia_horario_has_dia1_idx` (`horario_has_dia_id_dia_hora` ASC) VISIBLE,
  INDEX `fk_sessao_has_horario_has_dia_sessao1_idx` (`sessao_idsessao` ASC) VISIBLE,
  CONSTRAINT `fk_sessao_has_horario_has_dia_horario_has_dia1`
    FOREIGN KEY (`horario_has_dia_id_dia_hora`)
    REFERENCES `les`.`horario_has_dia` (`id_dia_hora`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_sessao_has_horario_has_dia_sessao1`
    FOREIGN KEY (`sessao_idsessao`)
    REFERENCES `les`.`sessao` (`idsessao`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`tarefa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`tarefa` (
  `idtarefa` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NOT NULL,
  `concluida` TINYINT NOT NULL,
  `Coordenador_Utilizador_idutilizador` INT NOT NULL,
  `colaborador_Utilizador_idutilizador` INT NULL DEFAULT NULL,
  `hora_inicio` TIME NULL DEFAULT NULL,
  `dia_dia` DATE NULL DEFAULT NULL,
  `sessao_idsessao` INT NULL DEFAULT NULL,
  `buscar` INT NULL DEFAULT NULL,
  `levar` INT NULL DEFAULT NULL,
  `inscricao_coletiva_inscricao_idinscricao` INT NULL DEFAULT NULL,
  PRIMARY KEY (`idtarefa`),
  INDEX `fk_tarefa_Coordenador_id` (`Coordenador_Utilizador_idutilizador` ASC) VISIBLE,
  INDEX `fk_tarefa_colaborador_id` (`colaborador_Utilizador_idutilizador` ASC) VISIBLE,
  INDEX `fk_tarefa_dia1_idx` (`dia_dia` ASC) VISIBLE,
  INDEX `fk_tarefa_sessao1_idx` (`sessao_idsessao` ASC) VISIBLE,
  INDEX `fk_tarefa_espaco1_idx` (`buscar` ASC) VISIBLE,
  INDEX `fk_tarefa_espaco2_idx` (`levar` ASC) VISIBLE,
  INDEX `fk_tarefa_inscricao_coletiva1_idx` (`inscricao_coletiva_inscricao_idinscricao` ASC) VISIBLE,
  CONSTRAINT `fk_tarefa_colaborador`
    FOREIGN KEY (`colaborador_Utilizador_idutilizador`)
    REFERENCES `les`.`colaborador` (`Utilizador_idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_tarefa_Coordenador`
    FOREIGN KEY (`Coordenador_Utilizador_idutilizador`)
    REFERENCES `les`.`coordenador` (`Utilizador_idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_tarefa_dia1`
    FOREIGN KEY (`dia_dia`)
    REFERENCES `les`.`dia` (`dia`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_tarefa_espaco1`
    FOREIGN KEY (`buscar`)
    REFERENCES `les`.`espaco` (`idespaco`),
  CONSTRAINT `fk_tarefa_espaco2`
    FOREIGN KEY (`levar`)
    REFERENCES `les`.`espaco` (`idespaco`),
  CONSTRAINT `fk_tarefa_inscricao_coletiva1`
    FOREIGN KEY (`inscricao_coletiva_inscricao_idinscricao`)
    REFERENCES `les`.`inscricao_coletiva` (`inscricao_idinscricao`),
  CONSTRAINT `fk_tarefa_sessao1`
    FOREIGN KEY (`sessao_idsessao`)
    REFERENCES `les`.`sessao` (`idsessao`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 23
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`transporte`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`transporte` (
  `idtransporte` INT NOT NULL AUTO_INCREMENT,
  `capacidade` INT NOT NULL,
  `identificacao` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`idtransporte`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`transporte_has_horario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`transporte_has_horario` (
  `transporte_idtransporte` INT NOT NULL,
  `id_transporte_has_horario` INT NOT NULL AUTO_INCREMENT,
  `origem` VARCHAR(45) NOT NULL,
  `destino` VARCHAR(45) NOT NULL,
  `horario_has_dia_id_dia_hora` INT NOT NULL,
  `n_passageiros` INT NULL DEFAULT '0',
  PRIMARY KEY (`id_transporte_has_horario`),
  INDEX `fk_transporte_has_Horario_transporte_id` (`transporte_idtransporte` ASC) VISIBLE,
  INDEX `fk_transporte_has_horario_paragem1_idx` (`origem` ASC) VISIBLE,
  INDEX `fk_transporte_has_horario_paragem2_idx` (`destino` ASC) VISIBLE,
  INDEX `fk_transporte_has_horario_horario_has_dia1_idx` (`horario_has_dia_id_dia_hora` ASC) VISIBLE,
  CONSTRAINT `fk_transporte_has_horario_horario_has_dia1`
    FOREIGN KEY (`horario_has_dia_id_dia_hora`)
    REFERENCES `les`.`horario_has_dia` (`id_dia_hora`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_transporte_has_horario_paragem1`
    FOREIGN KEY (`origem`)
    REFERENCES `les`.`paragem` (`paragem`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_transporte_has_horario_paragem2`
    FOREIGN KEY (`destino`)
    REFERENCES `les`.`paragem` (`paragem`),
  CONSTRAINT `fk_transporte_has_Horario_transporte`
    FOREIGN KEY (`transporte_idtransporte`)
    REFERENCES `les`.`transporte` (`idtransporte`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `les`.`transporte_has_inscricao`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `les`.`transporte_has_inscricao` (
  `inscricao_idinscricao` INT NOT NULL,
  `transporte_has_inscricao_id` INT NOT NULL AUTO_INCREMENT,
  `transporte_has_horario_id_transporte_has_horario` INT NOT NULL,
  `n_passageiros` INT NULL DEFAULT '0',
  PRIMARY KEY (`transporte_has_inscricao_id`),
  INDEX `fk_transporte_has_inscricao_inscricao_id` (`inscricao_idinscricao` ASC) VISIBLE,
  INDEX `fk_transporte_has_inscricao_transporte_has_horario1_idx` (`transporte_has_horario_id_transporte_has_horario` ASC) VISIBLE,
  CONSTRAINT `fk_transporte_has_inscricao_inscricao`
    FOREIGN KEY (`inscricao_idinscricao`)
    REFERENCES `les`.`inscricao` (`idinscricao`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_transporte_has_inscricao_transporte_has_horario1`
    FOREIGN KEY (`transporte_has_horario_id_transporte_has_horario`)
    REFERENCES `les`.`transporte_has_horario` (`id_transporte_has_horario`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
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
  `transporte_idtransporte` INT NOT NULL,
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
  `utilizador_has_notificacao_id` INT NOT NULL AUTO_INCREMENT,
  `estado` TINYINT NOT NULL DEFAULT '0',
  PRIMARY KEY (`utilizador_has_notificacao_id`),
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
AUTO_INCREMENT = 84
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

INSERT INTO `dia_aberto` VALUES (2020,'é agora mesmo','guilhas24@gmail.com','http://www.viviana.com','2020-07-27','2020-07-29','2020-07-01','2020-07-04','2020-07-13','2020-07-16',2.8,4.2);

INSERT INTO `utilizador` VALUES (1002,'Admin','admin@admin.com','987789987','03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7',4,NULL,2020),(1004,'cordenador','cordenador@cord.com','987789010','03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7',2,NULL,2020),(1005,'prof','prof@uni.com','967109177','03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7',3,NULL,2020),(1007,'Vasco','gui24@gmail.com','987090111','03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7',0,NULL,2020),(1008,'vasco','vasco@gmail.com','909909909','03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7',0,NULL,2020),(1009,'participante','v@v.com','123123123','03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7',0,NULL,2020),(1010,'Antonio Costa','co@co.com','123456789','e3c5bd099032e227ead7c99cf6768150ddf071f939e1a669edadf409670a8ec2',1,NULL,2020),(1011,'Miguel Carlos','miguelinho@carlos.com','978090123','03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7',1,NULL,2020),(1012,'Guilherme Sousa Correia','kkk@u.com','741852933','7bd0854665d161be3d4504443e438c409ea9db07156fdbc3d5d143bc72ff4c39',5,NULL,2020),(1014,'Guilherme Sousa Correia','guilhas24@gmail.com','123456789','7bd0854665d161be3d4504443e438c409ea9db07156fdbc3d5d143bc72ff4c39',5,NULL,2020);
INSERT INTO `campus` VALUES (4,'Gambelas'),(5,'Penha');

INSERT INTO `administrador` VALUES (1002);
INSERT INTO `unidade_organica` VALUES (9,'FCT',4),(10,'FCHS',4),(11,'ESGHT',5);
INSERT INTO `curso` VALUES (6,9,'LEI'),(7,11,'Gestão');
INSERT INTO `departamento` VALUES (5,'DEEI',9),(6,'DAH',10);
INSERT INTO `professor_universitario` VALUES (1005,5),(1014,6);
INSERT INTO `participante` VALUES (1007),(1008),(1009);

INSERT INTO `colaborador` VALUES (1010,6),(1011,6),(1012,6);
INSERT INTO `coordenador` VALUES (1004,9);
INSERT INTO `disponibilidade` VALUES (1010,'2020-07-27','08:00:00','23:00:00','Sem preferência',3),(1011,'2020-07-27','08:00:00','23:00:00','Sem preferência',4);

INSERT INTO `paragem` VALUES ('Gambelas'),('Penha'),('Terminal');
INSERT INTO `notificacao` VALUES (46,'Seja bem-vindo ao site do dia aberto','2020-07-02 16:43:55.935515',-1,1003,'Bem-vindo'),(47,'Seja bem-vindo ao site do dia aberto','2020-07-02 16:44:56.197261',-1,1004,'Bem-vindo'),(48,'Seja bem-vindo ao site do dia aberto','2020-07-02 16:46:05.667510',-1,1005,'Bem-vindo'),(49,'Seja bem-vindo ao site do dia aberto','2020-07-02 16:46:39.169280',-1,1006,'Bem-vindo'),(50,'Seja bem-vindo ao site do dia aberto','2020-07-02 16:46:39.182245',-1,1006,'Bem-vindo'),(51,'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.','2020-07-02 16:47:00.415221',1002,1005,'Alteração de dados no perfil'),(52,'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.','2020-07-02 16:47:21.600009',1002,1005,'Alteração de dados no perfil'),(53,'Seja bem-vindo ao site do dia aberto','2020-07-02 16:48:24.907746',-1,1007,'Bem-vindo'),(54,'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.','2020-07-02 16:49:50.598228',1002,1007,'Alteração de dados no perfil'),(55,'Nova inscrição de 6 pessoa(s) registada na atividade Brincar Com Números na sessão das 09:30:00.\nExistem ainda 20 lugares disponiveis.','2020-07-02 17:10:31.106664',1007,1005,'Nova Inscrição'),(56,'Nova inscrição de 8 pessoa(s) registada na atividade Matemática com o Rafa na sessão das 10:00:00.\nExistem ainda 20 lugares disponiveis.','2020-07-02 17:10:31.126627',1007,1005,'Nova Inscrição'),(57,'Seja bem-vindo ao site do dia aberto','2020-07-02 17:12:35.431696',-1,1008,'Bem-vindo'),(58,'Nova inscrição de 2 pessoa(s) registada na atividade Brincar Com Números na sessão das 09:30:00.\nExistem ainda 14 lugares disponiveis.','2020-07-02 17:14:26.763385',1008,1005,'Nova Inscrição'),(59,'Nova inscrição de 11 pessoa(s) registada na atividade Matemática com o Rafa na sessão das 10:00:00.\nExistem ainda 12 lugares disponiveis.','2020-07-02 17:14:26.775353',1008,1005,'Nova Inscrição'),(60,'Seja bem-vindo ao site do dia aberto','2020-07-02 17:15:42.437086',-1,1009,'Bem-vindo'),(61,'Nova inscrição de 9 pessoa(s) registada na atividade Brincar Com Números na sessão das 09:30:00.\nExistem ainda 12 lugares disponiveis.','2020-07-02 17:17:23.654786',1009,1005,'Nova Inscrição'),(62,'Nova inscrição de 1 pessoa(s) registada na atividade Matemática com o Rafa na sessão das 10:00:00.\nExistem ainda 1 lugares disponiveis.','2020-07-02 17:17:23.666755',1009,1005,'Nova Inscrição'),(63,'Seja bem-vindo ao site do dia aberto','2020-07-02 17:22:28.231747',-1,1010,'Bem-vindo'),(64,'Seja bem-vindo ao site do dia aberto','2020-07-02 17:27:30.171184',-1,1011,'Bem-vindo'),(65,'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.','2020-07-02 17:48:34.561469',1002,1010,'Alteração de dados no perfil'),(66,'Foi atribuido uma Nova Tarefa','2020-07-02 17:50:54.431862',1004,1010,'Tarefa'),(67,'Foi atribuido uma Nova Tarefa','2020-07-02 17:51:34.395226',1004,1011,'Tarefa'),(68,'Foi atribuido uma Nova Tarefa','2020-07-02 17:53:17.006383',1004,1011,'Tarefa'),(69,'Foi atribuido uma Nova Tarefa','2020-07-02 17:58:41.995776',1004,1010,'Tarefa'),(70,'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.','2020-07-02 18:20:46.653293',-1,1002,'Alteração de dados no perfil'),(71,'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.','2020-07-02 18:21:03.130196',-1,1002,'Alteração de dados no perfil'),(72,'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.','2020-07-02 18:30:59.309272',-1,1002,'Alteração de dados no perfil'),(73,'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.','2020-07-02 19:04:44.628093',-1,1002,'Alteração de dados no perfil'),(74,'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.','2020-07-02 19:12:18.344080',-1,1002,'Alteração de dados no perfil'),(75,'Foram feitas alterações nos dados do seu perfil. Por favor consulte as alterações.','2020-07-02 19:17:06.674064',-1,1011,'Alteração de dados no perfil'),(76,'Seja bem-vindo ao site do dia aberto','2020-07-02 19:25:16.735821',-1,1013,'Bem-vindo'),(77,'Seja bem-vindo ao site do dia aberto','2020-07-02 19:27:41.233163',-1,1013,'Bem-vindo');
INSERT INTO `utilizador_has_notificacao` VALUES (1004,47,85,0),(1005,48,86,0),(1005,51,89,0),(1002,51,90,0),(1005,52,91,0),(1002,52,92,0),(1007,53,93,1),(1007,54,94,1),(1002,54,95,1),(1005,55,96,0),(1007,55,97,0),(1005,56,98,0),(1007,56,99,0),(1008,57,100,0),(1005,58,101,0),(1008,58,102,0),(1005,59,103,0),(1008,59,104,0),(1009,60,105,0),(1005,61,106,0),(1009,61,107,0),(1005,62,108,0),(1009,62,109,0),(1010,63,110,0),(1011,64,111,0),(1010,65,112,0),(1002,65,113,0),(1010,66,114,0),(1004,66,115,0),(1011,67,116,1),(1004,67,117,1),(1011,68,118,1),(1004,68,119,1),(1010,69,120,0),(1004,69,121,0),(1002,70,122,0),(1002,71,123,0),(1002,72,124,0),(1002,73,125,1),(1002,74,126,0),(1011,75,127,0);
INSERT INTO `escola` VALUES (3,'Escola Secundária Tavira','Tavira','922345678','tavira@tavira.com'),(4,'Escola Faro','Faro','978878878','faro@faro.com'),(5,'Escola do Alentejo','Alentejo','987234596','alentejo@alentejo.com');
INSERT INTO `responsaveis` VALUES (3,'eu','guilhas24@gmail.com','980090090',3),(4,'eu','vasco@mail.com','909909902',4),(5,'eu','a@a.com','982234569',5),(6,'tu','tu@tu.com','090898716',5);
INSERT INTO `horario` VALUES ('08:00:00'),('08:15:00'),('08:30:00'),('08:45:00'),('09:00:00'),('09:15:00'),('09:30:00'),('09:45:00'),('10:00:00'),('10:30:00'),('11:00:00'),('11:30:00'),('12:00:00'),('12:30:00'),('13:00:00'),('13:30:00'),('14:00:00'),('14:30:00'),('15:00:00'),('15:30:00'),('16:00:00'),('16:30:00'),('17:00:00'),('17:30:00'),('18:00:00'),('18:30:00'),('19:00:00'),('19:30:00'),('20:00:00'),('20:30:00'),('21:00:00'),('21:30:00'),('22:00:00'),('22:30:00'),('23:00:00');
INSERT INTO `dia` VALUES ('2020-07-27'),('2020-07-28'),('2020-07-29');
INSERT INTO `horario_has_dia` VALUES ('09:30:00','2020-07-27',5),('10:00:00','2020-07-27',6),('10:30:00','2020-07-27',7),('11:00:00','2020-07-27',8),('11:30:00','2020-07-27',9),('12:00:00','2020-07-27',10),('12:30:00','2020-07-27',11),('13:00:00','2020-07-27',12),('13:30:00','2020-07-27',13),('14:00:00','2020-07-27',14),('14:30:00','2020-07-27',15),('15:00:00','2020-07-27',16),('15:30:00','2020-07-27',17),('16:00:00','2020-07-27',18),('16:30:00','2020-07-27',19),('17:00:00','2020-07-27',20),('17:30:00','2020-07-27',21),('18:00:00','2020-07-27',22),('18:30:00','2020-07-27',23),('19:00:00','2020-07-27',24),('19:30:00','2020-07-27',25),('20:00:00','2020-07-27',26),('20:30:00','2020-07-27',27),('21:00:00','2020-07-27',28),('21:30:00','2020-07-27',29),('22:00:00','2020-07-27',30),('22:30:00','2020-07-27',31),('23:00:00','2020-07-27',32),('09:30:00','2020-07-28',33),('10:00:00','2020-07-28',34),('10:30:00','2020-07-28',35),('11:00:00','2020-07-28',36),('11:30:00','2020-07-28',37),('12:00:00','2020-07-28',38),('12:30:00','2020-07-28',39),('13:00:00','2020-07-28',40),('13:30:00','2020-07-28',41),('14:00:00','2020-07-28',42),('14:30:00','2020-07-28',43),('15:00:00','2020-07-28',44),('15:30:00','2020-07-28',45),('16:00:00','2020-07-28',46),('16:30:00','2020-07-28',47),('17:00:00','2020-07-28',48),('17:30:00','2020-07-28',49),('18:00:00','2020-07-28',50),('18:30:00','2020-07-28',51),('19:00:00','2020-07-28',52),('19:30:00','2020-07-28',53),('20:00:00','2020-07-28',54),('20:30:00','2020-07-28',55),('21:00:00','2020-07-28',56),('21:30:00','2020-07-28',57),('22:00:00','2020-07-28',58),('22:30:00','2020-07-28',59),('23:00:00','2020-07-28',60),('09:30:00','2020-07-29',61),('10:00:00','2020-07-29',62),('10:30:00','2020-07-29',63),('11:00:00','2020-07-29',64),('11:30:00','2020-07-29',65),('12:00:00','2020-07-29',66),('12:30:00','2020-07-29',67),('13:00:00','2020-07-29',68),('13:30:00','2020-07-29',69),('14:00:00','2020-07-29',70),('14:30:00','2020-07-29',71),('15:00:00','2020-07-29',72),('15:30:00','2020-07-29',73),('16:00:00','2020-07-29',74),('16:30:00','2020-07-29',75),('17:00:00','2020-07-29',76),('17:30:00','2020-07-29',77),('18:00:00','2020-07-29',78),('18:30:00','2020-07-29',79),('19:00:00','2020-07-29',80),('19:30:00','2020-07-29',81),('20:00:00','2020-07-29',82),('20:30:00','2020-07-29',83),('21:00:00','2020-07-29',84),('21:30:00','2020-07-29',85),('22:00:00','2020-07-29',86),('22:30:00','2020-07-29',87),('23:00:00','2020-07-29',88),('10:30:00','2020-07-27',89),('08:00:00','2020-07-27',90),('08:15:00','2020-07-27',91),('08:30:00','2020-07-27',92),('08:45:00','2020-07-27',93),('09:00:00','2020-07-27',94),('09:15:00','2020-07-27',95),('09:45:00','2020-07-27',96),('08:00:00','2020-07-28',97),('08:15:00','2020-07-28',98),('08:30:00','2020-07-28',99),('08:45:00','2020-07-28',100),('09:00:00','2020-07-28',101),('09:15:00','2020-07-28',102),('09:45:00','2020-07-28',103),('08:00:00','2020-07-29',104),('08:15:00','2020-07-29',105),('08:30:00','2020-07-29',106),('08:45:00','2020-07-29',107),('09:00:00','2020-07-29',108),('09:15:00','2020-07-29',109),('09:45:00','2020-07-29',110);
INSERT INTO `inscricao` VALUES (3,12,'Tavira','Artes',0),(4,12,'Faro','Ciências',0),(5,12,'Alentejo','Ciências',0);
INSERT INTO `inscricao_coletiva` VALUES (1,'B',1007,3,14,3),(1,'A',1008,4,13,4),(2,'B',1009,5,10,5);
INSERT INTO `atividade` VALUES (6,'Brincar Com Números',20,'Estudantes',30,'brincadeirinha',1,1005,9,5,8,'tema','2'),(7,'Matemática com o Rafa',20,'lei estudantes',30,'uma porcaria',1,1005,9,6,8,'chumbar','3');
INSERT INTO `menu` VALUES (14,'Menu do dia 27','sopa de legumes\r\nsobremesa cenoura',5,10,463);
INSERT INTO `prato` VALUES (24,'Carne','vitela cozida',37,14),(26,'Peixe','douradinhos',0,14),(28,'Vegetariano','relva doce',0,14);
INSERT INTO `inscricao_has_prato` VALUES (3,24,1,14),(4,24,2,13),(5,24,3,10);
INSERT INTO `sessao` VALUES (5,17,20,6,5),(6,20,20,7,6);
INSERT INTO `inscricao_has_sessao` VALUES (3,5,4,6),(3,6,5,8),(4,5,6,2),(4,6,7,11),(5,5,8,9),(5,6,9,1);
INSERT INTO `transporte` VALUES (2,98,'Próximo 20'),(3,95,'Próximo 20');
INSERT INTO `transporte_has_horario` VALUES (3,1,'Terminal','Penha',64,24);
INSERT INTO `transporte_has_inscricao` VALUES (3,1,1,14),(5,2,1,10);
INSERT INTO `utilizador_has_notificacao` VALUES (1004,47,85,0),(1005,48,86,0),(1005,51,89,0),(1002,51,90,0),(1005,52,91,0),(1002,52,92,0),(1007,53,93,1),(1007,54,94,1),(1002,54,95,1),(1005,55,96,0),(1007,55,97,0),(1005,56,98,0),(1007,56,99,0),(1008,57,100,0),(1005,58,101,0),(1008,58,102,0),(1005,59,103,0),(1008,59,104,0),(1009,60,105,0),(1005,61,106,0),(1009,61,107,0),(1005,62,108,0),(1009,62,109,0),(1010,63,110,0),(1011,64,111,0),(1010,65,112,0),(1002,65,113,0),(1010,66,114,0),(1004,66,115,0),(1011,67,116,1),(1004,67,117,1),(1011,68,118,1),(1004,68,119,1),(1010,69,120,0),(1004,69,121,0),(1002,70,122,0),(1002,71,123,0),(1002,72,124,0),(1002,73,125,1),(1002,74,126,0),(1011,75,127,0);
INSERT INTO `espaco` VALUES (7,'Sala 1.21',5,'images/QspcR_ye_400x400.jpg'),(8,'A',4,'images/QspcR_ye_400x400_jzTYYPT.jpg');
INSERT INTO `anfiteatro` VALUES ('1','1',8);
INSERT INTO `sala` VALUES ('1','1',NULL,7);
INSERT INTO `tarefa` VALUES (23,'gambelas',0,1004,1010,NULL,NULL,6,NULL,NULL,NULL),(24,'teste',1,1004,1011,NULL,NULL,6,NULL,NULL,NULL),(25,'teste',1,1004,1011,'10:30:00','2020-07-27',6,8,8,5);




SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
