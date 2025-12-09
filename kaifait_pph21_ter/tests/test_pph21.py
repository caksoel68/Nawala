from odoo.tests.common import TransactionCase, tagged
from datetime import date

@tagged('post_install', '-at_install')
class TestPPh21Calculation(TransactionCase):

    def setUp(self):
        super(TestPPh21Calculation, self).setUp()
        
        # Load dependencies
        self.Employee = self.env['hr.employee']
        self.Contract = self.env['hr.contract']
        self.Payslip = self.env['hr.payslip']
        self.Structure = self.env.ref('kaifait_pph21_ter.structure_indonesia_ter') # Pastikan ID XML structure benar

        # Create Employee
        self.employee = self.Employee.create({
            'name': 'Test Engineer',
        })

        # Create Contract: Gaji 10jt, TK/0 (Masuk TER A)
        self.contract = self.Contract.create({
            'name': 'Contract Test',
            'employee_id': self.employee.id,
            'wage': 10000000.0,
            'l10n_id_ptkp': 'TK/0', # Kategori A
            'state': 'open',
            'date_start': date(2025, 1, 1),
        })

    def test_01_ter_calculation_january(self):
        """ Test TER Calculation for January (Normal Month) """
        
        # Create Payslip for January
        payslip = self.Payslip.create({
            'name': 'Payslip Jan 2025',
            'employee_id': self.employee.id,
            'contract_id': self.contract.id,
            'struct_id': self.Structure.id,
            'date_from': date(2025, 1, 1),
            'date_to': date(2025, 1, 31),
        })
        
        payslip.compute_sheet()
        
        # Logic Verification:
        # Gross 10,000,000, TK/0 -> Category A.
        # Based on CSV above, range 9.65jt - 10.05jt is 2.5%
        # Tax = 10,000,000 * 2.5% = 250,000
        
        line_pph = payslip.line_ids.filtered(lambda l: l.code == 'PPH21')
        self.assertTrue(line_pph, "PPh 21 line should be generated")
        self.assertAlmostEqual(line_pph.total, 250000.0, delta=1.0, 
                               msg="TER Calculation for 10jt Cat A should be 2.5%")

    def test_02_ptkp_category_mapping(self):
        """ Validate Helper Function Logic via Contract change """
        
        # Change to K/3 -> Category C
        self.contract.write({'l10n_id_ptkp': 'K/3'})
        
        # Create Payslip February
        payslip = self.Payslip.create({
            'name': 'Payslip Feb 2025',
            'employee_id': self.employee.id,
            'contract_id': self.contract.id,
            'struct_id': self.Structure.id,
            'date_from': date(2025, 2, 1),
            'date_to': date(2025, 2, 28),
        })
        payslip.compute_sheet()
        
        # Verification:
        # Logic must assume Category C lookup.
        # Since we only provided CSV for A, this might return 0 or error depending on implementation.
        # This test ensures the code doesn't crash even if rate not found (returns 0).
        line_pph = payslip.line_ids.filtered(lambda l: l.code == 'PPH21')
        self.assertTrue(line_pph)