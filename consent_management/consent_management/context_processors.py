from consent_management.models import GlobalInfo

def global_info(request):
    if GlobalInfo.objects.exists():
        return {
            "global_info": GlobalInfo.objects.all()[0]
        }
    else:
        return {}
