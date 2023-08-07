from django.urls import path

from mpesa.api.views import LNMCallbackUrlAPIView
#from mpesa.api.views import LNMCallbackUrlAPIView,NetPostAPIView

urlpatterns = [
    path('lnm/', LNMCallbackUrlAPIView.as_view(), name="lnm-callbackurl"),
    #path('netview/', NetPostAPIView.as_view(), name="netview-post"),

]
