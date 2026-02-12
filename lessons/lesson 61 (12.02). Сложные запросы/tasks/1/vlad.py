DROP TABLE Orders;
DROP TABLE Customers;
 CREATE TABLE Customers (
 CustomerID INTEGER PRIMARY KEY,
 FirstName TEXT,
 LastName TEXT,
 Email TEXT
 );
 
 CREATE TABLE Orders (
 OrderID INTEGER PRIMARY KEY,
 CustomerID INTEGER,
  OrderDate TEXT,
  Amount REAL,
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
  );
  
 INSERT INTO Customers (CustomerID, FirstName, LastName, Email)
VALUES
(1, "John", "Doe", "johndoe@example.com"),
(2, "Jane", "Smith", "janesmith@example.com");
 
  INSERT INTO Orders (OrderID, CustomerID, OrderDate, Amount)
VALUES
(101, 1, "2025-02-01", 100.50),
(102, 2, "2025-02-02", 200.75);
  
 SELECT
    A.FirstName, 
    A.LastName, 
    B.OrderID, 
    B.Amount
FROM Customers AS A
INNER JOIN Orders AS B ON A.CustomerID = B.CustomerID;



SELECT 
Customers.FirstName,
Customers.LastName,
NULL AS OrderID,
NULL AS TotalAmount

 
 
