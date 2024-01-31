mysql> CREATE TABLE etage (
    -> id int NOT NULL AUTO_INCREMENT,
    -> nom VARCHAR(255) NOT NULL,
    -> numero int NOT NULL,
    -> superficie int NOT NULL,
    -> PRIMARY KEY (id)
    -> );


mysql> CREATE TABLE salle (
    -> id int NOT NULL AUTO_INCREMENT,
    -> nom VARCHAR(255) NOT NULL,
    -> numero int NOT NULL,
    -> id_etage int NOT NULL,
    -> capacite int NOT NULL,
    -> PRIMARY KEY (id)
    -> );