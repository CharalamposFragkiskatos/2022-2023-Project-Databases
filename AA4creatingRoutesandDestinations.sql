

 INSERT INTO 'Destination' VALUES ('1', 'Άγαλμα Δία','Γριζάτα','5.00','11.5','10.8');
 INSERT INTO 'Destination' VALUES ('2', 'Άγαλμα Έρμή','Ζόλα','5.00','16.01','1.85');
 INSERT INTO 'Destination' VALUES ('3', 'Άγαλμα Alan Turing','Αγία Ειρήνη','10.00','1.5','1.5');
 INSERT INTO 'Destination' VALUES ('4', 'Άγαλμα Κρόνου','Κέντρο','5.00','7.5','8.1');
 INSERT INTO 'Destination' VALUES ('5', 'Άγαλμα Άγνωστου Στρατηγού','Κέντρο','10.00','6.9','7.1');
 INSERT INTO 'Destination' VALUES ('6', 'Μουσείο πολέμου','Κέντρο','5.00','7.5','9.03');
 INSERT INTO 'Destination' VALUES ('7', 'Μουσείο Μοντέρνας Τέχνης','Κέντρο','5.00','7.0','9.07');
 INSERT INTO 'Destination' VALUES ('8', 'Μουσείο Επιστημών','Κέντρο','5.00','6.41','9.12');
 INSERT INTO 'Destination' VALUES ('9', 'Μουσείο Σύγχρονης Αρχιτεκτονικής','Κέντρο','5.00','7.77','8.88');
 INSERT INTO 'Destination' VALUES ('10', 'Leopold','Πλάκα','5.00','7.01','7.02');
 INSERT INTO 'Destination' VALUES ('11','Πωσειδόνιο','Περιστέρι','5.00','9.01','9.03');
 INSERT INTO 'Destination' VALUES ('12','Ναός Διός','Περιστέρι','7.00','8.99','9.11');
 INSERT INTO 'Destination' VALUES ('13','Εκκλησία Αρχαίας Ρώμης','Περιστέρι','0','8.79','9.11');
 INSERT INTO 'Destination' VALUES ('14','Αιγυπτιακή Γέφυρα','Τζανάτα','3.00','5.32','5.22');
 INSERT INTO 'Destination' VALUES ('15','Μνημείο Πεσόντων','Κέντρο','10.00','6.9','7.11');

 INSERT INTO 'Destination' VALUES ('16','Μύρτος','Αγία Ειρήνη','0','1.01','1.03');
 INSERT INTO 'Destination' VALUES ('17','Πετανοί','Χαλάνδρι','0','5.99','6.11');
 INSERT INTO 'Destination' VALUES ('18','Αντίσαμος','Αγία Ειρήνη','0','0.79','1.11');
 INSERT INTO 'Destination' VALUES ('19','Πόρτο Χτένι','Κηφισιά','0','5.32','1.22');
 INSERT INTO 'Destination' VALUES ('20','Γυαλός','Χαλάνδρι','0','6.06','5.11');

 INSERT INTO 'Destination' VALUES ('21','Συναυλία Κορδέρου Μαυρονίου','Κέντρο','10.00','6.59','7.21');
 INSERT INTO 'Destination' VALUES ('22','Κλασικό Κονσέρτο','Άδαμας','8.00','7.99','9.11');

 INSERT INTO 'Attraction' VALUES ('1', 'Άγαλμα','0','1000');
 INSERT INTO 'Attraction' VALUES ('2', 'Άγαλμα','0','1320');
 INSERT INTO 'Attraction' VALUES ('3', 'Άγαλμα','0','1999');
 INSERT INTO 'Attraction' VALUES ('4', 'Άγαλμα','0','50');
 INSERT INTO 'Attraction' VALUES ('5', 'Άγαλμα','0','1950');
 INSERT INTO 'Attraction' VALUES ('6', 'Μουσείο','www.polem.museum.gr','2000');
 INSERT INTO 'Attraction' VALUES ('7', 'Μουσείο','www.art.museum.gr','2006');
 INSERT INTO 'Attraction' VALUES ('8', 'Μουσείο','www.sci.museum.gr','2004');
 INSERT INTO 'Attraction' VALUES ('9', 'Μουσείο','www.arch.museum.gr','2004');
 INSERT INTO 'Attraction' VALUES ('10', 'Μουσείο','www.leo.museum.gr','1999');
 INSERT INTO 'Attraction' VALUES ('11','Αρχαιολογικός Χώρος','www.poseid.gr','0');
 INSERT INTO 'Attraction' VALUES ('12','Αρχαιολογικός Χώρος','www.zeus.naos.gr','0');
 INSERT INTO 'Attraction' VALUES ('13','Ναός','www.itravel2.gr','2000');
 INSERT INTO 'Attraction' VALUES ('14','Γέφυρα','0','1058');
 INSERT INTO 'Attraction' VALUES ('15','Μνημείο','0','1950');

 INSERT INTO 'N_attraction' VALUES ('16','Παραλία');
 INSERT INTO 'N_attraction' VALUES ('17','Παραλία');
 INSERT INTO 'N_attraction' VALUES ('18','Παραλία');
 INSERT INTO 'N_attraction' VALUES ('19','Παραλία');
 INSERT INTO 'N_attraction' VALUES ('20','Παραλία');

 INSERT INTO 'event' VALUES ('21','Συναυλία','21:00','2023-05-11');
 INSERT INTO 'event' VALUES ('22','Συναυλία','21:30','2023-01-13');

 INSERT INTO 'Route' VALUES ('1', '0','Αγάλματα του Παρελθόντος','0','1h','0');
 INSERT INTO 'Route' VALUES ('2', '0','Το γαλάζιο της θάλασσας','0','1h','0');
 INSERT INTO 'Route' VALUES ('3', '0','Μουσεία','0','1h','0');
 INSERT INTO 'Route' VALUES ('4', '0','Σύγχρονη αρχιτεκτονική','0','1h','0');
 INSERT INTO 'Route' VALUES ('5', '0','Ο αρχαίος ναός Πωσειδώνιο','0','1h','0');
 INSERT INTO 'Route' VALUES ('6', '0','Ένας περίπατος στα μνημεία του πολέμου','0','1h','0');

INSERT INTO 'exists_in' VALUES ('1', '1');
INSERT INTO 'exists_in' VALUES ('1', '2');
INSERT INTO 'exists_in' VALUES ('1', '3');
INSERT INTO 'exists_in' VALUES ('1', '4');
INSERT INTO 'exists_in' VALUES ('1', '5');

INSERT INTO 'exists_in' VALUES ('2', '16');
INSERT INTO 'exists_in' VALUES ('2', '18');

INSERT INTO 'exists_in' VALUES ('3', '6');
INSERT INTO 'exists_in' VALUES ('3', '7');
INSERT INTO 'exists_in' VALUES ('3', '8');
INSERT INTO 'exists_in' VALUES ('3', '9');

INSERT INTO 'exists_in' VALUES ('4', '9');

INSERT INTO 'exists_in' VALUES ('5', '11');
INSERT INTO 'exists_in' VALUES ('5', '12');

INSERT INTO 'exists_in' VALUES ('6', '6');
INSERT INTO 'exists_in' VALUES ('6', '15');