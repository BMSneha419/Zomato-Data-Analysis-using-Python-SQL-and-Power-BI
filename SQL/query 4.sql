SELECT
    rating_category,
    COUNT(*) AS total_restaurants
FROM (
    SELECT
        CASE
            WHEN rating >= 4.5 THEN 'Excellent (4.5 - 5)'
            WHEN rating >= 4.0 THEN 'Very Good (4.0 - 4.4)'
            WHEN rating >= 3.5 THEN 'Good (3.5 - 3.9)'
            WHEN rating >= 3.0 THEN 'Average (3.0 - 3.4)'
            ELSE 'Below Average (< 3.0)'
        END AS rating_category
    FROM zomato_restaurants
    WHERE rating IS NOT NULL
) sub
GROUP BY rating_category
ORDER BY total_restaurants DESC;
