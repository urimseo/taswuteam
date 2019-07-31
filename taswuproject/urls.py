from django.contrib import admin
from django.urls import path, include

import tasuapp.views
import accounts.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tasuapp.views.home, name = 'home'),
    path('taxi/', tasuapp.views.taxi, name = 'taxi'),
    path('car/', tasuapp.views.car, name = 'car'),
    path('mypage/', tasuapp.views.mypage, name = 'mypage'),
    path('extra/', tasuapp.views.extra, name = 'extra'),
    path('accounts/', include('accounts.urls')),
    path('hwarang/',tasuapp.views.hwarang, name='hwarang'),
    path('taereung/',tasuapp.views.taereung, name='taereung'),
    path('seokgye/',tasuapp.views.seokgye, name='seokgye'),
]



