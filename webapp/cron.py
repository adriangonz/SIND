from django_cron import CronJobBase, Schedule
from models import ModbusData


class ReloadInfo(CronJobBase):
    RUN_EVERY_MINS = 2

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'webapp.reload_info'    # a unique code

    def do(self):
        ModbusData.set_data()
