import sqlite3

conn = sqlite3.connect('emp.db')
cur = conn.cursor()

def insert(name,age,doj,gender,address):
    sql = '''INSERT INTO employee VALUES(
    NULL, ? , ?, ?, ? , ?
    )'''
    cur.execute(sql,(name,age,doj,gender,address))
    conn.commit()

def remove(id):
    cur.execute("DELETE FROM employee WHERE id = ?",(id ,))
    conn.commit()

def update(id,name,age,doj,gender,address):
    sql = '''UPDATE employee SET name = ? , age = ?, doj = ? , address = ?,gender = ?
    WHERE id = ?'''
    cur.execute(sql,(name,age,doj,address,gender,id))
    conn.commit()

def fetch():
    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()
    return rows

def main():
    
    sql = '''CREATE TABLE IF NOT EXISTS employee( 
        id Integer Primary Key,
        name text,
        age text,
        doj text,
        gender text,
        address text
        )
        '''
    cur.execute(sql)
    conn.commit()

    insert("Nitheesh","18","10-10-2024","Male","CBE")
    #remove("2")
    #update("1","Nitheeeeesh","19","15-09-2024","CBE - 46")
    fetch()

if __name__ == "___main__":
    main()