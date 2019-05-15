from django.db import models

class Employee(models.Model):
     id=models.AutoField(primary_key=True)
     name=models.CharField(max_length=20)

class Book(models.Model):
    # 定义一个自增的id主键
    id = models.AutoField(primary_key=True)
    # 定义一个最大长度为32的varchar字段
    title = models.CharField(max_length=32)
class Publisher(models.Model):
    id = models.AutoField(primary_key=True) # 创建自增的一个主键
    name = models.CharField(null=False, max_length=64, unique=True) #varchar且不能为空的字段
#####--------------TEST---------------######

class LpActSuggest(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    sales_id = models.CharField(db_column='SALES_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    cust_id = models.CharField(db_column='CUST_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    act_type = models.CharField(db_column='ACT_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    act_generate_date = models.DateTimeField(db_column='ACT_GENERATE_DATE', blank=True, null=True)  # Field name made lowercase.
    act_expire_date = models.DateTimeField(db_column='ACT_EXPIRE_DATE', blank=True, null=True)  # Field name made lowercase.
    act_source_type = models.CharField(db_column='ACT_SOURCE_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    act_source_id = models.CharField(db_column='ACT_SOURCE_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateTimeField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'LP_ACT_SUGGEST'


class LpActType(models.Model):
    type_id = models.CharField(db_column='TYPE_ID', primary_key=True, max_length=32)  # Field name made lowercase.
    act_nm = models.CharField(db_column='ACT_NM', max_length=32, blank=True, null=True)  # Field name made lowercase.
    act_event = models.CharField(db_column='ACT_EVENT', max_length=32, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateTimeField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'LP_ACT_TYPE'


class LpDsGetui(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    cust_id = models.CharField(db_column='CUST_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    read_date = models.DateTimeField(db_column='READ_DATE', blank=True, null=True)  # Field name made lowercase.
    gt_lable1 = models.CharField(db_column='GT_LABLE1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gt_lable2 = models.CharField(db_column='GT_LABLE2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gt_lable3 = models.CharField(db_column='GT_LABLE3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gt_lable4 = models.CharField(db_column='GT_LABLE4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gt_lable5 = models.CharField(db_column='GT_LABLE5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gt_lable6 = models.CharField(db_column='GT_LABLE6', max_length=100, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateTimeField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'LP_DS_GETUI'


class LpDsPhone(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    sales_id = models.CharField(db_column='SALES_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    cust_id = models.CharField(db_column='CUST_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    read_date = models.DateTimeField(db_column='READ_DATE', blank=True, null=True)  # Field name made lowercase.
    contact_date = models.DateTimeField(db_column='CONTACT_DATE', blank=True, null=True)  # Field name made lowercase.
    contact_duration = models.DecimalField(db_column='CONTACT_DURATION', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateTimeField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'LP_DS_PHONE'


class LpDsSchedule(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    cust_id = models.CharField(db_column='CUST_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    type_id = models.CharField(db_column='TYPE_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    last_read = models.DateTimeField(db_column='LAST_READ', blank=True, null=True)  # Field name made lowercase.
    last_status = models.CharField(db_column='LAST_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    next_read = models.DateTimeField(db_column='NEXT_READ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'LP_DS_SCHEDULE'


class LpDsSrcType(models.Model):
    type_id = models.CharField(db_column='TYPE_ID', primary_key=True, max_length=32)  # Field name made lowercase.
    type_nm = models.CharField(db_column='TYPE_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    type_get_type = models.DecimalField(db_column='TYPE_GET_TYPE', max_digits=1, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    type_frequency = models.DecimalField(db_column='TYPE_FREQUENCY', max_digits=1, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'LP_DS_SRC_TYPE'


class LpDsWechat(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    cust_id = models.CharField(db_column='CUST_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    read_date = models.DateTimeField(db_column='READ_DATE', blank=True, null=True)  # Field name made lowercase.
    moment_date = models.DateTimeField(db_column='MOMENT_DATE', blank=True, null=True)  # Field name made lowercase.
    moment_text = models.CharField(db_column='MOMENT_TEXT', max_length=200, blank=True, null=True)  # Field name made lowercase.
    moment_img1 = models.CharField(db_column='MOMENT_IMG1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    moment_img2 = models.CharField(db_column='MOMENT_IMG2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    moment_img3 = models.CharField(db_column='MOMENT_IMG3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    moment_img4 = models.CharField(db_column='MOMENT_IMG4', max_length=100, blank=True, null=True)  # Field name made lowercase.
    moment_img5 = models.CharField(db_column='MOMENT_IMG5', max_length=100, blank=True, null=True)  # Field name made lowercase.
    moment_img7 = models.CharField(db_column='MOMENT_IMG7', max_length=100, blank=True, null=True)  # Field name made lowercase.
    moment_img8 = models.CharField(db_column='MOMENT_IMG8', max_length=100, blank=True, null=True)  # Field name made lowercase.
    moment_img9 = models.CharField(db_column='MOMENT_IMG9', max_length=100, blank=True, null=True)  # Field name made lowercase.
    moment_link = models.CharField(db_column='MOMENT_LINK', max_length=100, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateTimeField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'LP_DS_WECHAT'


class LpMgntCustMst(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    src = models.CharField(db_column='SRC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    phase = models.CharField(db_column='PHASE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=2, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.DateField(db_column='BIRTH_DATE', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    marriage = models.CharField(db_column='MARRIAGE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    child = models.CharField(db_column='CHILD', max_length=1, blank=True, null=True)  # Field name made lowercase.
    industry = models.CharField(db_column='INDUSTRY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    yearly_income = models.DecimalField(db_column='YEARLY_INCOME', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    yearly_expense = models.DecimalField(db_column='YEARLY_EXPENSE', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    house = models.CharField(db_column='HOUSE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    car = models.CharField(db_column='CAR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    health_check = models.CharField(db_column='HEALTH_CHECK', max_length=1, blank=True, null=True)  # Field name made lowercase.
    smoke = models.CharField(db_column='SMOKE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    alcohol = models.CharField(db_column='ALCOHOL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    phone_no = models.CharField(db_column='PHONE_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phone_nm = models.CharField(db_column='PHONE_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phone_company = models.CharField(db_column='PHONE_COMPANY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phone_role = models.CharField(db_column='PHONE_ROLE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    phone_email = models.CharField(db_column='PHONE_EMAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone_address = models.CharField(db_column='PHONE_ADDRESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone_group = models.CharField(db_column='PHONE_GROUP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wechat_no = models.CharField(db_column='WECHAT_NO', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wechat_nm = models.CharField(db_column='WECHAT_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wechat_memo = models.CharField(db_column='WECHAT_MEMO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wechat_img = models.CharField(db_column='WECHAT_IMG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wechat_country = models.CharField(db_column='WECHAT_COUNTRY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wechat_city = models.CharField(db_column='WECHAT_CITY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wechat_signature = models.CharField(db_column='WECHAT_SIGNATURE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    wechat_phone = models.CharField(db_column='WECHAT_PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    wechat_linkedin = models.CharField(db_column='WECHAT_LINKEDIN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    wechat_group = models.CharField(db_column='WECHAT_GROUP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    wechat_samegroup = models.CharField(db_column='WECHAT_SAMEGROUP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    weibo_id = models.CharField(db_column='WEIBO_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateTimeField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'LP_MGNT_CUST_MST'


class LpMgntSalesCust(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    sales_id = models.CharField(db_column='SALES_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    cust_id = models.CharField(db_column='CUST_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'LP_MGNT_SALES_CUST'


class LpMgntSalesMst(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    login_id = models.CharField(db_column='LOGIN_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    user_nm = models.CharField(db_column='USER_NM', max_length=20, blank=True, null=True)  # Field name made lowercase.
    login_pwd = models.CharField(db_column='LOGIN_PWD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    last_login = models.DateTimeField(db_column='LAST_LOGIN', blank=True, null=True)  # Field name made lowercase.
    head_img = models.CharField(db_column='HEAD_IMG', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    tel_no = models.CharField(db_column='TEL_NO', max_length=11, blank=True, null=True)  # Field name made lowercase.
    wechat_no = models.CharField(db_column='WECHAT_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    profile = models.CharField(db_column='PROFILE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='SEX', max_length=1, blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateField(db_column='BIRTHDAY', blank=True, null=True)  # Field name made lowercase.
    location_city = models.CharField(db_column='LOCATION_CITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    location_detail = models.CharField(db_column='LOCATION_DETAIL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='COMPANY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    department = models.CharField(db_column='DEPARTMENT', max_length=100, blank=True, null=True)  # Field name made lowercase.
    position_title = models.CharField(db_column='POSITION_TITLE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    work_date_start = models.DateField(db_column='WORK_DATE_START', blank=True, null=True)  # Field name made lowercase.
    user_sn = models.CharField(db_column='USER_SN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateTimeField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    # def format(self):
    #     return {u'create_date': self.create_date.strftime('%Y-%m-%d %H:%M:%S'),
    #             u'update_date': self.update_date.strftime('%Y-%m-%d %H:%M:%S')}
    class Meta:
        #managed = False
        db_table = 'LP_MGNT_SALES_MST'




class LpScoreLabel(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    score_label1 = models.CharField(db_column='SCORE_LABEL1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    score_label2 = models.CharField(db_column='SCORE_LABEL2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    score_label3 = models.CharField(db_column='SCORE_LABEL3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    score_label4 = models.CharField(db_column='SCORE_LABEL4', max_length=32, blank=True, null=True)  # Field name made lowercase.
    score_label5 = models.CharField(db_column='SCORE_LABEL5', max_length=32, blank=True, null=True)  # Field name made lowercase.
    score_label6 = models.CharField(db_column='SCORE_LABEL6', max_length=32, blank=True, null=True)  # Field name made lowercase.
    score_label7 = models.CharField(db_column='SCORE_LABEL7', max_length=32, blank=True, null=True)  # Field name made lowercase.
    score_label8 = models.CharField(db_column='SCORE_LABEL8', max_length=32, blank=True, null=True)  # Field name made lowercase.
    score_label9 = models.CharField(db_column='SCORE_LABEL9', max_length=32, blank=True, null=True)  # Field name made lowercase.
    score_label10 = models.CharField(db_column='SCORE_LABEL10', max_length=32, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateTimeField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'LP_SCORE_LABEL'


class LpScoreResult(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    cust_id = models.CharField(db_column='CUST_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    score = models.DecimalField(db_column='SCORE', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    latest_flg = models.CharField(db_column='LATEST_FLG', max_length=1, blank=True, null=True)  # Field name made lowercase.
    module_ver = models.CharField(db_column='MODULE_VER', max_length=10, blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    update_date = models.DateTimeField(db_column='UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'LP_SCORE_RESULT'
