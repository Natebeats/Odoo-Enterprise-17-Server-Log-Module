{
    'name': 'server_log',
    'version': '1.0',
    'summary': 'Verwaltung externer Server Logs',
    'author': 'GREENBAY Software',
    'category': 'Administartion',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/server_log_views.xml',

    ],
    'installable': True,
    'application': True,
}
