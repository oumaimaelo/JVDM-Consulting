from odoo.http import request
from odoo import fields, http
from odoo.addons.website_sale.controllers.main import WebsiteSale
import logging
_logger = logging.getLogger(__name__)

class WebsiteSale(WebsiteSale):

    @http.route(["/set/check/status"], type='json', auth="public", methods=['POST'], website=True)
    def payment_add_wallet(self, state, **kw):
        request.session['is_allowed'] = state

    @http.route(['/shop/payment/transaction/',
        '/shop/payment/transaction/<int:so_id>',
        '/shop/payment/transaction/<int:so_id>/<string:access_token>'], type='json', auth="public", website=True)
    def payment_transaction(self, acquirer_id, save_token=False, so_id=None, access_token=None, token=None, **kwargs):
        website = request.website
        if not request.session.get('is_allowed', False) and website.show_terms_conditions and website.show_checkbox_on_checkout:
            return False
        res = super(WebsiteSale, self).payment_transaction(acquirer_id, save_token, so_id, access_token, token, **kwargs)
        return res

    @http.route()
    def payment_confirmation(self, **post):
        res = super(WebsiteSale,  self).payment_confirmation(**post)
        request.session['is_allowed'] = False
        return res
