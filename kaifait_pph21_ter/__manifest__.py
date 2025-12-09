# -*- coding: utf-8 -*-
{
    'name': 'Indonesia PPh 21 TER 2025 (KaifaIT)',
    'version': '18.0.1.0.0',
    'summary': 'PPh 21 Calculation (TER & Article 17) with 1721-A1 Generator',
    'description': """
        Professional PPh 21 Addon for Odoo 18 CE.
        
        Key Features:
        1. Compliance: 
           - Jan-Nov: Effective Rate (TER) based on PP 58/2023.
           - December: Annualized calculation (Article 17) minus paid taxes.
        2. Reporting:
           - Automatic 1721-A1 Form Generator (PDF).
           - Monthly Tax Analysis (Pivot/Graph).
        3. Master Data:
           - Configurable TER Rates (A, B, C).
           - PTKP Status on Contracts.
           
        Includes Unit Tests & Demo Data.
    """,
    'author': 'Syamsul Maarif AB',
    'website': 'https://kaifait.com',
    'category': 'Human Resources/Payroll',
    'license': 'OPL-1',
    'depends': [
        'base', 
        'hr', 
        'hr_contract', 
        'om_hr_payroll'
    ],
    'data': [
        # 1. Security (Load first)
        'security/ir.model.access.csv',
        
        # 2. Master Data & Config
        'data/kaifa.pph.ter.csv',
        'data/salary_structure.xml',
        
        # 3. Views (Backend UI)
        'views/hr_contract_view.xml',
        'views/pph_ter_view.xml',
        'views/pph_analysis_view.xml',  # Pivot Report
        
        # 4. Wizards (Pop-up Windows)
        'wizard/pph21_a1_view.xml',     # Wizard Form
        
        # 5. Reports (Actions & Templates)
        'report/pph21_report.xml',      # Report Action
        'report/report_1721_a1_template.xml',    # PDF Template
    ],
    'demo': [
        'data/demo_data.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'price': 99.00,  # Nilai jual yang disarankan untuk fitur selengkap ini
    'currency': 'USD',
}