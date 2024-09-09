from miniolite.FileSQLite import FileSQLite


def test_filesqlite():
    file_db = FileSQLite("tmp/test.db")
    file_db.force_add_folder("/")
    file_db.force_add_folder("/data/docs/text/")
    file_db.force_add_folder("/data/imgs/img1/")
    list_folders_name = file_db.list_folder("/data/")
    print(list_folders_name)

    file_db.add_file("/data/docs/text/file1.txt",content="hello world!!")
    print(file_db.read_file("/data/docs/text/file1.txt"))
    print(file_db.list_files("/data/docs/text"))

    file_db.update_file("/data/docs/text/file1.txt",content="hello world, again!!")
    print(file_db.read_file("/data/docs/text/file1.txt"))

    print(file_db.delete_file("/data/docs/text/file1.txt"))
    print(file_db.list_files("/data/docs/text"))

    print(file_db.delete_folder("/data/docs"))
    print(file_db.list_folder("/data"))

    # print(file_db.delete_folder("/"))


    pass

if __name__ == '__main__':
    test_filesqlite()