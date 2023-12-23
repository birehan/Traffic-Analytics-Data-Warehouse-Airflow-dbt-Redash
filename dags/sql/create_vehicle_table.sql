  CREATE TABLE IF NOT EXISTS vehicle_data (
        "track_id" bigint PRIMARY KEY,
        "type" text,
        "traveled_d" double precision,
        "avg_speed" double precision
    );