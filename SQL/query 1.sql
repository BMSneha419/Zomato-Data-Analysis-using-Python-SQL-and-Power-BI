SELECT
    COUNT(*) AS total_restaurants,

    ROUND(AVG(rating)::numeric, 2) AS avg_rating,

    ROUND(AVG(average_price)::numeric, 2) AS avg_price,

    ROUND(AVG(average_delivery_time)::numeric, 2) AS avg_delivery_time,

    SUM(safety_flag) AS restaurants_with_safety,

    COUNT(*) - COUNT(rating) AS missing_ratings
FROM zomato_restaurants;
