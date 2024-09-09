from miniolite.FileSQLite import FileSQLite


def test_filesqlite():
    file_db = FileSQLite("tmp/test.db")
    file_db.force_add_folder("/")
    file_db.force_add_folder("/data/docs/text/")
    file_db.force_add_folder("/data/imgs/img1/")
    list_folders_name = file_db.list_directory("/data/")
    print(list_folders_name)
    pass

if __name__ == '__main__':
    test_filesqlite()