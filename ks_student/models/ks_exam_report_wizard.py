from odoo import api, _,  models, fields


class KSStudentExamReportWizard(models.TransientModel):
    _name = "ks.exam.report.wizard"
    _description = 'Exam Report Wizard'

    ks_name = fields.Many2one('ks.student.exam', string="Exam Name")
    ks_stu_name = fields.Many2many('ks.student', string="Student Name")
    ks_school_year = fields.Many2one('ks.school.year', 'Year', domain="[('is_current_year', '=', True)]")

    # def do_print(self):
    #     self.ensure_one()
    #     return {
    #         'type': 'ir.actions.report.xml',
    #         'report_name': 'ks_student.ks_student_report_id',
    #         'datas': {},
    #     }

    def ks_student_exam_report(self, student):
        ks_report_list = []
        for rec in self:
            ks_total_exam = rec.env['ks.student.exam'].search([('ks_student_id', '=', student.id),
                                                               ('name', '=', rec.ks_name.name),
                                                               ('ks_school_year', '=', rec.ks_school_year.id)])
            ks_report = {'ks_student_name': student.name,
                         'ks_student_class': rec.ks_name.ks_student_class_id.ks_class_id.name,
                         'ks_exam_name': rec.ks_name.name,
                         'ks_subject_name': [subject.display_name for subject in ks_total_exam.ks_exam_id],
                         'ks_obt_marks': [obt_marks.ks_obtained_marks for obt_marks in ks_total_exam],
                         'ks_max_marks': [max_marks.ks_max_marks for max_marks in ks_total_exam.ks_exam_id],
                         'ks_school_year': rec.ks_school_year.name
                         }
            # ks_report_list.append(ks_report)
        return ks_report

    def ks_student_details(self, student):
        ks_student_detail = []
        for rec in self:
            ks_student_report = rec.ks_student_exam_report(student)
            if ks_student_report:
                ks_student_detail.append(ks_student_report.get('ks_student_name'))
                ks_student_detail.append(ks_student_report.get('ks_student_class'))
                ks_student_detail.append(ks_student_report.get('ks_exam_name'))
            return ks_student_detail

    def ks_subject_details(self, subject, student):
        ks_subject_detail = []
        ks_student_report = self.ks_student_exam_report(student)
        if ks_student_report:
            for i in range(len(ks_student_report.get('ks_subject_name'))):
                if subject == ks_student_report.get('ks_subject_name')[i]:
                    ks_subject_detail.append(ks_student_report.get('ks_subject_name')[i])
                    ks_subject_detail.append(ks_student_report.get('ks_obt_marks')[i])
                    ks_subject_detail.append(ks_student_report.get('ks_max_marks')[i])
        return ks_subject_detail

    def ks_list_of_subject(self, student):
        ks_subject_detail = []
        ks_student_report = self.ks_student_exam_report(student)
        if ks_student_report:
            for i in range(len(ks_student_report.get('ks_subject_name'))):
                ks_subject_detail.append(ks_student_report.get('ks_subject_name')[i])
            return ks_subject_detail
