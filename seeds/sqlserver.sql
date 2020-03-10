CREATE DATABASE kafka;
GO
USE kafka;
EXEC sys.sp_cdc_enable_db;

CREATE TABLE kafka.dbo.ship (
    vessel_id int IDENTITY(1, 1) PRIMARY KEY
  , ship VARCHAR(max) NOT NULL
  , port VARCHAR(max) NOT NULL
);
EXEC sys.sp_cdc_enable_table @source_schema = 'dbo', @source_name = 'ship',
  @role_name = NULL, @capture_instance = 'v1-ship';

CREATE TABLE kafka.dbo.train (
    wagon_number int IDENTITY(1, 1) PRIMARY KEY
  , train VARCHAR(max) NOT NULL
  , station VARCHAR(max) NOT NULL
);
EXEC sys.sp_cdc_enable_table @source_schema = 'dbo', @source_name = 'train',
  @role_name = NULL, @capture_instance = 'v1-train';

GO
