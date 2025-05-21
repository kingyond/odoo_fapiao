{
    'name': 'China Fapiao Management',
    'version': '17.0.1.0.0',
    'category': 'Accounting/Accounting',
    'summary': '中国发票管理',
    'description': """
        中国发票管理模块
        管理特殊增值税发票和普通增值税发票
    """,
    'depends': ['account'],
    'data': [
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    'sequence': 1,
}
