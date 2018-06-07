import os
from convert import convert


def format_line(line):
	return '" {} "'.format(line.rstrip())


def sql_to_java(lines):
	first_line = 'String query = ""\n+ '
	java_lines = '\n+ '.join(format_line(line) for line in lines)
	return first_line + java_lines + ';'


if __name__ == '__main__':
	convert('sql.sql', 'java.java', sql_to_java)
