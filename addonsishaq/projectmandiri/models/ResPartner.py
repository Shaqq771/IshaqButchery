from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    is_buyer = fields.Boolean(string='Is Buyer')
    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')