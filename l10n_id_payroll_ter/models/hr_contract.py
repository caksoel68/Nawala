from odoo import models, fields, api

class HrContract(models.Model):
    _inherit = 'hr.contract'

    l10n_id_ptkp_code = fields.Selection([
        ('TK/0', 'TK/0'), ('TK/1', 'TK/1'), ('TK/2', 'TK/2'), ('TK/3', 'TK/3'),
        ('K/0', 'K/0'),   ('K/1', 'K/1'),   ('K/2', 'K/2'),   ('K/3', 'K/3'),
    ], string='Status PTKP', required=True, default='TK/0', help="Digunakan untuk penentuan Kategori TER")

    l10n_id_ter_category = fields.Selection([
        ('A', 'Kategori A'),
        ('B', 'Kategori B'),
        ('C', 'Kategori C')
    ], string='Kategori TER', compute='_compute_ter_category', store=True)

    # BPJS Configuration
    use_bpjs_kesehatan = fields.Boolean(string="Hitung BPJS Kesehatan", default=True)
    use_bpjs_ketenagakerjaan = fields.Boolean(string="Hitung BPJS Ketenagakerjaan", default=True)

    @api.depends('l10n_id_ptkp_code')
    def _compute_ter_category(self):
        for contract in self:
            code = contract.l10n_id_ptkp_code
            if code in ['TK/0', 'TK/1', 'K/0']:
                contract.l10n_id_ter_category = 'A'
            elif code in ['TK/2', 'TK/3', 'K/1', 'K/2']:
                contract.l10n_id_ter_category = 'B'
            elif code == 'K/3':
                contract.l10n_id_ter_category = 'C'
            else:
                contract.l10n_id_ter_category = 'A' # Default fallback