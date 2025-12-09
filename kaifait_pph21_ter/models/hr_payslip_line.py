from odoo import models, fields

class HrPayslipLine(models.Model):
    _inherit = 'hr.payslip.line'

    # Kita tarik field dari Header (slip_id) ke Line agar bisa dipakai di Pivot
    # store=True wajib agar performa report cepat
    date_from = fields.Date(related='slip_id.date_from', store=True, string='Start Date')
    date_to = fields.Date(related='slip_id.date_to', store=True, string='End Date')
    state = fields.Selection(related='slip_id.state', store=True, string='Status')
    
    # Tambahan: Agar bisa group by Department/Job di report line
    employee_id = fields.Many2one('hr.employee', related='slip_id.employee_id', store=True)