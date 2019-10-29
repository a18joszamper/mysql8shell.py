#
# MySQL 8 Shell
#
# This example shows a simple X DevAPI script to work with relational data
#
from mysqlsh import mysqlx # needed in case you run the code outside of the shell
# SQL CREATE TABLE statement
CREATE_TBL = """
CREATE TABLE `botiga`.`caixer` (
  id_caixer int primary key,
  dni_caixer varchar(9),
  nom_caixer varchar(45),
  cognom_caixer varchar(45),
  ntelf_caixer varchar(9)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
"""

# column list, user data structure
COLUMNS = ['id_caixer', 'dni_caixer', 'nom_caixer','cognom_caixer','ntelf_caixer']

user_info = {
  'host': 'localhost',
  'port': 33060,
  'user': 'root',
  'password': 'root',
}

print("Listing 4-6 Example - Python X DevAPI Demo with Relational Data.")

# Get a session (connection)
my_session = mysqlx.get_session(user_info)
# Precautionary drop schema
my_session.drop_schema('botiga')
# Create the database (schema)
my_db = my_session.create_schema('botiga')
# Execute the SQL statement to create the table
sql_res = my_session.sql(CREATE_TBL).execute()
# Get the table object
my_tbl = my_db.get_table('caixer')
# Insert some rows (data)
my_tbl.insert(COLUMNS).values( 123, "12366677Z", "Roser", "Avellan", "934524565").execute()
my_tbl.insert(COLUMNS).values( 54, "14366677W", "Fran", "Català", "932457825").execute()
my_tbl.insert(COLUMNS).values( 34, "11363547X", "Pau", "Barber", "938742595").execute()
my_tbl.insert(COLUMNS).values( 23, "12366677E", "Lluc", "Avellan", "932541525").execute()
# Execute a simple select (SELECT ∗ FROM)
print("\nShowing results after inserting all rows.")
my_res = my_tbl.select(COLUMNS).execute()
# Display the results . Demonstrates how to work with results
# Print the column names followed by the rows
column_names = my_res.get_column_names()
column_count = my_res.get_column_count()
for i in range(0,column_count):
    if i < column_count - 1:
        print "{0}, ".format(column_names[i]),
    else:
        print "{0}".format(column_names[i]),
print
for row in my_res.fetch_all():
    for i in range(0,column_count):
        if i < column_count - 1:
            print "{0}, ".format(row[i]),
        else:
            print "{0}".format(row[i]),
    print
# Execute a simple select (SELECT ∗ FROM)
my_res = my_tbl.select(COLUMNS).execute()
# Display the results
for row in my_res.fetch_all():
    print row
# Execute a simple select (SELECT ∗ FROM)
my_res = my_tbl.select(COLUMNS).execute()
# Display the results
for row in my_res.fetch_all():
    print row
print("Terminado!")
# Delete the database (schema)
my_session.drop_schema('botiga')
print("Base de datos botiga eliminada.")
