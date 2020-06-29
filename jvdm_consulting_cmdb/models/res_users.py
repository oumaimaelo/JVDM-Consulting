# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class Res_Users(models.Model):
#     _inherit = 'res.users'
#
#     landscp_read_access = fields.Boolean(string="Read Access", default=True)
#     landscp_write_access = fields.Boolean(string="Write Access", default=True)

class CMDBUsers(models.Model):
    _name = 'cmdb.users'

    user_id = fields.Many2one(comodel_name="res.users", string="User")
    landscp_read_access = fields.Boolean(string="Read Access", default=True)
    landscp_write_access = fields.Boolean(string="Write Access", default=True)
