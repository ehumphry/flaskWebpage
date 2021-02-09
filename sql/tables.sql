DROP DATABASE IF EXISTS Humphry;
CREATE DATABASE Humphry;
USE Humphry;

CREATE TABLE customerProfiles (
    firstName varchar(25),
    lastName varchar(25),
    address varchar(25),
    city varchar(25),
    state varchar(25),
    zipCode varchar(25),
    phone varchar(25),
    email varchar(25),
    customerId varchar (25),
    customerPaymentProfileId varchar (25),
    PRIMARY KEY (customerId)
);

CREATE TABLE transactions(
    customerId varchar(25),
    transactionId varchar(25),
    PRIMARY KEY (transactionId),
    FOREIGN KEY (customerId) REFERENCES customerProfiles(customerId)
);

-- DELIMITER //
-- CREATE PROCEDURE storeCustomerInformation(firstName VARCHAR(20),lastName VARCHAR(20), address VARCHAR(50), city VARCHAR(20) state VARCHAR(20) zipCode VARCHAR(5), phone VARCHAR(20), email VARCHAR(20), customerProfileId varchar (25) )
-- BEGIN
--         INSERT INTO customerProfiles (firstName, lastName, address, city, state, zipCode, phone, email, customerId passwd) VALUES (firstName,lastName,address, city, state, zipCode, phone, email, customerProfileId);
   
-- end; //

CREATE TABLE users(
    firstName varchar(25),
    lastName varchar(25),
    PRIMARY KEY (firstName)
);

INSERT INTO users (firstName, lastName)
VALUES ('Cardinal', 'Tom B. Erichsen');

