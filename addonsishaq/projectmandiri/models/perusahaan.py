from odoo import api, fields, models


class Perusahaan(models.Model):
    _name = 'projectmandiri.perusahaan'
    _description = 'New Description'

    name = fields.Char(string='Nama Perushaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telepon')
    daging_id = fields.Many2many(comodel_name='projectmandiri.daging', string='Daging')