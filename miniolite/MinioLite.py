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

    def search_path_step(self,path):
        parent_dir_list  = path.strip('/').split('/')
        parent_dir  = self.root
        for dir_step in parent_dir_list:
            parent_dir = parent_dir.get(dir_step)
            if not isinstance(parent_dir, Directory):
                raise FileNotFoundError(f"No directory or file found: {dir_step}")
        return parent_dir

    def add_root_hearder_to_path(self,path):
        path= path.strip('/')
        path = os.path.join(self.root_name,path)
        return path

    def list_directory(self,path):
        path = self.add_root_hearder_to_path(path)
        parent_dir = self.search_path_step(path)

        directory = parent_dir
        if isinstance(directory, Directory):
            return list(directory.keys())
        return []
        
    def create_root_directory(self):
        if self.root.get(self.root_name) is None:
            self.root[self.root_name] = Directory(name=self.root_name)
            self.commit()
        else:
            raise FileExistsError("Root directory already exists")

    def create_directory(self,path):
        path = self.add_root_hearder_to_path(path)
        parent_path, new_dir_name = os.path.split(path)
        parent_dir =  self.search_path_step(parent_path)

        if isinstance(parent_dir, Directory):
            parent_dir[new_dir_name] = Directory(name=new_dir_name)
            transaction.commit()
        else:
            raise FileNotFoundError(f"No directory found at {parent_path}")
    
    def create_file(self,path,content):
        path = self.add_root_hearder_to_path(path)
        parent_path, new_dir_name = os.path.split(path)
        parent_dir =  self.search_path_step(parent_path)
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
