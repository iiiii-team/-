from django.apps import AppConfig
from record_malfunction import models


class RecordMalfunctionConfig(AppConfig):
    name = 'record_malfunction'


class RecordMalfunction:
    def __init__(self,record_type,record):
        self.record_type = record_type
        self.record = record
        self.record_instance = record_type(**record)

    def send_to_db(self):
        self.record_type.save()





