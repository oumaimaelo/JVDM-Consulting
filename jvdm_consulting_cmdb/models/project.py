# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = "project.project"
    landscape_id = fields.Many2one('project.landscape', 'Landscape')

