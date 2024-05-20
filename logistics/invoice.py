from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View,generic
from core.utils import generateInvoice
from .models import Shipment, Invoice



class InvoiceListView(View):
    def get(self, *args, **kwargs):
        invoices = Invoice.objects.all()
        context = {
            "invoices":invoices,
        }

        return render(self.request, 'invoice/invoice-list.html', context)
    
    def post(self, request):        
        # import pdb;pdb.set_trace()
        invoice_ids = request.POST.getlist("invoice_id")
        invoice_ids = list(map(int, invoice_ids))

        update_status_for_invoices = int(request.POST['status'])
        invoices = Invoice.objects.filter(id__in=invoice_ids)
        # import pdb;pdb.set_trace()
        if update_status_for_invoices == 0:
            invoices.update(status=False)
        else:
            invoices.update(status=True)

        return redirect('invoice:invoice-list')




class CreateInvoiceView(generic.View) :

    template_name = "create-invoice.html"
    model = Shipment

    def get(self,request,*args,**kwargs) :
        return render(request,self.template_name,{})
    
    def post(self,request,*args,**kwargs) :
        shipment_tracking_number = request.POST.get("shipment_tracking_number")
        if not  shipment_tracking_number :
            return HttpResponse("shipment with that tracking number no longer exists")       
        shipment = get_object_or_404(self.model,tracking_number = shipment_tracking_number)
        invoice = generateInvoice(shipment,True)
        response = HttpResponse(invoice ,content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

        return response






class InvoiceDetailView(generic.DetailView) :
    template_name = 'invoice.html'
    model = Shipment

    def get_object(self) :
        return get_object_or_404(self.model,tracking_number = self.kwargs["shipment_tracking_number"]) 






