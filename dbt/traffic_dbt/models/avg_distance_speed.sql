
{{ config(
    materialized='view'
) }}

select d_avg."Average Distance" as "Average Distance", s_avg."Average Speed" as "Average Speed",
 t_val."Type Count" as "Vehicle Type"
from {{ ref('avg_dist_by_type') }} as d_avg, {{ ref('avg_speed_by_type') }} as s_avg,
 {{ ref('count_by_type') }} as t_val