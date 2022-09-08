
from django.contrib import admin
from django.urls import path
from pembukuan_kas.views import dashboard, laporan, transaksi, saldo , bulanan, detail
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),  
    path('transaksi/', transaksi,name='transaksi'),
    path('laporan/', laporan , name='laporan'),
    path('saldo/', saldo, name='saldo' ),
    path('bulanan/', bulanan, name= 'bulanan'),
    path('detail/<int:id>', detail, name='detail'),
]