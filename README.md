# miniolite

miniolite is a database library to replace pure file path saving.

## Install
```
pip install miniolite -i https://pypi.python.org/simple/
```

## Usage

- Step 1, initialize:

```

from miniolite.FileSQLite import FileSQLite

# initalize the database
file_db = FileSQLite("tmp/test.db")
```


- Step 2, create a folder:

```
# create folder
file_db.force_add_folder("/data/docs/text/")
```

- Step 3, add a file:
```
file_db.add_file("/data/docs/text/file1.txt",content="hello world!!")
```
- Step 4, list files:
```
file_db.list_files("/data/docs/text")
```
- Step 5, change a file:
```
file_db.update_file("/data/docs/text/file1.txt",content="hello world, again!!")
```
- Step 6, delete a file:
```
file_db.delete_file("/data/docs/text/file1.txt")
```
- Step 7, delete a folder:
```
file_db.delete_folder("/data/docs")
```
