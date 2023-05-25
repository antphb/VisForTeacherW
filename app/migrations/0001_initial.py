# Generated by Django 3.2.18 on 2023-03-22 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chitietdiem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diemhp', models.FloatField(blank=True, db_column='DiemHP', null=True)),
            ],
            options={
                'db_table': 'ChiTietDiem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Giaovien',
            fields=[
                ('magv', models.TextField(db_column='MaGV', primary_key=True, serialize=False)),
                ('tengv', models.TextField(blank=True, db_column='TenGV', null=True)),
                ('diachi', models.TextField(blank=True, db_column='DiaChi', null=True)),
                ('sdt', models.TextField(blank=True, db_column='SDT', null=True)),
                ('chucdanh', models.TextField(blank=True, db_column='ChucDanh', null=True)),
                ('nganh', models.TextField(blank=True, db_column='Nganh', null=True)),
            ],
            options={
                'db_table': 'GiaoVien',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hocphan',
            fields=[
                ('mahp', models.TextField(db_column='MaHP', primary_key=True, serialize=False)),
                ('tenhp', models.TextField(blank=True, db_column='TenHP', null=True)),
                ('sotc', models.TextField(blank=True, db_column='SoTC', null=True)),
            ],
            options={
                'db_table': 'HocPhan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lophoc',
            fields=[
                ('malh', models.TextField(db_column='MaLH', primary_key=True, serialize=False)),
                ('tenlh', models.TextField(blank=True, db_column='TenLH', null=True)),
            ],
            options={
                'db_table': 'LopHoc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sinhvien',
            fields=[
                ('masv', models.TextField(db_column='MaSV', primary_key=True, serialize=False)),
                ('hodem', models.TextField(blank=True, db_column='HoDem', null=True)),
                ('ten', models.TextField(blank=True, db_column='Ten', null=True)),
                ('gioitinh', models.BooleanField(blank=True, db_column='GioiTinh', null=True)),
                ('ngaysinh', models.DateField(blank=True, db_column='NgaySinh', null=True)),
                ('dantoc', models.TextField(blank=True, db_column='DanToc', null=True)),
                ('noisinh', models.TextField(blank=True, db_column='NoiSinh', null=True)),
                ('email', models.TextField(blank=True, db_column='Email', null=True)),
                ('sodt', models.TextField(blank=True, db_column='SoDT', null=True)),
            ],
            options={
                'db_table': 'SinhVien',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Taikhoan',
            fields=[
                ('magv', models.OneToOneField(db_column='MaGV', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app.giaovien')),
                ('password', models.TextField(blank=True, db_column='Password', null=True)),
            ],
            options={
                'db_table': 'TaiKhoan',
                'managed': False,
            },
        ),
    ]
