from odoo import api, models, _, fields
from odoo.exceptions import UserError, ValidationError
from datetime import date


class KsClassSubject(models.Model):
    _name = 'ks.class.subject'
    _rec_name = 'ks_subject_id'
    _description = 'Class Subject'

    ks_subject_id = fields.Many2one('ks.subject', 'Subject ID', required=True,)
    ks_class_sub_id = fields.Many2one('ks.division', 'Class Subject')
    ks_class_id = fields.Many2one('ks.class', 'Class ID', required=True)
    ks_division_id = fields.Many2one('ks.division', 'Division ID', required=True,
                                     domain="[('ks_class_id', '=', ks_class_id)]")
    ks_max_marks = fields.Integer('Max Marks', required=True)
    # ks_student_class_id = fields.Many2one('ks.student.class', 'Student Class ID')  # added a field for domain

    # _sql_constraints = [
    #     ('ks_division_id_uniq', 'unique (ks_division_id)', 'Division ID must be unique!'), ]

    @api.onchange('ks_max_marks')
    def ks_max_marks_check(self):
        for rec in self:
            if rec.ks_max_marks == 0:
                raise ValidationError(_("Max Marks can not be Zero(0)."))
