from odoo import api, models, fields
from datetime import date


class KsStudentExam(models.Model):
    _name = 'ks.student.exam'
    _description = 'Student Exam'

    name = fields.Char('Exam Name', required=True)
    ks_student_id = fields.Many2one('ks.student', 'Student ID', required=True)
    ks_class_id = fields.Many2one('ks.class', 'Class', required=True)
    ks_student_class_id = fields.Many2one('ks.student.class', 'Student Class ID', required=True,
                                          domain="[('ks_class_id', '=', ks_class_id)]")
    ks_exam_id = fields.Many2one('ks.class.subject', 'Subject', required=True,
                                 domain="[('ks_class_id', '=', ks_class_id)]")
    ks_school_year = fields.Many2one('ks.school.year', 'Year', domain="[('is_current_year', '=', True)]")
    ks_obtained_marks = fields.Integer('Obtained Marks', required=True)

    # @api.onchange('ks_student_class_id')
    # def ks_exam_id_domain(self):
    #     for rec in self:
    #         rec.ks_class_id = rec.ks_student_class_id.ks_class_id
    #         return rec.ks_class_id

