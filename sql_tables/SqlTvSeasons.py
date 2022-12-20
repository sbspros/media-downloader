from common.BaseClass import BaseClass
from sql_tables.SqlTable import SqlTable,SQLCreateError,SqlSelectError,SqlInsertError
from datetime import datetime 
import traceback

__author__ = "Richard Chamberlain"
__copyright__ = "Copyright 2022"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Richard Chamberlain"
__email__ = "richard@sbspros.ca"
__status__ = "Dev"

class SqlTvSeasons(SqlTable):
    table_exists=False

    def create_table(self,bc,conn):
        try:
            sql_create_table = " CREATE TABLE IF NOT EXISTS {table_name} (\
                id integer PRIMARY KEY,\
                tv_id text NOT NULL,\
                season_id text NOT NULL,\
                season_number text NOT NULL,\
                complete text NOT NULL,\
                air_date text NOT NULL,\
                creatation_date int NOT NULL,\
                modification_date NOT NULL\
                    ); ".format(table_name=self._table_name)
            conn.execute(sql_create_table)
        except:
            bc.log.error("\t"+":"+traceback.format_exc())
            raise SQLCreateError

    def update():
        pass

    def delete():
        pass

    def insert(self,bc,conn):
        try:
            store_date=int(datetime.now().timestamp())
            sql_insert = "\
                insert into {table_name} (\
                tv_id,season_number,\
                season_id,\
                complete,air_date,\
                creatation_date,modification_date) values(\
                '{tv_id}','{season_number}',\
                '{season_id}',\
                '{complete}','{air_date}',\
                {creatation_date},{modification_date});".format(\
                table_name=self._table_name,\
                tv_id=self._tv_id,\
                season_id=self._season_id,\
                season_number=self._season_number,\
                complete='False',\
                air_date=self._air_date,\
                creatation_date=store_date,\
                modification_date=store_date)
            conn.execute(sql_insert)
            conn.commit()
        except:
            bc.log.error("\t"+":"+traceback.format_exc())
            raise SqlInsertError        
        pass

    def select(self,bc,conn):

        try:
            sql_select = " ; ".format(table_name=self._table_name,\
                        name=self._name)
            conn.execute(sql_select)
            cursor = conn.execute(sql_select)
            return cursor.fetchall()
        except:
            bc.log.error("\t"+":"+traceback.format_exc())
            raise SqlSelectError
            
    def search_season(self,bc,conn,tv_id,season_number):
        select_return=[]
        sql_select = "select * from {table_name}\
            where tv_id='{tv_id}' \
            and season_number='{season_number}'\
             ; ".format(table_name=self._table_name,\
            tv_id=tv_id,\
            season_number=season_number)
        try:
            conn.execute(sql_select)
            cursor = conn.execute(sql_select)
            select_return= cursor.fetchall()
        except:
            bc.log.error(sql_select)
            bc.log.error("\t"+":"+traceback.format_exc())
        return select_return

    def in_database(self,bc,conn,tv_id,season_num):
        sql_select = "select * from {table_name}\
            where tv_id='{tv_id}'\
            and season_number='{season_number}' ; ".format(table_name=self._table_name,\
            tv_id=self._tv_id,\
            season_number=self._season_number)
        conn.execute(sql_select)
        cursor = conn.execute(sql_select)
        select_return= cursor.fetchall()
        if select_return==[]:
            return False
        return True