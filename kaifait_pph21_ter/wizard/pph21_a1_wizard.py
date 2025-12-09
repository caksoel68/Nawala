from odoo import models, fields, api
from datetime import date

class PPh21A1Wizard(models.TransientModel):
    _name = 'pph21.a1.wizard'
    _description = 'Wizard Bukti Potong 1721-A1'

    year = fields.Char(string='Tahun Pajak', default=lambda self: str(date.today().year - 1), required=True)
    employee_ids = fields.Many2many('hr.employee', string='Karyawan', required=True)
    company_id = fields.Many2one('res.company', string='Perusahaan', default=lambda self: self.env.company)

    # PERBAIKAN: Ubah nama dari 'action_print_a1' menjadi 'action_print' (sesuai XML)
    def action_print(self):
        data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'year': self.year,
                'employee_ids': self.employee_ids.ids,
                'company_id': self.company_id.id,
            },
        }
        # Pastikan referensi module benar ('kaifait_pph21_ter' atau nama folder module Anda)
        return self.env.ref('kaifait_pph21_ter.action_report_1721_a1').report_action(self, data=data)

    def get_a1_data(self, employee_id, year):
        """ 
        Logika inti untuk menarik data setahun. 
        Mengambil akumulasi dari Payslip Jan-Des tahun tersebut.
        """
        payslips = self.env['hr.payslip'].search([
            ('employee_id', '=', employee_id),
            ('state', '=', 'done'),
            ('date_to', '>=', f'{year}-01-01'),
            ('date_to', '<=', f'{year}-12-31'),
        ])

        gross_total = 0
        pph_total = 0
        
        # Mapping Code Salary Rule (Sesuaikan dengan Kode di DB Anda)
        for slip in payslips:
            for line in slip.line_ids:
                if line.code == 'GROSS': gross_total += line.total
                if line.code == 'PPH21': pph_total += line.total

        # Hitung Biaya Jabatan (5%, Max 6 Juta setahun)
        biaya_jabatan = min(gross_total * 0.05, 6000000)
        netto = gross_total - biaya_jabatan
        
        # Ambil PTKP dari Kontrak terakhir
        contract = payslips.sorted('date_to', reverse=True)[:1].contract_id
        ptkp_code = contract.l10n_id_ptkp if contract else 'TK/0'
        
        # Hardcode nilai PTKP (Idealnya ambil dari fungsi helper di model sebelumnya)
        ptkp_vals = {'TK/0': 54000000, 'K/0': 58500000, 'K/1': 63000000, 'K/3': 72000000} # dst..
        ptkp_amount = ptkp_vals.get(ptkp_code, 54000000)

        pkp = max(0, netto - ptkp_amount)
        pkp = (pkp // 1000) * 1000 # Floor rounding

        return {
            'gross': gross_total,
            'biaya_jabatan': biaya_jabatan,
            'netto': netto,
            'ptkp_code': ptkp_code,
            'ptkp_amount': ptkp_amount,
            'pkp': pkp,
            'pph_terutang': pph_total, # Asumsi perhitungan Payroll sudah akurat
        }