from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Penjualan(models.Model):
    _name = 'projectmandiri.penjualan'
    _description = 'Penjualan'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(
        string='Tanggal Transaksi',
        default=fields.Datetime.now())
    total_bayar = fields.Integer(
        string='Total Pembayaran',
        compute='_compute_totalbayar')
    detailpenjualan_ids = fields.One2many(
        comodel_name='projectmandiri.detailpenjualan',
        inverse_name='penjualan_id',
        string='Detail Penjualan')

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for line in self:
            result = sum(self.env['projectmandiri.detailpenjualan'].search(
                [('penjualan_id', '=', line.id)]).mapped('subtotal'))
            line.total_bayar = result


class DetailPenjualan(models.Model):
    _name = 'projectmandiri.detailpenjualan'
    _description = 'Detail'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(
        comodel_name='projectmandiri.penjualan',
        string='Detail Penjualan')
    daging_id = fields.Many2one(
        comodel_name='projectmandiri.daging',
        string='List Daging')
    harga_perkilo = fields.Integer(
        string='Harga Perkilo',
        onchange='_onchange_daging_id')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('harga_perkilo', 'qty')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.qty * line.harga_perkilo

    @api.onchange('daging_id')
    def _onchange_daging_id(self):
        if self.daging_id.harga_daging:
            self.harga_perkilo = self.daging_id.harga_daging
    
    @api.model
    def create(self, vals):
        line = super(DetailPenjualan, self).create(vals)
        if line.qty:
            self.env['projectmandiri.daging'].search(
                [('id', '=', line.daging_id.id)]
            ).write({'stok': line.daging_id.stok - line.qty})

        return line
    
    @api.constrains('qty')
    def check_quantity(self):
        for line in self:
            if line.qty < 1:
                raise ValidationError('Jumlah pembelian harus minimal 1, silahkan input dengan benar!')
            elif line.daging_id.stok < line.qty:
                raise ValidationError('Stok yang tersedia tidak mencukupi.')

    @api.ondelete(at_uninstall=False)
    def __ondelete_penjualan(self):
        if self.detailpenjualan_ids:
            penjualan = []
            for line in self:
                penjualan = self.env['projectmandiri.detailpenjualan'].search(
                    [('penjualan_id', '=', line.id)])
                print(penjualan)

            for ob in penjualan:
                print(ob.daging_id.name + ' ' + str(ob.qty))
                ob.daging_id.stok += ob.qty
    
    
    def unlink(self):
        if self.detailpenjualan_ids:
            penjualan = []
            for line in self:
                penjualan = self.env['projectmandiri.detailpenjualan'].search(
                    [('penjualan_id', '=', line.id)])
                print(penjualan)

            for ob in penjualan:
                print(ob.daging_id.name + ' ' + str(ob.qty))
                ob.daging_id.stok += ob.qty

        line = super(Penjualan, self).unlink()

    def write(self, vals):
      for line in self:
          data_asli = self.env['projectmandiri.detailpenjualan'].search([('penjualan_id', '=', line.id)])
          print(data_asli)

          for data in data_asli:
              print(str(data.daging_id.name) + " " + str(data.qty) + ' ' + str(data.daging_id.stok))
              data.daging_id.stok += data.qty
      
      line = super(Penjualan, self).write(vals)
      
      for line in self:
          data_setelah_edit = self.env['projectmandiri.detailpenjualan'].search([('penjualan_id', '=', line.id)])
          print(data_asli)
          print(data_setelah_edit)

          for data_baru in data_setelah_edit:
              if data_baru in data_asli:
                  print(data_baru.daging_id.name + " " + str(data_baru.qty) + ' ' + str(data_baru.daging_id.stok))
                  data_baru.daging_id.stok -= data_baru.qty
              else:
                  pass

      return line

    _sql_constraints = [
        ('no_nota_unik', 'unique (name)', 'Nomor Nota tidak boleh sama!')
    ]