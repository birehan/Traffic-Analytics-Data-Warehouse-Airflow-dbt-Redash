
{{ config(
    materialized='view'
) }}

select " type" as "Vehicle Type" , COUNT("track_id") as "Type Count"
from vehicle_data
Group by " type"