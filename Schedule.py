# -*- coding: utf-8 -*-
"""
Created on Sun May 23 00:44:50 2021

@author: Rafae
"""

import schedule
import time
from MakeOrder import Start



schedule.every(5).minutes.do(Start)
#schedule.every(30).seconds.do(showtime)

while True:
    schedule.run_pending()
    time.sleep(10)