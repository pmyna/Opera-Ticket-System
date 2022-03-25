CREATE SCHEMA `Mahera` ;

CREATE TABLE `Mahera`.`Visitor` (
  `KundenNr` INT NOT NULL,
  `Vorname` VARCHAR(45) NOT NULL,
  `Nachname` VARCHAR(45) NOT NULL,
  `PLZ` VARCHAR(45) NOT NULL,
  `Ort` VARCHAR(45) NOT NULL,
  `Strasse` VARCHAR(45) NOT NULL,
  `Hausnummer` VARCHAR(45) NOT NULL,
  `Telefonnummer` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`KundenNr`));


CREATE TABLE `Mahera`.`Show` (
  `Show_ID` INT NOT NULL,
  `Datum` DATETIME NOT NULL,
  `Urhzeit` VARCHAR(45) NOT NULL,
  `Oper_ID` VARCHAR(45) NOT NULL,
  `Sprache` VARCHAR(45) NOT NULL,
  `Saal` VARCHAR(45) NOT NULL,
  `Preis_Karte_Parkett` DECIMAL(45) NOT NULL,
  `Preis_Karte_Loge` DECIMAL(45) NOT NULL,
  PRIMARY KEY (`Show_ID`))
  FOREIGN KEY (`Oper_ID`)
  REFERENCES `Mahera`.`Oper` (`Oper_ID`);


CREATE TABLE `Mahera`.`Oper` (
  `Oper_ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Oper_ID`),
  UNIQUE INDEX `Name_UNIQUE` (`Name` ASC) VISIBLE);

CREATE TABLE `Mahera`.`Reserve` (
  `Reservierungsnummer` INT NOT NULL,
  `KundenNr` INT NULL,
  `Show_ID` INT NULL,
  PRIMARY KEY (`Reservierungsnummer`))
  FOREIGN KEY (`Show_ID`)
  REFERENCES `Mahera`.`Show` (`Show_ID`)
  FOREIGN KEY (`KundenNr`)
  REFERENCES `Mahera`.`Visitor` (`KundenNr`);


  # insert data into tables

  #visitor
INSERT INTO `Mahera`.`Visitor` (`KundenNr`, `Vorname`, `Nachname`, `PLZ`, `Ort`, `Strasse`, `Hausnummer`, `Telefonnummer`) VALUES ('1', 'Henrietta', 'Lacks', '1234', 'Berlin', 'Main', '2', '1234578');
INSERT INTO `Mahera`.`Visitor` (`KundenNr`, `Vorname`, `Nachname`, `PLZ`, `Ort`, `Strasse`, `Hausnummer`, `Telefonnummer`) VALUES ('2', 'Walter', 'Salmon', '2345', 'London', 'second', '5', '2345767');
INSERT INTO `Mahera`.`Visitor` (`KundenNr`, `Vorname`, `Nachname`, `PLZ`, `Ort`, `Strasse`, `Hausnummer`, `Telefonnummer`) VALUES ('3', 'Herbert', 'Hecht', '4567', 'New York', 'third', '6a', '3478692');
INSERT INTO `Mahera`.`Visitor` (`KundenNr`, `Vorname`, `Nachname`, `PLZ`, `Ort`, `Strasse`, `Hausnummer`, `Telefonnummer`) VALUES ('4', 'Margret', 'Thatcher', '3456', 'Boston', 'Forstweg', '56', '9876584');
INSERT INTO `Mahera`.`Visitor` (`KundenNr`, `Vorname`, `Nachname`, `PLZ`, `Ort`, `Strasse`, `Hausnummer`, `Telefonnummer`) VALUES ('5', 'Cinder', 'Binder', '9876', 'Halifax', 'Arendelle', '89', '7645276');

#opern
INSERT INTO `Mahera`.`Oper` (`Oper_ID`, `Name`) VALUES ('1', 'Zauberflöte');
INSERT INTO `Mahera`.`Oper` (`Oper_ID`, `Name`) VALUES ('2', 'Aida');
INSERT INTO `Mahera`.`Oper` (`Oper_ID`, `Name`) VALUES ('3', 'Carmen');
INSERT INTO `Mahera`.`Oper` (`Oper_ID`, `Name`) VALUES ('4', 'Hänsel und Gretel');
INSERT INTO `Mahera`.`Oper` (`Oper_ID`, `Name`) VALUES ('5', 'Groschenoper');

#show
INSERT INTO `Mahera`.`Show` (`Show_ID`, `Datum`, `Urhzeit`, `Oper_ID`, `Sprache`, `Saal`, `Preis_Parkett`, `Preis_Loge`) VALUES ('1', '21.03.2022', '20:00', '4', 'deutsch', '4', '45.6', '80.5');
INSERT INTO `Mahera`.`Show` (`Show_ID`, `Datum`, `Urhzeit`, `Oper_ID`, `Sprache`, `Saal`, `Preis_Parkett`, `Preis_Loge`) VALUES ('2', '04.04.2022', '22:00', '5', 'italienisch', '6', '56.7', '105.6');
INSERT INTO `Mahera`.`Show` (`Show_ID`, `Datum`, `Urhzeit`, `Oper_ID`, `Sprache`, `Saal`, `Preis_Parkett`, `Preis_Loge`) VALUES ('3', '01.06.2022', '21:10', '3', 'spanisch', '7', '98.0', '150.8');
INSERT INTO `Mahera`.`Show` (`Show_ID`, `Datum`, `Urhzeit`, `Oper_ID`, `Sprache`, `Saal`, `Preis_Parkett`, `Preis_Loge`) VALUES ('4', '24.06.2023', '18:35', '1', 'deutsch', '2', '56.2', '100.0');
INSERT INTO `Mahera`.`Show` (`Show_ID`, `Datum`, `Urhzeit`, `Oper_ID`, `Sprache`, `Saal`, `Preis_Parkett`, `Preis_Loge`) VALUES ('5', '24.12.2023', '20:15', '2', 'italienisch', '4', '70.6', '95.8');

#reserve
INSERT INTO `Mahera`.`Reserve` (`Reservierungsnummer`, `KundenNr`, `Show_ID`) VALUES ('23456', '5', '4');
INSERT INTO `Mahera`.`Reserve` (`Reservierungsnummer`, `KundenNr`, `Show_ID`) VALUES ('45457', '4', '4');
INSERT INTO `Mahera`.`Reserve` (`Reservierungsnummer`, `KundenNr`, `Show_ID`) VALUES ('46743', '3', '3');
INSERT INTO `Mahera`.`Reserve` (`Reservierungsnummer`, `KundenNr`, `Show_ID`) VALUES ('35778', '1', '1');
INSERT INTO `Mahera`.`Reserve` (`Reservierungsnummer`, `KundenNr`, `Show_ID`) VALUES ('34637', '2', '2');


