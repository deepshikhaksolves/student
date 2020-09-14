from odoo import api, models, fields
from datetime import date


class KsStudentExam(models.Model):
    _name = 'ks.student.exam'
    _description = 'Student Exam'

    name = fields.Char('Name', required=True)
    ks_student_id = fields.Many2one('ks.student', 'Student ID', required=True)
    ks_exam_id = fields.Many2one('ks.class.subject', 'Exam ID', required=True,
                                 domain="[('ks_student_id', '=', ks_student_id)]")
    ks_student_class_id = fields.Many2one('ks.student.class', 'Student Class ID', required=True)
    ks_obtained_marks = fields.Integer('Obtained Marks', required=True)

