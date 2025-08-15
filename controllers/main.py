# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class PetAdoptionController(http.Controller):

    @http.route(
        ["/pets", "/pets/page/<int:page>"], type="http", auth="public", website=True
    )
    def list_pets(self, page=1, **kw):
        """
        Renders the list of available pets on the website portal.
        """
        pets_per_page = 9
        total_pets = request.env["pet.pet"].search_count([("state", "=", "available")])
        pager = request.website.pager(
            url="/pets", total=total_pets, page=page, step=pets_per_page
        )
        pets = request.env["pet.pet"].search(
            [("state", "=", "available")], limit=pets_per_page, offset=pager["offset"]
        )
        return request.render(
            "pet_adoption_management.pet_list_template",
            {
                "pets": pets,
                "pager": pager,
            },
        )

    @http.route(
        '/pets/<model("pet.pet"):pet>', type="http", auth="public", website=True
    )
    def pet_details(self, pet, **kw):
        """
        Renders the detail page for a single pet.
        """
        return request.render(
            "pet_adoption_management.pet_detail_template", {"pet": pet}
        )

    @http.route("/pets/apply", type="http", auth="user", website=True, methods=["POST"])
    def apply_for_pet(self, **post):
        """
        Handles the submission of an adoption application.
        """
        pet_id = post.get("pet_id")
        if not pet_id:
            return request.redirect("/pets")

        request.env["adoption.application"].sudo().create(
            {
                "pet_id": int(pet_id),
                "applicant_partner_id": request.env.user.partner_id.id,
                "application_date": fields.Date.today(),
                "motivation": post.get("motivation"),
            }
        )

        return request.render("pet_adoption_management.application_thank_you_template")
