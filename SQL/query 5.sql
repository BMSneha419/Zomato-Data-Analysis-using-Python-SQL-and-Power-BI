SELECT
    cuisine,
    COUNT(*) AS total_restaurants,
    ROUND(AVG(average_price)::numeric, 2) AS avg_price,
    ROUND(AVG(rating)::numeric, 2) AS avg_rating,
    ROUND(AVG(average_delivery_time)::numeric, 2) AS avg_delivery_time
FROM zomato_restaurants
WHERE rating IS NOT NULL
GROUP BY cuisine
HAVING COUNT(*) >= 50
ORDER BY total_restaurants DESC;
