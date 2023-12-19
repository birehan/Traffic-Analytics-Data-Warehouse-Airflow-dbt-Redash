CREATE TABLE IF NOT EXISTS detailed_vehicle_info (
    id SERIAL PRIMARY KEY,
    track_id bigint,
    lat double precision,
    lon double precision,
    speed double precision,
    lon_acc double precision,
    lat_acc double precision,
    time double precision,
    FOREIGN KEY (track_id) REFERENCES vehicle_data(track_id)
);
