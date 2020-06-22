# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = "project.project"
    landscape_id = fields.Many2one('project.landscape', 'Landscape')


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.model
    def create(self, vals):
        result = super(ProjectTask, self).create(vals)
        if not result.user_id:
            result.user_id = result.project_id.user_id.id
        return result


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
