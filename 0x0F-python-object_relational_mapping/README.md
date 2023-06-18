
# 0x0F. Python - Object-relational mapping

## Tasks

### [0. Get all states](0-select_states.py)

Write a script that lists all `states` from the database hbtn\_0e\_0\_usa:

  * Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
  * You must use the module `MySQLdb` (`import MySQLdb`)
  * Your script should connect to a MySQL server running on `localhost` at port `3306`
  * Results must be sorted in ascending order by `states.id`
  * Results must be displayed as they are in the example below
  * Your code should not be executed when imported </br>

File: [0-select\_states.py](0-select_states.py)

### [1. Filter states](1-filter_states.py)
> Write a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`:

File: [1-filter\_states.py](1-filter_states.py)

### [2. Filter states by user input](2-my_filter_states.py)
> Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where name matches the argument.

File: [2-my\_filter\_states.py](2-my_filter_states.py)

### [3. SQL Injection...](3-my_safe_filter_states.py)
> Wait, do you remember the previous task? Did you test `"Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '"` as an input?
> What? Empty?
> Yes, it’s an SQL injection to delete all records of a table…

File:[3-my\_safe\_filter\_states.py](3-my_safe_filter_states.py)

### [4. Cities by states](4-cities_by_state.py)

> Write a script that lists all `cities` from the database `hbtn_0e_4_usa`

File: [4-cities\_\by\_state.py](4-cities_by_state.py)

### [5. All cities by state](5-filter_cities.py)

> Write a script that takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`

File: [5-filter\_cities.py](5-filter_cities.py)

### [6. First state model](model_state.py)

Write a python file that contains the class definition of a `State` and an instance `Base = declarative_base()`:
 * `state` class:
    * inherits from `Base` Tips
    * links to the MySQL table `states`
    * class attribute `id` that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
    * class attribute `name` that represents a column of a string with maximum 128 characters and can’t be null

 * You must use the module `SQLAlchemy`
 * Your script should connect to a MySQL server running on `localhost` at port `3306`
 * __WARNING__: all classes who inherit from `Base` must be imported before calling `Base.metadata.create_all(engine)`

File: [model\_state.py](model_state.py)

### [7. All states via SQLAlchemy](7-model_state_fetch_all.py)

> Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`

File: [7-model\_state\_fetch\_all.py](7-model_state_fetch_all.py)

### [8. First state](8-model_state_fetch_first.py)

> Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`

File: [8-model\_state\_fetch\_first.py](8-model_state_fetch_first.py)

### [9. Contains \`a\`](9-model_state_filter_a.py)

> Write a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`

File: [9-model\_state\_filter\_a.py](9-model_state_filter_a.py)

### [10. Get a state](10-model_state_my_get.py)

> Write a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`

File: [10-model\_state\_my\_get.py](10-model_state_my_get.py)

### [11. Add a new state](11-model_state_insert.py)

> Write a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`

File: [11-model\_state\_insert.py](11-model_state_insert.py)

### [12. Update a state](12-model_state_update_id_2.py)

> Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`

FIle: [12-model\_state\_update\_id\_2.py](12-model_state_update_id_2.py)

### [13. Delete states ](13-model_state_delete_a.py)

> Write a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`

FIle: [13-model\_state\_delete\_a.py](13-model_state_delete_a.py)

### [14. Cities in state](14-model_city_fetch_by_state.py)

> Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a `City`.
* City class:
  * inherits from Base (imported from model\_state)
  * links to the MySQL table cities
  * class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
  * class attribute name that represents a column of a string of 128 characters and can’t be null
  * class attribute state\_id that represents a column of an integer, can’t be null and is a foreign key to `states.id`
* You must use the module `SQLAlchemy`

> Next, write a script `14-model_city_fetch_by_state.py` that prints all `City` objects from the database `hbtn_0e_14_usa`:

File: [14-model\_city\_fetch\_by\_state.py](14-model_city_fetch_by_state.py), [model\_city.py](model_city.py)
