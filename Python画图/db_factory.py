#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import ConfigParser

class dbfactory(object):

    def __init__(self, dbhost, dbuser, dbpass, dbdatabase=None, dbport=3306):
        self.__dbhost = dbhost
        self.__dbuser = dbuser
        self.__dbpass = dbpass
        self.__dbdatabase = dbdatabase
        self.__dbport = dbport

    def get_connection(self):
        return mdb.connect(host=self.__dbhost, user=self.__dbuser, passwd=self.__dbpass, port=self.__dbport, db=self.__dbdatabase, charset="utf8")

def get_db_connection_production():
    sqlparam=ConfigParser.ConfigParser()
    sqlparam.read("sqlconfig.ini")
    dbhost = sqlparam.get('database_product', 'dbhost')
    dbuser = sqlparam.get('database_product', 'dbuser')
    dbpass = sqlparam.get('database_product', 'dbpass')
    dbport = sqlparam.getint('database_product', 'dbport')
    dbdatabase = sqlparam.get('database_product', 'dbdatabase')
    return dbfactory(dbhost, dbuser, dbpass, dbdatabase, dbport)

def get_db_connection_test():
    sqlparam=ConfigParser.ConfigParser()
    sqlparam.read("sqlconfig.ini")
    dbhost = sqlparam.get('database_test', 'dbhost')
    dbuser = sqlparam.get('database_test', 'dbuser')
    dbpass = sqlparam.get('database_test', 'dbpass')
    dbport = sqlparam.getint('database_test', 'dbport')
    dbdatabase = sqlparam.get('database_test', 'dbdatabase')
    return dbfactory(dbhost, dbuser, dbpass, dbdatabase, dbport)

def get_db_connection_debug():
    sqlparam=ConfigParser.ConfigParser()
    sqlparam.read("sqlconfig.ini")
    dbhost = sqlparam.get('database_debug', 'dbhost')
    dbuser = sqlparam.get('database_debug', 'dbuser')
    dbpass = sqlparam.get('database_debug', 'dbpass')
    dbport = sqlparam.getint('database_debug', 'dbport')
    dbdatabase = sqlparam.get('database_debug', 'dbdatabase')
    return dbfactory(dbhost, dbuser, dbpass, dbdatabase, dbport)

def get_db_dbdatabase_name():
    sqlparam=ConfigParser.ConfigParser()
    sqlparam.read("sqlconfig.ini")
    dbdatabase = sqlparam.get('database_test', 'dbdatabase')
    return dbdatabase