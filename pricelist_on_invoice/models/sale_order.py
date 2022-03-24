from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_invoice(self):
        """Sobreescribimos este metodo para pasarle a la factura la lista de precios"""

        self.ensure_one()
        ret = super()._prepare_invoice()
        ret["pricelist_id"] = self.pricelist_id.id

        return ret
