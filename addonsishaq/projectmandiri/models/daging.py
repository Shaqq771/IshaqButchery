from odoo import api, fields, models


class Daging(models.Model):
    _name = 'projectmandiri.daging'
    _description = 'New Description'

    name = fields.Char(string='Name')
    harga_daging = fields.Integer(string='Harga Daging', required=True)
    negaraasal_id = fields.Many2one(comodel_name='projectmandiri.negaraasal', string='Negara Asal', ondelete='cascade')
    perusahaan_id = fields.Many2many(comodel_name='projectmandiri.perusahaan', string='Perusahaan')
    stok = fields.Integer(string='Stok')
    
    
