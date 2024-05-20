
from logistics.models import Shipment
from django.template.loader import render_to_string
import pdfkit,os
from django.conf import settings
from django.urls import reverse


def generateInvoice(shipment,return_pdf=False):
    """
    invoice generator function that generates an invoice,stores it
    and returns the pdf,accepts shipment
    """
    from logistics.models import Invoice
    if not return_pdf : 
        output_path = "{}/{}.pdf".format(os.path.join(settings.BASE_DIR,'media/invoices'),shipment.tracking_number)
    else : output_path = False
    #create output path
    #x = open(output_path,'w')
    #x.close()
    template_name = "invoice.html"
    if not isinstance(shipment,Shipment) :
        raise ValueError("shipment must be and instance of the shopment models class")
    
    template = render_to_string(template_name,context={"shipment" : shipment})
 
    wk_path = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=wk_path)

    #create invoice 
    Invoice.objects.get_or_create(shipment = shipment)
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
    
