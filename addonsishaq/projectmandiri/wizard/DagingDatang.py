from odoo import api, fields, models

class DagingDatang(models.TransientModel):
    _name = 'projectmandiri.dagingdatang'

    daging_id = fields.Many2one(comodel_name='projectmandiri.daging', string='Nama Daging', required=True)
    jumlah = fields.Integer(string='Jumlah', required=False)

    def button_daging_datang(self):
        for rec in self:
            self.env['projectmandiri.daging'].search([('id', '=', rec.daging_id.id)]).write({'stok': rec.daging_id.stok +  rec.jumlah})