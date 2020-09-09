SELECT * FROM drinks
JOIN bars
ON drinks.drink = (SELECT drink FROM drinks WHERE id = 4) AND bar_id = bars.id
ORDER BY price;
