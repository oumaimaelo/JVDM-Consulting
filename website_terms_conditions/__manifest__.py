# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################
{
  "name"                 :  "Website Terms & Conditions",
  "summary"              :  """The module allows you to show terms and conditions section on the Odoo website. The section can be used to put in the store policies, rules, shipping policies, etc.""",
  "category"             :  "Website",
  "version"              :  "2.0.6",
  "author"               :  "Webkul Software Pvt. Ltd.",
  "website"              :  "https://store.webkul.com/Odoo-Website-Terms-And-Conditions.html",
  "description"          :  """Odoo Website Terms And Conditions
Odoo website Terms & Conditions
Website terms odoo
Store policies
Show shipping policies
Website policies
Odoo Display terms and conditions
Add website policies on webpage
Store policies webpage
Terms & conditions webpage
website agreement""",
  "live_test_url"        :  "http://odoodemo.webkul.com/?module=website_terms_conditions&custom_url=/shop/payment",
  "depends"              :  [
                             'website_sale',
                             'website_webkul_addons',
                            ],
  "data"                 :  [
                             'view/templates.xml',
                             'view/res_config_view.xml',
                             'view/webkul_addons_config_inherit_view.xml',
                            ],
  "demo"                 :  ['data/demo.xml'],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  20,
  "currency"             :  "USD",
  "pre_init_hook"        :  "pre_init_check",
}