# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AdoptionApplication(models.Model):
    _name = "adoption.application"
    _description = "Adoption Application"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Application Number",
        required=True,
        copy=False,
        readonly=True,
        index=True,
        default=lambda self: "New",
    )
    pet_id = fields.Many2one("pet.pet", string="Pet", required=True, tracking=True)
    applicant_partner_id = fields.Many2one(
        "res.partner",
        string="Applicant",
        required=True,
        default=lambda self: self.env.user.partner_id,
        tracking=True,
    )
    application_date = fields.Date(
        string="Application Date", default=fields.Date.today, required=True
    )
    stage_id = fields.Many2one(
        "adoption.application.stage",
        string="Stage",
        group_expand="_read_group_stage_ids",
        default=lambda self: self.env.ref(
            "pet_adoption_management.stage_submitted", raise_if_not_found=False
        ),
        tracking=True,
    )
    motivation = fields.Text(string="Motivation")
    company_id = fields.Many2one(
        "res.company", string="Company", default=lambda self: self.env.company
    )

    @api.model
    def create(self, vals):
        if vals.get("name", "New") == "New":
            vals["name"] = (
                self.env["ir.sequence"].next_by_code("adoption.application.sequence")
                or "New"
            )
        return super(AdoptionApplication, self).create(vals)

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        return self.env["adoption.application.stage"].search([], order=order)


class AdoptionApplicationStage(models.Model):
    _name = "adoption.application.stage"
    _description = "Adoption Application Stage"
    _order = "sequence, id"

    name = fields.Char(string="Stage Name", required=True)
    sequence = fields.Integer(string="Sequence", default=10)
    fold = fields.Boolean(string="Folded in Kanban")
