CREATE PROCEDURE dbo.shipping_today
@ship_city NVARCHAR(15), @shipping_company_id INT
AS

SELECT OrderID
FROM Orders
WHERE ShipCity = @ship_city
AND ShippedDate IS NULL
UPDATE Orders
SET ShipVia = @shipping_company_id,
ShippedDate = CURRENT_TIMESTAMP
WHERE ShipCity = @ship_city
AND ShippedDate IS NULL;
	
EXEC shipping_today 'Marseille', 3;



