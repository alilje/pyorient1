import pyorient.ogm
from pyorient.ogm import Graph, Config


# Connect to Database
a = Config.from_url(
   'plocal://localhost:2424/test',
   'root', 'c208lilje')

print(a.user)
print(a.cred)
print(a.db_name)
print(a.host)
print(a.port)
print(a.storage)