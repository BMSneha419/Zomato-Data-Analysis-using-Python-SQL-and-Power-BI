SELECT
    location,
    restaurant_name,
    rating,
    average_price,
    average_delivery_time,
    RANK() OVER (
        PARTITION BY location
        ORDER BY rating DESC
    ) AS location_rank
FROM zomato_restaurants
WHERE rating IS NOT NULL;
