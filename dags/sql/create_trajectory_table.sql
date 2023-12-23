 CREATE TABLE IF NOT EXISTS vehicle_trajectory (
        "detail_id" serial PRIMARY KEY,
        "track_id" bigint REFERENCES vehicle_data("track_id"),
        "lat" double precision,
        "lon" double precision,
        "speed" double precision,
        "lon_acc" double precision,
        "lat_acc" double precision,
        "time" double precision
);