import sqlite3
from utils import datetime_to_str

class DBManager(object):
    def __init__(self, database):
        self.conn = self.__create_connection(database)
        self.__init_db()

    def __create_connection(self, database):
        self.conn = None
        try:
            conn = sqlite3.connect(database,detect_types=sqlite3.PARSE_DECLTYPES)
        except Exception as e:
            print(e)
        return conn

    def __init_db(self):
        query = 'CREATE TABLE IF NOT EXISTS worktime' + \
                '( id INTEGER PRIMARY KEY AUTOINCREMENT, '+ \
                '  startDate TIMESTAMP NOT NULL, ' + \
                '  endDate TIMESTAMP NOT NULL, ' + \
                '  category TEXT, ' + \
                '  description TEXT)'
        if self.conn is not None:
            try:
                c = self.conn.cursor()
                c.execute(query)
                self.conn.commit()
            except Exception as e:
                print(e)

    def insert(self, start_date, end_date, category, description):
        query = 'INSERT INTO worktime' + \
                '(startDate, endDate, category, description)' + \
                ' VALUES(?,?,?,?)'
        values = (start_date, end_date, category, description)
        last_row_id = None
        if self.conn is not None:
            try:
                c = self.conn.cursor()
                c.execute(query, values)
                self.conn.commit()
                last_row_id = c.lastrowid
            except Exception as e:
                print(e)
        return last_row_id


    def delete(self, id):
        query = 'DELETE FROM worktime WHERE id=?'
        values = (id,)
        result = None
        if self.conn is not None:
            try:
                c = self.conn.cursor()
                c.execute(query, values)
                result = c.rowcount
                self.conn.commit()
            except Exception as e:
                print(e)
        return result

    def update(self, id, start_date, end_date, category, description):
        query = 'UPDATE worktime ' + \
                'SET startDate = ?, ' + \
                '    endDate = ?, ' + \
                '    category = ?, ' + \
                '    description = ? ' + \
                'WHERE id  =?'
        values = (start_date, end_date, category, description, id)
        result = None
        if self.conn is not None:
            try:
                c = self.conn.cursor()
                c.execute(query, values)
                result = c.rowcount
                self.conn.commit()
            except Exception as e:
                print(e)
        return result

        
    
    def get(self, id):
        query = 'SELECT startDate, endDate, category, description ' + \
                'FROM worktime ' + \
                'WHERE id = ?'
        values = (id,)
        work_time = None
        success = False
        if self.conn is not None:
            try:
                c = self.conn.cursor()
                c.execute(query, values)
                row = c.fetchone()
                success = True
                if row is not None:                                        
                    print(row[0])
                    work_time = dict(start_date=datetime_to_str(row[0]), end_date=datetime_to_str(row[1]), category=row[2], description=row[3], id=id)
            except Exception as e:
                print(e)
        return work_time, success

    def get_between (self, start_date, end_date):
        query = 'SELECT startDate, endDate, category, description, id ' + \
                'FROM worktime ' + \
                'WHERE startDate >= ? AND endDate <= ?'
        values = (start_date, end_date)
        work_time = None
        if self.conn is not None:
            try:
                c = self.conn.cursor()
                c.execute(query, values)
                rows = c.fetchall()
                work_time = []
                for row in rows:
                    work_time.append(dict(start_date=datetime_to_str(row[0]), end_date=datetime_to_str(row[1]), category=row[2], description=row[3], id=row[4]))
            except Exception as e:
                print(e)
        return work_time

    def close(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None
