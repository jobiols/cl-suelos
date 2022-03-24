from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    pricelist = fields.Char(
        "Tarifa",
        readonly=True,
    )
