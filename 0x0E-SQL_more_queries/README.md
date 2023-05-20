
# 0x0E. SQL - More queries

## Tasks

### 0. My privileges!
script that lists all privileges of the MySQL users user\_0d\_1 and user\_0d\_2 on your server (in localhost). </br>

File:[0-privileges.sql](0-privileges.sql)

### 1. Root user
Write a script that creates the MySQL server user user\_0d\_1.

  * user\_0d\_1 should have all privileges on your MySQL server
  * The user\_0d\_1 password should be set to user\_0d\_1\_pwd
  * If the user user\_0d\_1 already exists, your script should not fail </br>

File:[1-create\_user.sql](1-create_user.sql)

### 2. Read user

Write a script that creates the database hbtn\_0d\_2 and the user user\_0d\_2.

  * user\_0d\_2 should have only SELECT privilege in the database hbtn\_0d\_2
  * The user\_0d\_2 password should be set to user\_0d\_2\_pwd
  * If the database hbtn\_0d\_2 already exists, your script should not fail
  * If the user user\_0d\_2 already exists, your script should not fail </br>

File:[2-create\_read\_user.sql](2-create_read_user.sql)

### 3. Always a name

Write a script that creates the table force\_name on your MySQL server.

  - force\_name description:
  >> id INT
  >> name VARCHAR(256) can’t be null
  - The database name will be passed as an argument of the mysql command
  - If the table force\_name already exists, your script should not fail </br>

File:[3-force\_name.sql](3-force_name.sql)

### 4. ID can't be null

Write a script that creates the table id\_not\_null on your MySQL server.

  - id\_not\_null description:
    - id INT with the default value 1
    - name VARCHAR(256)
  - The database name will be passed as an argument of the mysql command
  - If the table id\_not\_null already exists, your script should not fail </br>

File:[4-never\_empty.sql](4-never_empty.sql)

### 5. Unique ID

Write a script that creates the table unique\_id on your MySQL server.

  - unique\_id description:
    - id INT with the default value 1 and must be unique
    - name VARCHAR(256)
  - The database name will be passed as an argument of the mysql command
  - If the table unique\_id already exists, your script should not fail </br>

File:[5-unique\_id.sql](5-unique_id.sql)


### 6. States table

Write a script that creates the database hbtn\_0d\_usa and the table states (in the database hbtn\_0d\_usa) on your MySQL server.

  - states description:
    - id INT unique, auto generated, can’t be null and is a primary key
    - name VARCHAR(256) can’t be null
  - If the database hbtn\_0d\_usa already exists, your script should not fail
  - If the table states already exists, your script should not fail </br>

File:[6-states.sql](6-states.sql)

### 7. Cities table

Write a script that creates the database hbtn\_0d\_usa and the table cities (in the database hbtn\_0d\_usa) on your MySQL server.

  - cities description:
    - id INT unique, auto generated, can’t be null and is a primary key
    - state\_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
    - name VARCHAR(256) can’t be null
  - If the database hbtn\_0d\_usa already exists, your script should not fail
  - If the table cities already exists, your script should not fail </br>

File:[7-cities.sql](7-cities.sql)

### 8. Cities of California

Write a script that lists all the cities of California that can be found in the database hbtn\_0d\_usa.

  - The states table contains only one record where name = California (but the id can be different, as per the example)
  - Results must be sorted in ascending order by cities.id
  - You are not allowed to use the JOIN keyword
  - The database name will be passed as an argument of the mysql command </br>

File:[8-cities\_of\_california\_subquery.sql](8-cities_of_california_subquery.sql)
