#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2024 yaqiang.sun.
# This source code is licensed under the license found in the LICENSE file
# in the root directory of this source tree.
#########################################################################
# Author: yaqiangsun
# Created Time: 2024/09/08 21:21:51
#########################################################################
import os
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from miniolite.sqlite_tool.base import SqliteBase,SqlalchemyBase


# 文件夹表
class Folder(SqlalchemyBase):
    __tablename__ = 'folders'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey('folders.id'))
    parent = relationship('Folder', remote_side=[id], backref='children')

    def __repr__(self):
        return f"<Folder(name={self.name}, parent_id={self.parent_id})>"

# 文件表
class File(SqlalchemyBase):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    folder_id = Column(Integer, ForeignKey('folders.id'))
    folder = relationship('Folder', backref='files')

    def __repr__(self):
        return f"<File(name={self.name}, folder_id={self.folder_id})>"



class FileSQLite(SqliteBase):
    def __init__(self, db_path= "tmp/info.db"):
        super().__init__(db_path)
        self.init_tables()
        self.root_name = "Root"
        self.add_root_folder()
    
    def add_root_hearder_to_path(self,path):
        path= path.strip('/')
        path = os.path.join(self.root_name,path)
        return path
    def split_path_step(self,path):
        dir_list  = path.strip('/').split('/')
        return dir_list

    @SqliteBase.with_session
    def add_folder(self,session, path):
        path = self.add_root_hearder_to_path(path)
        dir_list = self.split_path_step(path)
        pass
    

    @SqliteBase.with_session
    def add_root_folder(self,session):
        root_folder = session.query(Folder).filter_by(name=self.root_name).first()
        if root_folder is None:
            folder = Folder(name=self.root_name, parent_id=None)
            session.add(folder)
            session.commit()
        else:
            return root_folder

    @SqliteBase.with_session
    def force_add_folder(self,session,path):
        dir_list = self.split_path_step(path)
        parent_id = session.query(Folder).filter_by(name=self.root_name).first().id
        for dir_name in dir_list:
            folder_now = session.query(Folder).filter_by(name=dir_name,parent_id=parent_id).first()
            if folder_now is None:
                folder = Folder(name=dir_name, parent_id=parent_id)
                session.add(folder)
                session.commit()
                parent_id = folder.id
            else:
                parent_id = folder_now.id
