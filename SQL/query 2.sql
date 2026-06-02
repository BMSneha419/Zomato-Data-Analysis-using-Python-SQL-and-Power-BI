SELECT 
    location,
    COUNT(*) AS total_restaurants
FROM zomato_restaurants
GROUP BY location
ORDER BY total_restaurants DESC;
