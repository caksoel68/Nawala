from odoo import models, fields

class KaifaPphTer(models.Model):
    _name = 'kaifa.pph.ter'
    _description = 'Tabel Tarif PPh 21 TER'
    _order = 'category, min_income'

    category = fields.Selection([
        ('A', 'Kategori A'),
        ('B', 'Kategori B'),
        ('C', 'Kategori C'),
    ], string='Kategori TER', required=True)
    
    min_income = fields.Float(string='Penghasilan Min', required=True)
    max_income = fields.Float(string='Penghasilan Max', required=True)
    rate = fields.Float(string='Tarif (%)', required=True)