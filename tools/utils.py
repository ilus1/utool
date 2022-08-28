from datetime import datetime, date, timedelta
import json

class ToolsUtils:
    def count_days(self, date_created, diasEmprestimo):
        today = datetime.today()
        days =  today-date_created
        days = days.days
        if(days==diasEmprestimo): 
            return 0
        elif(days>diasEmprestimo):
            return (days-diasEmprestimo)
        else:
            return (diasEmprestimo-days)