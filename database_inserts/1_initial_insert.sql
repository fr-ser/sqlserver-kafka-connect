INSERT INTO kafka.dbo.increasing_ids (ship, port)
VALUES
      ('first',   'port_of_first')
    , ('second',  'port_of_second')
    , ('third',   'port_of_third')
;

INSERT INTO kafka.dbo.updated_at (ship, port, updated_at)
VALUES
      ('first',   'port_of_first',  '2020-01-01 00:38:54.840')
    , ('second',  'port_of_second', '2020-01-02 00:38:54.840')
    , ('third',   'port_of_third',  '2020-01-03 00:38:54.840')
;

INSERT INTO kafka.dbo.no_hints (ship, port)
VALUES
      ('first',   'port_of_first')
    , ('second',  'port_of_second')
    , ('third',   'port_of_third')
;
