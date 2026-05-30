SELECT p.product_category_name AS product_category ,
COUNT(items.order_item_id) as total_items_sold,
ROUND(SUM(items.price),2) AS gross_revenue,
ROUND(SUM(items.price - items.freight_value),2) AS net_revenue,
ROUND((SUM(items.price - items.freight_value)/ SUM(items.price)) * 100,2) AS profit_margin_perc 

FROM order_items as items

LEFT JOIN products AS p ON p.product_id = items.product_id

GROUP BY product_category 

LIMIT 100;







SELECT customer_id

 FROM customers

LEFT JOIN orders AS o ON orders.customer_id = customers.customer_id

LEFT JOIN order_payments AS op ON op.order_id = o.order_id


WHERE op.payment_value >= 500