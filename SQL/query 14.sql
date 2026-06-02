WITH location_metrics AS (
    SELECT
        location,
        COUNT(*) AS total_restaurants,
        ROUND(AVG(rating)::numeric, 2) AS avg_rating,
        ROUND(AVG(average_delivery_time)::numeric, 2) AS avg_delivery_time
    FROM zomato_restaurants
    WHERE rating IS NOT NULL
    GROUP BY location
),
benchmarks AS (
    SELECT
        *,
        AVG(avg_rating) OVER () AS overall_avg_rating,
        AVG(total_restaurants) OVER () AS overall_avg_volume
    FROM location_metrics
),
ranked_locations AS (
    SELECT
        location,
        total_restaurants,
        avg_rating,
        avg_delivery_time,
        overall_avg_rating,
        overall_avg_volume,
        RANK() OVER (ORDER BY total_restaurants DESC) AS volume_rank,
        RANK() OVER (ORDER BY avg_rating ASC) AS low_rating_rank,
        ROUND((overall_avg_rating - avg_rating)::numeric, 3) AS rating_gap
    FROM benchmarks
)
SELECT
    location,
    total_restaurants,
    avg_rating,
    avg_delivery_time,
    volume_rank,
    low_rating_rank,
    rating_gap
FROM ranked_locations
WHERE total_restaurants > overall_avg_volume
ORDER BY rating_gap DESC;
