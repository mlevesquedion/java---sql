import re
from convert import convert


def try_match(line):
	return re.search(r'\+ " (.+) "', line)


def extract_matches(lines):
	for line in lines:
		match = try_match(line)
		if match:
			yield match.group(1)


def java_to_sql(lines):
	sql_lines = extract_matches(lines)
	return '\n'.join(sql_lines)


if __name__ == '__main__':
	convert('java.java', 'sql.sql', java_to_sql)
