from miniolite import MinioLiteDB

# 初始化数据库
db = MinioLiteDB(path='tmp/test.db')
try:
    db.create_root_directory()
except Exception as e:
    print(e)
try:
    db.create_directory('/docs')
except Exception as e:
    print(e)
try:
    db.create_directory('/imgs')
except Exception as e:
    print(e)
# try:
#     db.create_directory('/files')
# except Exception as e:
#     print(e)

try:
    db.create_directory('/docs/text')
except Exception as e:
    print(e)
try:
    db.create_file('/docs/text/test.txt',content='Hello, World!')
except Exception as e:
    print(e)


print(db.list_directory('/'))
print(db.list_directory('/docs'))
print(db.list_directory('/docs/text'))

try:
    print(db.get_file('/docs/text/test.txt'))
except Exception as e:
    print(e)


print(db.delete('/docs'))

print(db.list_directory('/'))


# # 列出目录内容
# print("Docs directory:", db.list_directory('/docs'))

# # 读取文件内容
# print("README.txt content:", db.read_file('/docs/README.txt'))

# # 写入文件
# db.write_file('/docs/README.txt', 'Updated content for README file.')

# # 创建目录
# db.create_directory('/newdir')

# # 删除文件或目录
# db.delete('/newdir')
