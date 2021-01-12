import datetime
datetime.datetime.now().isocalendar()
from datetime import datetime 
apply_time = "2023-2-1"
week=datetime.strptime(apply_time,'%Y-%m-%d').strftime('%W')
print week
