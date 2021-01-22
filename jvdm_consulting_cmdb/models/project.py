# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = "project.project"
    landscape_id = fields.Many2one('project.landscape', 'Landscape')


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.model
    def create(self, vals):
        if 'project_id' in vals:
            project_id = self.env['project.project'].search([('id', '=', vals['project_id'])])
            if project_id:
                vals['user_id'] = project_id.user_id.id
        result = super(ProjectTask, self).create(vals)
        return result

    # def change_status(self):
    #     for record in self:


class ResPartner(models.Model):
    _inherit = 'res.partner'

    property_account_payable_id = fields.Many2one('account.account', company_dependent=True,
                                                  string="Account Payable",
                                                  domain="[('internal_type', '=', 'payable'), ('deprecated', '=', False)]",
                                                  help="This account will be used instead of the default one as the payable account for the current partner",
                                                  required=False)
    property_account_receivable_id = fields.Many2one('account.account', company_dependent=True,
                                                     string="Account Receivable",
                                                     domain="[('internal_type', '=', 'receivable'), ('deprecated', '=', False)]",
                                                     help="This account will be used instead of the default one as the receivable account for the current partner",
                                                     required=False)

