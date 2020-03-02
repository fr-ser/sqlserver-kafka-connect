CREATE DATABASE kafka;
GO
USE kafka;
EXEC sys.sp_cdc_enable_db;

CREATE TABLE kafka.dbo.one (
    vessel_id int IDENTITY(1, 1) PRIMARY KEY
  , ship VARCHAR(max) NOT NULL
  , port VARCHAR(max) NOT NULL
);

CREATE TABLE kafka.dbo.two (
    wagon_number int IDENTITY(1, 1) PRIMARY KEY
  , train VARCHAR(max) NOT NULL
  , station VARCHAR(max) NOT NULL
);

EXEC sys.sp_cdc_enable_table @source_schema = 'dbo', @source_name = 'one', @role_name = NULL, @supports_net_changes = 0;
EXEC sys.sp_cdc_enable_table @source_schema = 'dbo', @source_name = 'two', @role_name = NULL, @supports_net_changes = 0;
GO
