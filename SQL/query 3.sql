SELECT
    location,
    COUNT(*) AS total_restaurants,
    COUNT(rating) AS rated_restaurants,
    ROUND(AVG(rating)::numeric, 2) AS avg_rating
FROM zomato_restaurants
GROUP BY location
HAVING COUNT(rating) >= 50
ORDER BY avg_rating DESC;
