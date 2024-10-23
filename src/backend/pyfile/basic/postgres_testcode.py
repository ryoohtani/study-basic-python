# 下記コードはPythonとpostgressqlの接続確認用のソースコードである。
import psycopg2
from psycopg2 import sql

# PostgreSQLへの接続情報
DB_NAME = "pydb"
DB_USER = "admin"
DB_PASS = "pypost"
DB_HOST = "postgres"  # Docker Composeのサービス名を使います
DB_PORT = "5432"

# PostgreSQLに接続する関数
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

# テーブルを作成する関数
def create_table(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS test_table (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50) NOT NULL,
                    age INT NOT NULL
                );
            """)
            conn.commit()
            print("Table created successfully!")
    except Exception as e:
        print(f"Error creating table: {e}")
        conn.rollback()

# データを挿入する関数
def insert_data(conn, name, age):
    try:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO test_table (name, age) VALUES (%s, %s);", (name, age)
            )
            conn.commit()
            print("Data inserted successfully!")
    except Exception as e:
        print(f"Error inserting data: {e}")
        conn.rollback()

# データを取得する関数
def fetch_data(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM test_table;")
            rows = cur.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print(f"Error fetching data: {e}")

# データを更新する関数
def update_data(conn, record_id, new_age):
    try:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE test_table SET age = %s WHERE id = %s;", (new_age, record_id)
            )
            conn.commit()
            print("Data updated successfully!")
    except Exception as e:
        print(f"Error updating data: {e}")
        conn.rollback()

# データを削除する関数
def delete_data(conn, record_id):
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM test_table WHERE id = %s;", (record_id,))
            conn.commit()
            print("Data deleted successfully!")
    except Exception as e:
        print(f"Error deleting data: {e}")
        conn.rollback()

# メイン処理
if __name__ == "__main__":
    conn = connect_db()
    if conn:
        create_table(conn)
        insert_data(conn, "Alice", 30)
        insert_data(conn, "Bob", 25)
        print("Current data:")
        fetch_data(conn)
        update_data(conn, 1, 35)
        print("Data after update:")
        fetch_data(conn)
        delete_data(conn, 2)
        print("Data after delete:")
        fetch_data(conn)
        conn.close()

"""
dbの確認用のコマンド
まずPythonの開発環境のコンテナにアクセス
次に、venvにアクセス
そして右のファイルを実行 -> postgres_testcode.py
下記のようなログがでれば成功
Data deleted successfully!

さらなる確認を行いたいのであれば
dbコンテナにアクセスする
docker exec -it postgres-db psql -U admin -d pydb
下記コマンドを実行
SELECT * FROM test_table;

テーブルの存在確認が完了したらテーブルを削除コマンドを実行
DROP TABLE test_table;

テーブルの安否確認コマンド
\dt
"""