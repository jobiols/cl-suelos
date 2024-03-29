# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2022  jeo Software  (http://www.jeo-soft.com.ar)
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
    "name": "Pricelist on Invoice",
    "version": "13.0.1.0.0",
    "category": "Tools",
    "summary": "Agrega la tarifa en la factura",
    "author": "jeo Software",
    "depends": [
        "sale",
    ],
    "data": [
        "views/account_move_view.xml",
        "views/report_invoice.xml",
    ],
    "test": [],
    "installable": True,
    "application": False,
}
