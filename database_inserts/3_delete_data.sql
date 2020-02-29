DELETE FROM kafka.dbo.increasing_ids WHERE ship = 'first';

DELETE FROM kafka.dbo.updated_at WHERE ship = 'first';

DELETE FROM kafka.dbo.no_hints WHERE ship = 'first';
