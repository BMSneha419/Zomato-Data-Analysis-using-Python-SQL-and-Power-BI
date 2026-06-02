SELECT
    safety_flag,
    COUNT(*) AS total_restaurants,
    ROUND(AVG(rating)::numeric, 2) AS avg_rating,
    ROUND(AVG(average_delivery_time)::numeric, 2) AS avg_delivery_time
FROM zomato_restaurants
WHERE rating IS NOT NULL
GROUP BY safety_flag
ORDER BY safety_flag DESC;
