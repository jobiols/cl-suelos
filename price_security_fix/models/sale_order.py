from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def check_priority(self):
        pass
