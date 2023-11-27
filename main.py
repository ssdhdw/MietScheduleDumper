import get_info
from tqdm import tqdm
import sqlite3

info = get_info.GetInfo()

conn = sqlite3.connect("data.db")

table = conn.execute("""CREATE TABLE groups (
        name TEXT,
        day INTEGER,
        week INTEGER,
        time INTEGER,
        room TEXT,
        subject TEXT,
        teacher TEXT
)""")

def insert_value(conn, entry):
    sql = ''' INSERT INTO groups(name,day,week,time,room,subject,teacher)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, entry)
    conn.commit()

for group in tqdm(info.get_groups()):
    schedule = info.get_schedule(group)
    for data in schedule["Data"]:
        entry = [group, data['Day'], data['DayNumber'], data['Time']['Code'], data['Room']['Name'], data['Class']['Name'], data['Class']['TeacherFull']]
        insert_value(conn, entry)