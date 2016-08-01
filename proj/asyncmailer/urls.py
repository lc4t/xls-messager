"""URLs for the asyncmailer app."""
from compat import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index$', views.index),
    url(r'^get_variations$', views.get_variations),
    url(r'^get_json$', views.get_json),
    url(r'^retrieve$', views.retrieve),
    url(r'^presend$', views.presend),
    url(r'^send_by_email$', views.send_by_email),
    # append your urls here
]
