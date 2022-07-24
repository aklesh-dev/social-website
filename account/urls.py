from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # post views
    # path('login/',views.user_login, name='login'),
    # --login and logout urls
    # path('login/',auth_views.LoginView.as_view(), name='login'),
    # path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    # --change password urls
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # # --change password/done urls
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # # --reset password urls
    # path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # # -- reset  password/done urls
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # # --reset password confirm urls
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # # --reset password complete urls
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # --authentication URL pattern provided by django 
    path('', include('django.contrib.auth.urls')),
]
