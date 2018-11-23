# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReporteQuejaInherited(models.Model):
	_inherit = 'reporte.queja'

	tomado = fields.Char(string='tomado', size=64)
