# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
from odoo import api, fields, models
from odoo.tools.translate import _
from odoo.exceptions import Warning

class WebsiteTermsSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _name='website.config.terms.settings'

    label = fields.Char(string="Label", related="website_id.label", readonly=False)
    title = fields.Char(string="Title", related="website_id.title", readonly=False)
    content = fields.Html(string="Content", related="website_id.content", readonly=False)
    display_option = fields.Selection([('pop_up','Pop Up Window'),('same_page','Same Page')], string='How To display Terms & Conditions', related="website_id.display_option", readonly=False)
    show_terms_conditions = fields.Boolean("Show Terms And Conditions on Checkout", help="Enable this feature to show terms and conditions on Website.", related="website_id.show_terms_conditions", readonly=False)
    show_checkbox_on_checkout = fields.Boolean("Show Checkbox On Checkout", help="Show checkbox on checkout, in this case the checkobox will be dispalyed on website and the users will be retricted from checkout if the checkbox is unchecked.", related="website_id.show_checkbox_on_checkout", readonly=False)
