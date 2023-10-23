{
    'name': 'hospital management system',
    'version': '1.0.0',
    'sequence':-100,
    'category': 'hospital',
    'summary': 'hospital management system',
    'description': " hospital management system",
    'depends': ['base'],
    'data':[
        'security/ir.model.access.csv',
        'views/patient_view.xml',
        'views/doctor_view.xml',
        'views/medicine_view.xml',
        'views/appointment.xml',
        'views/menu.xml',
    ],
    'demo':[],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license':'LGPL-3'
}
