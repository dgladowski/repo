DROP TABLE IF EXISTS tbmiasta;
CREATE TABLE tbmiasta
(
    idKlient INTEGER PRIMARY KEY AUTOINCREMENT,
    imięKlient TEXT(10),
    nazwiskoKlient TEXT(15)
);

DROP TABLE IF EXISTS tbpowierzchnie;
CREATE TABLE tbpowierzchnie
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    powierzchnia_miasta DECIMAL,
    powierzchnia_zielona DECIMAL,
    data_aktualizacji DATE,
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES tbmiasta(id_miasta)
);

DROP TABLE IF EXISTS tbdane_gus;
CREATE TABLE tbdane_gus
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    liczba_mieszkancow INTEGER,
    liczba_kobiet INTEGER,
    grupa_wiekowa TEXT(10),
    data_aktualizacji DATE,
    id_miasta INTEGER,
    FOREIGN KEY (id_miasta) REFERENCES tbmiasta(id_miasta)
);
