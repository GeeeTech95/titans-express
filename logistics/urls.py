from django.urls import path
from . import views,invoice



urlpatterns = [

   path("shipment/detail/<str:tracking_number>/",views.ShipmentDetail.as_view(),name="shipment-detail"),
   path("shipment/track-shipment/",views.TrackShipment.as_view(),name="track-shipment"),
   
   
   #Invoices
   path("invoice/generate-invoice/",invoice.CreateInvoiceView.as_view(),name="generate-invoice"),
   path("invoices/<int:shipment_tracking_number>/view-invoice/",invoice.InvoiceDetailView.as_view(),name= 'view-shipment-invoice')

]