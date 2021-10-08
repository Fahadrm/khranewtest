# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError


class CRMChecklist(models.Model):
    _name = "crm.checklist"
    _description = 'CRM Checklist'

    name = fields.Char("Name", required=True)
    description = fields.Char("Description")
    stage_id = fields.Many2one('crm.stage', string='Stage', required=True)


class CalendarEvent(models.Model):
    _inherit = 'crm.lead'

    @api.depends('checklist_ids', 'stage_id')
    def _compute_checklist(self):
        for rec in self:

            total_len = self.env['crm.checklist'].search_count([('stage_id', '=', rec.stage_id.id)])
            total_checklist = self.env['crm.checklist'].search([('stage_id', '=', rec.stage_id.id)])
            check_list_len = 0
            for checklist in total_checklist:
                if checklist in rec.checklist_ids:
                    check_list_len += 1
            # if rec.checklist_ids:
            #     check_list_len = len(rec.checklist_ids)
            if total_len != 0:
                rec.checklist = (check_list_len * 100) / total_len
            else:
                rec.checklist = 0

    checklist_ids = fields.Many2many("crm.checklist", string="Checklist", domain="[('stage_id', '=', stage_id)]")
    checklist = fields.Float(string="Checklist Completed", compute="_compute_checklist", store=True, default=0.0,)

    def write(self, vals):
        if 'stage_id' in vals:
            if self.checklist != 100:
                raise UserError(_("Please complete the checklist."))
        return super(CalendarEvent, self).write(vals)


class Stage(models.Model):
    _inherit = "crm.stage"

    checklist_id = fields.One2many('crm.checklist', 'stage_id', string='Checklist')






