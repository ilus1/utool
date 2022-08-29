from datetime import datetime, date, timedelta
from faulthandler import disable
import json

class ToolsUtils:
    def count_days(self, date_created, lending_days):
        aux='dias'
        today = datetime.today()
        days =  today-date_created
        days = days.days
        if(days==lending_days): 
            return 'Hoje é a data de devolução da ferramenta'
        elif(days<lending_days and days-lending_days!=1):
            if(lending_days-days==1): aux='dia'
            return f'A devolução é daqui a {lending_days-days} {aux}'
        else:
            if(days-lending_days==1): aux='dia'
            return f'A devolução está atrasada {days-lending_days} {aux}'