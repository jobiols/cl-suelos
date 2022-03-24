from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    pricelist_id = fields.Many2one(
        'product.pricelist',
        string="Tarifa",
        readonly=True,
    )
