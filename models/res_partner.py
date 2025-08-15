# -*- coding: utf-8 -*-
from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    adoption_application_ids = fields.One2many(
        "adoption.application", "applicant_partner_id", string="Adoption Applications"
    )
