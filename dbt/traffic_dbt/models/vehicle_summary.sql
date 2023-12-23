{{ config(materialized='view') }}

with summary as (
  
    SELECT 
    " type" as "Automobile type",
    count(" type") as "Automobile count",
    Round(AVG(Cast(" traveled_d" as numeric)),2) as "Avg distance traveled",
    Round(AVG(cast(" avg_speed" as numeric)),2) as "Avg speed by automobile"
    from vehicle_data 
    GROUP BY " type" ORDER BY "Automobile count" ASC
  
)

SELECT * from summary