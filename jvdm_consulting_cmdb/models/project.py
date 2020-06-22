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

class ResUsers(models.Model):
    _inherit = 'res.users'

    landscape_read_access = fields.Boolean(string="Read Access", default=True)
    landscape_write_access = fields.Boolean(string="Write Access", default=True)

    def _get_access(self):
        group_cmdb_user_id = self.env['ir.model.data'].xmlid_to_res_id('jvdm_consulting_cmdb.group_cmdb_user')
        cmdb_user_ids = self.env['project.landscape']._get_users()
        model_id = self.env.ref('jvdm_consulting_cmdb.model_project_landscape')
        for rec in self:
            if rec.id in cmdb_user_ids:
                sql_query = """select perm_read, perm_write from ir_model_access where model_id = %s and group_id = %s"""
                params = (model_id.id, group_cmdb_user_id,)
                self.env.cr.execute(sql_query, params)
                results = self.env.cr.fetchall()
                rec.landscape_read_access = results[0][0]
                rec.landscape_write_access = results[0][1]

