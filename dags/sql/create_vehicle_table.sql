CREATE TABLE IF NOT EXISTS vehicle_data (
    "track_id" bigint PRIMARY KEY,
    "type" text,
    "traveled_d" double precision,
    "avg_speed" double precision,
    "lat" double precision,
    "lon" double precision,
    "speed" double precision,
    "lon_acc" double precision,
    "lat_acc" double precision,
    "time" double precision
);
