{
    'name': 'hospital management',
    'version': '1.0.0',
    'sequence':-100,
    'category': 'hospital',
    'summary': 'hospital management system',
    'description': " hospital management system",
    'depends': ['mail', 'product'],
    'data':[
        'security/ir.model.access.csv',
        'data/patient_tag_data.xml',
        'views/patient_view.xml',
        'wizard/cancel_appointment_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag.xml',
        'views/menu.xml',
    ],
    'demo':[],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license':'LGPL-3'
}
