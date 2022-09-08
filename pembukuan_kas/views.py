
from datetime import datetime, timedelta
from urllib.request import DataHandler
from django.shortcuts import render
import psycopg2
from pembukuan_kas import models
from datetime import date, timedelta


def dashboard(request):

    return  render(request, 'dashboard.html')

def detail(request, id):
    data = models.transaksi.objects.get(id=id)
    return render(request, 'detail.html', {
        'data' : data,
    })

def transaksi(request):
    if request.POST and request.FILES['Image']:
        varImage = request.FILES['Image']
        varUraian=request.POST["Uraian"]
        varTanggal=request.POST["Tanggal_Transaksi"]
        varStatus=request.POST["Status"]
        varNominal=request.POST["Nominal"]
        
        print(varUraian, varTanggal,'ZAHRAAA')
        models.transaksi.objects.create(Image= varImage, Uraian=varUraian, Tanggal_Transaksi=varTanggal,Status=varStatus, Nominal=varNominal)
    return render(request, 'transaksi.html') #django pake render


def saldo(request):
    transaksi_kredit= models.transaksi.objects.filter(Status= "Kredit")
    transaksi_debit= models.transaksi.objects.filter(Status= "Debit")
    array_kredit = [d.Nominal for d in transaksi_kredit]
    total_kredit = sum(array_kredit)
    array_debit = [d.Nominal for d in transaksi_debit]
    total_debit = sum(array_debit)
    saldo = total_debit-total_kredit
    return render(request, 'saldo.html',{
        "dataKredit": transaksi_kredit,
        "total_kredit": total_kredit,
        "dataDebit": transaksi_debit,
        "total_debit": total_debit,
        "saldo": saldo
    })

def laporan(request):
    next_week = date.today() + timedelta(days = 7)
    data = models.transaksi.objects.filter(Tanggal_Transaksi__gte=date.today(), Tanggal_Transaksi__lte=next_week)
    
    
    return render(request ,'laporan.html',{
        'data': data
    })

def bulanan(request):
    data = models.transaksi.objects.all()
    return render(request, 'bulanan.html',{
        "data": data
    })
