#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2024 yaqiang.sun.
# This source code is licensed under the license found in the LICENSE file
# in the root directory of this source tree.
#########################################################################
# Author: yaqiangsun
# Created Time: 2024/09/08 14:56:34
#########################################################################
import os

import ZODB, ZODB.FileStorage
import transaction

from miniolite.FileSystem import File,Directory

class MinioLiteDB:
    def __init__(self, path):
        self.storage = ZODB.FileStorage.FileStorage(path)
        self.db = ZODB.DB(self.storage)
        self.connection = self.db.open()
        self.root = self.connection.root()
        self.root_name = "Root"

    def __delete__(self):
        self.close()

    def close(self):
        self.connection.close()
        self.db.close()
        self.storage.close()

    def commit(self):
        transaction.commit()
    



    def list_directory(self,path):
        path= path.strip('/')
        path = os.path.join(self.root_name,path)
        parent_dir_list  = path.strip('/').split('/')
        parent_dir  = self.root
        for dir_name in parent_dir_list:
            parent_dir = parent_dir.get(dir_name)
            if isinstance(parent_dir, Directory):
                pass
            else:
                raise FileNotFoundError(f"No directory found: {parent_path}")
        directory = parent_dir
        if isinstance(directory, Directory):
            return list(directory.keys())
        return []
        
    def create_root_directory(self):
        if self.root.get('/') is None:
            self.root[self.root_name] = Directory(name=self.root_name)
            self.commit()
        else:
            raise FileExistsError("Root directory already exists")

    def create_directory(self,path):
        path= path.strip('/')
        path = os.path.join(self.root_name,path)
        if path in self.root:
            raise FileExistsError(f"Path already exists: {path}")
        parent_path, new_dir_name = os.path.split(path)
        parent_dir_list  = parent_path.strip('/').split('/')
        parent_dir  = self.root
        for dir_name in parent_dir_list:
            parent_dir = parent_dir.get(dir_name)
            if isinstance(parent_dir, Directory):
                pass
            else:
                raise FileNotFoundError(f"No directory found: {parent_path}")
        if isinstance(parent_dir, Directory):
            parent_dir[new_dir_name] = Directory(name=new_dir_name)
            transaction.commit()
        else:
            raise FileNotFoundError(f"No directory found at {parent_path}")
    
    def create_file(self,path,content):
        path= path.strip('/')
        path = os.path.join(self.root_name,path)
        if path in self.root:
            raise FileExistsError(f"Path already exists: {path}")
        parent_path, new_dir_name = os.path.split(path)
        parent_dir_list  = parent_path.strip('/').split('/')
        parent_dir  = self.root
        for dir_name in parent_dir_list:
            parent_dir = parent_dir.get(dir_name)
            if isinstance(parent_dir, Directory):
                pass
            else:
                raise FileNotFoundError(f"No directory found: {parent_path}")
        if isinstance(parent_dir, Directory):
            parent_dir[new_dir_name] = File(name=new_dir_name, content=content)
            transaction.commit()
        else:
            raise FileNotFoundError(f"No directory found at {parent_path}")

        
    def read_file(self,path):
        file = self.root.get(path)
        if isinstance(file, File):
            return file.content
        return None
    

    def delete(path):
        if path in self.root:
            del self.root[path]
            transaction.commit()
        else:
            raise FileNotFoundError(f"No such file or directory: {path}")
