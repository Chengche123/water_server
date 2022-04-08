# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BSensortype(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    measurename = models.CharField(db_column='MeasureName', max_length=20)  # Field name made lowercase.
    datatype = models.SmallIntegerField(db_column='DataType')  # Field name made lowercase.
    usewave = models.IntegerField(db_column='UseWave')  # Field name made lowercase.
    changzhou = models.IntegerField(db_column='ChangZhou', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'b_sensortype'


class BStationtype(models.Model):
    code = models.IntegerField(db_column='Code', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    autostart = models.IntegerField(db_column='AutoStart')  # Field name made lowercase.
    usechannel = models.IntegerField(db_column='UseChannel')  # Field name made lowercase.
    stationlevel = models.SmallIntegerField(db_column='StationLevel')  # Field name made lowercase.
    maxchannel = models.SmallIntegerField(db_column='MaxChannel')  # Field name made lowercase.
    defaultchannel = models.SmallIntegerField(db_column='DefaultChannel', blank=True, null=True)  # Field name made lowercase.
    defaultsensortype = models.SmallIntegerField(db_column='DefaultSensorType', blank=True, null=True)  # Field name made lowercase.
    defaultsensorname = models.CharField(db_column='DefaultSensorName', max_length=10, blank=True, null=True)  # Field name made lowercase.
    xunjianbegin = models.CharField(db_column='XunJianBegin', max_length=10, blank=True, null=True)  # Field name made lowercase.
    xunjianend = models.CharField(db_column='XunJianEnd', max_length=10, blank=True, null=True)  # Field name made lowercase.
    checktype = models.SmallIntegerField(db_column='CheckType', blank=True, null=True)  # Field name made lowercase.
    baudrate = models.IntegerField(db_column='BaudRate', blank=True, null=True)  # Field name made lowercase.
    protocoltypeid = models.IntegerField(db_column='ProtocolTypeID', blank=True, null=True)  # Field name made lowercase.
    protocolnum = models.IntegerField(db_column='ProtocolNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'b_stationtype'


class Config(models.Model):
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    useweb = models.CharField(db_column='UseWeb', max_length=6, db_collation='gbk_chinese_ci')  # Field name made lowercase.
    useyuliang = models.IntegerField(db_column='UseYuliang')  # Field name made lowercase.
    yuliangno = models.CharField(db_column='YuLiangNO', max_length=14)  # Field name made lowercase.
    usewater = models.IntegerField(db_column='UseWater')  # Field name made lowercase.
    usewell = models.IntegerField(db_column='UseWell')  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=200, db_collation='gbk_chinese_ci', blank=True, null=True)  # Field name made lowercase.
    ver = models.FloatField(db_column='Ver', blank=True, null=True)  # Field name made lowercase.
    gsm_zhongduanday = models.IntegerField(db_column='GSM_ZhongDuanDay', blank=True, null=True)  # Field name made lowercase.
    param1 = models.FloatField(db_column='Param1', blank=True, null=True)  # Field name made lowercase.
    param2 = models.FloatField(db_column='Param2', blank=True, null=True)  # Field name made lowercase.
    param3 = models.FloatField(db_column='Param3', blank=True, null=True)  # Field name made lowercase.
    param4 = models.FloatField(db_column='Param4', blank=True, null=True)  # Field name made lowercase.
    param5 = models.FloatField(db_column='Param5', blank=True, null=True)  # Field name made lowercase.
    param6 = models.FloatField(db_column='Param6', blank=True, null=True)  # Field name made lowercase.
    param7 = models.FloatField(db_column='Param7', blank=True, null=True)  # Field name made lowercase.
    param8 = models.FloatField(db_column='Param8', blank=True, null=True)  # Field name made lowercase.
    param9 = models.FloatField(db_column='Param9', blank=True, null=True)  # Field name made lowercase.
    param10 = models.FloatField(db_column='Param10', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'config'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HGroundstation(models.Model):
    autoid = models.BigAutoField(db_column='AutoID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime')  # Field name made lowercase.
    v1 = models.FloatField(db_column='V1', blank=True, null=True)  # Field name made lowercase.
    v2 = models.FloatField(db_column='V2', blank=True, null=True)  # Field name made lowercase.
    v3 = models.FloatField(db_column='V3', blank=True, null=True)  # Field name made lowercase.
    v4 = models.FloatField(db_column='V4')  # Field name made lowercase.
    v5 = models.FloatField(db_column='V5', blank=True, null=True)  # Field name made lowercase.
    v6 = models.FloatField(db_column='V6', blank=True, null=True)  # Field name made lowercase.
    v7 = models.FloatField(db_column='V7', blank=True, null=True)  # Field name made lowercase.
    v8 = models.FloatField(db_column='V8', blank=True, null=True)  # Field name made lowercase.
    v9 = models.FloatField(db_column='V9', blank=True, null=True)  # Field name made lowercase.
    datatype = models.SmallIntegerField(db_column='DataType')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=3)  # Field name made lowercase.
    flag = models.SmallIntegerField(db_column='Flag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_groundstation'


class HL2014(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udate = models.DateField(db_column='uDate', blank=True, null=True)  # Field name made lowercase.
    uhour = models.SmallIntegerField(db_column='uHour', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_l2014'


class HL2015(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udate = models.DateField(db_column='uDate', blank=True, null=True)  # Field name made lowercase.
    uhour = models.SmallIntegerField(db_column='uHour', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_l2015'


class HL2016(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udate = models.DateField(db_column='uDate', blank=True, null=True)  # Field name made lowercase.
    uhour = models.SmallIntegerField(db_column='uHour', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_l2016'


class HL2017(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udate = models.DateField(db_column='uDate', blank=True, null=True)  # Field name made lowercase.
    uhour = models.SmallIntegerField(db_column='uHour', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_l2017'


class HL2018(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udate = models.DateField(db_column='uDate', blank=True, null=True)  # Field name made lowercase.
    uhour = models.SmallIntegerField(db_column='uHour', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_l2018'


class HL2019(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udate = models.DateField(db_column='uDate', blank=True, null=True)  # Field name made lowercase.
    uhour = models.SmallIntegerField(db_column='uHour', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_l2019'


class HL2020(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udate = models.DateField(db_column='uDate', blank=True, null=True)  # Field name made lowercase.
    uhour = models.SmallIntegerField(db_column='uHour', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_l2020'


class HL2021(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udate = models.DateField(db_column='uDate', blank=True, null=True)  # Field name made lowercase.
    uhour = models.SmallIntegerField(db_column='uHour', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_l2021'


class HLog(models.Model):
    autoid = models.BigAutoField(db_column='AutoID', primary_key=True)  # Field name made lowercase.
    idmine = models.CharField(db_column='IDMine', max_length=6, blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=16, blank=True, null=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_log'


class HRepairlog(models.Model):
    autoid = models.BigAutoField(db_column='AutoID', primary_key=True)  # Field name made lowercase.
    idmine = models.CharField(db_column='IDMine', max_length=6, blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_repairlog'


class HS2014(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=9)  # Field name made lowercase.
    begintime = models.DateTimeField(db_column='BeginTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime')  # Field name made lowercase.
    stateid = models.SmallIntegerField(db_column='StateID')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=8)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_s2014'


class HS2015(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=9)  # Field name made lowercase.
    begintime = models.DateTimeField(db_column='BeginTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime')  # Field name made lowercase.
    stateid = models.SmallIntegerField(db_column='StateID')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=8)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_s2015'


class HS2016(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=9)  # Field name made lowercase.
    begintime = models.DateTimeField(db_column='BeginTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime')  # Field name made lowercase.
    stateid = models.SmallIntegerField(db_column='StateID')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=8)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_s2016'


class HS2017(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=9)  # Field name made lowercase.
    begintime = models.DateTimeField(db_column='BeginTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime')  # Field name made lowercase.
    stateid = models.SmallIntegerField(db_column='StateID')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=8)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_s2017'


class HS2018(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=9)  # Field name made lowercase.
    begintime = models.DateTimeField(db_column='BeginTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime')  # Field name made lowercase.
    stateid = models.SmallIntegerField(db_column='StateID')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=8)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_s2018'


class HS2019(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=9)  # Field name made lowercase.
    begintime = models.DateTimeField(db_column='BeginTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime')  # Field name made lowercase.
    stateid = models.SmallIntegerField(db_column='StateID')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=8)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_s2019'


class HS2020(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=9)  # Field name made lowercase.
    begintime = models.DateTimeField(db_column='BeginTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime')  # Field name made lowercase.
    stateid = models.SmallIntegerField(db_column='StateID')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=8)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_s2020'


class HS2021(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=9)  # Field name made lowercase.
    begintime = models.DateTimeField(db_column='BeginTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime')  # Field name made lowercase.
    stateid = models.SmallIntegerField(db_column='StateID')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=8)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_s2021'


class HSms(models.Model):
    autoid = models.BigAutoField(db_column='AutoID', primary_key=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=11, blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_sms'


class HWaring(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    valuestate = models.CharField(db_column='ValueState', max_length=10, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=500, blank=True, null=True)  # Field name made lowercase.
    waringtype = models.IntegerField()
    sendflag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'h_waring'


class HWatertype(models.Model):
    autoid = models.BigAutoField(db_column='AutoID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=15)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime')  # Field name made lowercase.
    reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'h_watertype'


class HX2012(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    valuestate = models.CharField(db_column='ValueState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valuetype = models.SmallIntegerField(db_column='ValueType', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    lastvalue = models.FloatField(db_column='LastValue', blank=True, null=True)  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_x2012'


class HX2013(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    valuestate = models.CharField(db_column='ValueState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valuetype = models.SmallIntegerField(db_column='ValueType', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    lastvalue = models.FloatField(db_column='LastValue', blank=True, null=True)  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_x2013'


class HX2014(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    valuestate = models.CharField(db_column='ValueState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valuetype = models.SmallIntegerField(db_column='ValueType', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    lastvalue = models.FloatField(db_column='LastValue', blank=True, null=True)  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_x2014'


class HX2015(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    valuestate = models.CharField(db_column='ValueState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valuetype = models.SmallIntegerField(db_column='ValueType', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    lastvalue = models.FloatField(db_column='LastValue', blank=True, null=True)  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_x2015'


class HX2016(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    valuestate = models.CharField(db_column='ValueState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valuetype = models.SmallIntegerField(db_column='ValueType', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    lastvalue = models.FloatField(db_column='LastValue', blank=True, null=True)  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_x2016'


class HX2017(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    valuestate = models.CharField(db_column='ValueState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valuetype = models.SmallIntegerField(db_column='ValueType', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    lastvalue = models.FloatField(db_column='LastValue', blank=True, null=True)  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_x2017'


class HX2018(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    valuestate = models.CharField(db_column='ValueState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valuetype = models.SmallIntegerField(db_column='ValueType', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    lastvalue = models.FloatField(db_column='LastValue', blank=True, null=True)  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_x2018'


class HX2019(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    valuestate = models.CharField(db_column='ValueState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valuetype = models.SmallIntegerField(db_column='ValueType', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    lastvalue = models.FloatField(db_column='LastValue', blank=True, null=True)  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_x2019'


class HX2020(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    valuestate = models.CharField(db_column='ValueState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valuetype = models.SmallIntegerField(db_column='ValueType', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    lastvalue = models.FloatField(db_column='LastValue', blank=True, null=True)  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_x2020'


class HX2021(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    valuestate = models.CharField(db_column='ValueState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valuetype = models.SmallIntegerField(db_column='ValueType', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    lastvalue = models.FloatField(db_column='LastValue', blank=True, null=True)  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'h_x2021'


class RGroundstation(models.Model):
    autoid = models.BigAutoField(db_column='AutoID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime')  # Field name made lowercase.
    v1 = models.FloatField(db_column='V1', blank=True, null=True)  # Field name made lowercase.
    v2 = models.FloatField(db_column='V2', blank=True, null=True)  # Field name made lowercase.
    v3 = models.FloatField(db_column='V3', blank=True, null=True)  # Field name made lowercase.
    v4 = models.FloatField(db_column='V4')  # Field name made lowercase.
    v5 = models.FloatField(db_column='V5', blank=True, null=True)  # Field name made lowercase.
    v6 = models.FloatField(db_column='V6', blank=True, null=True)  # Field name made lowercase.
    v7 = models.FloatField(db_column='V7', blank=True, null=True)  # Field name made lowercase.
    v8 = models.FloatField(db_column='V8', blank=True, null=True)  # Field name made lowercase.
    v9 = models.FloatField(db_column='V9', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag')  # Field name made lowercase.
    udatetime_last = models.DateTimeField(db_column='uDateTime_Last', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'r_groundstation'


class RSensorrealdata(models.Model):
    autoid = models.BigAutoField(db_column='AutoID', primary_key=True)  # Field name made lowercase.
    idgroup = models.CharField(db_column='IDGroup', max_length=2, blank=True, null=True)  # Field name made lowercase.
    idbureau = models.CharField(db_column='IDBureau', max_length=4, blank=True, null=True)  # Field name made lowercase.
    idmine = models.CharField(db_column='IDMine', max_length=6, blank=True, null=True)  # Field name made lowercase.
    idstation1 = models.CharField(db_column='IDStation1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    idstation2 = models.CharField(db_column='IDStation2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    idtongdao = models.SmallIntegerField(db_column='IDTongDao', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    valuestate = models.CharField(db_column='ValueState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    lastvalue = models.FloatField(db_column='LastValue', blank=True, null=True)  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'r_sensorrealdata'


class UArea(models.Model):
    autoid = models.BigAutoField(db_column='AutoID', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_area'


class UAreaflow(models.Model):
    autoid = models.AutoField(db_column='AutoID', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    flowtype = models.CharField(db_column='FlowType', max_length=50)  # Field name made lowercase.
    areatnum = models.SmallIntegerField(db_column='AreaTNum')  # Field name made lowercase.
    yujingvalue1 = models.FloatField(db_column='yujingValue1')  # Field name made lowercase.
    yujingvalue2 = models.FloatField(db_column='yujingValue2')  # Field name made lowercase.
    yujinguse = models.SmallIntegerField(db_column='yujingUse')  # Field name made lowercase.
    watertype = models.CharField(db_column='WaterType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updatetime = models.DateTimeField(db_column='UpDatetime', blank=True, null=True)  # Field name made lowercase.
    valuestate = models.CharField(db_column='ValueState', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_areaflow'


class UArearelation(models.Model):
    autoid = models.AutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    groundtag = models.CharField(db_column='GroundTag', max_length=1)  # Field name made lowercase.
    code14 = models.CharField(db_column='Code14', max_length=14)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_arearelation'


class UAreayujing(models.Model):
    autoid = models.AutoField(db_column='AutoID', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    groundtype = models.IntegerField(db_column='GroundType')  # Field name made lowercase.
    yujinguse = models.IntegerField(db_column='yujingUse', blank=True, null=True)  # Field name made lowercase.
    yujingvalue = models.FloatField(db_column='yujingValue', blank=True, null=True)  # Field name made lowercase.
    yujinglevel = models.IntegerField(db_column='yujingLevel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_areayujing'


class UAreayujingtable(models.Model):
    autoid = models.BigAutoField(db_column='AutoID', primary_key=True)  # Field name made lowercase.
    id = models.IntegerField(db_column='ID')  # Field name made lowercase.
    code14 = models.CharField(db_column='Code14', max_length=14)  # Field name made lowercase.
    stationtype = models.IntegerField(db_column='StationType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_areayujingtable'


class UBureau(models.Model):
    idbureau = models.CharField(db_column='IDBureau', primary_key=True, max_length=4)  # Field name made lowercase.
    idgroup = models.CharField(db_column='IDGroup', max_length=2)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_bureau'


class UGroundstation(models.Model):
    autoid = models.BigAutoField(db_column='AutoID', primary_key=True)  # Field name made lowercase.
    idgroup = models.CharField(db_column='IDGroup', max_length=2, blank=True, null=True)  # Field name made lowercase.
    idbureau = models.CharField(db_column='IDBureau', max_length=4, blank=True, null=True)  # Field name made lowercase.
    idmine = models.CharField(db_column='IDMine', max_length=6, blank=True, null=True)  # Field name made lowercase.
    code8 = models.CharField(db_column='Code8', max_length=8, blank=True, null=True)  # Field name made lowercase.
    code14 = models.CharField(db_column='Code14', max_length=14, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=200, blank=True, null=True)  # Field name made lowercase.
    holelevel = models.FloatField(db_column='HoleLevel', blank=True, null=True)  # Field name made lowercase.
    watertype = models.CharField(db_column='WaterType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sim = models.CharField(db_column='SIM', max_length=11, blank=True, null=True)  # Field name made lowercase.
    autosim = models.CharField(db_column='AutoSIM', max_length=11, blank=True, null=True)  # Field name made lowercase.
    gisuse = models.IntegerField(db_column='GISUse', blank=True, null=True)  # Field name made lowercase.
    gis_x = models.FloatField(db_column='GIS_X', blank=True, null=True)  # Field name made lowercase.
    gis_y = models.FloatField(db_column='GIS_Y', blank=True, null=True)  # Field name made lowercase.
    powertype = models.SmallIntegerField(db_column='PowerType', blank=True, null=True)  # Field name made lowercase.
    alarmuse = models.IntegerField(db_column='AlarmUse', blank=True, null=True)  # Field name made lowercase.
    alarmh = models.FloatField(db_column='AlarmH', blank=True, null=True)  # Field name made lowercase.
    alarml = models.FloatField(db_column='AlarmL', blank=True, null=True)  # Field name made lowercase.
    alarmtype = models.SmallIntegerField(db_column='AlarmType', blank=True, null=True)  # Field name made lowercase.
    alarmuse2 = models.IntegerField(db_column='AlarmUse2', blank=True, null=True)  # Field name made lowercase.
    alarmh2 = models.FloatField(db_column='AlarmH2', blank=True, null=True)  # Field name made lowercase.
    alarml2 = models.FloatField(db_column='AlarmL2', blank=True, null=True)  # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    sortnum = models.IntegerField(db_column='SortNum', blank=True, null=True)  # Field name made lowercase.
    usewarning = models.IntegerField(db_column='UseWarning', blank=True, null=True)  # Field name made lowercase.
    usesmswarning = models.IntegerField(db_column='UseSMSWarning', blank=True, null=True)  # Field name made lowercase.
    useemailwarning = models.IntegerField(db_column='UseEmailWarning', blank=True, null=True)  # Field name made lowercase.
    usedingshi = models.IntegerField(db_column='UseDingShi', blank=True, null=True)  # Field name made lowercase.
    usesmsdingshi = models.IntegerField(db_column='UseSMSDingShi', blank=True, null=True)  # Field name made lowercase.
    useemaildingshi = models.IntegerField(db_column='UseEmailDingShi', blank=True, null=True)  # Field name made lowercase.
    changerateuse = models.IntegerField(db_column='ChangeRateUse', blank=True, null=True)  # Field name made lowercase.
    changeratevalue = models.FloatField(db_column='ChangeRateValue', blank=True, null=True)  # Field name made lowercase.
    fangda = models.FloatField(db_column='FangDa', blank=True, null=True)  # Field name made lowercase.
    parm1 = models.FloatField(db_column='Parm1', blank=True, null=True)  # Field name made lowercase.
    parm2 = models.FloatField(db_column='Parm2', blank=True, null=True)  # Field name made lowercase.
    parm3 = models.FloatField(db_column='Parm3', blank=True, null=True)  # Field name made lowercase.
    xianchang = models.FloatField(db_column='XianChang', blank=True, null=True)  # Field name made lowercase.
    lingpin = models.FloatField(db_column='LingPin', blank=True, null=True)  # Field name made lowercase.
    kvalue = models.FloatField(db_column='KValue', blank=True, null=True)  # Field name made lowercase.
    holedepth = models.FloatField(db_column='HoleDepth', blank=True, null=True)  # Field name made lowercase.
    stationtype = models.IntegerField(db_column='StationType', blank=True, null=True)  # Field name made lowercase.
    param1 = models.CharField(db_column='Param1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    param2 = models.CharField(db_column='Param2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    param3 = models.FloatField(db_column='Param3', blank=True, null=True)  # Field name made lowercase.
    param4 = models.FloatField(db_column='Param4', blank=True, null=True)  # Field name made lowercase.
    param5 = models.FloatField(db_column='Param5', blank=True, null=True)  # Field name made lowercase.
    param6 = models.FloatField(db_column='Param6', blank=True, null=True)  # Field name made lowercase.
    param7 = models.FloatField(db_column='Param7', blank=True, null=True)  # Field name made lowercase.
    param8 = models.FloatField(db_column='Param8', blank=True, null=True)  # Field name made lowercase.
    param9 = models.FloatField(db_column='Param9', blank=True, null=True)  # Field name made lowercase.
    param10 = models.FloatField(db_column='Param10', blank=True, null=True)  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=100, blank=True, null=True)  # Field name made lowercase.
    formulatype = models.SmallIntegerField(db_column='FormulaType', blank=True, null=True)  # Field name made lowercase.
    changerateunit = models.FloatField(db_column='ChangeRateUnit', blank=True, null=True)  # Field name made lowercase.
    variation1 = models.FloatField(blank=True, null=True)
    variation2 = models.FloatField(blank=True, null=True)
    variation3 = models.FloatField(blank=True, null=True)
    alarmwtop3 = models.FloatField(db_column='AlarmWTop3')  # Field name made lowercase.
    alarmwtop2 = models.FloatField(db_column='AlarmWTop2')  # Field name made lowercase.
    alarmwtop1 = models.FloatField(db_column='AlarmWTop1')  # Field name made lowercase.
    alarmwbottom1 = models.FloatField(db_column='AlarmWBottom1')  # Field name made lowercase.
    alarmwbottom2 = models.FloatField(db_column='AlarmWBottom2')  # Field name made lowercase.
    alarmwbottom3 = models.FloatField(db_column='AlarmWBottom3')  # Field name made lowercase.
    alarmttop3 = models.FloatField(db_column='AlarmTTop3')  # Field name made lowercase.
    alarmttop2 = models.FloatField(db_column='AlarmTTop2')  # Field name made lowercase.
    alarmttop1 = models.FloatField(db_column='AlarmTTop1')  # Field name made lowercase.
    alarmtbottom1 = models.FloatField(db_column='AlarmTBottom1')  # Field name made lowercase.
    alarmtbottom2 = models.FloatField(db_column='AlarmTBottom2')  # Field name made lowercase.
    alarmtbottom3 = models.FloatField(db_column='AlarmTBottom3')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_groundstation'


class UGroup(models.Model):
    idgroup = models.CharField(db_column='IDGroup', primary_key=True, max_length=2)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_group'


class UMine(models.Model):
    idmine = models.CharField(db_column='IDMine', primary_key=True, max_length=6)  # Field name made lowercase.
    idgroup = models.CharField(db_column='IDGroup', max_length=2)  # Field name made lowercase.
    idbureau = models.CharField(db_column='IDBureau', max_length=4)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    maxusercount = models.IntegerField(db_column='MaxUserCount', blank=True, null=True)  # Field name made lowercase.
    useyuliang = models.IntegerField(db_column='UseYuliang', blank=True, null=True)  # Field name made lowercase.
    yuliangno = models.CharField(db_column='YuLiangNO', max_length=14, blank=True, null=True)  # Field name made lowercase.
    yuliangwarningtype = models.IntegerField(db_column='YuLiangWarningType', blank=True, null=True)  # Field name made lowercase.
    yuliangwarning2 = models.FloatField(db_column='YuLiangWarning2', blank=True, null=True)  # Field name made lowercase.
    yulianglasttime = models.DateTimeField(db_column='YuLiangLastTime', blank=True, null=True)  # Field name made lowercase.
    yuliang24h = models.FloatField(db_column='YuLiang24H', blank=True, null=True)  # Field name made lowercase.
    yuliang1h = models.FloatField(db_column='YuLiang1H', blank=True, null=True)  # Field name made lowercase.
    yuliang24lianxu = models.FloatField(db_column='YuLiang24LianXu', blank=True, null=True)  # Field name made lowercase.
    yuliangreal = models.FloatField(db_column='YuLiangReal', blank=True, null=True)  # Field name made lowercase.
    yuliangrealtime = models.DateTimeField(db_column='YuLiangRealTime', blank=True, null=True)  # Field name made lowercase.
    useground = models.IntegerField(db_column='UseGround', blank=True, null=True)  # Field name made lowercase.
    usewell = models.IntegerField(db_column='UseWell', blank=True, null=True)  # Field name made lowercase.
    yuliangtype = models.IntegerField(db_column='YuLiangType', blank=True, null=True)  # Field name made lowercase.
    qx_fengsu = models.FloatField(db_column='QX_FengSu', blank=True, null=True)  # Field name made lowercase.
    qx_qiwen = models.FloatField(db_column='QX_QiWen', blank=True, null=True)  # Field name made lowercase.
    qx_qiya = models.FloatField(db_column='QX_QiYa', blank=True, null=True)  # Field name made lowercase.
    qx_fengxiang = models.IntegerField(db_column='QX_FengXiang', blank=True, null=True)  # Field name made lowercase.
    qx_shidu = models.FloatField(db_column='QX_ShiDu', blank=True, null=True)  # Field name made lowercase.
    yl24htop3 = models.FloatField(db_column='YL24HTop3')  # Field name made lowercase.
    yl24htop2 = models.FloatField(db_column='YL24HTop2')  # Field name made lowercase.
    yl24htop1 = models.FloatField(db_column='YL24HTop1')  # Field name made lowercase.
    yl1htop3 = models.FloatField(db_column='YL1HTop3')  # Field name made lowercase.
    yl1htop2 = models.FloatField(db_column='YL1HTop2')  # Field name made lowercase.
    yl1htop1 = models.FloatField(db_column='YL1HTop1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_mine'


class USensor(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    idgroup = models.CharField(db_column='IDGroup', max_length=2)  # Field name made lowercase.
    idbureau = models.CharField(db_column='IDBureau', max_length=4)  # Field name made lowercase.
    idmine = models.CharField(db_column='IDMine', max_length=6)  # Field name made lowercase.
    idstation1 = models.CharField(db_column='IDStation1', max_length=3)  # Field name made lowercase.
    idstation2 = models.CharField(db_column='IDStation2', max_length=3)  # Field name made lowercase.
    idchannel = models.SmallIntegerField(db_column='IDChannel')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14)  # Field name made lowercase.
    sensorlevel = models.SmallIntegerField(db_column='SensorLevel')  # Field name made lowercase.
    sensortypeid = models.IntegerField(db_column='SensorTypeID')  # Field name made lowercase.
    sensortypename = models.CharField(db_column='SensorTypeName', max_length=10)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=500)  # Field name made lowercase.
    areaid = models.IntegerField(db_column='AreaID')  # Field name made lowercase.
    measurename = models.CharField(db_column='MeasureName', max_length=20)  # Field name made lowercase.
    gisuse = models.IntegerField(db_column='GISUse')  # Field name made lowercase.
    gis_x = models.CharField(db_column='GIS_X', max_length=20, blank=True, null=True)  # Field name made lowercase.
    gis_y = models.CharField(db_column='GIS_Y', max_length=20, blank=True, null=True)  # Field name made lowercase.
    warningtop3 = models.FloatField(db_column='WarningTop3', blank=True, null=True)  # Field name made lowercase.
    warningtop2 = models.FloatField(db_column='WarningTop2', blank=True, null=True)  # Field name made lowercase.
    warningtop1 = models.FloatField(db_column='WarningTop1', blank=True, null=True)  # Field name made lowercase.
    warningbottom1 = models.FloatField(db_column='WarningBottom1', blank=True, null=True)  # Field name made lowercase.
    warningbottom2 = models.FloatField(db_column='WarningBottom2', blank=True, null=True)  # Field name made lowercase.
    warningbottom3 = models.FloatField(db_column='WarningBottom3', blank=True, null=True)  # Field name made lowercase.
    usewarning = models.IntegerField(db_column='UseWarning', blank=True, null=True)  # Field name made lowercase.
    usevoicewarning = models.IntegerField(db_column='UseVoiceWarning', blank=True, null=True)  # Field name made lowercase.
    usesmswarning = models.IntegerField(db_column='UseSMSWarning', blank=True, null=True)  # Field name made lowercase.
    useemailwarning = models.IntegerField(db_column='UseEmailWarning', blank=True, null=True)  # Field name made lowercase.
    usedingshi = models.IntegerField(db_column='UseDingShi', blank=True, null=True)  # Field name made lowercase.
    usesmsdingshi = models.IntegerField(db_column='UseSMSDingShi', blank=True, null=True)  # Field name made lowercase.
    useemaildingshi = models.IntegerField(db_column='UseEmailDingShi', blank=True, null=True)  # Field name made lowercase.
    formula = models.CharField(db_column='Formula', max_length=100, blank=True, null=True)  # Field name made lowercase.
    formulatype = models.SmallIntegerField(db_column='FormulaType', blank=True, null=True)  # Field name made lowercase.
    datatype = models.SmallIntegerField(db_column='DataType', blank=True, null=True)  # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State')  # Field name made lowercase.
    usewave = models.IntegerField(db_column='UseWave', blank=True, null=True)  # Field name made lowercase.
    sortnum = models.IntegerField(db_column='SortNum', blank=True, null=True)  # Field name made lowercase.
    userange = models.IntegerField(db_column='UseRange', blank=True, null=True)  # Field name made lowercase.
    rangeh = models.FloatField(db_column='RangeH', blank=True, null=True)  # Field name made lowercase.
    rangel = models.FloatField(db_column='RangeL', blank=True, null=True)  # Field name made lowercase.
    changerateuse = models.IntegerField(db_column='ChangeRateUse', blank=True, null=True)  # Field name made lowercase.
    changeratevalue = models.FloatField(db_column='ChangeRateValue', blank=True, null=True)  # Field name made lowercase.
    changerateunit = models.FloatField(db_column='ChangeRateUnit', blank=True, null=True)  # Field name made lowercase.
    monitorsite = models.CharField(db_column='MonitorSite', max_length=50, blank=True, null=True)  # Field name made lowercase.
    holelevel = models.FloatField(db_column='HoleLevel', blank=True, null=True)  # Field name made lowercase.
    watertype = models.CharField(db_column='WaterType', max_length=50, blank=True, null=True)  # Field name made lowercase.
    variation = models.FloatField(blank=True, null=True)
    holedepth = models.FloatField(db_column='HoleDepth', blank=True, null=True)  # Field name made lowercase.
    onoffvalue = models.FloatField(db_column='OnOffValue', blank=True, null=True)  # Field name made lowercase.
    flowid = models.IntegerField(db_column='FlowID')  # Field name made lowercase.
    flowareaname = models.CharField(max_length=50)
    warnsectionh = models.FloatField(db_column='WarnSectionH')  # Field name made lowercase.
    warnsectionl = models.FloatField(db_column='WarnSectionL')  # Field name made lowercase.
    monitortype = models.SmallIntegerField(db_column='MonitorType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_sensor'


class UStation1(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    idgroup = models.CharField(db_column='IDGroup', max_length=2)  # Field name made lowercase.
    idbureau = models.CharField(db_column='IDBureau', max_length=4)  # Field name made lowercase.
    idmine = models.CharField(db_column='IDMine', max_length=6)  # Field name made lowercase.
    idstation1 = models.CharField(db_column='IDStation1', max_length=3)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=9)  # Field name made lowercase.
    stationtype = models.IntegerField(db_column='StationType')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100)  # Field name made lowercase.
    gisuse = models.IntegerField(db_column='GISUse')  # Field name made lowercase.
    gis_x = models.FloatField(db_column='GIS_X', blank=True, null=True)  # Field name made lowercase.
    gis_y = models.FloatField(db_column='GIS_Y', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    comport = models.IntegerField(db_column='ComPort', blank=True, null=True)  # Field name made lowercase.
    commstate = models.CharField(db_column='CommState', max_length=20, blank=True, null=True)  # Field name made lowercase.
    commstateid = models.SmallIntegerField(db_column='CommStateID', blank=True, null=True)  # Field name made lowercase.
    commbegin = models.DateTimeField(db_column='CommBegin', blank=True, null=True)  # Field name made lowercase.
    commend = models.DateTimeField(db_column='CommEnd', blank=True, null=True)  # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_station1'


class UStation2(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    idgroup = models.CharField(db_column='IDGroup', max_length=2)  # Field name made lowercase.
    idbureau = models.CharField(db_column='IDBureau', max_length=4)  # Field name made lowercase.
    idmine = models.CharField(db_column='IDMine', max_length=6)  # Field name made lowercase.
    idstation1 = models.CharField(db_column='IDStation1', max_length=3)  # Field name made lowercase.
    idstation2 = models.CharField(db_column='IDStation2', max_length=3)  # Field name made lowercase.
    idchannel = models.SmallIntegerField(db_column='IDChannel', blank=True, null=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=12)  # Field name made lowercase.
    stationtype = models.IntegerField(db_column='StationType')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100)  # Field name made lowercase.
    gisuse = models.IntegerField(db_column='GISUse')  # Field name made lowercase.
    gis_x = models.FloatField(db_column='GIS_X', blank=True, null=True)  # Field name made lowercase.
    gis_y = models.FloatField(db_column='GIS_Y', blank=True, null=True)  # Field name made lowercase.
    state = models.SmallIntegerField(db_column='State')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_station2'


class UUser(models.Model):
    user_id = models.CharField(db_column='User_ID', primary_key=True, max_length=16)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=16)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    sim = models.CharField(db_column='SIM', max_length=11)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    dingshisms = models.IntegerField(db_column='DingShiSMS')  # Field name made lowercase.
    dingshiemail = models.IntegerField(db_column='DingShiEmail')  # Field name made lowercase.
    warningsms = models.IntegerField(db_column='WarningSMS')  # Field name made lowercase.
    warningemail = models.IntegerField(db_column='WarningEmail')  # Field name made lowercase.
    usecontrol = models.IntegerField(db_column='UseControl')  # Field name made lowercase.
    useclient = models.IntegerField(db_column='UseClient')  # Field name made lowercase.
    useweb = models.IntegerField(db_column='UseWeb')  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=15)  # Field name made lowercase.
    idmine = models.CharField(db_column='IDMine', max_length=6, blank=True, null=True)  # Field name made lowercase.
    lastweblogintime = models.DateTimeField(db_column='LastWebLoginTime', blank=True, null=True)  # Field name made lowercase.
    waringlevel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'u_user'


class UWarningsms(models.Model):
    autoid = models.BigAutoField(db_column='AutoID', primary_key=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=11, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='Content', max_length=140, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_warningsms'
