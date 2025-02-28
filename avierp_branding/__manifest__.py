{
    "name": "Branding",
    "summary": "Specific branding and customization for ERP",
    "version": "1.0.0",
    "category": "Other",
    "website": "https://www.airdyna.co.zw",
    "author": "",    
    "installable": True,
    "application": False,
    "depends": [        
        "web",
        "mail",
        "mail_bot",
    ],    
    "data": [
        "data/ir_config_parameter.xml",
        "views/base.xml",
        "views/company.xml",
        "views/urls.xml",
        "data/bot.xml",
        "data/ir_config_parameter.xml",
    ],
    "assets": {
        "web._assets_primary_variables": [
            ('prepend', 'avierp_branding/static/src/scss/variables.scss'),
        ],
        "web.assets_backend": [
            "avierp_branding/static/src/js/**/*.js",
            "avierp_branding/static/src/xml/**/*.xml",
            'avierp_branding/static/src/scss/app_menu.scss',
            "avierp_branding/static/src/scss/app_form_caf.scss",
        ],        
    },
    "post_init_hook": "post_init_debranding",
    "uninstall_hook": "uninstall_debranding",
}
