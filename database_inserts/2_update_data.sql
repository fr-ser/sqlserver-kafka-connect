INSERT INTO kafka.dbo.one (ship, port) VALUES ('fourth', 'port_of_fourth');
UPDATE kafka.dbo.one SET port = 'new port of second' WHERE ship = 'second';

INSERT INTO kafka.dbo.two (train, station) VALUES ('fourth', 'station_of_fourth');
UPDATE kafka.dbo.two SET station = 'new port of second' WHERE train = 'second';
