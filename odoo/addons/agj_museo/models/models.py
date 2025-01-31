# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class agj_museo(models.Model):
#     _name = 'agj_museo.agj_museo'
#     _description = 'agj_museo.agj_museo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

