#coding:utf8
from django.db import models


# Create your models here.
#主机故障记录表

class RecordMachine(models.Model):
    '''
    machine_ip:主机ip
    malfunction_time:故障时间
    notify_persion:故障通知人
    record_persion:记录故障人
    malfunction_content:故障内容
    event_status:故障状态
    status:本条记录状态，是否被删除
    '''
    machine_ip = models.GenericIPAddressField()
    malfunction_time = models.DateField()
    notify_persion = models.CharField(max_length=50)
    record_persion = models.CharField(max_length=50,db_index=True)
    malfunction_content = models.TextField()
    event_status = models.BooleanField(db_index=True)
    status = models.IntegerField(default=1)

class RecordPayment(models.Model):
    '''
    malfunction_start_time:故障开始时间
    malfunction_stop_time:故障结束时间
    malfunction_type：故障类型
    malfunction_responsibility:故障责任方
    notify_persion:故障通知人
    record_persion:记录故障人
    malfunction_content:故障内容
    event_status:故障状态
    status:本条记录状态，是否被删除
    '''
    malfunction_start_time = models.DateField()
    malfunction_stop_time = models.DateField()
    malfunction_type = models.IntegerField()
    malfunction_responsibility = models.IntegerField()
    notify_persion = models.CharField(max_length=50)
    record_persion = models.CharField(max_length=50,db_index=True)
    malfunction_content = models.TextField()
    event_status = models.BooleanField(db_index=True)
    status = models.IntegerField(default=1)


class RecordNetwork(models.Model):
    '''
    malfunction_start_time:故障开始时间
    malfunction_stop_time:故障结束时间
    malfunction_type：故障类型
    malfunction_responsibility:故障责任方
    notify_persion:故障通知人
    record_persion:记录故障人
    malfunction_content:故障内容
    event_status:故障状态
    status:本条记录状态，是否被删除
    '''
    malfunction_start_time = models.DateField()
    malfunction_stop_time = models.DateField()
    malfunction_type = models.IntegerField()
    malfunction_responsibility = models.IntegerField()
    notify_persion = models.CharField(max_length=50)
    record_persion = models.CharField(max_length=50,db_index=True)
    malfunction_content = models.TextField()
    event_status = models.BooleanField(db_index=True)
    status = models.IntegerField(default=1)

class RecordApp(models.Model):
    '''
    malfunction_start_time:故障开始时间
    malfunction_stop_time:故障结束时间
    malfunction_type：故障类型
    malfunction_responsibility:故障责任方
    notify_persion:故障通知人
    record_persion:记录故障人
    malfunction_content:故障内容
    event_status:故障状态
    status:本条记录状态，是否被删除
    '''
    malfunction_start_time = models.DateField()
    malfunction_stop_time = models.DateField()
    malfunction_type = models.IntegerField()
    notify_persion = models.CharField(max_length=50)
    record_persion = models.CharField(max_length=50,db_index=True)
    malfunction_content = models.TextField()
    event_status = models.BooleanField(db_index=True)
    status = models.IntegerField(default=1)

class RecordMessage(models.Model):
    '''
    malfunction_start_time:故障开始时间
    malfunction_stop_time:故障结束时间
    malfunction_responsibility:故障责任方
    notify_persion:故障通知人
    record_persion:记录故障人
    malfunction_content:故障内容
    event_status:故障状态
    status:本条记录状态，是否被删除
    '''
    malfunction_start_time = models.DateField()
    malfunction_stop_time = models.DateField()
    notify_persion = models.CharField(max_length=50)
    record_persion = models.CharField(max_length=50,db_index=True)
    malfunction_content = models.TextField()
    event_status = models.BooleanField(db_index=True)
    status = models.IntegerField(default=1)

class RecordOther(models.Model):
    '''
    malfunction_start_time:故障开始时间
    malfunction_stop_time:故障结束时间
    malfunction_responsibility:故障责任方
    notify_persion:故障通知人
    record_persion:记录故障人
    malfunction_content:故障内容
    event_status:故障状态
    status:本条记录状态，是否被删除
    '''
    malfunction_start_time = models.DateField()
    malfunction_stop_time = models.DateField()
    notify_persion = models.CharField(max_length=50)
    record_persion = models.CharField(max_length=50,db_index=True)
    malfunction_content = models.TextField()
    event_status = models.BooleanField(db_index=True)
    status = models.IntegerField(default=1)


class RecordMachineRepiar(models.Model):
    '''
    malfunction_start_time:故障开始时间
    malfunction_stop_time:故障结束时间
    malfunction_responsibility:故障责任方
    notify_persion:故障通知人
    record_persion:记录故障人
    malfunction_content:故障内容
    event_status:故障状态
    status:本条记录状态，是否被删除
    '''
    machine_ip = models.GenericIPAddressField()
    malfunction_time = models.DateField()
    notify_persion = models.CharField(max_length=50)
    record_persion = models.CharField(max_length=50,db_index=True)
    malfunction_content = models.TextField()
    event_status = models.BooleanField(db_index=True)
    status = models.IntegerField(default=1)

class RecordCloseNotify(models.Model):
    '''
    malfunction_start_time:故障开始时间
    malfunction_stop_time:故障结束时间
    malfunction_responsibility:故障责任方
    notify_persion:故障通知人
    record_persion:记录故障人
    malfunction_content:故障内容
    event_status:故障状态
    status:本条记录状态，是否被删除
    service:服务类型
    '''
    machine_ip = models.GenericIPAddressField()
    service = models.TextField()
    malfunction_start_time = models.DateField()
    malfunction_stop_time = models.DateField()
    notify_persion = models.CharField(max_length=50)
    record_persion = models.CharField(max_length=50,db_index=True)
    malfunction_content = models.TextField()
    event_status = models.BooleanField(db_index=True)
    status = models.IntegerField(default=1)
