SELECT
    restaurant_name,
    location,
    rating,
    average_delivery_time,

    ROUND(
        AVG(rating) OVER (PARTITION BY location)::numeric, 
        2
    ) AS city_avg_rating,

    ROUND(
        AVG(average_delivery_time) OVER (PARTITION BY location)::numeric, 
        2
    ) AS city_avg_delivery_time,

    ROUND(
        (rating - AVG(rating) OVER (PARTITION BY location))::numeric,
        2
    ) AS rating_diff_from_city_avg,

    ROUND(
        (AVG(average_delivery_time) OVER (PARTITION BY location) - average_delivery_time)::numeric,
        2
    ) AS delivery_time_advantage

FROM zomato_restaurants
WHERE rating IS NOT NULL
  AND average_delivery_time IS NOT NULL;
