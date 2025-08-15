# -*- coding: utf-8 -*-
from odoo import fields, models


class PetSpecies(models.Model):
    _name = "pet.species"
    _description = "Pet Species"
    _order = "name"

    name = fields.Char(string="Name", required=True)


class PetBreed(models.Model):
    _name = "pet.breed"
    _description = "Pet Breed"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    species_id = fields.Many2one("pet.species", string="Species", required=True)


class PetTag(models.Model):
    _name = "pet.tag"
    _description = "Pet Tag"
    _order = "name"

    name = fields.Char(string="Name", required=True)
    color = fields.Integer(string="Color Index")
