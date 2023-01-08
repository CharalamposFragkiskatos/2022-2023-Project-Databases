BEGIN TRANSACTION;

DROP TABLE IF EXISTS "User";
CREATE TABLE IF NOT EXISTS "User" (
	"user_id"	INTEGER,
	"f_name"	STRING NOT NULL,
	"l_name"	STRING NOT NULL,
	"email"	STRING UNIQUE,
	PRIMARY KEY("user_id" )
);

DROP TABLE IF EXISTS "Guided_tour";
CREATE TABLE IF NOT EXISTS "Guided_tour" (
	"tour_id"	INTEGER,
    "name" STRING NOT NULL UNIQUE,
	"duration"	VARCHAR(5) NOT NULL DEFAULT "1.0h",  
	"date"	DATE NOT NULL CHECK("date" >= '2023-01-08'),
	"time"	TIME NOT NULL,
	"language"	TEXT NOT NULL,
    "cost" FLOAT DEFAULT 5.0 CHECK("cost" >=0.0),
	"no_of_atr"	INTEGER DEFAULT 0 NOT NULL,

	PRIMARY KEY("tour_id" )
);

DROP TABLE IF EXISTS "Reserves";
CREATE TABLE IF NOT EXISTS "Reserves" (
	"user_id"	INTEGER,
	"tour_id"	INTEGER,
    
	PRIMARY KEY("user_id","tour_id"),
    FOREIGN	KEY ("user_id") REFERENCES "User"("user_id")
    	ON	DELETE	CASCADE	ON	UPDATE	CASCADE,
    FOREIGN	KEY ("tour_id") REFERENCES "Guided_tour"("tour_id")
        ON	DELETE	CASCADE	ON	UPDATE	CASCADE
);

DROP TABLE IF EXISTS "Business";
CREATE TABLE IF NOT EXISTS "Business" (
	"b_id"	INTEGER,
	"name"	STRING NOT NULL,
	"URL"	STRING  UNIQUE DEFAULT NULL,
	"location"	VARCHAR(20) NOT NULL,
	"price_range" STRING NOT NULL,
	"rating"	REAL DEFAULT 0.0,
    "no_of_revs" integer check("no_of_revs">=0),
	"phone"	VARCHAR(15) UNIQUE DEFAULT NULL,
	"x"	DECIMAL(4,2) NOT NULL ,
	"y"	DECIMAL(4,2) NOT NULL ,
    UNIQUE("x","y"),
	PRIMARY KEY("b_id")
    
);

DROP TABLE IF EXISTS "Accomodation";
CREATE TABLE IF NOT EXISTS "Accomodation" (
	"ac_id"	INTEGER,
	"type"	TEXT,
	PRIMARY KEY("ac_id")
    FOREIGN KEY ("ac_id") REFERENCES "Business"("b_id")
        ON	DELETE	CASCADE	ON	UPDATE	CASCADE
);

DROP TABLE IF EXISTS "Estiasi";
CREATE TABLE IF NOT EXISTS "Estiasi" (
	"e_id"	INTEGER,
	"type"	TEXT,
	PRIMARY KEY("e_id")
    FOREIGN KEY ("e_id") REFERENCES "Business"("b_id")
        ON	DELETE	CASCADE	ON	UPDATE	CASCADE
);

DROP TABLE IF EXISTS "Review";
CREATE TABLE IF NOT EXISTS "Review" (
	"user_id"	INTEGER,
	"b_id"	INTEGER,
	"comment"	TEXT DEFAULT NULL,
	"rating"	DECIMAL(2,1) NOT NULL CHECK("rating" BETWEEN 0.0 AND 5.0),
	"date"	INTEGER NOT NULL CHECK("date" BETWEEN '2016-01-08' AND '2022-12-31'),
	PRIMARY KEY("user_id","b_id"),
    FOREIGN	KEY ("user_id") REFERENCES "User"("user_id"),
    FOREIGN	KEY ("b_id") REFERENCES "Business"("b_id") 
        ON	DELETE	CASCADE	ON	UPDATE	CASCADE  
        
);


DROP TABLE IF EXISTS "Destination";
CREATE TABLE IF NOT EXISTS "Destination" (
	"dest_id"	integer ,
	"title"	VARCHAR(20) NOT NULL,
    "location"	VARCHAR(20) NOT NULL,
    "cost"	FLOAT DEFAULT 0 CHECK ("cost" >=0.0),
    "x"	DECIMAL(4,2) NOT NULL ,
    "y"	DECIMAL(4,2) NOT NULL,
    UNIQUE ("x","y"),
	PRIMARY KEY("dest_id")
);

DROP TABLE IF EXISTS "Exists_in";
CREATE TABLE IF NOT EXISTS "Exists_in" (
    "r_id" integer,
    "dest_id" integer,
    PRIMARY KEY("dest_id", "r_id"),
    FOREIGN KEY("r_id") REFERENCES "Route"("r_id")
        ON DELETE CASCADE ON UPDATE CASCADE
    FOREIGN KEY("dest_id") REFERENCES "Destination"("dest_id")
        ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS "Route";
CREATE TABLE IF NOT EXISTS "Route" (
    "r_id" integer,
    "total_cost" float check ("cost" >= 0.0),
    "title" string,
    "no_of_dest" integer default 0,
    "est_time" float NOT NULL,
    "distance" float NOT NULL CHECK ("distance">=0.0),
    PRIMARY KEY("r_id")
);

DROP TABLE IF EXISTS "Event";
CREATE TABLE IF NOT EXISTS "Event" (
	"ev_id"	integer ,
	"type"	VARCHAR(10) NOT NULL,
    "time"	TIME ,
    "date"	DATE NOT NULL CHECK("date">='2023-01-08'),
	PRIMARY KEY("ev_id"),
    FOREIGN KEY("ev_id") REFERENCES "Destination"("dest_id")
        ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS "Attraction";
CREATE TABLE IF NOT EXISTS "Attraction" (
	"atr_id"	integer ,
	"type"	VARCHAR(10) NOT NULL,
    "URL"	VARCHAR(15) ,
    "contrustion_date"	DATE,
	PRIMARY KEY("atr_id"),
    FOREIGN KEY("atr_id") REFERENCES "Destination"("dest_id")
        ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS "N_attraction";
CREATE TABLE IF NOT EXISTS "N_attraction" (
	"na_id"	integer ,
	"type"	VARCHAR(10) NOT NULL,
	PRIMARY KEY("na_id"),
    FOREIGN KEY("na_id") REFERENCES "Destination"("dest_id")
        ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS "Includes";
CREATE TABLE IF NOT EXISTS "Includes" (
    "tour_id" integer ,
    "atr_id" integer ,
    PRIMARY KEY("atr_id", "tour_id"),
    FOREIGN KEY("tour_id") REFERENCES "Guided_tour"("tour_id")
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY("atr_id") REFERENCES "Attraction"("atr_id")
        ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS "Activity";
CREATE TABLE IF NOT EXISTS "Activity" (
	"act_id"	integer ,
	"na_id"	integer ,
    "cost"	DECIMAL(5,2) CHECK ("cost">=0.0),
    "title"	varchar(10) NOT NULL,
    "type"	varchar(10) NOT NULL,
	PRIMARY KEY("na_id","act_id"),
    FOREIGN KEY("na_id") REFERENCES "N_attraction"("na_id")
);

DROP TABLE IF EXISTS "transport";
CREATE TABLE IF NOT EXISTS "transport" (
	"trans_id"	integer ,
	"type"	VARCHAR(10) NOT NULL,
    "line"	VARCHAR(10) NOT NULL,
	PRIMARY KEY("trans_id")
);

DROP TABLE IF EXISTS "cov_locations";
CREATE TABLE IF NOT EXISTS "cov_locations" (
	"trans_id"	integer ,
    "location_name" VARCHAR(20) ,
	PRIMARY KEY("trans_id", "location_name"),
    FOREIGN KEY("trans_id") REFERENCES "transport"("trans_id")
        ON DELETE CASCADE ON UPDATE CASCADE 
);


DROP TABLE IF EXISTS "Saved";
CREATE TABLE IF NOT EXISTS "Saved"(
    "user_id" integer ,
    "r_id" integer,
    PRIMARY KEY("user_id","r_id"),
    FOREIGN KEY("user_id") REFERENCES "User"("user_id"),
    FOREIGN KEY("r_id") REFERENCES "Route"("r_id")
);


DROP TRIGGER IF EXISTS "route_count_trig";
    CREATE TRIGGER IF NOT EXISTS "route_count_trig"
    AFTER INSERT ON EXISTS_IN
	FOR EACH ROW
    BEGIN
	UPDATE ROUTE 
    SET no_of_dest=no_of_dest + 1,
        total_cost = total_cost + (select d.cost from destination as d where d.dest_id=new.dest_id)

    where new.r_id = ROUTE.r_id;

	END;



DROP TRIGGER IF EXISTS "guided_tour_trig";
    CREATE TRIGGER IF NOT EXISTS "guided_tour_trig"
    AFTER INSERT ON INCLUDES
	FOR EACH ROW
    BEGIN
	UPDATE GUIDED_TOUR 
    SET no_of_atr= no_of_atr +1
    
    WHERE new.tour_id = GUIDED_TOUR.tour_id;
    END;

DROP TRIGGER IF EXISTS "main"."business_count_trig";
CREATE TRIGGER IF NOT EXISTS "business_count_trig"
    AFTER INSERT ON REVIEW
    BEGIN
	UPDATE BUSINESS 
    SET no_of_revs=  no_of_revs  + 1, 
	rating = ROUND(rating + (new.rating - rating)/(no_of_revs +1),1)
	 
	where business.b_id == new.b_id;
    END;

drop index if exists "dest_location_idx";
create index if not exists "dest_rating_idx" on "destination"("location");


drop index if exists "bus_rating_idx";
CREATE INDEX "bus_rating_idx" ON "business"("rating");

COMMIT;