# -*- coding: utf-8 -*-
{
    'name': 'Payroll Indonesia - TER & PP 58/2023',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/Payroll',
    'summary': 'Payroll Indonesia Implementation complying with PP 58/2023 (TER) and PPh 21 2024',
    'description': """
Payroll Indonesia Enterprise Edition
====================================
Modul ini mengimplementasikan perhitungan gaji sesuai regulasi Indonesia terbaru:
* PP 58 Tahun 2023 (Tarif Efektif Rata-rata / TER).
* Perhitungan PPh 21 Jan-Nov (TER) dan Desember (Tarif Pasal 17).
* Integrasi BPJS Kesehatan dan Ketenagakerjaan.
* Integrasi Penuh dengan Accounting (via om_hr_payroll_account).
* Report Slip Gaji Standar Indonesia (QWeb).

Fitur:
* Master Data TER (Kategori A, B, C) yang dapat diupdate via CSV/UI.
* Otomatisasi penentuan kategori TER berdasarkan PTKP di Kontrak.
* Salary Rules Pythonic yang transparan.
* Slip Gaji PDF siap cetak dengan format Indonesia.
    """,
    'author': 'Syamsul Maarif AB',
    'website': 'https://kaifait.com',
    'license': 'OPL-1',
    'depends': [
        'hr',
        'hr_contract',
        'om_hr_payroll',
        'om_hr_payroll_account',
    ],
    'data': [
        # 1. Security (Load paling awal)
        'security/ir.model.access.csv',
        
        # 2. Data Master (Load file CSV yang sudah direvisi)
        'data/hr.payroll.ter.rate.csv', 
        
        # 3. Data Salary Rules
        'data/salary_rules_data.xml',
        
        # 4. Views
        'views/ter_master_view.xml',
        'views/hr_contract_view.xml',
        
        # 5. Reports
        'report/report_action.xml',
        'report/report_payslip_template.xml',
    ],
    'demo': [],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}