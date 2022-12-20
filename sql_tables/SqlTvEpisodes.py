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

class SqlTvEpisodes(SqlTable):
    table_exists=False

    def create_table(self,bc,conn):
        try:
            sql_create_table = " CREATE TABLE IF NOT EXISTS {table_name} (\
                id integer PRIMARY KEY,\
                tv_id text NOT NULL,\
                season_number text NOT NULL,\
                episode_number text NOT NULL,\
                air_date text NOT NULL,\
                download text NOT NULL,\
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
                tv_id,\
                season_number,\
                episode_number,\
                air_date,\
                download,\
                creatation_date,modification_date) values(\
                '{tv_id}',\
                '{season_number}',\
                '{episode_number}',\
                '{air_date}',\
                '{download}',\
                {creatation_date},{modification_date});".format(\
                table_name=self._table_name,\
                tv_id=self._tv_id,\
                season_number=self._season_number,\
                episode_number=self._episode_number,\
                air_date=self._air_date,\
                download=self._download,\
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
            cursor = conn.execute(sql_select)
            return cursor.fetchall()
        except:
            bc.log.error("\t"+":"+traceback.format_exc())
            raise SqlSelectError 

    def episode_reset(self,bc,conn):
        store_date=int(datetime.now().timestamp()) 
        sql_update="update {table_name}\
            set modification_date={modification_date},\
            download='False';".format(\
            table_name=self._table_name,\
            modification_date=store_date)
        cur = conn.cursor()
        cur.execute(sql_update)
        conn.commit()

    def episode_download(self,bc,conn,tv_id,season_number,episode_number):
        store_date=int(datetime.now().timestamp()) 
        sql_update="update {table_name}\
            set modification_date={modification_date},\
            download='True'\
            where tv_id='{tv_id}'\
            and season_number='{season_number}'\
            and episode_number='{episode_number}'\
            and download='False';\
                        ".format(\
            table_name=self._table_name,\
            modification_date=store_date,\
            tv_id=tv_id,\
            season_number=season_number,\
            episode_number=episode_number\
           )
        bc.log.error(sql_update)
        cur = conn.cursor()
        cur.execute(sql_update)
        conn.commit()

    def search_episode(self,bc,conn,tv_id,season_number,episode_number):
        select_return=[]
        sql_select = "select * from {table_name}\
            where tv_id='{tv_id}' \
            and season_number='{season_number}'\
            and episode_number='{episode_number}'\
             ; ".format(table_name=self._table_name,\
            tv_id=tv_id,\
            season_number=season_number,\
            episode_number=episode_number\
           )
        try:
            cursor = conn.execute(sql_select)
            select_return= cursor.fetchall()
        except:
            bc.log.error(sql_select)
            bc.log.error("\t"+":"+traceback.format_exc())
        return select_return
        
    def in_database(self,bc,conn):
        sql_select = "select * from {table_name}\
            where tv_id='{tv_id}'\
            and season_number='{season_number}'\
            and episode_number='{episode_number}' ; ".format(table_name=self._table_name,\
            tv_id=self._tv_id,\
            season_number=self._season_number,\
            episode_number=self._episode_number  )
        cursor = conn.execute(sql_select)
        select_return= cursor.fetchall()
        if select_return==[]:
            return False
        return True


    def search_downloadable(self,bc,conn):
        select_return=[]
        sql_select = "select * from tv_episodes\
            JOIN tv_shows\
            where tv_shows.tv_id=tv_episodes.tv_id\
            and download='False'\
            and tv_episodes.air_date like '2022%';"\
            .format(table_name=self._table_name)
        try:
            cursor = conn.execute(sql_select)
            select_return= cursor.fetchall()
        except:
            bc.log.error(sql_select)
            bc.log.error("\t"+":"+traceback.format_exc())
        return select_return
        