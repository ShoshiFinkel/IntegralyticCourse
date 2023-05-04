CREATE TRIGGER update_units_in_stock ON [Order Details]
AFTER INSERT
AS
BEGIN
DECLARE @new_product INT, @product_quantity SMALLINT
SELECT  @new_product = inserted.[ProductID] ,
		@product_quantity = INSERTED.[Quantity] FROM INSERTED
UPDATE Products SET UnitsInStock = UnitsInStock - @product_quantity 
WHERE ProductID = @new_product 
END
GO

SELECT UnitsInStock FROM Products
WHERE ProductID = 2

INSERT INTO [Order Details] (OrderID, ProductID, UnitPrice, Quantity, Discount)
VALUES (11076, 2, 15.20, 10, 0); 

SELECT UnitsInStock FROM Products
WHERE ProductID = 2