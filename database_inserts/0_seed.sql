CREATE DATABASE kafka;
GO
USE kafka;
EXEC sys.sp_cdc_enable_db;

CREATE TABLE kafka.dbo.increasing_ids (
    id_num int IDENTITY(1, 1) PRIMARY KEY
  , ship VARCHAR(max) NOT NULL
  , port VARCHAR(max) NOT NULL
);

CREATE TABLE kafka.dbo.updated_at (
    id_num int IDENTITY(1, 1) PRIMARY KEY
  , updated_at datetime NOT NULL
  , ship VARCHAR(max) NOT NULL
  , port VARCHAR(max) NOT NULL
);

CREATE TABLE kafka.dbo.no_hints (
    id_num int IDENTITY(1, 1) PRIMARY KEY
  , ship VARCHAR(max) NOT NULL
  , port VARCHAR(max) NOT NULL
);

EXEC sys.sp_cdc_enable_table @source_schema = 'dbo', @source_name = 'increasing_ids', @role_name = NULL, @supports_net_changes = 0;
EXEC sys.sp_cdc_enable_table @source_schema = 'dbo', @source_name = 'updated_at', @role_name = NULL, @supports_net_changes = 0;
EXEC sys.sp_cdc_enable_table @source_schema = 'dbo', @source_name = 'no_hints', @role_name = NULL, @supports_net_changes = 0;
GO