
{{ config(
    materialized='view'
) }}

select " traveled_d" as "Traveled Distance" , COUNT("track_id") as "Vehicle Count"
from vehicle_data
Group by " traveled_d"