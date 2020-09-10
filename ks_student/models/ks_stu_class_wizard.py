from odoo import api, _,  models, fields


class KSStudentClassWizard(models.TransientModel):
    _name = "ks.student.class.wizard"
    _description = 'Student Class Wizard'

    ks_name = fields.Many2many('ks.student', string="Name")
    ks_class_id = fields.Many2one('ks.class', string='Class')
    ks_division_id = fields.Many2one('ks.division', 'Class Division', required=True,
                                     domain="[('ks_class_id', '=', ks_class_id)]")
    ks_year_id = fields.Many2one('ks.school.year', 'Year', required=True)

    def ks_create_student_class(self):
        ks_sub_list = []
        for rec in self:
            ks_total_student = self.env['ks.student.class'].search([('ks_student_id', 'in', rec.ks_name.ids)])
            for ks_sub in rec.ks_division_id.ks_class_subject_ids:
                ks_sub_list.append([0, 0, {
                    'ks_subject_id': ks_sub.id,
                    # 'ks_student_class_id': rec.ks_class_id.id,
                }])
            for student in rec.ks_name:
                if student in ks_total_student.ks_student_id:
                    for ks_student in ks_total_student:
                        if student.id == ks_student.ks_student_id.id:
                            ks_student.write({'ks_subjects_ids': ks_sub_list})
                else:
                    student_dict = {'ks_student_id': student.id,
                                    'ks_class_id': rec.ks_class_id.id,
                                    'ks_division_id': rec.ks_division_id.id,
                                    'ks_subjects_ids': ks_sub_list,
                                    'ks_year_id': rec.ks_year_id.id}
                    rec.env['ks.student.class'].create(student_dict)



