{
    'name': 'MyCustomModule',
    'version': '1.0',
    'summary': 'A brief description of my module',
    'sequence': 10,
    'description': """
    A more detailed description of what my module does.
    """,
    'category': 'Tools',
    'author': 'Your Name',
    'website': 'http://www.yourwebsite.com',
    'depends': ['base'],  # لیست وابستگی‌ها
    'data': [
        'security/ir.model.access.csv',
        'views/my_model_views.xml',
    ],
    'application':True,
    'installable': True,
    'auto_install': False,
}
