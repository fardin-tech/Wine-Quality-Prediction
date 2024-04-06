from mlproject.constants import SCHEMA_FILE_PATH
from mlproject.utlis.common import read_yaml
print('f')
schema=read_yaml(SCHEMA_FILE_PATH)
print('e')
print(schema.COLUMNS.keys())
print('hello')