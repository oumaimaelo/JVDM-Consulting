# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectLandscape(models.Model):
    _name = "project.landscape"
    _inherit = ['mail.thread']

    name = fields.Char(size=128)
    description = fields.Char()
    version = fields.Char()
    systeme_ids = fields.One2many('systeme', 'landscape_id', string='Systèmes')
    project_ids = fields.One2many('project.project', 'landscape_id', 'project')
    active = fields.Boolean(default=True)
    user_ids = fields.Many2many(comodel_name="res.users", relation="landscape_user_rel",
                                compute='_get_users', inverse='_set_users',
                                column1="landscape_id", column2="user_id", string="Users")

    def _get_users(self):
        group_cmdb_user_id = self.env['ir.model.data'].xmlid_to_res_id('jvdm_consulting_cmdb.group_cmdb_user')
        users_ids = []
        sql_query = """select uid from res_groups_users_rel where gid = %s"""
        params = (group_cmdb_user_id,)
        self.env.cr.execute(sql_query, params)
        results = self.env.cr.fetchall()
        for users_id in results:
            users_ids.append(users_id[0])

        self.user_ids = self.env['res.users'].browse(users_ids)
        return users_ids

    def _set_users(self):
        group_cmdb_user_id = self.env['ir.model.data'].xmlid_to_res_id('jvdm_consulting_cmdb.group_cmdb_user')
        group_object = self.env['res.groups'].browse(group_cmdb_user_id) \
            .write({'users': [(4, user.id) for user in self.user_ids
                              if user.landscape_read_access and user.landscape_write_access]})
