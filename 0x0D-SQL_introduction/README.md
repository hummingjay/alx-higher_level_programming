
# 0x0D. SQL - Introduction

## Learning Objectives

### General

  * What’s a database
  * What’s a relational database
  * What does SQL stand for
  * What’s MySQL
  * How to create a database in MySQL
  * What does DDL and DML stand for
  * How to CREATE or ALTER a table
  * How to SELECT data from a table
  * How to INSERT, UPDATE or DELETE data
  * What are subqueries
  * How to use MySQL functions

## More Info

### Comments for SQL file

>> $ cat my\_script.sql
>> -- 11 first students in the Batch ID=11
>> -- because Batch 11 is the best!
>> SELECT id, name FROM students WHERE batch\_id = 11 ORDER BY created\_at DESC LIMIT 11;
>> $

### Install MySQL 8.0 on Ubuntu 20.04 LTS

>> $ sudo apt update
>> $ sudo apt install mysql-server
>> ...
>> $ mysql --version
>> mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86\_64 \(\(Ubuntu\)\)
>> $

## Tasks

### 0. List databases

Write a script that lists all databases of your MySQL server. </br>

File:[0-list\_databases.sql](0-list_databases.sql)

### 1. Create a database
Write a script that creates the database hbtn\_0c\_0 in your MySQL server.

  - If the database hbtn\_0c\_0 already exists, your script should not fail
  - You are not allowed to use the SELECT or SHOW statements </br>

File:[1-create\_database\_if\_missing.sql](1-create_database_if_missing.sql)

### 2. Delete a database 

Write a script that deletes the database hbtn\_0c\_0 in your MySQL server.

  - If the database hbtn\_0c\_0 doesn’t exist, your script should not fail
  - You are not allowed to use the SELECT or SHOW statements </br>

File:[2-remove\_database.sql](2-remove_database.sql)
