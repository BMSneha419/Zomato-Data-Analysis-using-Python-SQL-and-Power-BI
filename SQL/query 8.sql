SELECT
    location,
    COUNT(*) AS total_restaurants,
    ROUND(AVG(rating)::numeric, 2) AS avg_rating,
    ROUND(AVG(average_price)::numeric, 2) AS avg_price,
    ROUND(
        AVG(rating / NULLIF(average_price, 0))::numeric, 
        4
    ) AS value_for_money_score
FROM zomato_restaurants
WHERE rating IS NOT NULL
GROUP BY location
HAVING COUNT(*) >= 50
ORDER BY value_for_money_score DESC;
