Assignment: Product
Objectives:
Practice creating a class and making instances from it
Practice accessing the methods and attributes of different instances
Practice altering an instance's attributes
The owner of a store wants a program to track products. Create a product class to fill the following requirements.

Product Class:
Attributes:

Price
Item Name
Weight
Brand
Status: default "for sale"
Methods:

Sell: changes status to "sold"
Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
Return Item: takes reason_for_return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been opened, set the status to "used" and apply a 20% discount.  (use "defective", "like_new", or "opened" as three possible value for reason_for_return).
Display Info: show all product details.
Every method that doesn't have to return something should return self so methods can be chained.