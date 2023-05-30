import datetime
from django.http import JsonResponse
from django.db.models import Avg, Q, Exists, OuterRef, Subquery, Sum

from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt,csrf_protect 
from .models import *
import pandas as pd
import numpy as np
# {{request.user.is_superuser}}
# Create your views here.
sotinChi= {
    "13": 120,
    "14": 128,
    "15": 146,
    "16": 156,
}

nganhHoc={
    "KHMT": "Khoa Học Máy Tính",
    "HTTT": "Hệ Thống Thông Tin",
    "KTPM": "Kỹ Thuật Phần Mềm",
    "CNTT": "Công Nghệ Thông Tin",
    "KHDL": "Khoa Học Dữ Liệu",
}

khoahoc={
    "13": "2017 - 2018",
    "14": "2018 - 2019",
    "15": "2019 - 2020",
    "16": "2020 - 2021",
    "17": "2021 - 2022",
}

def sotinChicuaKhoa(lophoc):
    tongsotinchi=None
    for i in sotinChi.keys():
        if i in lophoc:
            tongsotinchi=sotinChi[i]
            break
    return tongsotinchi

def nganhHoccuaKhoa(lophoc):
    nganh=None
    for i in nganhHoc.keys():
        if i in lophoc:
            nganh=nganhHoc[i]
            break
    return nganh

def khoahoccuaKhoa(lophoc):
    khoa=None
    for i in khoahoc.keys():
        if i in lophoc:
            khoa=khoahoc[i]
            break
    return khoa

def Graduate_student_list(Magv):
    graduated=[]
    giang_vien = Giaovien.objects.get(magv=Magv)
    student=Sinhvien.objects.filter(malop__magv=giang_vien)
    for stu in student:
        try:
            hoclucStudent=Hocluc.objects.get(masv=stu.masv)
            tinchiStu=hoclucStudent.sotinchi
            lophop= stu.malop.malh.strip()
            tongsotinchi= sotinChicuaKhoa(lophop)
            # chung chi toeic
            diemhe4=round(hoclucStudent.thangdiem4,2)
            chungChiToeic=Chitietdiem.objects.get(masv=stu.masv,mahp="4203002027")

            gdqp= Chitietdiem.objects.filter(
                    masv__masv=stu.masv,
                    mahp__mahp__in=['4203003242', '4203003354']
                ).values('masv').annotate(avg_diemhp=Avg('diemhp'))
            avgdiemgdqp=gdqp[0]['avg_diemhp']

            gdtc= Chitietdiem.objects.filter(
                    masv__masv=stu.masv,
                    mahp__mahp__in=['4203003307', '4203003306']
                ).values('masv').annotate(avg_diemhp=Avg('diemhp'))
            # print(gdtc)
            avgdiemgdtc=gdtc[0]['avg_diemhp']

            if chungChiToeic.diemhp>=450 and diemhe4 >=2.00 and avgdiemgdqp>=3 and avgdiemgdtc>=3 and tinchiStu>=tongsotinchi:
                graduated.append(stu)
        except:
            pass

    return graduated


class home(View):
    def get(self, request):
        giaovien=Giaovien.objects.get(magv=request.user)
        gioitinh="Nam" if giaovien.gioitinh else "Nữ"
        ngaysinh=giaovien.ngaysinh.strftime('%d/%m/%Y')
        diachi=giaovien.diachi.split("-")[3]
        sumStudentClass=0
        if request.user.is_superuser:
            try:
                giaoviens=Giaovien.objects.all()
                classOfTeacher=Lophoc.objects.all()
                tongSoLop=classOfTeacher.count()
                tongSoSinhVien=Sinhvien.objects.all().count()
                soluongTotnghiep=0
                for gv in giaoviens:
                    soluongTotnghiep+=len(Graduate_student_list(gv.magv))
            except:
                pass
        else:
            classOfTeacher=Lophoc.objects.filter(magv=giaovien.magv)
            tongSoLop=classOfTeacher.count()
            # print(classOfTeacher)
            soluongTotnghiep=len(Graduate_student_list(request.user))
        for sumClass in classOfTeacher:
            sumStudentClass+=Sinhvien.objects.filter(malop=sumClass.malh).count()
        return render(request, 'app/home.html',locals())

class base(View):
    def get(self, request):
        if request.user.is_superuser:
            classOfTeacher=Lophoc.objects.all()
        else:
            giaovien=Giaovien.objects.get(magv=request.user)
            classOfTeacher=Lophoc.objects.filter(magv=giaovien.magv)
        dict_class={}
        for cOT in classOfTeacher:
            dict_class[cOT.malh.strip()]=cOT.tenlh.strip()
        return JsonResponse(dict_class)
        

class APIClass(APIView):
    def get(self, request):
        if request.user.is_superuser:
            giaovien=Giaovien.objects.all()
            classOfTeacher=Lophoc.objects.all()
        else:
            giaovien=Giaovien.objects.get(magv=request.user)
            classOfTeacher=Lophoc.objects.filter(magv=giaovien.magv)
        # print(classOfTeacher)
        class_List_dict={}
        sumStudentClass=0
        for sumClass in classOfTeacher:
            count_student_in_class=Sinhvien.objects.filter(malop=sumClass.malh).count()
            class_List_dict[sumClass.tenlh.strip()]=count_student_in_class
            sumStudentClass+=count_student_in_class
        class_List_dict["ALL"]=sumStudentClass
        return Response(class_List_dict)


class tableStudent(View):
    def get(self, request,val):
        try:
            val=val.strip()
            if val=="ALL":
                if request.user.is_superuser:
                    students=Sinhvien.objects.all().order_by('ten')
                    # Lấy trường malh trong bảng lớp học
                else:
                    lophoc=[i.malh.strip() for i in Lophoc.objects.filter(magv=Giaovien.objects.get(magv=request.user).magv)]
                    students = Sinhvien.objects.filter(Q(malop__in=lophoc)).order_by('ten')
                # print(students)
            elif val=="Graduated":
                if request.user.is_superuser:
                    giaovien=Giaovien.objects.all()
                    students=[]
                    for gv in giaovien:
                        students.extend(Graduate_student_list(gv.magv))
                else:
                    students=Graduate_student_list(request.user)
            else:
                students = Sinhvien.objects.filter(malop=val).order_by('ten')
            maLop=val
            ngaysinhs=[]
            gioitinhs=[]
            diemtb4s=[]
            soTCs=[]
            notes=[]
            
            for student in students:
                ngaysinh=student.ngaysinh.strftime('%Y/%m/%d')
                ngaysinhs.append(ngaysinh)
                gioitinhs.append("Nam" if student.gioitinh==True else "Nữ")
                diemtb4s.append(round(Hocluc.objects.filter(masv=student.masv)[0].thangdiem4,2))
                # print(val)
                soTCs.append(Hocluc.objects.filter(masv=student.masv)[0].sotinchi)
                notes.append(Ghichu.objects.filter(masv=student.masv).count())
            dslh = [x.strip() for x in Lophoc.objects.all().values_list('malh', flat=True)]
            data=zip(students,ngaysinhs,gioitinhs,diemtb4s,soTCs,notes)        
            return render(request, 'app/tableStudent.html', locals())
        except:
            return render(request, 'app/home.html', locals())
    
class APIChartBarScoreView(APIView):
    def get(self, request,val):
        if val=="ALL".lower():
            if request.user.is_superuser:
                students=Sinhvien.objects.all().order_by('ten')
            else:
                lophoc=[i.malh.strip() for i in Lophoc.objects.filter(magv=Giaovien.objects.get(magv=request.user).magv)]
                students = Sinhvien.objects.filter(Q(malop__in=lophoc)).order_by('ten')
        else:
            students = Sinhvien.objects.filter(malop=val).order_by('ten')

        scores = {}
        msSt={}
        for student in students:
            hocluc=Hocluc.objects.filter(masv=student.masv)
            name=student.hodem.strip()+" "+student.ten.strip()
            scores[name] = round(hocluc[0].thangdiem4,2)
            msSt[name]=student.masv
        sumdict={}
        sumdict['scores']=scores
        sumdict['msSt']=msSt
        return Response(sumdict)
    
class APIChartScatterScoreView(APIView):
    def get(self, request):
        if request.user.is_superuser:
            lophoc=[i.malh.strip() for i in Lophoc.objects.all()]
        else:
            lophoc=[i.malh.strip() for i in Lophoc.objects.filter(magv=Giaovien.objects.get(magv=request.user).magv)]
        dictLop_Score={}
        for grade in lophoc:
            students = Sinhvien.objects.filter(Q(malop=grade)).order_by('ten')
            scores = {}
            for student in students:
                hocluc=Hocluc.objects.filter(masv=student.masv)
                name=student.hodem.strip()+" "+student.ten.strip() + " - " + student.masv.strip()
                scores[name] = round(hocluc[0].thangdiem4,2)
            dictLop_Score[grade]=scores

        return Response(dictLop_Score)

class APIChartBarSexView(APIView):
    def get(self, request):
        if request.user.is_superuser:
            lophoc=[i.malh.strip() for i in Lophoc.objects.all()]
        else:
            lophoc=[i.malh.strip() for i in Lophoc.objects.filter(magv=Giaovien.objects.get(magv=request.user).magv)]
        students = Sinhvien.objects.filter(Q(malop__in=lophoc)).order_by('ten')
        sexs={}
        for grade in lophoc:
            students = Sinhvien.objects.filter(Q(malop=grade)).order_by('ten')
            sexs[grade]={}
            sexs[grade]['Nam']=0
            sexs[grade]['Nữ']=0
            for student in students:
                if student.gioitinh==True:
                    sexs[grade]['Nam']+=1
                else:
                    sexs[grade]['Nữ']+=1
            
        return Response(sexs)    

class APIChartBarRankALLView(APIView):
    def get(self,request):
        if request.user.is_superuser:
            lophoc=[i.malh.strip() for i in Lophoc.objects.all()]
        else:
            lophoc=[i.malh.strip() for i in Lophoc.objects.filter(magv=Giaovien.objects.get(magv=request.user).magv)]
        students = Sinhvien.objects.filter(Q(malop__in=lophoc)).order_by('ten')
        ranks={}
        # {"xuất sắc": {"KHDL16A": 10, "KHMT": 6}}
        # 'Xuất sắc', 'Giỏi', 'Khá', 'Trung bình', 'Trung bình yếu', 'Kém'
        ranks['Xuất sắc']={}
        ranks['Giỏi']={}
        ranks['Khá']={}
        ranks['Trung bình']={}
        ranks['Trung bình yếu']={}
        ranks['Kém']={}
        for grade in lophoc:
            students = Sinhvien.objects.filter(Q(malop=grade)).order_by('ten')
            for student in students:
                hocluc=Hocluc.objects.filter(masv=student.masv)
                rank=str(hocluc[0].xeploai).strip()
                ranks[rank][grade]=ranks[rank].get(grade,0)+1
            for rank in ranks:
                if ranks[rank].get(grade,0)==0:
                    ranks[rank][grade]=0
        
        return Response(ranks)


class APIChartPieRankView(APIView):
    def get(self, request,val):
        if val=="ALL".lower():
            if request.user.is_superuser:
                students=Sinhvien.objects.all().order_by('ten')
            else:
                lophoc=[i.malh.strip() for i in Lophoc.objects.filter(magv=Giaovien.objects.get(magv=request.user).magv)]
                students = Sinhvien.objects.filter(Q(malop__in=lophoc)).order_by('ten')
        else:
            students = Sinhvien.objects.filter(malop=val).order_by('ten')
        ranks={}
        for student in students:
            hocluc=Hocluc.objects.filter(masv=student.masv)
            rank=str(hocluc[0].xeploai).strip()
            ranks[rank]=ranks.get(rank,0)+1
        # print(ranks)
        ranks = dict(sorted(ranks.items(),key=lambda x: ['Xuất sắc', 'Giỏi', 'Khá', 'Trung bình', 'Trung bình yếu', 'Kém'].index(x[0])))
        return Response(ranks)


class infomationStudent(View):
    def get(self, request, val):
        student = Sinhvien.objects.get(masv=val)
        hoclucStudent=Hocluc.objects.get(masv=student.masv)
        if request.user.is_superuser:
            dslh = [x.strip() for x in Lophoc.objects.all().values_list('malh', flat=True)]
        tinchiStu=hoclucStudent.sotinchi

        noisinh=student.noisinh.split(",")[-1].strip()
        gioitinh="Nam" if student.gioitinh==True else "Nữ"
        ngaysinh=student.ngaysinh.strftime('%d/%m/%Y')
        countGhiChu=Ghichu.objects.filter(masv=val).count()

        # 4203002027 chứng chỉ toeic
        totnghieped="Đang học"
        lophop= student.malop.malh.strip()
        tongsotinchi= sotinChicuaKhoa(lophop)
        nganhHoc=nganhHoccuaKhoa(lophop)
        khoaHoc= khoahoccuaKhoa(lophop)
        try:
            # chung chi toeic
            diemhe4=round(hoclucStudent.thangdiem4,2)
            chungChiToeic=Chitietdiem.objects.get(masv=student.masv,mahp="4203002027")

            gdqp= Chitietdiem.objects.filter(
                    masv__masv=student.masv,
                    mahp__mahp__in=['4203003242', '4203003354']
                ).values('masv').annotate(avg_diemhp=Avg('diemhp'))
            avgdiemgdqp=gdqp[0]['avg_diemhp']

            gdtc= Chitietdiem.objects.filter(
                    masv__masv=student.masv,
                    mahp__mahp__in=['4203003307', '4203003306']
                ).values('masv').annotate(avg_diemhp=Avg('diemhp'))
            # print(gdtc)
            avgdiemgdtc=gdtc[0]['avg_diemhp']

            if chungChiToeic.diemhp>=450 and diemhe4 >=2.00 and avgdiemgdqp>=3 and avgdiemgdtc>=3 and tinchiStu>=tongsotinchi:
                totnghieped="Đã tốt nghiệp"
        except Exception as e:
            # print(e)
            pass

        return render(request, 'app/infoStudent.html', locals())

class detailInfoStudent(View):
    def get(self,request,val):
        student = Sinhvien.objects.get(masv=val)

        noisinh=student.noisinh.split(",")[-1].strip()
        diachi= student.noisinh.strip()
        hoten=student.hodem.strip()+" "+student.ten.strip()
        gioitinh="Nam" if student.gioitinh==True else "Nữ"
        lophoc=student.malop.tenlh.strip()
        ngaysinh=student.ngaysinh.strftime('%Y/%m/%d')
        dantoc=student.dantoc.strip()
        sdt=student.sodt.strip()
        email=student.email.strip()

        return render(request, 'app/detailInfoStudent.html', locals())

class APIChartBarScoreStudentXView(APIView):
    def get(self,request,val):
        student = Sinhvien.objects.get(masv=val)
        lophoc=student.malop
        diemhocphan=Chitietdiem.objects.filter(masv=student.masv) 
        dicttong={}
        score_hocphan={}
        mahpHoc={}
        for i in diemhocphan:
            namehp=i.mahp.tenhp.strip()
            if namehp =="Tiếng anh 1" or namehp == "Tiếng Anh 2" or namehp=="Chứng chỉ TOEIC 450":
                continue
            score_hocphan[namehp]=round(i.diemhp,2)
            mahpHoc[i.mahp.mahp]=namehp
        dicttong['score_hocphan']=score_hocphan
        key_mhp=mahpHoc.keys()
        mean_score={}

        student_in_Class=Sinhvien.objects.filter(malop=lophoc)
        masv_in_Class=[i.masv for i in student_in_Class]
        # print(masv_in_Class)
        for mahp in key_mhp:
            diemhocphanall=Chitietdiem.objects.filter(Q(mahp=mahp) & Q(masv__in=masv_in_Class))
            count=0
            sum=0
            for dhp in diemhocphanall:
                count+=1
                sum+=dhp.diemhp
            mean_score[mahpHoc[mahp]]=round(sum/count,2)

        dicttong['mean_score']=mean_score
        return Response(dicttong)


class APIChartRidialBarTinhChiStudentXView(APIView):
    def get(self,request, val):
        student = Sinhvien.objects.get(masv=val)
        lophoc=student.malop.malh.strip()
        hoclucStudent=Hocluc.objects.filter(masv=student.masv)
        dictTinChi={}
        # soTCcurrent=str(student.masv.sotinchi)
        tinchiStu=hoclucStudent[0].sotinchi

        dictTinChi['allpercentTinChi']=100
        dictTinChi['tinchiStu']=tinchiStu
        
        sotinchi=sotinChicuaKhoa(lophoc)
        dictTinChi['tinchiAll']=sotinchi
        percentTinChi=int((tinchiStu/sotinchi)*100)
        dictTinChi['percentTinChi']=percentTinChi
        # dictTinChi['tinchiAll']=156
        return Response(dictTinChi)

class APISummaryRankSubjectStudentX(APIView):
    def get(self,request,val):
        student = Sinhvien.objects.filter(masv=val).order_by('ten')
        student=student[0]
        diemhocphan=Chitietdiem.objects.filter(masv=student.masv)
        rank_hocphan={}
        rank_thang4={}
        for i in diemhocphan:
            namehp=i.mahp.tenhp.strip()
            if namehp =="Tiếng anh 1" or namehp == "Tiếng Anh 2":
                continue
            rankdiem=i.diemhp
            if rankdiem>=9 and rankdiem<=10:
                rank_thang4[namehp]="4.0"
                rank_hocphan['A+']=rank_hocphan.get('A+',0)+1
            elif rankdiem>=8.5 and rankdiem<9:
                rank_thang4[namehp]="3.8"
                rank_hocphan['A']=rank_hocphan.get('A',0)+1
            elif rankdiem>=8 and rankdiem<8.5:
                rank_thang4[namehp]="3.5"
                rank_hocphan['B+']=rank_hocphan.get('B+',0)+1
            elif rankdiem>=7 and rankdiem<8:
                rank_thang4[namehp]="3.0"
                rank_hocphan['B']=rank_hocphan.get('B',0)+1
            elif rankdiem>=6 and rankdiem<7:
                rank_thang4[namehp]="2.5"
                rank_hocphan['C+']=rank_hocphan.get('C+',0)+1
            elif rankdiem>=5.5 and rankdiem<6:
                rank_thang4[namehp]="2.0"
                rank_hocphan['C']=rank_hocphan.get('C',0)+1
            elif rankdiem>=5 and rankdiem<5.5:
                rank_thang4[namehp]="1.5"
                rank_hocphan['D+']=rank_hocphan.get('D+',0)+1
            elif rankdiem>=4 and rankdiem<5:
                rank_thang4[namehp]="1.0"
                rank_hocphan['D']=rank_hocphan.get('D',0)+1
            elif rankdiem>=0 and rankdiem<4:
                rank_thang4[namehp]="0"
                rank_hocphan['F']=rank_hocphan.get('F',0)+1
        disSum={}
        rank_hocphan = dict(sorted(rank_hocphan.items(), key=lambda x: ["A+", "A", "B+", "B", "C+", "C", "D+","D","F"].index(x[0])))
        disSum['rank_hocphan']=rank_hocphan
        rank_thang4=dict(sorted(rank_thang4.items(), key=lambda x: x[1], reverse=True))
        disSum['rank_thang4']=rank_thang4
        return Response(disSum)
    

class listNoteStudent(View):
    def get(self,request,val, masv):
        if val.lower() == "all" and masv.lower() == "all":
            ghichu= Ghichu.objects.all()
            tenlophoc= "Tất cả"
        elif val.lower() != "all" and masv.lower() == "all":
            ghichu= Ghichu.objects.filter(masv__malop=val)
            if len(ghichu) != 0:
                tenlophoc= ghichu[0].masv.malop.tenlh
        else:
            ghichu= Ghichu.objects.filter(masv=masv)
            if len(ghichu) != 0:
                tenlophoc= ghichu[0].masv.malop.tenlh
        ngayNote=[]
        for i in ghichu:
            ngayNote.append(i.ngay.strftime('%Y/%m/%d'))
        data=zip(ghichu,ngayNote)
        return render(request, 'app/listNoteStudent.html',locals())

class detailin4Teacher(View):
    def get(self,request):
        val= request.user
        giaovien= Giaovien.objects.get(magv=val)
        gioitinh="Nam" if giaovien.gioitinh else "Nữ"
        ngaysinh=giaovien.ngaysinh.strftime('%d/%m/%Y')
        return render(request, 'app/detailinfoTeach.html',locals())

class deleteNoteStudent(View):
    def get(self,request,mssv,id):
        SinhVienghichu= Ghichu.objects.get(masv=mssv, id=id)
        # print(SinhVienghichu.masv.masv, SinhVienghichu.id)
        SinhVienghichu.delete()
        return  redirect(request.META.get('HTTP_REFERER'))

class addNoteStudent(View):
    def post(self,request,mssv):
        masv= mssv
        magv= request.user
        ngay= request.POST['addNgay']
        noidung= request.POST['addNoiDung']
        # print(masv, magv ,noidung, ngay)
        ghichu= Ghichu(masv= Sinhvien.objects.get(masv=masv), magv= Giaovien.objects.get(magv=magv), noidung=noidung, ngay=ngay)
        ghichu.save()
        return redirect(request.META.get('HTTP_REFERER'))

class editNoteStudent(View):
    def post(self,request,mssv,id):
        ngay= request.POST['editNgay']
        noidung= request.POST['editNoiDung']
        ghichu= Ghichu.objects.get(masv=mssv, id=id)
        ghichu.noidung= noidung
        ghichu.ngay= ngay
        ghichu.save()
        return redirect(request.META.get('HTTP_REFERER'))
    
class editInfoTeacher(View):
    def post(self,request):
        msgv= request.POST['msgv']
        email= request.POST['email']
        sdt= request.POST['sdt']
        tinhThanh= request.POST['tinhthanh']
        quanHuyen= request.POST['quanhuyen']
        phuongXa= request.POST['phuongxa']
        sonhaDuong= request.POST['sonhatenduong']
        diachi= sonhaDuong + "-" + phuongXa + "-" + quanHuyen + "-" + tinhThanh
        # print(msgv, email, sdt, diachi)
        giaovien= Giaovien.objects.get(magv=msgv)
        giaovien.email= email
        giaovien.sdt= sdt
        giaovien.diachi= diachi
        giaovien.save()
        request.user.email = email
        request.user.save()
        return redirect(request.META.get('HTTP_REFERER'))

class AddInfoTeacher(View):
    def post(self,request):
        msgv= request.POST['mgv']
        tengv= request.POST['tengv']
        gioitinh= request.POST['gioitinh']
        ngaysinh= request.POST['ngaysinh']
        sdt= request.POST['sdt']
        email= request.POST['email']
        sonhatenduong= request.POST['sonhatenduong']
        tinhthanh= request.POST['tinhthanh']
        quanhuyen= request.POST['quanhuyen']
        phuongxa= request.POST['phuongxa']
        chucdanh= request.POST['hocvi']
        phanhang= request.POST['phanhang']
        chuyennganh= request.POST['chuyennganh']
        chucvi= request.POST['chucvi']
        diachi= sonhatenduong + "-" + phuongxa + "-" + quanhuyen + "-" + tinhthanh
        giaovien= Giaovien(magv=msgv, tengv=tengv, gioitinh=gioitinh, ngaysinh=ngaysinh, sdt=sdt, email=email, diachi=diachi, chucdanh=chucdanh, phanhang=phanhang, nganh=chuyennganh, chucvu=chucvi)
        giaovien.save()
        user= User.objects.create_user(username=msgv, password="11111111", email=email)
        user.save()
        return redirect(request.META.get('HTTP_REFERER'))

class addClass(View):
    def post(self,request):
        malop= request.POST['malop']
        tenlop= request.POST['tenlop']
        gv= request.POST['gv']
        magv=gv.split("-")[0]
        lophoc= Lophoc(malh=malop, tenlh=tenlop, magv=Giaovien.objects.get(magv=magv))
        lophoc.save()
        return redirect(request.META.get('HTTP_REFERER'))

def conv(string):
    if string[-1:] == "*":
        return string[:len(string)-1].strip()
    else:
        return string.strip()

def sp(string):
    return string.split('(')[0]   


def fun_update_Score(file_nien_giam, file_diem):
    df_ng = pd.read_excel(file_nien_giam)
    df_ng.columns = df_ng.iloc[6].tolist()
    df_ng = df_ng.iloc[7:].dropna(subset=['Mã môn học'])
    HP = df_ng[["Mã học phần", "Tên môn học", "Số tín chỉ"]].dropna()
    HP["Tên môn học"] = HP["Tên môn học"].apply(conv)
    HP["Số tín chỉ"] = HP["Số tín chỉ"].apply(sp)
    HP = HP.astype({"Mã học phần": np.int64})

    mhp = [str(HP["Mã học phần"].values[i]) for i in range(len(HP))]
    tenhp = [str(HP["Tên môn học"].values[i]) for i in range(len(HP))]
    sotc = [str(HP["Số tín chỉ"].values[i]) for i in range(len(HP))]

    ds_hp = []

    for m, t, s in zip(mhp, tenhp, sotc):
        hp = {"mhp": m, "tenhp": t, "soTC": s}
        ds_hp.append(hp)

    df2 = pd.read_excel(file_diem)
    df2.columns = df2.iloc[7].tolist()
    df2 = df2.iloc[8:].dropna(subset=['Họ đệm']).reset_index(drop=True)
    a = pd.DataFrame(ds_hp)
    df2.columns = [str(i).strip() for i in df2.columns]
    len_sub = len(ds_hp)

    mssv = [str(df2["Mã sinh viên"].values[i]) for i in range(len(df2)) for j in range(len_sub) if str(df2.iloc[:, j+4][i]) != 'nan']
    mhp = [a["mhp"][a["tenhp"]==df2.columns[j+4]].values[0] for i in range(len(df2)) for j in range(len_sub) if str(df2.iloc[:, j+4][i]) != 'nan']
    dtp = [str(df2.iloc[:, j+4][i]) for i in range(len(df2)) for j in range(len_sub) if str(df2.iloc[:, j+4][i]) != 'nan']

    ds_dsv = []

    for m, t, s in zip(mssv, mhp, dtp):
        hp = {"mssv": m, "mhp": t, "dtp": s}
        ds_dsv.append(hp)
    # các cột 'Học lực', 'nan', 'nan', 'nan', 'nan'  và đổi tên cột thành "Số tín chỉ","Điểm 10", "Điểm4","Điểm chữ", "Xếp loại" 
    df3 = df2.iloc[:, -7:-2]
    df3.columns = ["Số tín chỉ","Điểm 10", "Điểm4","Điểm chữ", "Xếp loại"]  
    # Bây giờ thêm df2["Mã sinh viên"] vào df3
    df3["Mã sinh viên"] = df2["Mã sinh viên"]
    # hocluc= Hocluc.objects.create(masv= Sinhvien.objects.get(masv=df3["Mã sinh viên"][i]), sotinchi= df3["Số tín chỉ"][i], thangdiem10= df3["Điểm 10"][i], thangdiem4= df3["Điểm4"][i], diemchu= df3["Điểm chữ"][i], xeploai= df3["Xếp loại"][i])
    for i in range(len(df3)):
        try:
            hocluc= Hocluc.objects.get(masv= Sinhvien.objects.get(masv=df3["Mã sinh viên"][i]))
        except:
            hocluc= Hocluc.objects.create(masv= Sinhvien.objects.get(masv=df3["Mã sinh viên"][i]))
        hocluc.sotinchi= df3["Số tín chỉ"][i]
        hocluc.thangdiem10= df3["Điểm 10"][i]
        hocluc.thangdiem4= df3["Điểm4"][i]
        hocluc.diemchu= df3["Điểm chữ"][i]
        hocluc.xeploai= df3["Xếp loại"][i]
        hocluc.save()

    # chitietdiem= Chitietdiem.objects.all()
    for i in range(len(ds_dsv)):
        if Chitietdiem.objects.filter(masv=ds_dsv[i]["mssv"], mahp=ds_dsv[i]["mhp"]).exists():
            chitietdiem= Chitietdiem.objects.get(masv=ds_dsv[i]["mssv"], mahp=ds_dsv[i]["mhp"])
            chitietdiem.dtp= ds_dsv[i]["dtp"]
            # chitietdiem.save()
        else:
            chitietdiem= Chitietdiem(masv= Sinhvien.objects.get(masv=ds_dsv[i]["mssv"]), mahp= Hocphan.objects.get(mahp=ds_dsv[i]["mhp"]), diemhp= ds_dsv[i]["dtp"])
                # chitietdiem.save()

class UpdateScore(View):
    def get(self,request):
        return render(request, 'app/UpdateScore.html',locals())
    
    def post(self, request):
        name_file_niengiam= request.POST['name_file_niengiam']
        name_file_diem= request.POST['name_file_diem']
        fun_update_Score(name_file_niengiam,name_file_diem)
        return redirect(request.META.get('HTTP_REFERER'))

def fun_update_Student(name_file,name_lop):
    df3 = pd.read_excel(name_file)
    df3.columns = df3.iloc[7].tolist()
    df3.drop(df3.columns[12], axis=1, inplace=True)
    df3 = df3.iloc[8:, :13].dropna(subset=['Họ đệm']).reset_index(drop=True)
    msv = [value if pd.notnull(value) else '' for value in df3['Mã SV'].tolist()]
    ho = [value if pd.notnull(value) else '' for value in df3['Họ đệm'].tolist()]
    ten = [value if pd.notnull(value) else '' for value in df3['Tên'].tolist()]
    sex = [value if pd.notnull(value) else '' for value in df3['Giới tính'].tolist()]
    date = [value if pd.notnull(value) else '' for value in df3['Ngày sinh'].tolist()]
    race = [value if pd.notnull(value) else '' for value in df3['Dân tộc'].tolist()]
    tg = [value if pd.notnull(value) else '' for value in df3['Tôn giáo'].tolist()]
    hk = [value if pd.notnull(value) else '' for value in df3['Hộ khẩu thường trú'].tolist()]
    wborn = [value if pd.notnull(value) else '' for value in df3['Nơi Sinh'].tolist()]
    ema = [value if pd.notnull(value) else '' for value in df3['Email'].tolist()]
    sdt = [value if pd.notnull(value) else '' for value in df3['Số ĐT'].tolist()]
    gc = [value if pd.notnull(value) else '' for value in df3['Ghi chú'].tolist()]

    today= datetime.date.today()
    malophoc=Lophoc.objects.get(malh=name_lop)
    sinhvienTT= Sinhvien.objects.filter(malop= malophoc)
    giaovien = malophoc.magv
    if len(sinhvienTT) == 0:
        for m, h, t, s, d, r, tg, hk, w, e, sdt_1, gc in zip(msv, ho, ten, sex, date, race, tg, hk, wborn, ema, sdt, gc):
            gioitinh= 1 if s == 'Nam' else 0
            # “03/10/2002” value has an invalid date format. It must be in YYYY-MM-DD format
            ns= datetime.datetime.strptime(d, '%d/%m/%Y').strftime('%Y-%m-%d')
            sinhvien = Sinhvien(masv= m, malop=malophoc, hodem=h,ten=t,gioitinh=gioitinh,ngaysinh=ns,dantoc=r,noisinh=hk,email=e,sodt=sdt_1)
            sinhvien.save()
            if gc != '':
                sinhvienghichu= Sinhvien.objects.get(masv=m)
                ghichusv= Ghichu.objects.create(masv= sinhvienghichu, magv= giaovien, noidung=gc, ngay=today)
    else:
        for m, h, t, s, d, r, tg, hk, w, e, sdt_1, gc in zip(msv, ho, ten, sex, date, race, tg, hk, wborn, ema, sdt, gc):
            gioitinh= 1 if s == 'Nam' else 0
            ns= datetime.datetime.strptime(d, '%d/%m/%Y').strftime('%Y-%m-%d')
            sinhvien= Sinhvien.objects.get(Q(masv=m) & Q(malop=malophoc))
            sinhvien.hodem=h
            sinhvien.ten=t
            sinhvien.gioitinh=gioitinh
            sinhvien.ngaysinh=ns
            sinhvien.dantoc=r
            sinhvien.noisinh=hk
            sinhvien.email=e
            sinhvien.sodt=sdt_1
            sinhvien.save()
            if gc != '':
                ghichutontai= Ghichu.objects.filter(masv=sinhvien)
                for gcTT in ghichutontai:
                    if gcTT.noidung != gc:
                        ghichusv= Ghichu(masv=sinhvien ,magv= giaovien, noidung=gc, ngay=today)
                        ghichusv.save()
        dssvTT=sinhvienTT.values_list('masv', flat=True)
        for mssvTT in dssvTT:
            if mssvTT not in msv:
                sinhvien= Sinhvien.objects.get(Q(masv=mssvTT) & Q(malop=malophoc))
                sinhvien.delete()
    

class UpdateStudentList(View):
    def get(self,request):
        giaovien= Giaovien.objects.exclude(chucvu = 'Admin')
        lophoc= Lophoc.objects.all()
        # sắp xếp theo tên lớp
        lophoc= sorted(lophoc, key=lambda x: x.tenlh)
        return render(request, 'app/UpdateStudent.html',locals())
    def post(self, request):
        name_file= request.POST['name_file']
        name_lophoc= request.POST['name_lophoc']
        fun_update_Student(name_file, name_lophoc)
        return redirect(request.META.get('HTTP_REFERER'))

class editInfoStudent(View):
    def post(self,request):
        mssv= request.POST['mssv']
        hoten= request.POST['hoten']
        lop= request.POST['lop']
        gioitinh= request.POST['gioitinh']
        dantoc= request.POST['dantoc']
        email= request.POST['email']
        sodt= request.POST['sodt']
        ngaysinh= request.POST['ngaysinh']
        sonhatenduong= request.POST['sonhatenduong']
        tinhthanh= request.POST['tinhthanh']
        quanhuyen= request.POST['quanhuyen']
        phuongxa= request.POST['phuongxa']
        diachi= sonhatenduong + "," + phuongxa + "," + quanhuyen + "," + tinhthanh
        tmpHoTen= hoten.split(" ")
        hoten= tmpHoTen[-1]
        hodem= " ".join(tmpHoTen[0:-1])
        # print(mssv, hoten, lop, gioitinh, dantoc, email, sodt, ngaysinh, diachi)
        sinhvien= Sinhvien.objects.get(masv=mssv)
        sinhvien.hodem= hodem
        sinhvien.ten= hoten
        sinhvien.malop= Lophoc.objects.get(malh=lop)
        sinhvien.gioitinh=  int(gioitinh)
        sinhvien.dantoc= dantoc
        sinhvien.email= email
        sinhvien.sodt= sodt
        sinhvien.ngaysinh= ngaysinh
        sinhvien.noisinh= diachi
        sinhvien.save()
        return redirect(request.META.get('HTTP_REFERER'))

class deleteInfoStudent(View):
    def get(self,request,mssv):
        chitietdiem= Chitietdiem.objects.filter(masv=mssv)
        chitietdiem.delete()
        sinhvien= Sinhvien.objects.get(masv=mssv)
        sinhvien.delete()
        return redirect(request.META.get('HTTP_REFERER'))

class aboutus(View):
    def get(self,request):
        return render(request, 'app/aboutUs.html',locals())
    
def logout_user(request):
    logout(request)
    return redirect('login')

