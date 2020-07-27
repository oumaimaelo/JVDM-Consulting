# -*- coding: utf-8 -*-
#################################################################################
#
#    Copyright (c) 2015-Present Webkul Software Pvt. Ltd. (<https://webkul.com/>)
#
#################################################################################
from odoo import api, fields, models
import logging
from odoo.http import request
_logger = logging.getLogger(__name__)

class Website(models.Model):
	_inherit = 'website'

	label = fields.Char(string="Label",default='Terms and Conditions')
	title = fields.Char(string="Title",default='I Agree with the Terms and Conditions')
	content = fields.Html(string="Content",default='The content of the pages of this website is for your general information and use only. It is subject to change without notice. All trade marks reproduced in this website which are not the property of, or licensed to, the operator are acknowledged on the website.- This website contains material which is owned by or licensed to us. This material includes, but is not limited to, the design, layout, look, appearance and graphics. Reproduction is prohibited other than in accordance with the copyright notice, which forms part of these terms and conditions.')
	display_option = fields.Selection([('pop_up','Pop Up Window'),('same_page','Same Page')], string='How To display Terms & Conditions',default='pop_up')
	show_terms_conditions = fields.Boolean("Show Terms And Conditions on Checkout", help="Enable this feature to show terms and conditions on Website.",default=True)
	show_checkbox_on_checkout = fields.Boolean("Show Checkbox On Checkout", help="Show checkbox on checkout, in this case the checkobox will be dispalyed on website and the users will be retricted from checkout if the checkbox is unchecked.",default=True)

	@api.model
	def get_info(self):
		content = self.content
		label = self.label
		title = self.title
		display_option = self.display_option
		show_terms_conditions = self.show_terms_conditions
		show_checkbox_on_checkout = self.show_checkbox_on_checkout
		return {
			'content': content,
			'label': label,
			'title': title,
			'display_option': True if display_option == 'pop_up' else False,
			'show_terms_conditions': show_terms_conditions,
			'show_checkbox_on_checkout': show_checkbox_on_checkout,
		}

	# For demo purpose only
	@api.model
	def create_order(self):
		website = self.env['website'].get_current_website()
		request.website = website
		sale_order = website.sale_get_order(force_create=True)
		sale_order._cart_update(
			product_id=self.env.ref('product.product_product_3').id,
			add_qty=0,
			set_qty=1,
			product_custom_attribute_values=None,
			no_variant_attribute_values=None
		)
		# Flow for shop/confirm_order
		sale_order.onchange_partner_shipping_id()
		sale_order.order_line._compute_tax_id()
		request.session['sale_last_order_id'] = sale_order.id
		request.website.sale_get_order(update_pricelist=True)
		return True
