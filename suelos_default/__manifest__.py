# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2021  jeo Software  (http://www.jeo-soft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------------
{
    "name": "suelos13",
    "version": "13.0.1.0.0",
    "category": "Tools",
    "summary": "Proyecto Suelos",
    "author": "jeo Software",
    "depends": [
        "standard_depends_ce",
        "sale",
        "sale_management",
        "purchase",
        "stock",
        "product_in_box",
        "base_user_role",
        "custom_rights",
        "price_security",
        "sale_discount_limit",
        "price_security_fix",
        "pricelist_on_invoice",
        # Contabilidad
        "account",
        "account_ux",
        "l10n_ar_export_arba",
        "l10n_ar_export_sicore",
    ],
    "data": [],
    "test": [],
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": [],
    "env-ver": "2",
    "odoo-license": "CE",
    "port": "8069",
    "prod_server": "ec2-user@suelos13",
    "config": [
        "max_cron_threads = 1",
    ],
    "git-repos": [
        "git@github.com:jobiols/cl-suelos.git",
        "git@github.com:jobiols/odoo-addons.git",
        "git@github.com:jobiols/odoo-jeo-ce.git",
        # Odoomates
        # ==========================================================================================
        "https://github.com/odoomates/odooapps odoomates-odooapps",
        # Gabriela Rivero
        # ==========================================================================================
        "https://github.com/regaby/odoo-custom regaby-odoo-custom",
        # todos juntos
        # ==========================================================================================
        "https://github.com/OCA/account-financial-reporting oca-account-financial-reporting",  # noqa
        "https://github.com/OCA/account-financial-tools oca-account-financial-tools",
        "https://github.com/OCA/account-invoicing oca-account-invoicing",
        "https://github.com/OCA/account-payment oca-account-payment",
        "https://github.com/OCA/reporting-engine oca-reporting-engine",
        "https://github.com/OCA/sale-workflow oca-sale-workflow",
        "https://github.com/OCA/server-backend oca-server-backend",
        "https://github.com/OCA/server-tools oca-server-tools",
        "https://github.com/OCA/server-ux oca-server-ux",
        "https://github.com/OCA/stock-logistics-workflow oca-stock-logistics-workflow",
        "https://github.com/OCA/web oca-web",
        "https://github.com/ingadhoc/account-financial-tools ingadhoc-account-financial-tools",  # noqa
        "https://github.com/ingadhoc/account-payment ingadhoc-account-payment",
        "https://github.com/ingadhoc/aeroo_reports ingadhoc-aeroo_reports",
        "https://github.com/ingadhoc/argentina-reporting ingadhoc-argentina-reporting",
        "https://github.com/ingadhoc/argentina-sale ingadhoc-argentina-sale",
        "https://github.com/ingadhoc/miscellaneous ingadhoc-miscellaneous",
        "https://github.com/quilsoft-org/odoo-argentina ingadhoc-odoo-argentina",
        "https://github.com/ingadhoc/odoo-argentina-ce ingadhoc-odoo-argentina-ce",
        "https://github.com/ingadhoc/product ingadhoc-product",
        "https://github.com/ingadhoc/reporting-engine ingadhoc-reporting-engine",
        "https://github.com/ingadhoc/sale ingadhoc-sale",
        "https://github.com/ingadhoc/stock ingadhoc-stock",
    ],
    "docker-images": [
        "odoo jobiols/odoo-jeo:13.0",
        "postgres postgres:10.1-alpine",
    ],
}
