SELECT Users.user_id as buyer_id, Users.join_date  as join_date, IFNULL(orders_in_2019, 0) as orders_in_2019
FROM Users 
LEFT JOIN (
SELECT buyer_id, count(*) as orders_in_2019 FROM Orders
WHERE order_date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY buyer_id) Orders ON Users.user_id = Orders.buyer_id
ORDER BY buyer_id