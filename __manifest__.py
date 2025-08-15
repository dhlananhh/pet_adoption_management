# -*- coding: utf-8 -*-
{
    "name": "Pet Adoption Management",
    "summary": """
        Manage the entire pet adoption process, from pet catalog to adoption applications.""",
    "description": """
        This module provides a comprehensive system for animal shelters and rescue organizations to manage their pets and the adoption lifecycle. Features include a detailed pet catalog, management of adoption applications, and a public-facing website portal for prospective adopters.
    """,
    "author": "Lan Anh",
    "website": "https://github.com/dhlananhh/pet_adoption_management",
    "category": "Services/Adoption",
    "version": "1.0",
    "depends": ["base", "website", "mail", "portal"],
    "data": [
        # 1. Security: Load groups and access rights first.
        "security/security.xml",
        "security/ir.model.access.csv",
        # 2. Data: Load initial data records.
        "data/adoption_application_stage_data.xml",
        "data/pet_tag_data.xml",
        "data/pet_species_and_breed_data.xml",
        # 3. Views: Load the backend UI.
        "views/pet_catalog_views.xml",
        "views/pet_pet_views.xml",
        "views/adoption_application_views.xml",
        # 4. Website: Load the frontend templates.
        "views/pet_adoption_portal_templates.xml",
    ],
    "application": True,
    "installable": True,
    "license": "LGPL-3",
}
