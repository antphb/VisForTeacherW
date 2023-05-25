from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Chitietdiem)
class ChitietdiemModelAdmin(admin.ModelAdmin):
    list_display = ['mahp','masv','diemhp']

@admin.register(Giaovien)
class GiaovienModelAdmin(admin.ModelAdmin):
    list_display = ['magv','tengv','diachi','sdt','chucdanh','nganh','email','phanhang','chucvu']

@admin.register(Hocphan)
class HocphanModelAdmin(admin.ModelAdmin):
    list_display = ['mahp','tenhp','sotc']

@admin.register(Lophoc)
class LophocModelAdmin(admin.ModelAdmin):
    list_display = ['malh','tenlh','magv']

@admin.register(Sinhvien)
class SinhvienModelAdmin(admin.ModelAdmin):
    list_display = ['masv','hodem','ten','malop','gioitinh','ngaysinh','dantoc','noisinh','email','sodt']

@admin.register(Ghichu)
class GhichuModelAdmin(admin.ModelAdmin):
    list_display = ['id','masv','magv','noidung','ngay']

@admin.register(Hocluc)
class HoclucModelAdmin(admin.ModelAdmin):
    list_display = ['masv','sotinchi','thangdiem10','thangdiem4','diemchu','xeploai']


