INSERT INTO kafka.dbo.ship (ship, port) VALUES ('fourth', 'port_of_fourth');
UPDATE kafka.dbo.ship SET port = 'new port of second' WHERE ship = 'second';

INSERT INTO kafka.dbo.train (train, station) VALUES ('fourth', 'station_of_fourth');
UPDATE kafka.dbo.train SET station = 'new port of second' WHERE train = 'second';
