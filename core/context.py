from django.core.exceptions import ObjectDoesNotExist
import datetime

def core(request) :
    prepend = "https://" if request.is_secure() else "http://"
    host = request.get_host()
    #reg_link  = prepend + host + request.user.user_admin.reg_link
    ctx = {}

    ctx['liquidity'] = 53199180
    ctx['site_name_verbose'] = "Titan Express"
    ctx['site_name'] = "Titan Express"
    ctx['site_name_full'] = "Titan Express"
    ctx['support_email'] = "support@titansexpress.com"
    ctx['site_email'] = "support@titansexpress.com"
    ctx['site_phone'] = "+16305279499"
    ctx['site_whatsapp_no'] = "+16305279499"
    ctx['site_address'] = "167-169 Great Portland Street, London"

    epoch_time = datetime.datetime(1970, 1, 1)
    date_now = datetime.datetime.now()
    delta = (date_now - epoch_time)
    users_served = int(delta.total_seconds()  / 102003)
    packages_delivered = int(delta.total_seconds()  / 23003)

    ctx['package_delivered'] = packages_delivered if packages_delivered < 121000 else 121000
    ctx['users_served'] = users_served if users_served < 35624 else  35624


  
    
    return ctx  


    
        