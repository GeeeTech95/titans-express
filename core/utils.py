
from logistics.models import Shipment
import pdfkit,os
from django.conf import settings
from django.urls import reverse


def generateInvoice(shipment,return_pdf=False,request = False):
    """
    invoice generator function that generates an invoice,stores it
    and returns the pdf,accepts shipment
    """
    from logistics.models import Invoice
    if not return_pdf : 
        output_path = "{}/{}.pdf".format(os.path.join(settings.BASE_DIR,'media/invoices'),shipment.tracking_number)
    else : output_path = False

    if not isinstance(shipment,Shipment) :
        raise ValueError("shipment must be and instance of the shopment models class")
    
    #"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
    if settings.DEBUG :
        wk_path = os.path.join(settings.BASE_DIR,'core','wkhtmltopdf','bin','wkhtmltopdf.exe')
    
    else :
        wk_path = "/usr/bin/wkhtmltopdf"



    config = pdfkit.configuration(wkhtmltopdf=wk_path)

    #create invoice 
    Invoice.objects.get_or_create(shipment = shipment)
    if request : 
        invoice_url = request.build_absolute_uri(reverse("view-shipment-invoice",args=[shipment.tracking_number]))
    else :
       invoice_url = "{}{}".format(settings.SITE_URL,reverse("view-shipment-invoice",args=[shipment.tracking_number]))

    #return bool or pdf
    is_generated_or_pdf = pdfkit.from_url(
            invoice_url,
            output_path=output_path,
            configuration=config,
            options={ 
            'page-height' : "220mm",
            "page-width" : "230mm",
            "zoom" : 1.7
             })   
    
    return is_generated_or_pdf
    
