/** @odoo-module **/

import { Dialog } from "@web/core/dialog/dialog";
import { ErrorDialog, WarningDialog, RPCErrorDialog  } from "@web/core/errors/error_dialogs";
import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";

patch(Dialog.prototype, {
    setup() {
        super.setup();
        const app_system_name = session.app_system_name || "AirDyna";
        this.title = app_system_name;
    },
});