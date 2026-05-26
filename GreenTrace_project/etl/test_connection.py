from sqlalchemy import create_engine

engine = create_engine(
"mysql+pymysql://root:dbms2006@localhost/green_trace_dw"
)

connection = engine.connect()

print("Connected to MySQL successfully!")

connection.close()