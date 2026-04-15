/*
a) In the table for actor there list Columns, Indexes, Foreign Keys, and Triggers. Within 'Column', it includes actor_id, first_name, last_name, and last_update
b) Within the table 'Columns' for film, it includes film_id, title, description, etc. It includes a lot of tables that accosciate with film. 
c) Another table that contains the columns for both actor_id and film_id is in the table film_actor
d) In the rental table, it includes the date of when a film was rented or returned. Additionally, it includes the customer and employee. At first it was hard to read since there is so much information, but as you look closer it gets easier to read.
e) Within the inventory table, inventory_id, film_id, store_id, last_update.
f) I think the best table to use to understand the names of all films that were rented on a specific date, is the rental table. Since it logs all the films that was rented also using the inventory table to keep track. 
*/

SELECT rental_id FROM sakila.rental;
SELECT film_id FROM sakila.inventory;
