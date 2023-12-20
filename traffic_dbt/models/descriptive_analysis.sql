SELECT
    COUNT(*) AS total_rows,
    AVG(" traveled_d") AS avg_traveled_d,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY " traveled_d") AS median_traveled_d,
    MIN(" traveled_d") AS min_traveled_d,
    MAX(" traveled_d") AS max_traveled_d,
    STDDEV(" traveled_d") AS stddev_traveled_d,
    
    AVG(" avg_speed") AS avg_avg_speed,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY " avg_speed") AS median_avg_speed,
    MIN(" avg_speed") AS min_avg_speed,
    MAX(" avg_speed") AS max_avg_speed,
    STDDEV(" avg_speed") AS stddev_avg_speed
    
FROM vehicle_data
