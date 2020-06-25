# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Res_Users(models.Model):
    _inherit = 'res.users'

    landscp_read_access = fields.Boolean(string="Read Access", default=True)
    landscp_write_access = fields.Boolean(string="Write Access", default=True)
