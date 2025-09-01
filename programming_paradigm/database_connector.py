
import mysql.connector

mydbconnector = mysql.connector.connect(
    hostName="localhost",
    user='root',
    pswd="Janvier@19205",
    database="my_database2025"

)
print(mydbconnector.get_server_info())
