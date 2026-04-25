USE northwind;

/*1. Write a query to find the price of the cheapest item that Northwind sells. Then write a
second query to find the name of the product that has that price.*/
SELECT MIN(UnitPrice) FROM products;
SELECT ProductID, ProductName, UnitPrice FROM products
WHERE UnitPrice = 2.5;

/*2. Write a query to find the average price of all items that Northwind sells.*/
SELECT AVG(UnitPrice) AS 'AVG_Of_All_Items' FROM products;
SELECT ROUND(AVG(UnitPrice),2)AS 'AVG_Of_All_Items' FROM products; -- Rounding to the nearest cent

/*3. Write a query to find the price of the most expensive item that Northwind sells. Then
write a second query to find the name of the product with that price, plus the name of
the supplier for that product.*/
SELECT MAX(UnitPrice) AS 'Price' FROM products;
SELECT ProductID, ProductName, UnitPrice, suppliers.CompanyName
FROM products
JOIN suppliers ON products.SupplierID = suppliers.SupplierID
WHERE UnitPrice = 263.5000;

/*4. Write a query to find total monthly payroll (the sum of all the employees’ monthly
salaries).*/
SELECT SUM(employees.Salary) AS 'TotalSalary' from employees;
SELECT FORMAT(ROUND(SUM(employees.Salary),2),2) AS 'TotalSalary' from employees;

/*5. Write a query to identify the highest salary and the lowest salary amounts which any
employee makes. (Just the amounts, not the specific employees!)*/
SELECT MAX(employees.Salary) AS 'Highest', MIN(employees.Salary) AS 'Lowest' FROM employees;

/*6. Write a query to find the name and supplier ID of each supplier and the number of
items they supply. Hint: Join is your friend here.*/
SELECT
	s.SupplierID,
    s.CompanyName AS 'SupplierName',
    COUNT(p.SupplierID) AS 'ItemsSupplied'
FROM suppliers AS s 
JOIN products AS p 
	ON s.SupplierID = p.SupplierID
GROUP BY SupplierID, SupplierName;

/*7. Write a query to find the list of all category names and the average price for items in
each category.*/
SELECT
	c.CategoryName,
    ROUND(AVG(p.UnitPrice),2) AS 'AVG_PRICE'
FROM categories AS c
JOIN products AS p
	ON p.CategoryID = c.CategoryID
GROUP BY c.CategoryName;

/*8. Write a query to find, for all suppliers that provide at least 5 items to Northwind,
what is the name of each supplier and the number of items they supply.*/
SELECT
	s.SupplierID,
    s.CompanyName AS 'Supplier',
    COUNT(p.SupplierID) AS 'ItemsSupplied'
FROM suppliers AS s
JOIN products AS p
	ON p.SupplierID = s.SupplierID
GROUP BY SupplierID, Supplier
HAVING ItemsSupplied >= 5;

/*9. Write a query to list products currently in inventory by the product id, product name,
and inventory value (calculated by multiplying unit price by the number of units on
hand). Sort the results in descending order by value. If two or more have the same
value, order by product name. If a product is not in stock, leave it off the list.*/

SELECT
	ProductID,
    ProductName,
    (UnitPrice * UnitsInStock) AS 'InventoryValue'
FROM products
WHERE UnitsInStock > 0
ORDER BY 
	InventoryValue DESC,
    ProductName
;


    




























