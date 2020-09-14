from odoo import api, _,  models, fields


class KSStudentExamReportWizard(models.TransientModel):
    _name = "ks.exam.report.wizard"
    _description = 'Exam Report Wizard'

    ks_name = fields.Many2one('ks.student.exam', string="Exam Name")
    name = fields.Many2one('ks.student', string="Student Name")

    def do_print(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'ks_student.ks_student_report_id',
            'datas': {},
        }

    def ks_student_exam_report(self):
        ks_report_list = []
        for rec in self:
            ks_total_exam = rec.env['ks.student.exam'].search([('ks_student_id', '=', rec.name.id),
                                                               ('name', '=', rec.ks_name.name)])
            ks_report = {'ks_student_name': rec.name.name,
                         'ks_student_class': rec.ks_name.ks_student_class_id.ks_class_id.name,
                         'ks_exam_name': rec.ks_name.name,
                         'ks_subject_name': [subject.display_name for subject in ks_total_exam.ks_exam_id],
                         'ks_obt_marks': [obt_marks.ks_obtained_marks for obt_marks in ks_total_exam],
                         'ks_max_marks': [max_marks.ks_max_marks for max_marks in ks_total_exam.ks_exam_id],
                         'ks_school_year': rec.ks_name.ks_student_class_id.ks_year_id.name
                         }
            ks_report_list.append(rec.name.name)
            ks_report_list.append(rec.ks_name.ks_student_class_id.ks_class_id.name)
            ks_report_list.append(rec.ks_name.name)
            for sub in ks_report.get('ks_subject_name'):
                ks_report_list.append(sub)
            return ks_report_list
