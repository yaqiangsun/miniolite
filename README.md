# miniolite

miniolite is a database library to replace pure file path saving.

## Usage

- Step 1, initialize:

```

from miniolite import MinioLiteDB

# initalize the database
db = MinioLiteDB(path='tmp/test.db')

# init the root directory
db.create_root_directory()
```
- Step 2, create a directory:

```
db.create_directory('/docs')
```

- Step 3, create a file:

```
db.create_file('/docs/test.txt', 'hello world')
```

- Step 4, read a file:

```
db.get_file('/docs/test.txt')
```

- Step 5, delete a file:

```
db.delete_file('/docs/test.txt')
```

- Step 6, delete a directory:

```
db.delete('/docs')
```

- Step 7, list all files and directory in a directory:

```
db.list_directory('/docs')
```