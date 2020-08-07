# -*- coding: utf-8 -*-

from odoo import models, fields, api


class sale_order_template(models.Model):
    _inherit = 'sale.order.template'

    x_terms_and_conditions_approval = fields.Text(string="Terms and Conditions Approval",)
    x_terms_and_conditions = fields.Text(string="Terms and Conditions")
