# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Systeme(models.Model):
    _name = "systeme"
    _inherit = ['mail.thread']

    name = fields.Char(size=128)
    landscape_id = fields.Many2one('project.landscape', 'Landscape')
    landscape_desc = fields.Char('Description', related='landscape_id.description', store=True)
    ip = fields.Char('URL', size=128)
    server_id = fields.Many2one('jvdm.server', 'Server', size=128)
    user = fields.Char('Login', size=128)
    password = fields.Char('Password', size=128)
    master_password = fields.Char('Master Password', size=128)
    db_user = fields.Char('Login', size=128)
    db_password = fields.Char('Password', size=128)
    active = fields.Boolean(default=True)

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        print('domain:', domain)
        print('fields:', fields)
        print('groupby:', groupby)
        res = super(Systeme, self).read_group(domain, fields, groupby, offset=offset, limit=limit, orderby=orderby,
                                            lazy=lazy)
        if groupby and groupby[0] == "landscape_id":
            landscapes = self.env['project.landscape'].search([])
            if landscapes:
                result = [{
                            '__domain': domain + [('landscape_id', '=', landscape.id)],
                            'landscape_desc': landscape.description,
                            'landscape_id': (landscape.id, landscape.name),
                            'landscape_id_count': self.search_count(domain + [('landscape_id', '=', landscape.id)])
                          } for landscape in landscapes if self.search_count(domain + [('landscape_id', '=', landscape.id)]) != 0]
                print('result:', result)
                return result
        print('result:', res)
        return res
    # @api.onchange('landscape_id')
    # def description_of_landscape(self):
    #     print("****")
    #     self.landscape_desc = self.landscape_id.description

    def run_system(self):
        pass

class Server(models.Model):
    _name = "jvdm.server"
    _inherit = ['mail.thread']

    name = fields.Char(size=128)
    port = fields.Char('Port SSH', size=128)
    ip = fields.Char('IP', size=128)
    mac = fields.Char('MAC', size=128)
    user = fields.Char('Login', size=128)
    password = fields.Char('Password', size=128)
    systeme_ids = fields.One2many('systeme', 'server_id')
    active = fields.Boolean(default=True)
    note = fields.Text('Notes complémentaires')
    private_key = fields.Binary(string='Private Key')
    # private_key2 = fields.Many2one('ir.attachment', string='Private Key')

    def run_server(self):
        from sys import platform
        import os, subprocess, base64
        for server in self:
            name = server.env['res.users'].browse(server._uid).name
            if platform == "linux" or platform == "linux2":
                user = server.user
                ip = server.ip
                port = server.port
                password = server.password
                if all(x.isalpha() or x.isspace() for x in name) and user and ip and all(' ' not in x for x in [user, ip]) and (port is False or port and port.isdigit() or port.isspace()):
                    port = ' -p ' + server.port if port and port.isdigit() else ''
                    if server.private_key:
                        file_location = os.path.join(os.path.expanduser('~'), '{}.pem'.format(server.name or "False"))
                        with open(file_location, "w") as f:
                            f.write(base64.b64decode(server.private_key).decode('utf8'))
                            f.close()
                        os.chmod(file_location, 0o600)
                        key = ' -i ' + file_location
                    else:
                        key = ''
                    message = server.wrap_with_color('Welcome', 'yel') + server.wrap_with_color(name+",", 'blu') + (server.wrap_with_color(
                        'The Server Password is:', 'yel') + server.wrap_with_color(password, 'red') if password and ' ' not in password and not key else '')
                    command = ("sshpass -p {password} ".format(password=password) if password and ' ' not in password and not key else '') + \
                        "ssh -t {login}@{ip}{port}{key} 'echo -e \"{message}\"; bash -l'".format(
                            login=user,
                            ip=ip,
                            port=port,
                            key=key,
                            message=message)
                    subprocess.run(["gnome-terminal", "-e", command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    # if server.private_key:
                    #     os.remove(file_location)
                else:
                    raise ValidationError('Vérifier si tous vos entrées sont présents et correctes')
            else:
                raise ValidationError('Hello {}, vous utilisez une plate-forme {}, cette fonctionnalité est valable uniquement pour les systèmes linux !'.format(name, platform))

    @staticmethod
    def wrap_with_color(string, color):
        colors = {
            'red': '\e[1;31m',
            'grn': '\e[1;32m',
            'yel': '\e[1;33m',
            'blu': '\e[1;34m',
            'mag': '\e[1;35m',
            'cyn': '\e[1;36m',
        }
        end = '\e[0m'

        return colors[color]+string+end+' '