mysql> SELECT * FROM etudiant where age = (select max(age) from etudiant);