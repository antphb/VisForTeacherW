# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Chitietdiem(models.Model):
    masv = models.ForeignKey('Sinhvien', models.DO_NOTHING, db_column='MaSV')  # Field name made lowercase.
    mahp = models.ForeignKey('Hocphan', models.DO_NOTHING, db_column='MaHP')  # Field name made lowercase.
    diemhp = models.FloatField(db_column='DiemHP', blank=True, null=True)  # Field name made lowercase.
    id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'ChiTietDiem'


class Ghichu(models.Model):
    masv = models.ForeignKey('Sinhvien', models.DO_NOTHING, db_column='MaSV', blank=True, null=True)  # Field name made lowercase.
    magv = models.ForeignKey('Giaovien', models.DO_NOTHING, db_column='MaGV', blank=True, null=True)  # Field name made lowercase.
    noidung = models.TextField(db_column='Noidung', blank=True, null=True)  # Field name made lowercase.
    ngay = models.DateField(db_column='Ngay', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GhiChu'


class Giaovien(models.Model):
    magv = models.CharField(db_column='MaGV', primary_key=True, max_length=8)  # Field name made lowercase.
    tengv = models.CharField(db_column='TenGV', max_length=255, blank=True, null=True)  # Field name made lowercase.
    diachi = models.CharField(db_column='DiaChi', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sdt = models.CharField(db_column='SDT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    chucdanh = models.CharField(db_column='ChucDanh', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nganh = models.CharField(db_column='Nganh', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gioitinh = models.BooleanField(db_column='GioiTinh', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=100, blank=True, null=True)  # Field name made lowercase.
    phanhang = models.CharField(db_column='PhanHang', max_length=50, blank=True, null=True)  # Field name made lowercase.
    chucvu = models.CharField(db_column='ChucVu', max_length=50, blank=True, null=True)  # Field name made lowercase.
    ngaysinh = models.DateField(db_column='NgaySinh', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GiaoVien'


class Hocluc(models.Model):
    masv = models.OneToOneField('Sinhvien', models.DO_NOTHING, db_column='MaSV', primary_key=True)  # Field name made lowercase.
    sotinchi = models.IntegerField(db_column='SoTinChi', blank=True, null=True)  # Field name made lowercase.
    thangdiem10 = models.FloatField(db_column='ThangDiem10', blank=True, null=True)  # Field name made lowercase.
    thangdiem4 = models.FloatField(db_column='ThangDiem4', blank=True, null=True)  # Field name made lowercase.
    diemchu = models.CharField(db_column='DiemChu', max_length=25, blank=True, null=True)  # Field name made lowercase.
    xeploai = models.CharField(db_column='XepLoai', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HocLuc'


class Hocphan(models.Model):
    mahp = models.CharField(db_column='MaHP', primary_key=True, max_length=10)  # Field name made lowercase.
    tenhp = models.CharField(db_column='TenHP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sotc = models.SmallIntegerField(db_column='SoTC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HocPhan'


class Lophoc(models.Model):
    malh = models.CharField(db_column='MaLH', primary_key=True, max_length=25)  # Field name made lowercase.
    tenlh = models.CharField(db_column='TenLH', max_length=25, blank=True, null=True)  # Field name made lowercase.
    magv = models.ForeignKey(Giaovien, models.DO_NOTHING, db_column='MaGV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LopHoc'


class Sinhvien(models.Model):
    masv = models.CharField(db_column='MaSV', primary_key=True, max_length=8)  # Field name made lowercase.
    hodem = models.CharField(db_column='HoDem', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', max_length=255, blank=True, null=True)  # Field name made lowercase.
    malop = models.ForeignKey(Lophoc, models.DO_NOTHING, db_column='MaLop', blank=True, null=True)  # Field name made lowercase.
    gioitinh = models.BooleanField(db_column='GioiTinh', blank=True, null=True)  # Field name made lowercase.
    ngaysinh = models.DateField(db_column='NgaySinh', blank=True, null=True)  # Field name made lowercase.
    dantoc = models.CharField(db_column='DanToc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    noisinh = models.CharField(db_column='NoiSinh', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sodt = models.CharField(db_column='SoDT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ghichu = models.TextField(db_column='GhiChu', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SinhVien'


class Taikhoan(models.Model):
    magv = models.OneToOneField(Giaovien, models.DO_NOTHING, db_column='MaGV', primary_key=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TaiKhoan'


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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
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
