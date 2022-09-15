# -*- coding: utf-8 -*-
# from odoo import http


# class Projectmandiri(http.Controller):
#     @http.route('/projectmandiri/projectmandiri', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/projectmandiri/projectmandiri/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('projectmandiri.listing', {
#             'root': '/projectmandiri/projectmandiri',
#             'objects': http.request.env['projectmandiri.projectmandiri'].search([]),
#         })

#     @http.route('/projectmandiri/projectmandiri/objects/<model("projectmandiri.projectmandiri"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('projectmandiri.object', {
#             'object': obj
#         })

from crypt import methods
import json


import json

from odoo import http, models, fields
from odoo.http import request


class Projectmandiri(http.Controller):
    @http.route('/projectmandiri/getdaging', auth='public', method=['GET'])
    def getDaging(self, **kw):
        daging = request.env['projectmandiri.daging'].search([])
        items = []

        for item in daging:
            items.append({
                'nama_daging': item.name,
                'harga_daging' : item.harga_daging,
                'stok': item.stok
            })
        
        return json.dumps(items)

    @http.route('/projectmandiri/getperusahaan', auth='public', method=['GET'])
    def getPerusahaan(self, **kw):
        perusahaan = request.env['projectmandiri.perusahaan'].search([])
        items = []

        for item in perusahaan:
            items.append({
                'nama_perusahaan': item.name,
                'alamat': item.alamat,
                'no_telepon': item.no_telp,
                'daging_id': item.daging_id[0].name
            })
        
        return json.dumps(items)