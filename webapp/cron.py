from django_cron import cronScheduler, Job
from models import ModbusData

class ReloadInfo(Job):
    # run every 300 seconds (5 minutes)
    run_every = 5

    def job(self):
        

cronScheduler.register(ReloadInfo)
