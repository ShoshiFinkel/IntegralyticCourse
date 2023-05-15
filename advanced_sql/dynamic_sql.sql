SELECT * FROM Products
WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM Products);

--DECLARE 
@sql NVARCHAR(1000),
@table_name NVARCHAR(50)

SET @table_name = 'Products';
SET @sql = 'SELECT * FROM ' + @table_name +
' WHERE UnitPrice > (SELECT AVG(UnitPrice) FROM ' + @table_name +');'
PRINT @sql
EXEC sp_executesql @sql

SELECT Customers.CustomerID, Orders.OrderID, Orders.OrderDate
FROM Customers
INNER JOIN Orders
ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerID;

DECLARE 
@sql NVARCHAR(1000),
@table1 NVARCHAR(50),
@table2 NVARCHAR(50);

SET @table1 = 'Customers';
SET @table2 = 'Orders';
SET @sql = 'SELECT ' + @table1 +'.CustomerID, ' + @table2 + '.OrderID, ' + @table2 +'.OrderDate
FROM ' + @table1 +
' INNER JOIN ' + @table2 +
' ON ' + @table1 +'.CustomerID = ' + @table2 +'.CustomerID
ORDER BY ' + @table1 +'.CustomerID;'
PRINT @sql;
EXEC sp_executesql @sql;


