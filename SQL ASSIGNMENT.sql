SELECT *  FROM [SalesLT].[Customer]

SELECT [FirstName],[MiddleName],[LastName],[Suffix] FROM [SalesLT].[Customer]

SELECT [SalesPerson], CONCAT([Title], ' ',[FirstName]) AS CustomerName ,[Phone] FROM  [SalesLT].[Customer]

/*Question2*/

SELECT DISTINCT [City],[StateProvince] FROM [SalesLT].[Address] ORDER BY [City] ASC;
SELECT TOP 10 [Weight],[Name] FROM [SalesLT].[Product] WHERE [Weight] IS NOT NULL ORDER BY [Weight] DESC;

/*Question3*/
SELECT [Name],[Color],[Size],[ProductModelID] FROM [SalesLT].[Product] WHERE [ProductModelID]=1;
SELECT [ProductNumber],[Name],[Color],[Size] FROM [SalesLT].[Product] WHERE COLOR IN('Black','Red','White') AND Size IN ('S','M')
SELECT [ProductNumber],[Name],[ListPrice] FROM [SalesLT].[Product] WHERE [ProductNumber] LIKE 'BK-%'
SELECT [ProductNumber],[Name],[ListPrice] FROM [SalesLT].[Product] WHERE [ProductNumber] LIKE 'BK-%[^R]%__';

/*Notes for above query :- BK- specifies that the product number must start with "BK-".
        [^R] ensures that the next character is not "R".
        % represents any sequence of characters after that.
        - indicates that the product number must contain a dash before the final two numerals.
        __ (two underscores) specifies exactly two characters (digits in this case) at the end of the product number*/
/*Question4*/
SELECT a.[CompanyName],b.[SalesOrderID],b.[TotalDue]FROM [SalesLT].[Customer] AS a
JOIN [SalesLT].[SalesOrderHeader] AS b ON a.[CustomerID]=b.[CustomerID]
/*Combing both with JOIN*/
/*Note:-This query retrieves the CompanyName from the SalesLT.Customer table
and the SalesOrderID and TotalDue from the SalesLT.SalesOrderHeader table, 
linking them through the CustomerID to provide a report of customers and their sales orders
so: This is an alias for the table SalesLT.SalesOrderHeader. Aliases are created using the AS keyword
or simply by providing a name right after the table name in the FROM clause.
Dot Notation: When you see so.SalesOrderID or so.TotalDue, 
it means you are referencing the SalesOrderID and TotalDue columns from the table that has been aliased as so.*/

SELECT a.AddressType,a.CustomerID,so.AddressLine1,so.City,so.StateProvince,so.Postalcode,so.CountryRegion FROM SalesLT.CustomerAddress AS a
JOIN SalesLT.Address AS so ON a.AddressID = so.AddressID
WHERE a.AddressType = 'Main Office';
/*Question5*/
SELECT a.CompanyName,a.FirstName,a.LastName,so.SalesOrderID,so.TotalDue FROM SalesLT.Customer AS a
JOIN SalesLT.SalesOrderHeader AS so ON a.CustomerID  = so.CustomerID
/*Question6*/
/*Challenge 6.1 Retrieve the order ID and freight cost of each order */
 SELECT SalesOrderID,
        ROUND(Freight, 2) AS FreightCost
 FROM SalesLT.SalesOrderHeader;
 
/*Challenge 6.2 Add the shipping method */
 SELECT SalesOrderID,
        ROUND(Freight, 2) AS FreightCost,
        LOWER(ShipMethod) AS ShippingMethod
 FROM SalesLT.SalesOrderHeader;

/*Challenge 6.3 Add shipping date details */
  SELECT SalesOrderID,
        ROUND(Freight, 2) AS FreightCost,
        LOWER(ShipMethod) AS ShippingMethod,
        YEAR(ShipDate) AS ShipYear,
        DATENAME(mm, ShipDate) AS ShipMonth,
        DAY(ShipDate) AS ShipDay
 FROM SalesLT.SalesOrderHeader;



