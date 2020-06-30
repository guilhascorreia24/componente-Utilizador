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
  `Administrador_Utilizador_idutilizador` INT NOT NULL,
  `preco_almoco_estudante` FLOAT NOT NULL DEFAULT '0',
  `preco_almoco_professor` FLOAT NOT NULL,
  PRIMARY KEY (`ano`),
  INDEX `fk_dia_aberto_Administrador_id` (`Administrador_Utilizador_idutilizador` ASC) VISIBLE,
  CONSTRAINT `fk_dia_aberto_Administrador`
    FOREIGN KEY (`Administrador_Utilizador_idutilizador`)
    REFERENCES `les`.`administrador` (`Utilizador_idutilizador`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
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
  `assunto` VARCHAR(45) NOT NULL,
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

INSERT INTO `utilizador` VALUES (1002,'Admin','admin@admin.com','978989822','0afb00138d8e73348ec1fe41fd3d3a8fcbd90156b263bfa5791ba0e095f42cfc',4,NULL,NULL);

INSERT INTO `paragem` VALUES ('Gambelas'),('Penha'),('Terminal');

INSERT INTO `administrador` VALUES (1002);

INSERT INTO `dia_aberto` VALUES (2019,'Dia Aberto 2019!!!!!!!!','dia@aberto.com','http://www.diaaberto.com','2019-12-12','2019-12-12','2019-11-18','2019-11-21','2019-11-12','2019-11-14',1002,2.8,4.2),(2020,'Dia Aberto 2020!!!!!!!!!!','dia@aberto.com','http://www.diaaberto.com','2020-07-20','2020-07-24','2020-06-25','2020-07-04','2020-06-25','2020-07-04',1002,2.8,4.2);

INSERT INTO `utilizador` VALUES (1004,'Coordenador','cordenador@cord.com','981111111','03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7',2,NULL,2020),(1005,'ProfUni','profuni@uni.com','987654321','03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7',3,NULL,2020),(1006,'Colaborador','colab@colab.com','987123456','03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7',1,NULL,2020),(1007,'Coordenador2','cordenador2@cord.com','987678987','03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7',2,NULL,2020),(1008,'Participante','participante@p.com','987765492','03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7',0,NULL,2020),(1009,'Grupo','grupo@grupo.com','987101001','03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7',0,NULL,2020),(1010,'Colaborador2','colab2@colab.com','281689255','03bf9a1bb3709a941ae48af64151c57345b8acdb612b20c9f318ffd1cac2cbb7',1,NULL,2020);

INSERT INTO `dia` VALUES ('2020-07-20'),('2020-07-21'),('2020-07-22'),('2020-07-23'),('2020-07-24');

INSERT INTO `horario` VALUES ('09:30:00'),('10:00:00'),('10:30:00'),('11:00:00'),('11:30:00'),('12:00:00'),('12:30:00'),('13:00:00'),('13:30:00'),('14:00:00'),('14:30:00'),('15:00:00'),('15:30:00'),('16:00:00'),('16:30:00'),('17:00:00'),('17:30:00'),('18:00:00');

INSERT INTO `horario_has_dia` VALUES ('12:00:00','2020-07-20',7),('12:00:00','2020-07-21',8),('12:00:00','2020-07-22',9),('12:00:00','2020-07-23',10),('12:00:00','2020-07-24',11),('09:30:00','2020-07-20',12),('10:00:00','2020-07-20',13),('10:30:00','2020-07-20',14),('16:30:00','2020-07-20',15),('18:00:00','2020-07-20',16),('11:00:00','2020-07-20',20),('11:30:00','2020-07-20',21),('12:00:00','2020-07-20',22),('12:30:00','2020-07-20',23),('13:00:00','2020-07-20',24),('13:30:00','2020-07-20',25),('14:00:00','2020-07-20',26),('14:30:00','2020-07-20',27),('15:00:00','2020-07-20',28),('15:30:00','2020-07-20',29),('16:00:00','2020-07-20',30),('17:00:00','2020-07-20',32),('17:30:00','2020-07-20',33),('09:30:00','2020-07-21',35),('10:00:00','2020-07-21',36),('10:30:00','2020-07-21',37),('11:00:00','2020-07-21',38),('11:30:00','2020-07-21',39),('12:00:00','2020-07-21',40),('12:30:00','2020-07-21',41),('13:00:00','2020-07-21',42),('13:30:00','2020-07-21',43),('14:00:00','2020-07-21',44),('14:30:00','2020-07-21',45),('15:00:00','2020-07-21',46),('15:30:00','2020-07-21',47),('16:00:00','2020-07-21',48),('16:30:00','2020-07-21',49),('17:00:00','2020-07-21',50),('17:30:00','2020-07-21',51),('18:00:00','2020-07-21',52),('09:30:00','2020-07-22',53),('10:00:00','2020-07-22',54),('10:30:00','2020-07-22',55),('11:00:00','2020-07-22',56),('11:30:00','2020-07-22',57),('12:00:00','2020-07-22',58),('12:30:00','2020-07-22',59),('13:00:00','2020-07-22',60),('13:30:00','2020-07-22',61),('14:00:00','2020-07-22',62),('14:30:00','2020-07-22',63),('15:00:00','2020-07-22',64),('15:30:00','2020-07-22',65),('16:00:00','2020-07-22',66),('16:30:00','2020-07-22',67),('17:00:00','2020-07-22',68),('17:30:00','2020-07-22',69),('18:00:00','2020-07-22',70),('09:30:00','2020-07-23',71),('10:00:00','2020-07-23',72),('10:30:00','2020-07-23',73),('11:00:00','2020-07-23',74),('11:30:00','2020-07-23',75),('12:00:00','2020-07-23',76),('12:30:00','2020-07-23',77),('13:00:00','2020-07-23',78),('13:30:00','2020-07-23',79),('14:00:00','2020-07-23',80),('14:30:00','2020-07-23',81),('15:00:00','2020-07-23',82),('15:30:00','2020-07-23',83),('16:00:00','2020-07-23',84),('16:30:00','2020-07-23',85),('17:00:00','2020-07-23',86),('17:30:00','2020-07-23',87),('18:00:00','2020-07-23',88),('09:30:00','2020-07-24',89),('10:00:00','2020-07-24',90),('10:30:00','2020-07-24',91),('11:00:00','2020-07-24',92),('11:30:00','2020-07-24',93),('12:00:00','2020-07-24',94),('12:30:00','2020-07-24',95),('13:00:00','2020-07-24',96),('13:30:00','2020-07-24',97),('14:00:00','2020-07-24',98),('14:30:00','2020-07-24',99),('15:00:00','2020-07-24',100),('15:30:00','2020-07-24',101),('16:00:00','2020-07-24',102),('16:30:00','2020-07-24',103),('17:00:00','2020-07-24',104),('17:30:00','2020-07-24',105),('18:00:00','2020-07-24',106);

INSERT INTO `campus` VALUES (4,'Penha'),(5,'Gambelas');

INSERT INTO `menu` VALUES (14,'Menu do dia 20','Sopa de Alface; Sobremesa Mousse',5,7,229),(16,'Menu do dia 20','Sopa de Coentros; Sobremesa Pudim',4,7,10);

INSERT INTO `prato` VALUES (24,'Vegetariano','Tofu',0,14),(25,'Carne','Bife',21,14),(26,'Peixe','Dourada Grelhada c/ batata',0,14),(27,'Carne','Bifão',0,16),(28,'Vegetariano','Alfaces c/ tomate',0,16),(29,'Peixe','Douradinhos',0,16);

INSERT INTO `transporte` VALUES (2,90,'Próximo 20'),(3,90,'Próximo 20'),(4,90,'Próximo 20'),(5,90,'Próximo 20');

INSERT INTO `transporte_has_horario` VALUES (2,1,'Terminal','Gambelas',12,20),(3,2,'Gambelas','Terminal',16,0),(4,3,'Terminal','Penha',12,0),(5,4,'Penha','Terminal',16,0);

INSERT INTO `unidade_organica` VALUES (6,'FCT',5),(7,'ESGHT',4),(8,'FCHS',5);

INSERT INTO `curso` VALUES (6,6,'LEI'),(7,8,'Psicologia'),(8,7,'Gestão');

INSERT INTO `espaco` VALUES (7,'Sala 1.21',5,'images/frases-bonitas-1000x500.jpg'),(8,'A',4,'images/frases-bonitas-1000x500_xxun09i.jpg');

INSERT INTO `anfiteatro` VALUES ('1','0',8);

INSERT INTO `sala` VALUES ('1','1',NULL,7);

INSERT INTO `departamento` VALUES (5,'DEEI',6),(6,'DOPEO',7);

INSERT INTO `coordenador` VALUES (1004,6),(1007,7);

INSERT INTO `professor_universitario` VALUES (1005,5);

INSERT INTO `colaborador` VALUES (1006,6),(1010,8);

INSERT INTO `disponibilidade` VALUES (1006,'2020-07-20','09:30:00','18:00:00','Ajudar Docente',3),(1010,'2020-07-20','09:30:00','18:00:00','Sem preferência',4);

INSERT INTO `atividade` VALUES (6,'Brincar Com Números',20,'Estudantes',30,'brincadeirinha',1,1005,7,6,8,'Mixórdia de Tematica','2'),(7,'Psicologia a Sapos',20,'Estudantes',40,'psicologia',1,1005,6,5,7,'tema','4');

INSERT INTO `sessao` VALUES (5,10,20,6,13),(6,1,20,7,7);

INSERT INTO `escola` VALUES (3,'Secundária Tavira','Tavira','982828281','tavira@tavira.com');

INSERT INTO `participante` VALUES (1008),(1009);

INSERT INTO `inscricao` VALUES (6,12,'Tavira','Ciencias',0),(7,12,'Tavira','Ciências',0);

INSERT INTO `inscricao_individual` VALUES (0000000001,1008,6,982182123);

INSERT INTO `inscricao_coletiva` VALUES (1,'B',1009,3,20,7);

INSERT INTO `inscricao_has_prato` VALUES (6,25,4,1),(7,25,5,20);

INSERT INTO `inscricao_has_sessao` VALUES (6,6,7,1),(7,5,8,10),(7,6,9,10);

INSERT INTO `responsaveis` VALUES (3,'Leonardo Ramos','lucy@gmail.com','987101092',7);

INSERT INTO `transporte_has_inscricao` VALUES (7,3,1,20);

INSERT INTO `tarefa` VALUES (23,'Auxiliar Atividade Brincar Com Números',1,1004,1006,NULL,NULL,5,NULL,NULL,NULL),(50,'Auxilio Psicologia',0,1004,1006,NULL,NULL,6,NULL,NULL,NULL),(51,'Auxiliar Psicologia',0,1007,1006,NULL,NULL,6,NULL,NULL,NULL),(52,'Acompanhamento',0,1007,1010,'10:00:00','2020-07-20',NULL,7,8,7);

INSERT INTO `notificacao` VALUES (46,'Seja bem-vindo ao site do dia aberto','2020-06-26 13:04:31.844695',-1,1004,'Bem-vindo'),(47,'Seja bem-vindo ao site do dia aberto','2020-06-26 13:05:57.844008',-1,1005,'Bem-vindo'),(48,'Seja bem-vindo ao site do dia aberto','2020-06-26 13:16:14.117540',-1,1006,'Bem-vindo'),(63,'Foi atribuido uma Nova Tarefa','2020-06-26 13:47:09.279487',1004,1006,'Tarefa'),(64,'Foi atribuido uma Nova Tarefa','2020-06-26 13:50:13.980687',1004,1006,'Tarefa'),(65,'Foi atribuido uma Nova Tarefa','2020-06-26 13:52:46.587536',1004,1006,'Tarefa'),(66,'Foi atribuido uma Nova Tarefa','2020-06-26 13:53:50.844692',1004,1006,'Tarefa'),(67,'Seja bem-vindo ao site do dia aberto','2020-06-26 13:55:17.969872',-1,1007,'Bem-vindo'),(68,'Foi atribuido uma Nova Tarefa','2020-06-26 13:59:02.553012',1007,1006,'Tarefa'),(69,'Seja bem-vindo ao site do dia aberto','2020-06-26 14:11:44.984522',-1,1010,'Bem-vindo'),(70,'Foi atribuido uma Nova Tarefa','2020-06-26 14:19:16.897381',1007,1010,'Tarefa'),(71,'Tudo bem?','2020-06-26 14:25:20.381828',1004,1006,'Oi'),(72,'  Transporte criado com Sucesso!','2020-06-26 14:30:10.145631',-1,1002,'Submissao do Transporte'),(73,'  Transporte criado com Sucesso!','2020-06-26 14:30:56.712846',-1,1002,'Submissao do Transporte');

INSERT INTO `utilizador_has_notificacao` VALUES (1004,46,84,0),(1005,47,85,1),(1006,48,86,0),(1006,63,101,0),(1006,64,102,0),(1006,65,103,0),(1006,66,104,0),(1007,67,105,0),(1006,68,106,0),(1010,69,107,0),(1010,70,108,0),(1006,71,109,1),(1004,71,110,1),(1002,72,111,0),(1002,73,112,0);

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
