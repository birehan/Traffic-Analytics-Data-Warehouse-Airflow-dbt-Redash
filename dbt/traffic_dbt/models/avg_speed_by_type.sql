{{ config(
    materialized='view'
) }}

select " type" as "Vehicle Type" , AVG(" avg_speed"::numeric) as "Average Speed"
from vehicle_data
Group by " type"