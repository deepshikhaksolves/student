from odoo import api, _,  models, fields


class KSStudentSubjectsWizard(models.TransientModel):
    _name = "ks.student.subject.wizard"
    _description = 'Student Subject Wizard'

    ks_subject_id = fields.Many2one('ks.subject', 'Subject ID')
    ks_student_class_id = fields.Many2one('ks.student.class', 'Class ID')

    def ks_create_student_subject(self):
        for rec in self:
            ks_total_sub = self.env['ks.student.subject'].search([('ks_subject_id', 'in', rec.ks_subject_id.ids),
                                                 ('ks_student_class_id', '=', rec.ks_student_class_id.id)])
            for subject in rec.ks_subject_id:
                if subject in ks_total_sub.ks_subject_id:
                    for ks_subject in ks_total_sub:
                        if subject.id == ks_subject.ks_subject_id.id:
                            ks_subject.write({'ks_subject_id': ks_subject.ks_subject_id.id})
                else:
                    student_dict = {'ks_subject_id': subject.id,
                                    'ks_class_id': rec.ks_class_id.id}
                    rec.env['ks.student.subject'].create(student_dict)



