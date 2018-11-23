# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReporteQuejas(models.Model):
	_inherit = 'reporte.queja'

	tomado = fields.Char(string='Tomado', size=64)
