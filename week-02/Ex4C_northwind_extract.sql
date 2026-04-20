/*
a) The table that holds all the item that are sold is the products table.
b) The table that holds all of the categories of items sold are in the categories table. 
*/

USE northwind;

SELECT * FROM employees; 
-- 5a) The employee that has a similar name as a bird is Margaret Peacock

SELECT * FROM products;
-- 6a) 77 record was returned

SELECT * FROM categories;
-- 7c) The categorie id for seafood is 8

SELECT OrderID, OrderDate, ShipName, ShipCountry FROM orders LIMIT 50;

