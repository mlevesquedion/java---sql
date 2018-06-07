from os import unlink
from pytest import fixture
from time import time
from sql_to_java import sql_to_java
from convert import convert


def timestamp(filename):
  return f'{filename}{round(time())}'


@fixture
def from_filename():
  from_filename = timestamp('from')
  with open(from_filename, 'w') as from_file:
    from_file.write('SELECT [reference], [estimation], [name], [description], [notes], [from],')  
  yield from_filename
  unlink(from_filename)


@fixture
def to_filename():
  to_filename = timestamp('to') 
  yield to_filename
  unlink(to_filename) 


def test_convert(from_filename, to_filename):
  convert(from_filename, to_filename, sql_to_java)
  with open(to_filename) as to_file:
    assert to_file.read() == 'String query = ""\n+ " SELECT [reference], [estimation], [name], [description], [notes], [from], ";'
