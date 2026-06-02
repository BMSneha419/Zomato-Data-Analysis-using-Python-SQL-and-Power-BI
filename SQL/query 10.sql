WITH city_performance AS (
    SELECT
        location,
        COUNT(*) AS total_restaurants,
        ROUND(AVG(rating)::numeric, 2) AS avg_rating,
        ROUND(AVG(average_price)::numeric, 2) AS avg_price,
        ROUND(AVG(average_delivery_time)::numeric, 2) AS avg_delivery_time
    FROM zomato_restaurants
    WHERE rating IS NOT NULL
    GROUP BY location
)

SELECT
    location,
    total_restaurants,
    avg_rating,
    avg_price,
    avg_delivery_time,

    -- Window Functions
    RANK() OVER (ORDER BY avg_rating DESC) AS rating_rank,
    DENSE_RANK() OVER (ORDER BY total_restaurants DESC) AS volume_rank,
    ROUND(
        avg_rating / AVG(avg_rating) OVER (),
        3
    ) AS rating_index
FROM city_performance
WHERE total_restaurants >= 50
ORDER BY rating_rank;
