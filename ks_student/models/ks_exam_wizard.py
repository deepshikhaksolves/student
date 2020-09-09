from odoo import api, _,  models, fields


class KSStudentExamWizard(models.TransientModel):
    _name = "ks.exam.wizard"
    _description = 'Exam Wizard'

    ks_name = fields.Many2one('ks.student', string="Name")
    ks_exam_id = fields.Many2one('ks.class.subject', 'Exam ID', required=True)
    ks_obtained_marks = fields.Integer('Marks')

    def ks_create_student_exam(self):
        for rec in self:
            ks_total_student = self.env['ks.student.exam'].search([('ks_student_id', 'in', rec.ks_name.ids),
                                                 ('ks_exam_id', '=', rec.ks_exam_id.id)])
            for ks_student in ks_total_student:
                ks_student.write({'ks_obtained_marks': rec.ks_obtained_marks})
            else:
                student_exam_dict = {'name': rec.ks_name.name,
                                     'ks_student_id': rec.ks_name.id,
                                     'ks_exam_id': rec.ks_exam_id.id,
                                     'ks_student_class_id': rec.ks_exam_id.ks_class_id.id,
                                     'ks_obtained_marks': rec.ks_obtained_marks,
                                     }
                rec.env['ks.student.exam'].create(student_exam_dict)
