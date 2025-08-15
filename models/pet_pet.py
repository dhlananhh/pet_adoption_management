# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PetPet(models.Model):
    _name = "pet.pet"
    _description = "Pet"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string="Name", required=True, tracking=True)
    breed_id = fields.Many2one(
        "pet.breed", string="Breed", required=True, tracking=True
    )
    species_id = fields.Many2one(
        "pet.species", string="Species", related="breed_id.species_id", store=True
    )
    age = fields.Integer(string="Age (months)")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("unknown", "Unknown")],
        string="Gender",
        default="unknown",
    )
    description = fields.Text(string="Description")
    image = fields.Image(string="Image", max_width=512, max_height=512)
    tag_ids = fields.Many2many("pet.tag", string="Tags")
    state = fields.Selection(
        [
            ("available", "Available"),
            ("adopted", "Adopted"),
        ],
        string="Status",
        default="available",
        tracking=True,
    )
    adoption_application_ids = fields.One2many(
        "adoption.application", "pet_id", string="Adoption Applications"
    )
    application_count = fields.Integer(
        string="Application Count", compute="_compute_application_count"
    )

    @api.depends("adoption_application_ids")
    def _compute_application_count(self):
        for pet in self:
            pet.application_count = len(pet.adoption_application_ids)
