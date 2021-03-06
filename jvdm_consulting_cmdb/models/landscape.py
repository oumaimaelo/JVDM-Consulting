# -*- coding: utf-8 -*-
from odoo.exceptions import UserError
from odoo import models, fields, api, _


class ProjectLandscape(models.Model):
    _name = "project.landscape"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(size=128)
    description = fields.Char()
    version = fields.Char()
    systeme_ids = fields.One2many('systeme', 'landscape_id', string='Systèmes')
    project_ids = fields.One2many('project.project', 'landscape_id', 'project')
    active = fields.Boolean(default=True)
    # user_ids = fields.Many2many(comodel_name="res.users", relation="landscape_user_rel",
    #                             column1="landscape_id", column2="user_id", string="Users")
    cmdb_user_ids = fields.Many2many(comodel_name="cmdb.users", relation="landscape_user_rel1",
                                     column1="landscape_id", column2="cmdb_user_id", string="Users")

    def write(self, vals):
        group_cmdb_manager_id = self.env['ir.model.data'].xmlid_to_res_id('jvdm_consulting_cmdb.group_cmdb_manager')
        manager_ids = self.env['res.groups'].sudo().browse(group_cmdb_manager_id).users.ids
        user_id = self.env.user.id
        for record in self:
            cmdb_user_id = record.cmdb_user_ids.filtered(lambda u: u.user_id.id == user_id)
            if (user_id not in manager_ids) and not cmdb_user_id.landscp_write_access:
                raise UserError(
                    _('You are not allowed to write on the current record, only managers can do.'))
        result = super(ProjectLandscape, self).write(vals)
        # if 'user_ids' in vals:
        if 'cmdb_user_ids' in vals:
            # group_cmdb_manager_id = self.env['ir.model.data'].xmlid_to_res_id('jvdm_consulting_cmdb.group_cmdb_manager')
            # manager_ids = self.env['res.groups'].sudo().browse(group_cmdb_manager_id).users.partner_id.ids
            # usr_id = self.env.user.partner_id.id
            if user_id not in manager_ids:
                raise UserError(
                    _('You are not allowed to add or remove users from the current landscape, only managers can do.'))
            else:
                unsubscribed_ids = self.message_partner_ids.ids
                if self.env.user.partner_id.id in unsubscribed_ids:
                    unsubscribed_ids.remove(self.env.user.partner_id.id)
                self.message_unsubscribe(partner_ids=unsubscribed_ids)
                self.message_subscribe(
                    partner_ids=[cmdb_user.user_id.partner_id.id for cmdb_user in self.cmdb_user_ids
                                 if cmdb_user.landscp_read_access or cmdb_user.landscp_write_access] + manager_ids)
                group_cmdb_user_id = self.env['ir.model.data'].xmlid_to_res_id('jvdm_consulting_cmdb.group_cmdb_user')
                group_object = self.env['res.groups'].sudo().browse(group_cmdb_user_id) \
                    .write({'users': [(4, cmdb_user.user_id.id) for cmdb_user in self.cmdb_user_ids
                                      if cmdb_user.landscp_read_access and cmdb_user.landscp_write_access]})
        return result
