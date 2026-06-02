WITH city_metrics AS (
    SELECT
        location,
        COUNT(*) AS total_restaurants,
        ROUND(AVG(rating)::numeric, 2) AS avg_rating,
        ROUND(AVG(average_delivery_time)::numeric, 2) AS avg_delivery_time
    FROM zomato_restaurants
    WHERE rating IS NOT NULL
    GROUP BY location
),
ranked_cities AS (
    SELECT
        location,
        total_restaurants,
        avg_rating,
        avg_delivery_time,

        RANK() OVER (ORDER BY avg_rating DESC) AS rating_rank,

        RANK() OVER (ORDER BY avg_delivery_time ASC) AS delivery_speed_rank
    FROM city_metrics
)
SELECT
    location,
    total_restaurants,
    avg_rating,
    avg_delivery_time,
    rating_rank,
    delivery_speed_rank,

    ROUND(
        (delivery_speed_rank - rating_rank)::numeric / NULLIF(rating_rank, 0),
        3
    ) AS delivery_gap_index
FROM ranked_cities
ORDER BY delivery_gap_index DESC;
