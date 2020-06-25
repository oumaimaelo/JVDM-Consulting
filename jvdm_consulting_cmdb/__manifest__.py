# -*- coding: utf-8 -*-
{
    'name': "JVDM Consulting CMDB",

    'summary': """
        The Configuration Database Management""",

    'description': """
        The configuration management database (CMDB) is a repository that acts as a data warehouse for information technology (IT) organizations. Its contents are intended to hold a collection of IT assets that are commonly referred to as configuration items (CI), as well as descriptive relationships between such assets. When populated, the repository becomes a means of understanding how critical assets such as information systems are composed, what their upstream sources or dependencies are, and what their downstream targets are.

        La Configuration Management DataBase (abrégé CMDB), ou base de données de gestion de configuration, est une base de données unifiant les composants d'un système informatique. Elle permet de comprendre l'organisation entre ceux-ci et de modifier leur configuration. La CMDB est un composant fondamental d'une architecture ITIL.
    """,

    'author': "JVDM Consulting",
    'website': "https://www.jvdm.consulting/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': '',
    'version': '1.0',
    'sequence': 24,

    # any module necessary for this one to work correctly
    'depends': ['base',
                'project'],

    'qweb': ['static/src/xml/cmdb.xml'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/project_views.xml',
        'views/landscape_views.xml',
        'views/server_views.xml',
        'views/system_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
