# Generated by Django 3.2.18 on 2023-04-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_authgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ghichu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noidung', models.TextField(blank=True, db_column='Noidung', null=True)),
                ('ngay', models.DateField(blank=True, db_column='Ngay', null=True)),
            ],
            options={
                'db_table': 'GhiChu',
                'managed': False,
            },
        ),
    ]
