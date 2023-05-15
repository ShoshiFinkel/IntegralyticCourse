
DECLARE
	@year SMALLINT,
	@profits DECIMAL(10,2),
	@store_id INT,
--	@sql NVARCHAR(1000)

SET @store_id = 2
SET @sql = 'DECLARE cursor_stores_profits CURSOR FOR
			SELECT YEAR(o.order_date) year, SUM((oi.list_price - (oi.list_price * oi.discount)) * oi.quantity) profits
			FROM sales.orders o
			JOIN sales.order_items oi
			ON o.order_id = oi.order_id
			WHERE o.store_id = '+CAST(@store_id AS varchar) + 
			' GROUP BY YEAR(o.order_date)
			ORDER BY SUM((oi.list_price - (oi.list_price * oi.discount)) * oi.quantity) DESC;'

EXEC sp_executesql @sql;

OPEN cursor_stores_profits;
FETCH NEXT FROM cursor_stores_profits INTO
	@year, @profits;
WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT 'The profit of store ' + CAST(@store_id AS VARCHAR) + ' for ' + CAST(@year AS VARCHAR) + ' is: ' + CAST(@profits AS VARCHAR);
		FETCH NEXT FROM cursor_stores_profits INTO
		@year, @profits;
	END;
CLOSE cursor_stores_profits;
DEALLOCATE cursor_stores_profits;

---


DECLARE
	@product_id INT,
	@list_price DECIMAL(8,2),
	@new_table_name NVARCHAR(75) = 'production.productid',
	@price_increase DECIMAL(4,2) = 0.05,
	@year_increase SMALLINT = 2019,
	@sql NVARCHAR(MAX)

SET @sql = 'DECLARE price_increase CURSOR FOR
			SELECT product_id, list_price
			FROM production.products
			WHERE product_id IN (13, 4, 6, 7, 12);'

EXEC sp_executesql @sql;

OPEN price_increase;
FETCH NEXT FROM price_increase INTO
	@product_id, @list_price;
WHILE @@FETCH_STATUS = 0
	BEGIN
		DECLARE @create_table NVARCHAR(MAX)
		SET @create_table = 'IF NOT EXISTS (SELECT * FROM sysobjects WHERE name = ''' + @new_table_name + CAST(@product_id AS varchar) + ''' and xtype=''U'')
			CREATE TABLE ' + @new_table_name + CAST(@product_id AS varchar) + ' (
			pricing_id INT IDENTITY PRIMARY KEY,
			year SMALLINT,
			price DECIMAL(8,2));
		    INSERT INTO ' + @new_table_name + CAST(@product_id AS varchar) + ' (year, price)
			SELECT ' + CAST(@year_increase AS varchar) + ' , list_price + (list_price * ' + CAST(@price_increase AS varchar) + ') new_price
			FROM production.products
			WHERE product_id = ' + CAST(@product_id AS varchar) +' ;'
		EXEC sp_executesql @create_table
		FETCH NEXT FROM price_increase INTO
		@product_id, @list_price;
	END;
CLOSE price_increase;
DEALLOCATE price_increase;
