SELECT
    price_category,
    delivery_speed_category,
    COUNT(*) AS total_restaurants,
    ROUND(AVG(rating)::numeric, 2) AS avg_rating,
    ROUND(AVG(average_delivery_time)::numeric, 2) AS avg_delivery_time
FROM zomato_restaurants
WHERE rating IS NOT NULL
GROUP BY price_category, delivery_speed_category
ORDER BY price_category, avg_rating DESC;
