SELECT Users.user_id AS buyer_id, Users.join_date, SUM(IF(Orders.order_date >= '2019-01-01',1,0)) AS orders_in_2019 FROM Users 
LEFT JOIN Orders ON Users.user_id = Orders.buyer_id 
GROUP BY Users.user_id 
ORDER BY Users.user_id;
