"""TeachForTeacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from . import views
from django.contrib.auth import views as auth_views
from .forms import *
urlpatterns = [
    path('', RedirectView.as_view(url='/login/'),name='index'),
    
    path("profile/",views.home.as_view(),name="home"),
    
    path("APIbase/",views.base.as_view(),name="APIbase"),
    path("APIClass/",views.APIClass.as_view(),name="apiClass"),
    path('chart-data-score-home/<slug:val>', views.APIChartBarScoreView.as_view(), name='chart_bar_score'),
    path('chart-data-rank-home/<slug:val>', views.APIChartPieRankView.as_view(), name='chart_pie_rank'),
    path('chart-data-score-student-x/<slug:val>', views.APIChartBarScoreStudentXView.as_view(), name='chart_bar_score_student_x'),
    path('API-chart-scatter-score/', views.APIChartScatterScoreView.as_view(), name='api_chart_scatter_score'),
    path('API-chart-bar-sex/',views.APIChartBarSexView.as_view(),name="api_chart_bar_sex"),
    path('API-chart-bar-rank-all/',views.APIChartBarRankALLView.as_view(),name="api_chart_bar_rank_all"),

    path('chart-data-SoTinChi-student-x/<slug:val>', views.APIChartRidialBarTinhChiStudentXView.as_view(), name='chart_Radialbar_SoTinChi_student_x'),

    path('chart-data-RankScore-student-x/<slug:val>', views.APISummaryRankSubjectStudentX.as_view(), name='chart_data_RankScore_student_x'),

    
    path("tableStudent/<slug:val>",views.tableStudent.as_view(),name="tableStudent"),

    path("infoStudent/<slug:val>",views.infomationStudent.as_view(),name="infoStudent"),
    path("detail-student/<val>",views.detailInfoStudent.as_view(),name="detailstudent"),
    path("list-note-student/<val>/<masv>",views.listNoteStudent.as_view(),name="list-note-student"),

    path("detail-note-student/<mssv>/<id>",views.deleteNoteStudent.as_view(),name="detail-note-student"),
    path("add-note-student/<mssv>",views.addNoteStudent.as_view(),name="add-note-student"),
    path("edit-note-student/<mssv>/<id>",views.editNoteStudent.as_view(),name="edit-note-student"),

    path("edit-info-teacher/",views.editInfoTeacher.as_view(),name="edit-info-teacher"),

    path("detail-teacher/",views.detailin4Teacher.as_view(),name="detail-teacher"),

    path("update-list-score/",views.UpdateScore.as_view(),name="update-list-score"),

    # Login 
    path('login/',auth_views.LoginView.as_view(template_name='login/login.html', authentication_form=LoginForm),name='login'),
    
    path('change-password/',auth_views.PasswordChangeView.as_view(template_name='login/changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='change_password'),

    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='login/changepassworddone.html'),name='password_change_done'),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='login/resetPassword.html',form_class=MyPasswordResetForm),name='password_reset'),

    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='login/resetPasswordDone.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='login/resetPasswordConfirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='login/resetPasswordComplete.html'),name='password_reset_complete'),

    path("logout_user",views.logout_user,name="logout_user"),
]
