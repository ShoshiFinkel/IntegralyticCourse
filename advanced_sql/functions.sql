--CREATE FUNCTION dbo.supplier_products
--(@num_units_in_stock INT)
--RETURNS TABLE
--AS
--RETURN
--(WITH suppliers_below AS(
-- SELECT SupplierID, SUM(UnitsInStock) sum_units_in_stock
 --FROM Products
 --GROUP BY SupplierID
 --HAVING  SUM(UnitsInStock) < @num_units_in_stock)
 --SELECT ProductID
 --FROM Products p
 --JOIN suppliers_below s
 --ON p.SupplierID = s.SupplierID
--)
--GO

--SELECT * FROM supplier_products (60);

CREATE FUNCTION dbo.employee_orders
(@employee_id TINYINT, @year VARCHAR(4))
RETURNS INT
AS
BEGIN
	DECLARE @num_orders INT
		SELECT @num_orders = COUNT(OrderID)
		FROM Orders
		WHERE EmployeeID = @employee_id
		AND OrderDate LIKE '%'+ @year +'%'
	RETURN @num_orders
END;

SELECT dbo.employee_orders(6, '1997')
