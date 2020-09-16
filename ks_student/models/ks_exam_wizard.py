from odoo import api, _,  models, fields


class KSStudentExamWizard(models.TransientModel):
    _name = "ks.exam.wizard"
    _description = 'Exam Wizard'

    ks_name = fields.Many2one('ks.exam', string="Exam Name", required=True)
    name = fields.Many2one('ks.student', string="Student Name", required=True)
    ks_student_class_id = fields.Many2one('ks.student.class', 'Student Class ID', required=True)
    ks_exam_id = fields.Many2one('ks.class.subject', 'Subject', required=True)
    ks_school_year = fields.Many2one('ks.school.year', 'Year', required=True,
                                     domain="[('is_current_year', '=', True)]")
    ks_obtained_marks = fields.Integer('Obtained Marks', required=True)

    def ks_create_student_exam(self):
        for rec in self:
            ks_total_student = self.env['ks.student.exam'].search([('ks_student_id', '=', rec.name.id),
                                                ('ks_exam_id', '=', rec.ks_exam_id.id),
                                                ('ks_school_year', '=', rec.ks_school_year.id)])
            for ks_student in ks_total_student:
                ks_student.write({'ks_obtained_marks': rec.ks_obtained_marks})
            else:
                student_exam_dict = {'name': rec.ks_name.name,
                                     'ks_student_id': rec.name.id,
                                     'ks_exam_id': rec.ks_exam_id.id,
                                     'ks_student_class_id': rec.name.ks_student_history_ids.id,
                                     'ks_obtained_marks': rec.ks_obtained_marks,
                                     'ks_school_year': rec.ks_school_year.id,
                                     }
                rec.env['ks.student.exam'].create(student_exam_dict)
