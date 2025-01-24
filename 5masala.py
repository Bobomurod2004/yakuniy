from  datetime import datetime

data = datetime.fromisocalendar(2025,1,23)
data1 = datetime.fromisocalendar(2025,1,29)
natija = data1-data
print(natija)