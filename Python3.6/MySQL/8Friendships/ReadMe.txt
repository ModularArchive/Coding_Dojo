Assignment: Friendships
Objectives:
Practice creating databases
Practice SQL queries and self joins
Please import friendsDB.sql.  This will create two new tables: users and friendships.  

Using the below ERD as reference, write a SQL query that returns a list of users along with their friends' names.



Your results should look like below:

first_name	last_name	friend_first_name	friend_last_name
Amy	Giver	Eli	Byers
Amy	Giver	Big	Bird
Amy	Giver	Kermit	The Frog
Eli	Byers	Kermit	The Frog
Eli 	Byers	Marky	Mark
Marky 	Mark	Big	Bird
Your actual query will look something similar to this:

SELECT * FROM users 
LEFT JOIN friendships ON ____=____ 
LEFT JOIN users as user2 ON ____ = ____
Take note that we're joining the users table again but we're specifying the second users table as user2.  You can then reference the second users by calling user2 (e.g. user2.id, user2.first_name, etc).  

You can also rename the fields that are displayed on the result by using the as keyword, like the below example:   

SELECT user2.first_name as friend_first_name, user2.last_name as friend_last_name, ...  FROM ...
Knowing how to do joins can be tricky but is used quite often and will most likely appear again in your belt exam.

Additional Exercise
Please also write the SQL queries needed to perform the following tasks:

Return all users who are friends with Kermit, make sure their names are displayed in results.
 Return the count of all friendships
Find out who has the most friends and return the count of their friends.
Create a new user and make them friends with Eli Byers, Kermit The Frog, and Marky Mark
Return the friends of Eli in alphabetical order
Remove Marky Mark from Eli’s friends.
Return all friendships, displaying just the first and last name of both friends