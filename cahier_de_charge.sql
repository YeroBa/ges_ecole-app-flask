
Pour realiser ce projet nous avons du creer les tables suivants avec les relations definis ci-dessous ainsi que utilise le framework Flask

La table classe_eleves definis: les eleves inscrits dans un classe bien definies. Par exemple (Penda Sarr inscrit dans la classe de Terminal S2).

La table classe permet de remplire le nom des classes

La table eleve permet de remplire les attributs des eleves ainsi que l admin qui a creer ce dernier

et enfin la table user pour l administrateur du systeme

Les interfaces sont bien definies dans le code 


BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER NOT NULL,
	"username"	VARCHAR(20) NOT NULL,
	"email"	VARCHAR(120) NOT NULL,
	"image_file"	VARCHAR(20) NOT NULL,
	"password"	VARCHAR(60) NOT NULL,
	UNIQUE("username"),
	UNIQUE("email"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "classe" (
	"id"	INTEGER NOT NULL,
	"nom_classe"	VARCHAR(50) NOT NULL,
	PRIMARY KEY("id"),
	UNIQUE("nom_classe")
);
CREATE TABLE IF NOT EXISTS "eleve" (
	"id"	INTEGER NOT NULL,
	"prenom_eleve"	VARCHAR(255) NOT NULL,
	"nom_eleve"	VARCHAR(100) NOT NULL,
	"sexe"	VARCHAR(50) NOT NULL,
	"user_id"	INTEGER NOT NULL,
	PRIMARY KEY("id"),
	FOREIGN KEY("user_id") REFERENCES "user"("id")
);
CREATE TABLE IF NOT EXISTS "classe_eleves" (
	"classe_id"	INTEGER NOT NULL,
	"eleve_id"	INTEGER NOT NULL,
	"date_inscrit"	DATETIME NOT NULL,
	PRIMARY KEY("classe_id","eleve_id"),
	FOREIGN KEY("classe_id") REFERENCES "classe"("id"),
	FOREIGN KEY("eleve_id") REFERENCES "eleve"("id")
);
INSERT INTO "user" VALUES (1,'yeroba','yeroba8@gmail.com','default.jpg','$2b$12$pweox5vu3XkXFaORPrxxIun1Am/8icMbgKtO/vhBNksG0/Gu.8RW.');
INSERT INTO "classe" VALUES (1,'Terminal S1');
INSERT INTO "classe" VALUES (2,'Terminal S2');
INSERT INTO "classe" VALUES (3,'Terminal L1a');
INSERT INTO "classe" VALUES (4,'Terminal L1b');
INSERT INTO "eleve" VALUES (1,'q','ba','Masculin',1);
INSERT INTO "eleve" VALUES (2,'Penda','Sarr','Feminin',1);
INSERT INTO "classe_eleves" VALUES (1,1,'2019-10-08 01:19:49.644501');
INSERT INTO "classe_eleves" VALUES (2,2,'2019-10-08 01:29:47.757806');
COMMIT;
