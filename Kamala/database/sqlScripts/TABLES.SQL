CREATE TABLE Login
(
   UserName     varchar(25) UNIQUE  NOT NULL PRIMARY KEY, 
   Password   varchar(16) NOT NULL
   
);
CREATE TABLE Accounts
(
  Ac_Number Int(8)  Unique NOT NULL PRIMARY KEY,
  Ac_Type char(25) NOT NULL,
  FinancialInstitution char(25) NOT NULL,
  UserName Varchar(25) NOT NULL,
  FOREIGN KEY (UserName)
);
CREATE TABLE Transaction
(
  Ac_Number Int(8),
  Trans_ID Varchar(25),
  Trans_Date Date NOT NULL, 
  Trans_Type Char(8) NOT NULL,
  Trans_Description Varchar(255) NOT NULL,
  Amount Varchar(5) NOT NULL,
  Location CHAR(15),
  FOREIGN KEY (Ac_Number)
);

CREATE TABLE Category
(
  MerchantName CHAR(25) NOT NULL,
  CategoryName CHAR(25) NOT NULL,
  Location char(15)
  );
  
SHOW DATABASES;
USE test;
SHOW TABLES;
