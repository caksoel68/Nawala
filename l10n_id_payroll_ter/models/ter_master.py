from odoo import models, fields, api

class HrPayrollTerRate(models.Model):
    # DIBERBAIKI: Harus sama dengan nama file CSV
    _name = 'hr.payroll.ter.rate'  
    _description = 'Tarif Efektif Rata-rata (TER) PP 58/2023'
    _order = 'category, min_income'

    name = fields.Char(string='Kode Tarif', compute='_compute_name', store=True)
    category = fields.Selection([
        ('A', 'Kategori A (TK/0, TK/1, K/0)'),
        ('B', 'Kategori B (TK/2, TK/3, K/1, K/2)'),
        ('C', 'Kategori C (K/3)'),
    ], string='Kategori TER', required=True)
    
    min_income = fields.Float(string='Penghasilan Min', required=True)
    max_income = fields.Float(string='Penghasilan Max', required=True)
    rate = fields.Float(string='Tarif (%)', required=True, digits=(12, 2))

    @api.depends('category', 'min_income', 'max_income')
    def _compute_name(self):
        for rec in self:
            rec.name = f"TER {rec.category}: {rec.min_income:,.0f} - {rec.max_income:,.0f}"

    @api.model
    def get_ter_rate(self, category, gross_income):
        domain = [
            ('category', '=', category),
            ('min_income', '<=', gross_income),
            ('max_income', '>=', gross_income)
        ]
        rule = self.search(domain, limit=1)
        if rule:
            return rule.rate
        return 0.0