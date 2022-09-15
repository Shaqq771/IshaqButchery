from odoo import api, fields, models


class Object(models.Model):
    _name = 'projectmandiri.object'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime(string='Tanggal Lahir')

class Breeder(models.Model):
    _name = 'projectmandiri.breeder'
    _inherit = 'projectmandiri.object'
    _description = 'New Description'

    id_breeder = fields.Char(string='ID breeder')
    
 