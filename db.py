import psycopg2


class DB:
    def __init__(self) -> None:
        self.connect = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="Cosmonaut_19",
            port="2000",
            dbname="master_project"
        )
        self.cursor = self.connect.cursor()
        self.connect.autocommit = True

    def create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS client_details(
                            id serial primary key,
                            name varchar(30),
                            username varchar(30),
                            phone_number varchar(20),
                            address varchar(50),
                            pr_image_link varchar(300) )""")
    def insert_table(self,name, username,phone_number, address, pr_image_link):
        self.cursor.execute(f"""INSERT INTO client_details ({name}, {username}, {phone_number}, {address}, {pr_image_link}) 
                            VALUES (%s, %s, %s, %s, %s)""")
        self.connect.commit()
    def sql_query(self,query):
        try:
            self.cursor.execute(query)
        except:
            return[]
        else:
            return self.cursor.fetchall()
        
db = DB()

# db.cursor.execute("alter table client_details add column ")

# db.cursor.execute("insert into client_details ()")
