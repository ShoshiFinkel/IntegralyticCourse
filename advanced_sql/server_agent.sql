CREATE PROCEDURE dbo.CustomerNotification
AS
BEGIN

	EXEC sp_executesql N' USE Northwind2;'

	EXEC sp_executesql N' If object_ID(''CustomerEmail'',''V'') is not null 
					drop view CustomerEmail;'
	
	EXEC sp_executesql N' CREATE VIEW dbo.CustomerEmail
				AS
				SELECT CustomerID
				FROM Orders
				WHERE OrderDate BETWEEN DATEADD(WEEK, -1, GETDATE()) AND GETDATE();'

END;

 EXEC CustomerNotification





CREATE PROCEDURE dbo.LargeOrders
AS
BEGIN
	EXEC sp_executesql N' USE Northwind2;'
	
	EXEC sp_executesql N' If object_ID(''PriorityOrders'',''V'') is not null 
					drop view PriorityOrders;'
	
	EXEC sp_executesql N' CREATE VIEW dbo.PriorityOrders
				AS
				SELECT o.CustomerID,
					SUM(od.quantity) Total,
					CASE
						WHEN SUM(od.quantity) >= 20 THEN 1
						ELSE 0
						END AS LargeShipment
				FROM Orders o
				JOIN [Order Details] od
				ON o.OrderID = od.OrderID
				WHERE OrderDate BETWEEN DATEADD(WEEK, -1, GETDATE()) AND GETDATE()
				GROUP BY CustomerID;'

END;

EXEC LargeOrders;



INSERT INTO Orders VALUES('SIMOB', 7, '2023-05-08 00:00:00.000', '2023-05-14 00:00:00.000',	
	NULL, 2, 18.44,	'Simons bistro', 'Vinbæltet 34', 'Kobenhavn', NULL,	1734, 'Denmark');
INSERT INTO [Order Details] Values(11078, 12, 14.00, 3, 0),
	(11078, 42, 9.80, 3, 0), (11078, 51, 42.40, 6, 0.15), (11078, 11, 14.00, 4, 0);
INSERT INTO Orders VALUES('HANAR', 4, '2023-05-08 00:00:00.000', '2023-05-13 00:00:00.000',	
	NULL, 2, 65.83,	'Hanari Carnes', 'Rua do Paço, 67', 'Rio de Janeiro', 'RJ',	05454-876, 'Brazil');
INSERT INTO [Order Details] Values(11079, 12, 14.00, 3, 0),
	(11079, 42, 9.80, 7, 0), (11079, 51, 42.40, 2, 0.05), (11079, 11, 14.00, 6, 0);
INSERT INTO Orders VALUES('WELLI', 3, '2023-05-07 00:00:00.000', '2023-05-13 00:00:00.000',	
	NULL, 2, 13.97,	'Wellington Importadora', 'Rua do Mercado, 12', 'Resende', 'SP', 08737-363, 'Brazil');
INSERT INTO [Order Details] Values(11080, 55, 19.20, 3, 0.15),
	(11080, 74, 8.00, 7, 0), (11080, 2, 15.20, 2, 0.05), (11080, 16, 13.90, 6, 0);
INSERT INTO Orders VALUES('WHITC', 5, '2023-05-08 00:00:00.000', '2023-05-11 00:00:00.000',	
	NULL, 1, 4.56,	'White Clover Markets', '1029 - 12th Ave. S.', 'Seattle', 'WA', 98124, 'USA');
INSERT INTO [Order Details] Values(11081, 55, 19.20, 4, 0),
	(11081, 74, 8.00, 3, 0), (11081, 2, 15.20, 2, 0.05), (11081, 16, 13.90, 1, 0);
INSERT INTO Orders VALUES('RATTC', 8, '2023-05-09 00:00:00.000', '2023-05-13 00:00:00.000',	
	NULL, 3, 48.29,	'Rattlesnake Canyon Grocery', '2817 Milton Dr.', 'Albuquerque', 'NM', 87110, 'USA');
INSERT INTO [Order Details] Values(11082, 55, 19.20, 3, 0.15),
	(11082, 74, 8.00, 7, 0), (11082, 2, 15.20, 2, 0.05);
