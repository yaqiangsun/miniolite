from miniolite.FileSQLite import FileSQLite


def test_filesqlite():
    file_db = FileSQLite("tmp/test.db")
    file_db.force_add_folder("/data/docs/text/")
    file_db.force_add_folder("/data/imgs/img1/")
    pass

if __name__ == '__main__':
    test_filesqlite()