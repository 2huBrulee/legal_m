# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ReporteQueja(models.Model):
	_inherit = 'reporte.queja'

	tomado = fields.Text()
