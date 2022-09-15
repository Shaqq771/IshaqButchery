from odoo import api, fields, models


class NegaraAsal(models.Model):
    _name = 'projectmandiri.negaraasal'
    _description = 'New Description'

    name = fields.Selection([('united states', 'United States'), ('japan', 'Japan'), ('brazil', 'Brazil'), ('australia', 'Australia')], string='Negara Asal')
    kode_negara = fields.Char(string='Kode Negara Asal Daging')

    @api.onchange('name')
    def _onchange_negara_asal(self):
        if self.name == 'united states':
            self.kode_negara = 'US'
        elif self.name == 'japan':
            self.kode_negara = 'JPN'
        elif self.name == 'brazil':
            self.kode_negara = 'BRA'
        elif self.name == 'australia':
            self.kode_negara = 'AUS'
    kode_daging = fields.Char(string='Kode Daging')
    daging_ids = fields.One2many(comodel_name='projectmandiri.daging', inverse_name='negaraasal_id', string='Daftar Daging')
    jumlah = fields.Char(compute='_compute_jumlah', string='Jumlah')

    @api.depends('daging_ids')
    def _compute_jumlah(self):
        for record in self:
            a = self.env['projectmandiri.daging'].search([('negaraasal_id', '=', record.id)]).mapped('name')
            b = len(a)
            record.jumlah = b
            record.daftar = a
    
    daftar = fields.Char(string='Daftar isi')
    
    
    
