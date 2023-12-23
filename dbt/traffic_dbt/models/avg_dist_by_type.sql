{{ config(
    materialized='view'
) }}

SELECT " type" as "Vehicle Type", AVG(" traveled_d"::numeric) AS "Average Distance"
FROM vehicle_data
GROUP BY " type"