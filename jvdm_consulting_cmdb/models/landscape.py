# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectLandscape(models.Model):
    _name = "project.landscape"
    name = fields.Char(size=128)
    description = fields.Char()
    version = fields.Char()
    systeme_ids = fields.One2many('systeme', 'landscape_id', string='Systèmes')
    project_ids = fields.One2many('project.project', 'landscape_id', 'project')
    active = fields.Boolean()