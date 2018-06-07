from sql_to_java import sql_to_java
from java_to_sql import java_to_sql


sql = '''\
SELECT 1
FROM campaigns
JOIN dogs
WHERE x = :fetch'''


java = '''\
""
+ " SELECT 1 "
+ " FROM campaigns "
+ " JOIN dogs "
+ " WHERE x = :fetch ";'''


def test_sql_to_java():
	lines = sql.splitlines()
	expected = java
	assert expected == sql_to_java(lines)


def test_java_to_sql():
	lines = java.splitlines()
	expected = sql
	assert expected == java_to_sql(lines)
