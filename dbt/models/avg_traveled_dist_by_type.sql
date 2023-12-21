SELECT " type", AVG(" traveled_d") AS avg_distance
FROM vehicle_data
GROUP BY " type"
