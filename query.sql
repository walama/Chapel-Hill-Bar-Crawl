SELECT * FROM drinks
JOIN bars
ON drinks.drink_type = "beer" AND bar_id = bars.id
ORDER BY price;
