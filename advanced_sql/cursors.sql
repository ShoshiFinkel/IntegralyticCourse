DECLARE
	@counter TINYINT = 0,
	@city NVARCHAR(75),
	@total_orders INT;
DECLARE cursor_city_orders CURSOR
FOR SELECT
	c.city, COUNT(o.order_id) total_orders
	FROM sales.customers c
	JOIN sales.orders o
	ON c.customer_id = o.customer_id
	WHERE c.state = 'NY'
	GROUP BY c.city
	ORDER BY total_orders DESC;
OPEN cursor_city_orders;
FETCH NEXT FROM cursor_city_orders INTO
	@city, @total_orders;
WHILE @@FETCH_STATUS = 0 AND @counter < 10
	BEGIN
		PRINT 'City: ' + @city +', Total Orders: ' + CAST(@total_orders AS VARCHAR);
		FETCH NEXT FROM cursor_city_orders INTO
		@city, @total_orders;
		SET @counter = @counter + 1
	END;
CLOSE cursor_city_orders;
DEALLOCATE cursor_city_orders;

---

DECLARE
	@manager_id TINYINT,
	@email NVARCHAR(100),
	@pending_orders INT;
DECLARE cursor_pending_orders CURSOR
FOR SELECT
	s.manager_id ,MAX(s.email) email , COUNT(o.order_id) pending_orders
	FROM sales.staffs s
	JOIN sales.orders o
	ON s.staff_id = o.staff_id
	WHERE o.order_status = 1
	GROUP BY s.manager_id;
OPEN cursor_pending_orders;
FETCH NEXT FROM cursor_pending_orders INTO
	@manager_id, @email, @pending_orders;
WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT 'Send an email to: ' + @email +'. This manager has: ' + CAST(@pending_orders AS VARCHAR) + ' pending orders.';
		FETCH NEXT FROM cursor_pending_orders INTO
		@manager_id, @email, @pending_orders;
	END;
CLOSE cursor_pending_orders;
DEALLOCATE cursor_pending_orders;

---

DECLARE
	@order_status TINYINT = 3,
	@order_id INT;
DECLARE cursor_reject_orders CURSOR
FOR SELECT
	o.order_id
	FROM sales.orders o
	JOIN sales.staffs s
	ON o.staff_id = s.staff_id
	WHERE s.first_name LIKE 'V%'
	AND o.order_status = 1;
OPEN cursor_reject_orders;
FETCH NEXT FROM cursor_reject_orders INTO
	@order_id;
WHILE @@FETCH_STATUS = 0
	BEGIN
		UPDATE sales.orders 
		SET order_status = @order_status
		OUTPUT inserted.*
		WHERE order_id IN (SELECT
							o.order_id
							FROM sales.orders o
							JOIN sales.staffs s
							ON o.staff_id = s.staff_id
							WHERE s.first_name LIKE 'V%'
							AND o.order_status = 1);
		FETCH NEXT FROM cursor_reject_orders INTO
		@order_id;
	END;
CLOSE cursor_reject_orders;
DEALLOCATE cursor_reject_orders;



