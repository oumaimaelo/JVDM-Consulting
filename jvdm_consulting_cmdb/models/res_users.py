# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class Res_Users(models.Model):
#     _inherit = 'res.users'
#
#     landscp_read_access = fields.Boolean(string="Read Access", default=True)
#     landscp_write_access = fields.Boolean(string="Write Access", default=True)

class CMDBUsers(models.Model):
    _name = 'cmdb.users'

    @api.onchange('landscp_write_access')
    def _onchange_landscp_write_access(self):
        if self.landscp_write_access:
            self.landscp_read_access = True

    @api.onchange('landscp_read_access')
    def _onchange_landscp_read_access(self):
        if not self.landscp_read_access:
            self.landscp_write_access = False

    user_id = fields.Many2one(comodel_name="res.users", string="User")
    landscp_read_access = fields.Boolean(string="Read Access", default=True)
    landscp_write_access = fields.Boolean(string="Write Access", default=True)
