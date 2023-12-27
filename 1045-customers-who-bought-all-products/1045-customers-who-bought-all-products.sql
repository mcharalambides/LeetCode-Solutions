select customer_id
from (select distinct customer_id,product_key from Customer) temp inner join Product on temp.product_key  = Product.product_key
Group By temp.customer_id
having count(*) = (select count(*) from Product)