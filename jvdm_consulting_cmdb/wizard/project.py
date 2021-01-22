from odoo import api, fields, models
from odoo.osv import expression

class ProjectTaskStatus(models.TransientModel):
    _name = 'project.task.status'

    def _domain_product_id(self):
        task_ids = self.env.context.get('active_ids')
        if task_ids:
            tasks = self.env['project.task'].browse(task_ids)
            projects = tasks.mapped('project_id.id')
            domain = expression.AND([[('project_ids', '=', project)] for project in projects])
            return domain
        else:
            return [('project_ids', '=', False)]

    stage_id = fields.Many2one('project.task.type', string='Stage', domain=_domain_product_id, copy=False)

    def confirm(self):
        task_ids = self.env.context.get('active_ids')
        if task_ids:
            tasks = self.env['project.task'].browse(task_ids)
            tasks.write({'stage_id': self.stage_id.id})