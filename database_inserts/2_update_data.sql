INSERT INTO kafka.dbo.increasing_ids (ship, port) VALUES ('fourth',   'port_of_fourth');
INSERT INTO kafka.dbo.increasing_ids (ship, port) VALUES ('second',   'new port of second');

INSERT INTO kafka.dbo.updated_at (ship, port, updated_at)
VALUES ('fourth',   'port_of_fourth',  '2020-01-04 00:38:54.840');
UPDATE kafka.dbo.updated_at SET
        port = 'new port of second'
    ,   updated_at = '2020-01-05 00:38:54.840'
WHERE ship = 'second';


INSERT INTO kafka.dbo.no_hints (ship, port) VALUES ('fourth',   'port_of_fourth');
UPDATE kafka.dbo.no_hints SET port = 'new port of second' WHERE ship = 'second';
