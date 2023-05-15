----DECLARE
--@sql NVARCHAR(1000),
--@month NVARCHAR(2),
--@year NVARCHAR(4),
--@commission NVARCHAR(5)

--SET @month = '05';
--SET @year = '2016';
--SET @commission = '0.01';
--SET @sql = 'SELECT (s.first_name + SPACE(1) +s.last_name) name,
--COUNT(o.order_id) amount_of_orders,
--SUM((oi.list_price - (oi.list_price * oi.discount)) * oi.quantity) * ' + @commission + ' commission,
--SUM((oi.list_price - (oi.list_price * oi.discount)) * oi.quantity) sum_profits,
--MAX(st.store_name) store
--FROM sales.staffs s
--JOIN sales.orders o
--ON s.staff_id = o.staff_id
--JOIN sales.order_items oi
--ON o.order_id = oi.order_id
--JOIN sales.stores st
--ON s.store_id = st.store_id
--WHERE o.order_status = 4
--AND MONTH(order_date) = ' + @month + ' AND YEAR(order_date) = ' + @year +
--' GROUP BY s.first_name , s.last_name';

--PRINT @sql;
--EXEC sp_executesql @sql;


WITH latest_date AS (
	SELECT b.brand_id, b.brand_name, MAX(o.order_date) latest_date
	FROM production.brands b
	JOIN production.products p
	ON b.brand_id = p.brand_id
	JOIN sales.order_items oi
	ON p.product_id = oi.product_id
	JOIN sales.orders o
	ON oi.order_id = o.order_id
	GROUP BY b.brand_id, b.brand_name
	)
SELECT ld.brand_name, ld.latest_date, SUM(oi.list_price) total_sales
FROM latest_date ld
JOIN production.products p
ON ld.brand_id = p.brand_id
JOIN sales.order_items oi
ON p.product_id = oi.product_id
JOIN sales.orders o
ON oi.order_id = o.order_id
GROUP BY ld.brand_name, ld.latest_date














----DECLARE
--@time NVARCHAR(150),
--@sql NVARCHAR(1000);

--SET @time = 'last_execution_time';
--SET @sql ='SELECT execquery.' + @time + ' AS date_time,
--execsql.TEXT AS [Script]
--FROM sys.dm_exec_query_stats AS execquery
--CROSS APPLY sys.dm_exec_sql_text(execquery.sql_handle) AS execsql
--ORDER BY execquery.last_execution_time DESC'

--PRINT @sql;
--EXEC sp_executesql @sql;


--DECLARE
--@variable NVARCHAR(50),
--@sql NVARCHAR(1000)
--SET @variable = 'total'
--SET @sql =
--'SELECT DISTINCT
--    o.name AS ObjectName,
--    CASE o.type
--        WHEN ''U'' THEN ''Table''
--        WHEN ''V'' THEN ''View''
--        WHEN ''FN'' THEN ''Scalar Function''
--        WHEN ''IF'' THEN ''Inline Table-valued Function''
--        WHEN ''TF'' THEN ''Table-valued Function''
--        WHEN ''P'' THEN ''Stored Procedure''
--    END AS ObjectType,
--    m.definition AS ObjectDefinition
--FROM
--    sys.sql_modules m
--INNER JOIN
--    sys.objects o ON m.object_id = o.object_id
--WHERE
--    m.definition LIKE ''%'+@variable+'%''
--ORDER BY
--    ObjectType,
--    ObjectName;'
--PRINT @sql;
--EXEC sp_executesql @sql;

