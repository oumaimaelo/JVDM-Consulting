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


# class ResUsers(models.Model):
#     _inherit = 'res.users'
#
#     last_timesheet_date = fields.Boolean("Keep last timesheet date")


# class AccountAnalyticLine(models.Model):
#     _inherit = 'account.analytic.line'
#
#     def _default_date(self):
#         if self.env.user.last_timesheet_date:
#             record = self.env['account.analytic.line'].search([('user_id', '=', self._uid)], limit=1)
#             if record:
#                 return record.date
#         return fields.Date.context_today(self)
#
#     date = fields.Date('Date', required=True, index=True, default=_default_date)