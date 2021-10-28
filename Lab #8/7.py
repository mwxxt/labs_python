from datetime import datetime
date = datetime.now()
print(date.strftime("\n Date: %Y.%m.%d")) 
print(date.strftime("\nMonth: %B | Day: %d | Year: %Y\n"))