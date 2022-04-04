# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class c:\users\nico\desktop\work\mymodules\sample(models.Model):
#     _name = 'c:\users\nico\desktop\work\mymodules\sample.c:\users\nico\desktop\work\mymodules\sample'
#     _description = 'c:\users\nico\desktop\work\mymodules\sample.c:\users\nico\desktop\work\mymodules\sample'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
