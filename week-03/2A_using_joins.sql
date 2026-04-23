USE northwind;

/*1)Create a single query to list the product id, product name, unit price and category
name of all products. Order by category name and within that, by product name. */
SELECT ProductID, ProductName, UnitPrice, CategoryName FROM products
JOIN categories
ON products.CategoryID = categories.CategoryID
ORDER BY CategoryName, ProductName;

/*2)Create a single query to list the product id, product name, unit price and supplier
name of all products that cost more than $75. Order by product name */
SELECT ProductID, ProductName, UnitPrice, CompanyName FROM products
JOIN suppliers
ON products.SupplierID = suppliers.SupplierID
WHERE UnitPrice > 75
ORDER BY ProductName;

/*3)Create a single query to list the product id, product name, unit price, category name,
and supplier name of every product. Order by product name. */
SELECT ProductID, ProductName, UnitPrice, CategoryName, CompanyName FROM products
JOIN categories on products.CategoryID = categories.CategoryID
JOIN suppliers on products.SupplierID = suppliers.SupplierID
ORDER BY ProductName;

/*4)Create a single query to list the order id, ship name, ship address, and shipping
company name of every order that shipped to Germany. Assign the shipping company
name the alias ‘Shipper.’ Order by the name of the shipper, then the name of who it
shipped to */
SELECT orders.OrderID, orders.ShipName, orders.ShipAddress, shippers.CompanyName AS Shippers,
orders.ShipCountry 
FROM orders
JOIN shippers ON orders.ShipVia = shippers.ShipperID
WHERE ShipCountry = 'Germany'
ORDER BY Shippers, ShipName;

/*5)Start from the same query as above (#4), but omit OrderID and add logic to group by
ship name, with a count of how many orders were shipped for that ship name. */
SELECT orders.ShipName, COUNT(ShipName) AS "Number of Orders" ,orders.ShipAddress, 
shippers.CompanyName AS Shippers,
orders.ShipCountry 
FROM orders
JOIN shippers ON orders.ShipVia = shippers.ShipperID
WHERE ShipCountry = 'Germany'
GROUP BY ShipName, ShipAddress, Shippers, ShipCountry
ORDER BY Shippers, ShipName;

/*6)Create a single query to list the order id, order date, ship name, ship address of all
orders that included Sasquatch Ale. */ 
-- Used `order details` table because it had OrderID and ProductID
SELECT
	orders.OrderID,
    OrderDate,
    ShipName,
    ShipAddress,
    ProductName
FROM orders
JOIN `order details` ON `order details`.OrderID = orders.OrderID
JOIN products ON products.ProductID = `order details`.ProductID
WHERE ProductName = 'Sasquatch Ale';


