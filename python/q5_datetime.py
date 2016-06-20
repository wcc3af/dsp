# Hint:  use Google to find python function

from datetime import datetime
####a)
date_format_a = "%m-%d-%Y"
date_start_a = datetime.strptime('01-02-2013', date_format_a)
date_stop_a = datetime.strptime('07-28-2015', date_format_a)

delta_a = date_stop_a - date_start_a
answer = delta_a.days

####b)
date_format_b = "%m%d%Y"
date_start_b = datetime.strptime('12312013', date_format_b)
date_stop_b = datetime.strptime('05282015', date_format_b)

delta_b = date_stop_b - date_start_b
answer = delta_b.days

####c)
date_format_c = "%d-%b-%Y"
date_start_c = datetime.strptime('15-Jan-1994', date_format_c)
date_stop_c = datetime.strptime('14-Jul-2015', date_format_c)

delta_c = date_stop_c - date_start_c
answer = delta_c.days
