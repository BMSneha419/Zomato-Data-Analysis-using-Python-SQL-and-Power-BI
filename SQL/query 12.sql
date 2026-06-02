WITH city_metrics AS (
    SELECT
        location,
        COUNT(*) AS total_restaurants,
        AVG(rating) AS avg_rating,
        AVG(average_delivery_time) AS avg_delivery_time
    FROM zomato_restaurants
    WHERE rating IS NOT NULL
    GROUP BY location
),
ranked_cities AS (
    SELECT
        location,
        total_restaurants,
        ROUND(avg_rating::numeric, 2) AS avg_rating,
        ROUND(avg_delivery_time::numeric, 2) AS avg_delivery_time,

        RANK() OVER (ORDER BY avg_rating DESC) AS rating_rank,
        RANK() OVER (ORDER BY avg_delivery_time ASC) AS delivery_speed_rank,

        ROUND(
            (avg_rating / AVG(avg_rating) OVER ())::numeric,
            3
        ) AS rating_index
    FROM city_metrics
)
SELECT *
FROM ranked_cities
ORDER BY rating_rank, delivery_speed_rank;
