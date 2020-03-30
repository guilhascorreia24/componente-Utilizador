
INSERT INTO `atividade` (`idAtividade`, `titulo`, `capacidade`, `publico_alvo`, `duracao`, `descricao`, `validada`, `professor_universitario_Utilizador_idutilizador`, `unidade_organica_idUO`, `Departamento_idDepartamento`, `espaco_idespaco`) VALUES
(1, 'At1', 120, '1', 1, '1', 1, 1, 2, 3, 2),
(2, 'at2', 120, '908', 1290, 'kldsfj', 1, 1, 3, 3, 3);


INSERT INTO `campus` (`idCampus`, `nome`) VALUES
(3, 'Gambelas'),
(4, 'Penha');

-- --------------------------------------------------------

INSERT INTO `departamento` (`idDepartamento`, `nome`, `unidade_organica_idUO`) VALUES
(2, 'kajshdkha', 3),
(3, 'kwjulkjf', 3);

INSERT INTO `dia` (`dia`) VALUES
('2020-03-17');
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(60, 'Notification', '0001_initial', '2020-03-30 20:25:24.367632');

INSERT INTO `espaco` (`idespaco`, `nome`, `campus_idCampus`) VALUES
(2, 'sndf,msdn', 4),
(3, 'jkwiuerwy', 4);


INSERT INTO `horario` (`hora`) VALUES
('11:34:22'),
('30:41:25');


INSERT INTO `horario_has_dia` (`horario_hora`, `Dia_dia`, `id_dia_hora`) VALUES
('11:34:22', '2020-03-17', 2);


INSERT INTO `menu` (`idMenu`, `precoAluno`, `PrecoProfessor`, `tipo`, `menu`, `Campus_idCampus`, `horario_has_dia_id_dia_hora`, `nralmoçosdisponiveis`) VALUES
(1, 1, 1, 'Carne', 'Porxo', 3, 2, 2),
(3, 1, 1, 'Peixe', 'sdfsdf', 4, 2, 100),
(4, 1, 3, 'Veg', 'Vaca', 3, 2, 5);

INSERT INTO `prato` (`idPrato`, `nralmocos`, `descricao`, `Menu_idMenu`) VALUES
(11, 12, '', 1),
(12, 13, '', 4),
(13, 1, '', 3),
(14, 12, '', 1),
(15, 12, '', 1);


INSERT INTO `professor_universitario` (`Utilizador_idutilizador`, `departamento_idDepartamento`) VALUES
(1, 3);


INSERT INTO `sessao` (`idsessao`, `nrinscritos`, `vagas`, `Atividade_idAtividade`, `horario_has_dia_id_dia_hora`) VALUES
(1, 30, 0, 1, 2),
(2, 0, 0, 1, 2);

INSERT INTO `unidade_organica` (`idUO`, `sigla`, `Campus_idCampus`) VALUES
(2, 'HFJ', 3),
(3, 'HFG', 4),
(4, 'BCG', 3);


INSERT INTO `utilizador` (`idutilizador`, `nome`, `email`, `telefone`, `password`, `userName`, `validada`) VALUES
(1, 'dsklfjsdlkfj', 'ksjdlfksjdlfjk@kjghdkfjgh.com', '987654', 'wertyuiojkwhf83ufn', 'kdsljfdfk', 1),
(2, 'jkewhrkwejhr', 'skjdfhksjdfh@gmail.vom', '09876578', 'ksdfskdjfhkjsdh', 'kjdsfhsjdkfhq', 0),
(3, 'sdfdsf', 'wersdsvsdsdv@gmaofk.smdm', '123456', 'sdfksldjfskljc', 'nada', 0);


