CREATE TABLE public.ship (
    vessel_id INTEGER PRIMARY KEY
  , ship TEXT NOT NULL
  , port TEXT NOT NULL
);

CREATE TABLE public.train (
    wagon_number INTEGER PRIMARY KEY
  , train TEXT NOT NULL
  , station TEXT NOT NULL
);
