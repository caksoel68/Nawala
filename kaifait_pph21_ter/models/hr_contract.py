from odoo import models, fields, api

class HrContract(models.Model):
    _inherit = 'hr.contract'

    l10n_id_ptkp = fields.Selection([
        ('TK/0', 'TK/0 - Tidak Kawin, 0 Tanggungan'),
        ('TK/1', 'TK/1 - Tidak Kawin, 1 Tanggungan'),
        ('TK/2', 'TK/2 - Tidak Kawin, 2 Tanggungan'),
        ('TK/3', 'TK/3 - Tidak Kawin, 3 Tanggungan'),
        ('K/0', 'K/0 - Kawin, 0 Tanggungan'),
        ('K/1', 'K/1 - Kawin, 1 Tanggungan'),
        ('K/2', 'K/2 - Kawin, 2 Tanggungan'),
        ('K/3', 'K/3 - Kawin, 3 Tanggungan'),
    ], string='Status PTKP (PPh 21)', default='TK/0', required=True,
    help="Digunakan untuk menentukan Kategori TER (A, B, atau C) dan perhitungan masa pajak terakhir.")