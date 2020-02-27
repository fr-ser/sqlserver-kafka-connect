CREATE TABLE master.dbo.kafka_increasing_ids (
    id_num int IDENTITY(1, 1) PRIMARY KEY
  , ship VARCHAR(max) NOT NULL
  , port VARCHAR(max) NOT NULL
);

CREATE TABLE master.dbo.kafka_updated_at (
    id_num int IDENTITY(1, 1) PRIMARY KEY
  , updated_at datetime NOT NULL
  , ship VARCHAR(max) NOT NULL
  , port VARCHAR(max) NOT NULL
);

CREATE TABLE master.dbo.kafka_no_hints (
    id_num int IDENTITY(1, 1) PRIMARY KEY
  , ship VARCHAR(max) NOT NULL
  , port VARCHAR(max) NOT NULL
);
