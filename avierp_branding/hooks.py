from odoo import api, SUPERUSER_ID

MENU_ICON_REPLACEMENT = {
    "mail.menu_root_discuss": "mail,static/description/icon.png",
    "calendar.mail_menu_calendar": "calendar,static/description/icon.png",
    "hr_employee_transfer.menu_employee_transfer": "hr_employee_transfer,static/description/transfer_icon.png",
    "note.menu_note_notes": "note,static/description/icon.png",
    "spreadsheet_oca.spreadsheet_spreadsheet_menu": "spreadsheet_oca,static/description/icon.png",
    "helpdesk_mgmt.helpdesk_ticket_main_menu": "helpdesk_mgmt,static/description/icon.png",
    "contacts.menu_contacts": "contacts,static/description/icon.png",
    "crm.crm_menu_root": "crm,static/description/icon.png",
    "sale.sale_menu_root": "sale_management,static/description/icon.png",
    "spreadsheet_dashboard.spreadsheet_dashboard_menu_root": "spreadsheet_dashboard,static/description/icon.png",
    "account.menu_finance": "account,static/description/icon.png",
    "project.menu_main_pm": "project,static/description/icon.png",
    "hr_timesheet.timesheet_menu_root": "hr_timesheet,static/description/icon_timesheet.png",
    "website.menu_website_configuration": "website,static/description/icon.png",
    "mass_mailing.mass_mailing_menu_root": "mass_mailing,static/description/icon.png",
    "document_knowledge.menu_document_root": "document_knowledge,static/description/icon.png",
    "survey.menu_surveys": "survey,static/description/icon.png",
    "purchase.menu_purchase_root": "avierp_branding/static/icon/purchase_menu_purchase_root.png",
    "stock.menu_stock_root": "stock,static/description/icon.png",
    "mgmtsystem.menu_mgmtsystem_root": "mgmtsystem,static/description/icon.png",
    "maintenance.menu_maintenance_title": "maintenance,static/description/icon.png",
    "hr.menu_hr_root": "hr,static/description/icon.png",
    "hr_attendance.menu_hr_attendance_root": "hr_attendance,static/description/icon.png",
    "hr_recruitment.menu_hr_recruitment_root": "hr_recruitment,static/description/icon.png",
    "hr_holidays.menu_hr_holidays_root": "hr_holidays,static/description/icon.png",
    "hr_expense.menu_hr_expense_root": "hr_expense,static/description/icon.png",
    "data_recycle.menu_data_cleaning_root": "data_recycle,static/description/icon.png",
    "base.menu_management": "base,static/description/modules.png",
    "base.menu_administration": "base,static/description/settings.png",
    "purchase.menu_purchase_root": "avierp_branding/static/icon/purchase_menu_purchase_root.png",
}


def post_init_debranding(env):

    odoobot = env["res.users"].browse(SUPERUSER_ID)
    odoobot.write({"name": "System"})
    odoobot.partner_id.write({"email": "system@example.com"})

    intro_msg = env.ref("mail.module_install_notification")
    intro_msg.write({"subject": "Welcome!"})

    top_menus = env["ir.ui.menu"].search([("parent_id", "=", False)])
    for m in top_menus:
        xml_id = m.get_external_id()[m.id]
        if MENU_ICON_REPLACEMENT.get(xml_id):
            new_icon = xml_id.replace(".", "_")
            m.write({"web_icon": f"avierp_branding,static/icon/{new_icon}.png"})


def uninstall_debranding(env):
    top_menus = env["ir.ui.menu"].search([("parent_id", "=", False)])
    for m in top_menus:
        xml_id = m.get_external_id()[m.id]
        replacement = MENU_ICON_REPLACEMENT.get(xml_id)
        if replacement:
            m.write({"web_icon": replacement})
