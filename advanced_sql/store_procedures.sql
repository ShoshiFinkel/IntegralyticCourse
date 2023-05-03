--CREATE PROCEDURE dbo.profits_last_day
--AS
--SELECT (UnitPrice - (UnitPrice * Discount)) * Quantity AS total_price
--FROM [Order Details] AS od
--JOIN Orders o
--ON o.OrderID = od.OrderID
--WHERE o.OrderDate = (SELECT MAX(OrderDate) FROM Orders);

--EXEC profits_last_day;

--CREATE PROCEDURE dbo.points
--AS
--SELECT CustomerID, COUNT(OrderID) * 5 AS points
--FROM orders 
--GROUP BY CustomerID
--ORDER BY points DESC;


--EXEC points;

--CREATE PROCEDURE dbo.country_suppliers
--@country VARCHAR(75)
--AS
--SELECT SupplierID, Address, City, PostalCode, Country
--FROM Suppliers 
--WHERE Country = @country;

--EXEC country_suppliers 'FRANCE';

--CREATE PROCEDURE dbo.year_orders
--@year VARCHAR(4)
--AS
--WITH five_products AS(
--SELECT OrderID, COUNT(DISTINCT(ProductID)) product_amount
--FROM [Order Details]
--GROUP BY OrderID
--)
--SELECT o.OrderID, o.CustomerID, o.OrderDate 
--FROM Orders o
--JOIN five_products fp
--ON o.OrderID = fp.OrderID
--WHERE o.OrderDate like '%'+ @year + '%'
--AND fp.product_amount >= 5;


--EXEC year_orders '1996';
--CREATE PROCEDURE dbo.product_by_year_and_country
--@product VARCHAR(75), @year VARCHAR(4), @country VARCHAR(75)
--AS
--SELECT od.OrderID, o.OrderDate, od.ProductID, p.ProductName, o.ShipCountry
--FROM Orders o
--JOIN [Order Details] od
--ON o.OrderID = od.OrderID
--JOIN Products p
--ON p.ProductID = od.ProductID
--WHERE o.OrderDate like '%'+ @year + '%'
--AND o.ShipCountry = @country
--AND p.ProductName = @product;

--EXEC product_by_year_and_country'Ikura','1997', 'USA';

--DECLARE @units_in_stock INT, @supplier_id SMALLINT
--SET @units_in_stock = 20
--SET @supplier_id = 6

--SELECT *
--FROM Products
--WHERE UnitsInStock > @units_in_stock
--AND SupplierID = @supplier_id;

CREATE PROCEDURE dbo.get_late_orders
AS
WITH late_orders AS(
	SELECT OrderID FROM Orders
	WHERE (ShippedDate - OrderDate) >= 14 OR ShippedDate IS NULL
	)
UPDATE dbo.[Order Details]
SET 
Discount = Discount + 0.05
FROM [Order Details] od 
    INNER JOIN late_orders  lo 
    ON od.OrderID = lo.OrderID 
SELECT count(OrderID) FROM Orders
WHERE (ShippedDate - OrderDate) >= 14 OR ShippedDate IS NULL


EXEC get_late_orders;

SELECT count(OrderID) FROM Orders
WHERE (ShippedDate - OrderDate) >= 14 OR ShippedDate IS NULL

