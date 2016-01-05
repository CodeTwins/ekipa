from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class EkipaApp(CMSApp):
    name = _('Ekipa')
    urls = ['ekipa.urls', ]
    app_name = 'ekipa'


apphook_pool.register(EkipaApp)
