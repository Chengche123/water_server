from django.db import models
from django.contrib.auth.models import User


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
        managed = True
        db_table = 'u_sensor'
        ordering = ['-sensortypename']


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
        ordering = ['-udatetime']

    def __str__(self):
        return str(self.value)


class HX2022(models.Model):
    autoid = models.BigAutoField(db_column='Autoid', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=14, blank=True, null=True)  # Field name made lowercase.
    udatetime = models.DateTimeField(db_column='uDateTime', blank=True, null=True, auto_now_add=True)  # Field name made lowercase.
    originalvalue = models.FloatField(db_column='OriginalValue', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.
    valuestate = models.CharField(db_column='ValueState', max_length=100, blank=True, null=True)  # Field name made lowercase.
    valuetype = models.SmallIntegerField(db_column='ValueType', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    lastvalue = models.FloatField(db_column='LastValue', blank=True, null=True)  # Field name made lowercase.
    lasttime = models.DateTimeField(db_column='LastTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'h_x2022'
        ordering = ['-udatetime']
        indexes = [
            models.Index(fields=['code']),
            models.Index(fields=['udatetime']),
        ]

    def __str__(self):
        return str(self.value)


class UserExtend(models.Model):
    # 级联删除
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extend')
    telephone_number = models.CharField(max_length=30, blank=True, null=True)
    # 是否能够访问站点
    is_access = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)


class AlarmThreshold(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='alarm_threshold')
    sensor = models.ForeignKey(USensor, on_delete=models.CASCADE, related_name='alarm_threshold')
    threshold_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # bit0：电话 bit1：短信 bit2：邮箱
    method = models.SmallIntegerField(default=0)

    class Meta:
        db_table = 'alarm_threshold'
        # https://docs.djangoproject.com/zh-hans/4.0/ref/models/options/#constraints
        # https://docs.djangoproject.com/zh-hans/4.0/ref/models/constraints/#uniqueconstraint
        constraints = [
            models.UniqueConstraint(fields=['user', 'sensor'], name='unique_threshold')
        ]
