# -*- coding: utf-8 -*-
{
    'name': "Gestionar liga de futbol",  # Titulo del módulo
    'summary': "Gestionar una liga de futbol :) (Version avanzada)",  # Resumen de la funcionaliadad
    'description': """
    Gestor de Liga de futbol (Version avanzada)
    ==============
    """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "SGE",
    'website': "",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [

      
        #Estos dos primeros ficheros:
        #1) El primero indica grupo de seguridad basado en rol
        #2) El segundo indica la politica de acceso del modelo
        #Mas información en https://www.odoo.com/documentation/14.0/es/developer/howtos/rdtraining/05_securityintro.html
        #Y en www.odoo.yenthevg.com/creating-security-groups-odoo/
        #'security/groups.xml',
        'security/ir.model.access.csv',

        #Aqui distintas vistas de equipo (vistas diferentes, mismo modelo)
        'views/liga_equipo.xml',
        'views/liga_equipo_clasificacion.xml',
        #Vista a un informe
        'report/liga_equipo_clasificacion_report.xml',
        #Aqui vista sobre los partidos
        'views/liga_partido.xml',
        #Añadimos un Wizard para introducir equipos
        'wizard/liga_equipo_wizard.xml'
        
    ],
    # Fichero con data de demo si se inicializa la base de datos con "demo data" (No incluido en ejemplo)
    # 'demo': [
    #     'demo.xml'
    # ],
}
