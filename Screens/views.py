from django.shortcuts import render
import matplotlib.pyplot as plt
import numpy as np


# Create your views here.


def index(request):
    if request.method == 'POST':
        request.session['client_name'] = request.POST.get('client_name')
        request.session['industry'] = request.POST.get('industry')
        request.session['company_add'] = request.POST.get('company_add')
        request.session['assessor_name'] = request.POST.get('assessor_name')
        request.session['assessor_email_add'] = request.POST.get('assessor_email_add')
        request.session['brief_project_desc'] = request.POST.get('brief_project_desc')
        request.session['reviewed_by'] = request.POST.get('reviewed_by')
        request.session['assessment_portfolio'] = request.POST.get('assessment_portfolio')
        client_name = request.session.get('company_name')
        industry = request.session.get('industry')
        company_add = request.session.get('company_add')
        assessor_name = request.session.get('assessor_name')
        assessor_email_add = request.session.get('assessor_email_add')
        brief_project_desc = request.session.get('brief_project_desc')
        assessment_portfolio = request.session.get('assessment_portfolio')

        context = {
            'client_name': client_name,
            'industry': industry,
            'company_add': company_add,
            'assessor_name': assessor_name,
            'assessor_email_add': assessor_email_add,
            'brief_project_desc': brief_project_desc,
            'assessment_portfolio': assessment_portfolio,

        }
        return render(request, 'initial-screen.html', context)
    else:
        return render(request, 'index.html')


def introduction(request):
    return render(request, 'introduction.html')


def initial_screen(request):
    if request.method == 'POST':
        is1_1 = request.POST.get('is1_1')
        is1_2 = request.POST.get('is1_2')
        is1_3 = request.POST.get('is1_3')
        is1_4 = request.POST.get('is1_4')
        is1_5 = request.POST.get('is1_5')
        is1_6 = request.POST.get('is1_6')
        is1_7 = request.POST.get('is1_7')
        is1_8 = request.POST.get('is1_8')
        is1_9 = request.POST.get('is1_9')
        is1_10 = request.POST.get('is1_10')
        is1_11 = request.POST.get('is1_11')
        is1_12 = request.POST.get('is1_12')
        is1_13 = request.POST.get('is1_13')

        as1_1 = request.POST.get('as1_1')
        as1_2 = request.POST.get('as1_2')
        as1_3 = request.POST.get('as1_3')
        as1_4 = request.POST.get('as1_4')
        as1_5 = request.POST.get('as1_5')
        as1_6 = request.POST.get('as1_6')
        as1_7 = request.POST.get('as1_7')
        as1_8 = request.POST.get('as1_8')
        as1_9 = request.POST.get('as1_9')
        as1_10 = request.POST.get('as1_10')

        cs1_1 = request.POST.get('cs1_1')
        cs1_2 = request.POST.get('cs1_2')
        cs1_3 = request.POST.get('cs1_3')
        cs1_4 = request.POST.get('cs1_4')
        cs1_5 = request.POST.get('cs1_5')
        cs1_6 = request.POST.get('cs1_6')
        cs1_7 = request.POST.get('cs1_7')
        cs1_8 = request.POST.get('cs1_8')
        cs1_9 = request.POST.get('cs1_9')
        cs1_10 = request.POST.get('cs1_10')
        cs1_11 = request.POST.get('cs1_11')

        ks1_1 = request.POST.get('ks1_1')
        ks1_2 = request.POST.get('ks1_2')
        ks1_3 = request.POST.get('ks1_3')
        ks1_4 = request.POST.get('ks1_4')
        ks1_5 = request.POST.get('ks1_5')
        ks1_6 = request.POST.get('ks1_6')
        ks1_7 = request.POST.get('ks1_7')
        ks1_8 = request.POST.get('ks1_8')
        ks1_9 = request.POST.get('ks1_9')
        ks1_10 = request.POST.get('ks1_10')
        ks1_11 = request.POST.get('ks1_11')
        ks1_12 = request.POST.get('ks1_12')
        ks1_13 = request.POST.get('ks1_13')
        ks1_14 = request.POST.get('ks1_14')

        rs1_1 = request.POST.get('rs1_1')
        rs1_2 = request.POST.get('rs1_2')
        rs1_3 = request.POST.get('rs1_3')
        rs1_4 = request.POST.get('rs1_4')
        rs1_5 = request.POST.get('rs1_5')
        rs1_6 = request.POST.get('rs1_6')
        rs1_7 = request.POST.get('rs1_7')
        rs1_8 = request.POST.get('rs1_8')
        rs1_9 = request.POST.get('rs1_9')
        rs1_10 = request.POST.get('rs1_10')
        rs1_11 = request.POST.get('rs1_11')
        rs1_12 = request.POST.get('rs1_12')
        rs1_13 = request.POST.get('rs1_13')
        rs1_14 = request.POST.get('rs1_14')

        input = {
            'is1_1': is1_1,
            'is1_2': is1_2,
            'is1_3': is1_3,
            'is1_4': is1_4,
            'is1_5': is1_5,
            'is1_6': is1_6,
            'is1_7': is1_7,
            'is1_8': is1_8,
            'is1_9': is1_9,
            'is1_10': is1_10,
            'is1_11': is1_11,
            'is1_12': is1_12,
            'is1_13': is1_13,

            'as1_1': as1_1,
            'as1_2': as1_2,
            'as1_3': as1_3,
            'as1_4': as1_4,
            'as1_5': as1_5,
            'as1_6': as1_6,
            'as1_7': as1_7,
            'as1_8': as1_8,
            'as1_9': as1_9,
            'as1_10': as1_10,

            'cs1_1': cs1_1,
            'cs1_2': cs1_2,
            'cs1_3': cs1_3,
            'cs1_4': cs1_4,
            'cs1_5': cs1_5,
            'cs1_6': cs1_6,
            'cs1_7': cs1_7,
            'cs1_8': cs1_8,
            'cs1_9': cs1_9,
            'cs1_10': cs1_10,
            'cs1_11': cs1_11,

            'ks1_1': ks1_1,
            'ks1_2': ks1_2,
            'ks1_3': ks1_3,
            'ks1_4': ks1_4,
            'ks1_5': ks1_5,
            'ks1_6': ks1_6,
            'ks1_7': ks1_7,
            'ks1_8': ks1_8,
            'ks1_9': ks1_9,
            'ks1_10': ks1_10,
            'ks1_11': ks1_11,
            'ks1_12': ks1_12,
            'ks1_13': ks1_13,
            'ks1_14': ks1_14,

            'rs1_1': rs1_1,
            'rs1_2': rs1_2,
            'rs1_3': rs1_3,
            'rs1_4': rs1_4,
            'rs1_5': rs1_5,
            'rs1_6': rs1_6,
            'rs1_7': rs1_7,
            'rs1_8': rs1_8,
            'rs1_9': rs1_9,
            'rs1_10': rs1_10,
            'rs1_11': rs1_11,
            'rs1_12': rs1_12,
            'rs1_13': rs1_13,
            'rs1_14': rs1_14,
        }

        table = TotalScoreInitial(input, request)
        is_avg_score = table.is_all_score()[1]

        table = AssessmentTotalScore(input, request)
        as_total_score = table.as_all_score()[0]
        as_avg_score = table.as_all_score()[1]
        comp_total_score = table.as_all_score()[2]
        dao_total_score = table.as_all_score()[3]
        ra_total_score = table.as_all_score()[4]
        rp_total_score = table.as_all_score()[5]
        aa_av_score = table.as_all_score()[6]

        request.session['aa_av_score'] = aa_av_score

        table = CustomerTotalScore(input, request)
        cs_total_score = table.cs_all_score()[0]
        cs_avg_score = table.cs_all_score()[1]
        compc_total_score = table.cs_all_score()[2]
        daoc_total_score = table.cs_all_score()[3]
        rac_total_score = table.cs_all_score()[4]
        rpc_total_score = table.cs_all_score()[5]
        aac_av_score = table.cs_all_score()[6]

        request.session['aac_av_score'] = aac_av_score

        table = KycTotalScore(input, request)
        ks_total_score = table.ks_all_score()[0]
        ks_avg_score = table.ks_all_score()[1]
        compk_total_score = table.ks_all_score()[2]
        daok_total_score = table.ks_all_score()[3]
        rak_total_score = table.ks_all_score()[4]
        rpk_total_score = table.ks_all_score()[5]
        aak_av_score = table.ks_all_score()[6]

        request.session['aak_av_score'] = aak_av_score

        table = RegulatoryTotalScore(input, request)
        rs_total_score = table.rs_all_score()[0]
        rs_avg_score = table.rs_all_score()[1]
        compr_total_score = table.rs_all_score()[2]
        cusr_total_score = table.rs_all_score()[3]
        regr_total_score = table.rs_all_score()[4]
        rar_total_score = table.rs_all_score()[5]
        aar_av_score = table.rs_all_score()[6]

        request.session['aar_av_score'] = aar_av_score

        total_avg = ((as_avg_score + cs_avg_score + ks_avg_score + rs_avg_score) / 4)
        total_avg = "{:.2f}".format(total_avg)

        request.session['total_avg'] = total_avg

        # adding data into session

        request.session['dao_total_score'] = dao_total_score
        request.session['ra_total_score'] = ra_total_score
        request.session['rp_total_score'] = rp_total_score
        request.session['comp_total_score'] = comp_total_score
        request.session['daoc_total_score'] = daoc_total_score
        request.session['rac_total_score'] = rac_total_score
        request.session['rpc_total_score'] = rpc_total_score
        request.session['compc_total_score'] = compc_total_score
        request.session['daok_total_score'] = daok_total_score
        request.session['rak_total_score'] = rak_total_score
        request.session['rpk_total_score'] = rpk_total_score
        request.session['compk_total_score'] = compk_total_score
        request.session['compr_total_score'] = compr_total_score
        request.session['cusr_total_score'] = cusr_total_score
        request.session['regr_total_score'] = regr_total_score
        request.session['rar_total_score'] = rar_total_score

        spider1(request)
        spider2(request)
        spider3(request)
        spider4(request)
        print('method called................')

        context = {
            'input': input,
            'is_avg_score': is_avg_score,
            'as_total_score': as_total_score,
            'as_avg_score': as_avg_score,
            'cs_total_score': cs_total_score,
            'cs_avg_score': cs_avg_score,
            'ks_total_score': ks_total_score,
            'ks_avg_score': ks_avg_score,
            'rs_total_score': rs_total_score,
            'rs_avg_score': rs_avg_score,
            'total_avg': total_avg,
            'comp_total_score': comp_total_score,
            'dao_total_score': dao_total_score,
            'ra_total_score': ra_total_score,
            'rp_total_score': rp_total_score,
            'aa_av_score': aa_av_score,
            'compc_total_score': compc_total_score,
            'daoc_total_score': daoc_total_score,
            'rac_total_score': rac_total_score,
            'rpc_total_score': rpc_total_score,
            'aac_av_score': aac_av_score,
            'compk_total_score': compk_total_score,
            'daok_total_score': daok_total_score,
            'rak_total_score': rak_total_score,
            'rpk_total_score': rpk_total_score,
            'aak_av_score': aak_av_score,
            'compr_total_score': compr_total_score,
            'cusr_total_score': cusr_total_score,
            'regr_total_score': regr_total_score,
            'rar_total_score': rar_total_score,
            'aar_av_score': aar_av_score,
        }
        return render(request, 'kyc_dashboard.html', context)
    else:
        return render(request, 'initial-screen.html')


class TotalScoreInitial:
    def __init__(self, input, request):
        self.input = input
        self.score = 0

    def is1_1(self):
        self.score = 0
        if self.input.get('is1_1') == '1':
            self.score = 1
        elif self.input.get('is1_1') == '2':
            self.score = 2
        elif self.input.get('is1_1') == '3':
            self.score = 3
        elif self.input.get('is1_1') == '4':
            self.score = 4
        return self.score

    def is1_2(self):
        self.score = 0
        if self.input.get('is1_2') == '1':
            self.score = 1
        elif self.input.get('is1_2') == '2':
            self.score = 2
        elif self.input.get('is1_2') == '3':
            self.score = 3
        elif self.input.get('is1_2') == '4':
            self.score = 4
        return self.score

    def is1_3(self):
        self.score = 0
        if self.input.get('is1_3') == '1':
            self.score = 1
        elif self.input.get('is1_3') == '2':
            self.score = 2
        elif self.input.get('is1_3') == '3':
            self.score = 3
        elif self.input.get('is1_3') == '4':
            self.score = 4
        return self.score

    def is1_4(self):
        self.score = 0
        if self.input.get('is1_4') == '1':
            self.score = 1
        elif self.input.get('is1_4') == '2':
            self.score = 2
        elif self.input.get('is1_4') == '3':
            self.score = 3
        elif self.input.get('is1_4') == '4':
            self.score = 4
        return self.score

    def is1_5(self):
        self.score = 0
        if self.input.get('is1_5') == '1':
            self.score = 1
        elif self.input.get('is1_5') == '2':
            self.score = 2
        elif self.input.get('is1_5') == '3':
            self.score = 3
        elif self.input.get('is1_5') == '4':
            self.score = 4
        return self.score

    def is1_6(self):
        self.score = 0
        if self.input.get('is1_6') == '1':
            self.score = 1
        elif self.input.get('is1_6') == '2':
            self.score = 2
        elif self.input.get('is1_6') == '3':
            self.score = 3
        elif self.input.get('is1_6') == '4':
            self.score = 4
        return self.score

    def is1_7(self):
        self.score = 0
        if self.input.get('is1_7') == '1':
            self.score = 1
        elif self.input.get('is1_7') == '2':
            self.score = 2
        elif self.input.get('is1_7') == '3':
            self.score = 3
        elif self.input.get('is1_7') == '4':
            self.score = 4
        return self.score

    def is1_8(self):
        self.score = 0
        if self.input.get('is1_8') == '1':
            self.score = 1
        elif self.input.get('is1_8') == '2':
            self.score = 2
        elif self.input.get('is1_8') == '3':
            self.score = 3
        elif self.input.get('is1_8') == '4':
            self.score = 4
        return self.score

    def is1_9(self):
        self.score = 0
        if self.input.get('is1_9') == '1':
            self.score = 1
        elif self.input.get('is1_9') == '2':
            self.score = 2
        elif self.input.get('is1_9') == '3':
            self.score = 3
        elif self.input.get('is1_9') == '4':
            self.score = 4
        return self.score

    def is1_10(self):
        self.score = 0
        if self.input.get('is1_10') == '1':
            self.score = 1
        elif self.input.get('is1_10') == '2':
            self.score = 2
        elif self.input.get('is1_10') == '3':
            self.score = 3
        elif self.input.get('is1_10') == '4':
            self.score = 4
        return self.score

    def is1_11(self):
        self.score = 0
        if self.input.get('is1_11') == '1':
            self.score = 1
        elif self.input.get('is1_11') == '2':
            self.score = 2
        elif self.input.get('is1_11') == '3':
            self.score = 3
        elif self.input.get('is1_11') == '4':
            self.score = 4
        return self.score

    def is1_12(self):
        self.score = 0
        if self.input.get('is1_12') == '1':
            self.score = 1
        elif self.input.get('is1_12') == '2':
            self.score = 2
        elif self.input.get('is1_12') == '3':
            self.score = 3
        elif self.input.get('is1_12') == '4':
            self.score = 4
        return self.score

    def is1_13(self):
        self.score = 0
        if self.input.get('is1_13') == '1':
            self.score = 1
        elif self.input.get('is1_13') == '2':
            self.score = 2
        elif self.input.get('is1_13') == '3':
            self.score = 3
        elif self.input.get('is1_13') == '4':
            self.score = 4
        return self.score

    def is_all_score(self):
        is1_1_score = self.is1_1()
        is1_2_score = self.is1_2()
        is1_3_score = self.is1_3()
        is1_4_score = self.is1_4()
        is1_5_score = self.is1_5()
        is1_6_score = self.is1_6()
        is1_7_score = self.is1_7()
        is1_8_score = self.is1_8()
        is1_9_score = self.is1_9()
        is1_10_score = self.is1_10()
        is1_11_score = self.is1_11()
        is1_12_score = self.is1_12()
        is1_13_score = self.is1_13()

        is_total_score = is1_1_score + is1_2_score + is1_3_score + is1_4_score + is1_5_score + is1_6_score + is1_7_score\
                         + is1_8_score + is1_9_score + is1_10_score + is1_11_score + is1_12_score + is1_13_score

        avg_score_ini = round((is_total_score/13), 2)
        return [is_total_score, avg_score_ini]


class AssessmentTotalScore:
    def __init__(self, input, request):
        self.input = input
        self.score = 0

    def as1_1(self):
        self.score = 0
        if self.input.get('as1_1') == '1':
            self.score = 1
        elif self.input.get('as1_1') == '2':
            self.score = 2
        elif self.input.get('as1_1') == '3':
            self.score = 3
        elif self.input.get('as1_1') == '4':
            self.score = 4
        return self.score

    def as1_2(self):
        self.score = 0
        if self.input.get('as1_2') == '1':
            self.score = 1
        elif self.input.get('as1_2') == '2':
            self.score = 2
        elif self.input.get('as1_2') == '3':
            self.score = 3
        elif self.input.get('as1_2') == '4':
            self.score = 4
        return self.score

    def as1_3(self):
        self.score = 0
        if self.input.get('as1_3') == '1':
            self.score = 1
        elif self.input.get('as1_3') == '2':
            self.score = 2
        elif self.input.get('as1_3') == '3':
            self.score = 3
        elif self.input.get('as1_3') == '4':
            self.score = 4
        return self.score

    def as1_4(self):
        self.score = 0
        if self.input.get('as1_4') == '1':
            self.score = 1
        elif self.input.get('as1_4') == '2':
            self.score = 2
        elif self.input.get('as1_4') == '3':
            self.score = 3
        elif self.input.get('as1_4') == '4':
            self.score = 4
        return self.score

    def as1_5(self):
        self.score = 0
        if self.input.get('as1_5') == '1':
            self.score = 1
        elif self.input.get('as1_5') == '2':
            self.score = 2
        elif self.input.get('as1_5') == '3':
            self.score = 3
        elif self.input.get('as1_5') == '4':
            self.score = 4
        return self.score

    def as1_6(self):
        self.score = 0
        if self.input.get('as1_6') == '1':
            self.score = 1
        elif self.input.get('as1_6') == '2':
            self.score = 2
        elif self.input.get('as1_6') == '3':
            self.score = 3
        elif self.input.get('as1_6') == '4':
            self.score = 4
        return self.score

    def as1_7(self):
        self.score = 0
        if self.input.get('as1_7') == '1':
            self.score = 1
        elif self.input.get('as1_7') == '2':
            self.score = 2
        elif self.input.get('as1_7') == '3':
            self.score = 3
        elif self.input.get('as1_7') == '4':
            self.score = 4
        return self.score

    def as1_8(self):
        self.score = 0
        if self.input.get('as1_8') == '1':
            self.score = 1
        elif self.input.get('as1_8') == '2':
            self.score = 2
        elif self.input.get('as1_8') == '3':
            self.score = 3
        elif self.input.get('as1_8') == '4':
            self.score = 4
        return self.score

    def as1_9(self):
        self.score = 0
        if self.input.get('as1_9') == '1':
            self.score = 1
        elif self.input.get('as1_9') == '2':
            self.score = 2
        elif self.input.get('as1_9') == '3':
            self.score = 3
        elif self.input.get('as1_9') == '4':
            self.score = 4
        return self.score

    def as1_10(self):
        self.score = 0
        if self.input.get('as1_10') == '1':
            self.score = 1
        elif self.input.get('as1_10') == '2':
            self.score = 2
        elif self.input.get('as1_10') == '3':
            self.score = 3
        elif self.input.get('as1_10') == '4':
            self.score = 4
        return self.score

    def as_all_score(self):
        as1_1_score = self.as1_1()
        as1_2_score = self.as1_2()
        as1_3_score = self.as1_3()
        as1_4_score = self.as1_4()
        as1_5_score = self.as1_5()
        as1_6_score = self.as1_6()
        as1_7_score = self.as1_7()
        as1_8_score = self.as1_8()
        as1_9_score = self.as1_9()
        as1_10_score = self.as1_10()

        as_total_score = as1_1_score + as1_2_score + as1_3_score + as1_4_score + as1_5_score + as1_6_score \
                         + as1_7_score + as1_8_score + as1_9_score + as1_10_score

        comp_total_score = round(((as1_1_score + as1_2_score)/2), 2)

        dao_total_score = round((as1_3_score/1), 2)

        ra_total_score = round(((as1_4_score + as1_5_score)/2), 2)

        rp_total_score = round(((as1_6_score + as1_7_score + as1_8_score + as1_9_score + as1_10_score)/5), 2)

        aa_av_score = round(((comp_total_score + dao_total_score + ra_total_score + rp_total_score)/4), 2)

        as_avg_score = round((as_total_score / 10), 2)
        return [as_total_score, as_avg_score, comp_total_score, dao_total_score, ra_total_score,
                rp_total_score, aa_av_score]


class CustomerTotalScore:
    def __init__(self, input, request):
        self.input = input
        self.score = 0

    def cs1_1(self):
        self.score = 0
        if self.input.get('cs1_1') == '1':
            self.score = 1
        elif self.input.get('cs1_1') == '2':
            self.score = 2
        elif self.input.get('cs1_1') == '3':
            self.score = 3
        elif self.input.get('cs1_1') == '4':
            self.score = 4
        return self.score

    def cs1_2(self):
        self.score = 0
        if self.input.get('cs1_2') == '1':
            self.score = 1
        elif self.input.get('cs1_2') == '2':
            self.score = 2
        elif self.input.get('cs1_2') == '3':
            self.score = 3
        elif self.input.get('cs1_2') == '4':
            self.score = 4
        return self.score

    def cs1_3(self):
        self.score = 0
        if self.input.get('cs1_3') == '1':
            self.score = 1
        elif self.input.get('cs1_3') == '2':
            self.score = 2
        elif self.input.get('cs1_3') == '3':
            self.score = 3
        elif self.input.get('cs1_3') == '4':
            self.score = 4
        return self.score

    def cs1_4(self):
        self.score = 0
        if self.input.get('cs1_4') == '1':
            self.score = 1
        elif self.input.get('cs1_4') == '2':
            self.score = 2
        elif self.input.get('cs1_4') == '3':
            self.score = 3
        elif self.input.get('cs1_4') == '4':
            self.score = 4
        return self.score

    def cs1_5(self):
        self.score = 0
        if self.input.get('cs1_5') == '1':
            self.score = 1
        elif self.input.get('cs1_5') == '2':
            self.score = 2
        elif self.input.get('cs1_5') == '3':
            self.score = 3
        elif self.input.get('cs1_5') == '4':
            self.score = 4
        return self.score

    def cs1_6(self):
        self.score = 0
        if self.input.get('cs1_6') == '1':
            self.score = 1
        elif self.input.get('cs1_6') == '2':
            self.score = 2
        elif self.input.get('cs1_6') == '3':
            self.score = 3
        elif self.input.get('cs1_6') == '4':
            self.score = 4
        return self.score

    def cs1_7(self):
        self.score = 0
        if self.input.get('cs1_7') == '1':
            self.score = 1
        elif self.input.get('cs1_7') == '2':
            self.score = 2
        elif self.input.get('cs1_7') == '3':
            self.score = 3
        elif self.input.get('cs1_7') == '4':
            self.score = 4
        return self.score

    def cs1_8(self):
        self.score = 0
        if self.input.get('cs1_8') == '1':
            self.score = 1
        elif self.input.get('cs1_8') == '2':
            self.score = 2
        elif self.input.get('cs1_8') == '3':
            self.score = 3
        elif self.input.get('cs1_8') == '4':
            self.score = 4
        return self.score

    def cs1_9(self):
        self.score = 0
        if self.input.get('cs1_9') == '1':
            self.score = 1
        elif self.input.get('cs1_9') == '2':
            self.score = 2
        elif self.input.get('cs1_9') == '3':
            self.score = 3
        elif self.input.get('cs1_9') == '4':
            self.score = 4
        return self.score

    def cs1_10(self):
        self.score = 0
        if self.input.get('cs1_10') == '1':
            self.score = 1
        elif self.input.get('cs1_10') == '2':
            self.score = 2
        elif self.input.get('cs1_10') == '3':
            self.score = 3
        elif self.input.get('cs1_10') == '4':
            self.score = 4
        return self.score

    def cs1_11(self):
        self.score = 0
        if self.input.get('cs1_11') == '1':
            self.score = 1
        elif self.input.get('cs1_11') == '2':
            self.score = 2
        elif self.input.get('cs1_11') == '3':
            self.score = 3
        elif self.input.get('cs1_11') == '4':
            self.score = 4
        return self.score

    def cs_all_score(self):
        cs1_1_score = self.cs1_1()
        cs1_2_score = self.cs1_2()
        cs1_3_score = self.cs1_3()
        cs1_4_score = self.cs1_4()
        cs1_5_score = self.cs1_5()
        cs1_6_score = self.cs1_6()
        cs1_7_score = self.cs1_7()
        cs1_8_score = self.cs1_8()
        cs1_9_score = self.cs1_9()
        cs1_10_score = self.cs1_10()
        cs1_11_score = self.cs1_11()

        cs_total_score = cs1_1_score + cs1_2_score + cs1_3_score + cs1_4_score + cs1_5_score + cs1_6_score \
                         + cs1_7_score + cs1_8_score + cs1_9_score + cs1_10_score + cs1_11_score

        compc_total_score = round(((cs1_1_score + cs1_2_score)/2), 2)

        daoc_total_score = round(((cs1_3_score + cs1_4_score + cs1_5_score + cs1_6_score)/4), 2)

        rac_total_score = round(((cs1_7_score + cs1_8_score + cs1_9_score + cs1_10_score)/4), 2)

        rpc_total_score = round((cs1_11_score/1), 2)

        aac_av_score = round(((compc_total_score + daoc_total_score + rac_total_score + rpc_total_score)/4), 2)

        cs_avg_score = round((cs_total_score / 11), 2)
        return [cs_total_score, cs_avg_score, compc_total_score, daoc_total_score, rac_total_score,
                rpc_total_score, aac_av_score]


class KycTotalScore:
    def __init__(self, input, request):
        self.input = input
        self.score = 0

    def ks1_1(self):
        self.score = 0
        if self.input.get('ks1_1') == '1':
            self.score = 1
        elif self.input.get('ks1_1') == '2':
            self.score = 2
        elif self.input.get('ks1_1') == '3':
            self.score = 3
        elif self.input.get('ks1_1') == '4':
            self.score = 4
        return self.score

    def ks1_2(self):
        self.score = 0
        if self.input.get('ks1_2') == '1':
            self.score = 1
        elif self.input.get('ks1_2') == '2':
            self.score = 2
        elif self.input.get('ks1_2') == '3':
            self.score = 3
        elif self.input.get('ks1_2') == '4':
            self.score = 4
        return self.score

    def ks1_3(self):
        self.score = 0
        if self.input.get('ks1_3') == '1':
            self.score = 1
        elif self.input.get('ks1_3') == '2':
            self.score = 2
        elif self.input.get('ks1_3') == '3':
            self.score = 3
        elif self.input.get('ks1_3') == '4':
            self.score = 4
        return self.score

    def ks1_4(self):
        self.score = 0
        if self.input.get('ks1_4') == '1':
            self.score = 1
        elif self.input.get('ks1_4') == '2':
            self.score = 2
        elif self.input.get('ks1_4') == '3':
            self.score = 3
        elif self.input.get('ks1_4') == '4':
            self.score = 4
        return self.score

    def ks1_5(self):
        self.score = 0
        if self.input.get('ks1_5') == '1':
            self.score = 1
        elif self.input.get('ks1_5') == '2':
            self.score = 2
        elif self.input.get('ks1_5') == '3':
            self.score = 3
        elif self.input.get('ks1_5') == '4':
            self.score = 4
        return self.score

    def ks1_6(self):
        self.score = 0
        if self.input.get('ks1_6') == '1':
            self.score = 1
        elif self.input.get('ks1_6') == '2':
            self.score = 2
        elif self.input.get('ks1_6') == '3':
            self.score = 3
        elif self.input.get('ks1_6') == '4':
            self.score = 4
        return self.score

    def ks1_7(self):
        self.score = 0
        if self.input.get('ks1_7') == '1':
            self.score = 1
        elif self.input.get('ks1_7') == '2':
            self.score = 2
        elif self.input.get('ks1_7') == '3':
            self.score = 3
        elif self.input.get('ks1_7') == '4':
            self.score = 4
        return self.score

    def ks1_8(self):
        self.score = 0
        if self.input.get('ks1_8') == '1':
            self.score = 1
        elif self.input.get('ks1_8') == '2':
            self.score = 2
        elif self.input.get('ks1_8') == '3':
            self.score = 3
        elif self.input.get('ks1_8') == '4':
            self.score = 4
        return self.score

    def ks1_9(self):
        self.score = 0
        if self.input.get('ks1_9') == '1':
            self.score = 1
        elif self.input.get('ks1_9') == '2':
            self.score = 2
        elif self.input.get('ks1_9') == '3':
            self.score = 3
        elif self.input.get('ks1_9') == '4':
            self.score = 4
        return self.score

    def ks1_10(self):
        self.score = 0
        if self.input.get('ks1_10') == '1':
            self.score = 1
        elif self.input.get('ks1_10') == '2':
            self.score = 2
        elif self.input.get('ks1_10') == '3':
            self.score = 3
        elif self.input.get('ks1_10') == '4':
            self.score = 4
        return self.score

    def ks1_11(self):
        self.score = 0
        if self.input.get('ks1_11') == '1':
            self.score = 1
        elif self.input.get('ks1_11') == '2':
            self.score = 2
        elif self.input.get('ks1_11') == '3':
            self.score = 3
        elif self.input.get('ks1_11') == '4':
            self.score = 4
        return self.score

    def ks1_12(self):
        self.score = 0
        if self.input.get('ks1_12') == '1':
            self.score = 1
        elif self.input.get('ks1_12') == '2':
            self.score = 2
        elif self.input.get('ks1_12') == '3':
            self.score = 3
        elif self.input.get('ks1_12') == '4':
            self.score = 4
        return self.score

    def ks1_13(self):
        self.score = 0
        if self.input.get('ks1_13') == '1':
            self.score = 1
        elif self.input.get('ks1_13') == '2':
            self.score = 2
        elif self.input.get('ks1_13') == '3':
            self.score = 3
        elif self.input.get('ks1_13') == '4':
            self.score = 4
        return self.score

    def ks1_14(self):
        self.score = 0
        if self.input.get('ks1_14') == '1':
            self.score = 1
        elif self.input.get('ks1_14') == '2':
            self.score = 2
        elif self.input.get('ks1_14') == '3':
            self.score = 3
        elif self.input.get('ks1_14') == '4':
            self.score = 4
        return self.score

    def ks_all_score(self):
        ks1_1_score = self.ks1_1()
        ks1_2_score = self.ks1_2()
        ks1_3_score = self.ks1_3()
        ks1_4_score = self.ks1_4()
        ks1_5_score = self.ks1_5()
        ks1_6_score = self.ks1_6()
        ks1_7_score = self.ks1_7()
        ks1_8_score = self.ks1_8()
        ks1_9_score = self.ks1_9()
        ks1_10_score = self.ks1_10()
        ks1_11_score = self.ks1_11()
        ks1_12_score = self.ks1_12()
        ks1_13_score = self.ks1_13()
        ks1_14_score = self.ks1_14()

        ks_total_score = ks1_1_score + ks1_2_score + ks1_3_score + ks1_4_score + ks1_5_score + ks1_6_score \
                         + ks1_7_score + ks1_8_score + ks1_9_score + ks1_10_score + ks1_11_score \
                         + ks1_12_score + ks1_13_score + ks1_14_score

        compk_total_score = round(((ks1_1_score + ks1_2_score + ks1_3_score + ks1_4_score + ks1_5_score)/5), 2)

        daok_total_score = round(((ks1_6_score + ks1_7_score)/2), 2)

        rak_total_score = round(((ks1_8_score + ks1_9_score + ks1_10_score)/3), 2)

        rpk_total_score = round(((ks1_11_score + ks1_12_score + ks1_13_score + ks1_14_score)/4), 2)

        aak_av_score = round(((compk_total_score + daok_total_score + rak_total_score + rpk_total_score)/4), 2)

        ks_avg_score = round((ks_total_score / 14), 2)
        return [ks_total_score, ks_avg_score, compk_total_score, daok_total_score, rak_total_score,
                rpk_total_score, aak_av_score]


class RegulatoryTotalScore:
    def __init__(self, input, request):
        self.input = input
        self.score = 0

    def rs1_1(self):
        self.score = 0
        if self.input.get('rs1_1') == '1':
            self.score = 1
        elif self.input.get('rs1_1') == '2':
            self.score = 2
        elif self.input.get('rs1_1') == '3':
            self.score = 3
        elif self.input.get('rs1_1') == '4':
            self.score = 4
        return self.score

    def rs1_2(self):
        self.score = 0
        if self.input.get('rs1_2') == '1':
            self.score = 1
        elif self.input.get('rs1_2') == '2':
            self.score = 2
        elif self.input.get('rs1_2') == '3':
            self.score = 3
        elif self.input.get('rs1_2') == '4':
            self.score = 4
        return self.score

    def rs1_3(self):
        self.score = 0
        if self.input.get('rs1_3') == '1':
            self.score = 1
        elif self.input.get('rs1_3') == '2':
            self.score = 2
        elif self.input.get('rs1_3') == '3':
            self.score = 3
        elif self.input.get('rs1_3') == '4':
            self.score = 4
        return self.score

    def rs1_4(self):
        self.score = 0
        if self.input.get('rs1_4') == '1':
            self.score = 1
        elif self.input.get('rs1_4') == '2':
            self.score = 2
        elif self.input.get('rs1_4') == '3':
            self.score = 3
        elif self.input.get('rs1_4') == '4':
            self.score = 4
        return self.score

    def rs1_5(self):
        self.score = 0
        if self.input.get('rs1_5') == '1':
            self.score = 1
        elif self.input.get('rs1_5') == '2':
            self.score = 2
        elif self.input.get('rs1_5') == '3':
            self.score = 3
        elif self.input.get('rs1_5') == '4':
            self.score = 4
        return self.score

    def rs1_6(self):
        self.score = 0
        if self.input.get('rs1_6') == '1':
            self.score = 1
        elif self.input.get('rs1_6') == '2':
            self.score = 2
        elif self.input.get('rs1_6') == '3':
            self.score = 3
        elif self.input.get('rs1_6') == '4':
            self.score = 4
        return self.score

    def rs1_7(self):
        self.score = 0
        if self.input.get('rs1_7') == '1':
            self.score = 1
        elif self.input.get('rs1_7') == '2':
            self.score = 2
        elif self.input.get('rs1_7') == '3':
            self.score = 3
        elif self.input.get('rs1_7') == '4':
            self.score = 4
        return self.score

    def rs1_8(self):
        self.score = 0
        if self.input.get('rs1_8') == '1':
            self.score = 1
        elif self.input.get('rs1_8') == '2':
            self.score = 2
        elif self.input.get('rs1_8') == '3':
            self.score = 3
        elif self.input.get('rs1_8') == '4':
            self.score = 4
        return self.score

    def rs1_9(self):
        self.score = 0
        if self.input.get('rs1_9') == '1':
            self.score = 1
        elif self.input.get('rs1_9') == '2':
            self.score = 2
        elif self.input.get('rs1_9') == '3':
            self.score = 3
        elif self.input.get('rs1_9') == '4':
            self.score = 4
        return self.score

    def rs1_10(self):
        self.score = 0
        if self.input.get('rs1_10') == '1':
            self.score = 1
        elif self.input.get('rs1_10') == '2':
            self.score = 2
        elif self.input.get('rs1_10') == '3':
            self.score = 3
        elif self.input.get('rs1_10') == '4':
            self.score = 4
        return self.score

    def rs1_11(self):
        self.score = 0
        if self.input.get('rs1_11') == '1':
            self.score = 1
        elif self.input.get('rs1_11') == '2':
            self.score = 2
        elif self.input.get('rs1_11') == '3':
            self.score = 3
        elif self.input.get('rs1_11') == '4':
            self.score = 4
        return self.score

    def rs1_12(self):
        self.score = 0
        if self.input.get('rs1_12') == '1':
            self.score = 1
        elif self.input.get('rs1_12') == '2':
            self.score = 2
        elif self.input.get('rs1_12') == '3':
            self.score = 3
        elif self.input.get('rs1_12') == '4':
            self.score = 4
        return self.score

    def rs1_13(self):
        self.score = 0
        if self.input.get('rs1_13') == '1':
            self.score = 1
        elif self.input.get('rs1_13') == '2':
            self.score = 2
        elif self.input.get('rs1_13') == '3':
            self.score = 3
        elif self.input.get('rs1_13') == '4':
            self.score = 4
        return self.score

    def rs1_14(self):
        self.score = 0
        if self.input.get('rs1_14') == '1':
            self.score = 1
        elif self.input.get('rs1_14') == '2':
            self.score = 2
        elif self.input.get('rs1_14') == '3':
            self.score = 3
        elif self.input.get('rs1_14') == '4':
            self.score = 4
        return self.score

    def rs_all_score(self):
        rs1_1_score = self.rs1_1()
        rs1_2_score = self.rs1_2()
        rs1_3_score = self.rs1_3()
        rs1_4_score = self.rs1_4()
        rs1_5_score = self.rs1_5()
        rs1_6_score = self.rs1_6()
        rs1_7_score = self.rs1_7()
        rs1_8_score = self.rs1_8()
        rs1_9_score = self.rs1_9()
        rs1_10_score = self.rs1_10()
        rs1_11_score = self.rs1_11()
        rs1_12_score = self.rs1_12()
        rs1_13_score = self.rs1_13()
        rs1_14_score = self.rs1_14()

        rs_total_score = rs1_1_score + rs1_2_score + rs1_3_score + rs1_4_score + rs1_5_score \
                         + rs1_6_score + rs1_7_score + rs1_8_score + rs1_9_score + rs1_10_score \
                         + rs1_11_score + rs1_12_score + rs1_13_score + rs1_14_score

        compr_total_score = round(((rs1_1_score + rs1_2_score + rs1_3_score)/3), 2)

        cusr_total_score = round(((rs1_4_score + rs1_5_score + rs1_6_score + rs1_7_score)/4), 2)

        regr_total_score = round(((rs1_8_score + rs1_9_score + rs1_10_score + rs1_11_score + rs1_12_score)/5), 2)

        rar_total_score = round(((rs1_13_score + rs1_14_score)/2), 2)

        aar_av_score = round(((compr_total_score + cusr_total_score + regr_total_score + rar_total_score)/4), 2)

        rs_avg_score = round((rs_total_score/14), 2)
        return [rs_total_score, rs_avg_score, compr_total_score, cusr_total_score, regr_total_score, +
                rar_total_score, aar_av_score]


def final_score(request):
    if request.method == 'GET':
        avg_ass_score = request.session.get('aa_av_score')
        avg_aac_score = request.session.get('aac_av_score')
        avg_aak_score = request.session.get('aak_av_score')
        avg_aar_score = request.session.get('aar_av_score')
        total_avg = request.session.get('total_avg')

        assessment_portfolio = request.session.get('assessment_portfolio')
        if assessment_portfolio == '1':
            portfolio_screen = '1'
        else:
            portfolio_screen = '2'
        aa = '0'
        aac = '0'
        aak = '0'
        aar = '0'
        if avg_ass_score == 4:
            aa = '4'
        elif avg_ass_score >= 2.99:
            aa = '3'
        elif avg_ass_score >= 1.99:
            aa = '2'
        elif avg_ass_score >= 1:
            aa = '1'
        if avg_aac_score == 4:
            aac = '4'
        elif avg_aac_score >= 2.99:
            aac = '3'
        elif avg_aac_score >= 1.99:
            aac = '2'
        elif avg_aac_score >= 1:
            aac = '1'
        if avg_aak_score == 4:
            aak = '4'
        elif avg_aak_score >= 2.99:
            aak = '3'
        elif avg_aak_score >= 1.99:
            aak = '2'
        elif avg_aak_score >= 1:
            aak = '1'
        if avg_aar_score == 4:
            aar = '4'
        elif avg_aar_score >= 2.99:
            aar = '3'
        elif avg_aar_score >= 1.99:
            aar = '2'
        elif avg_aar_score >= 1:
            aar = '1'
        context = {
            'avg_ass_score': avg_ass_score,
            'avg_aac_score': avg_aac_score,
            'avg_aak_score': avg_aak_score,
            'avg_aar_score': avg_aar_score,
            'total_avg': total_avg,
            'aa': aa,
            'aac': aac,
            'aak': aak,
            'aar': aar,
            'portfolio_screen': portfolio_screen,
            # 'meter': meter,
        }
        return render(request, 'final_score.html', context)


def kyc_dashboard(request):
    return render(request, 'kyc_dashboard.html')


def spider1(request):
    dao_total_score = request.session.get('dao_total_score')
    ra_total_score = request.session.get('ra_total_score')
    rp_total_score = request.session.get('rp_total_score')
    comp_total_score = request.session.get('comp_total_score')
    aa_av_score = request.session.get('aa_av_score')

    plot1_score = (str(aa_av_score) + '/4')

    labels = ['Risk Assessment', 'DAO Support', 'Compliance', 'Risk Parameters']
    markers = [1, 2, 3, 4]
    stats = [ra_total_score, dao_total_score, comp_total_score, rp_total_score]

    labels = np.array(labels)
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    stats = np.concatenate((stats, [stats[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    if aa_av_score >= 3:
        ax.plot(angles, stats,  'o-', color='g', linewidth=2)
        ax.fill(angles, stats, color='g', alpha=0.25)
        plt.text(10, 0.8, plot1_score, fontsize=18, weight='bold', color='g')
    elif aa_av_score >= 2:
        ax.plot(angles, stats, 'o-', color='y', linewidth=2)
        ax.fill(angles, stats, color='y', alpha=0.25)
        plt.text(10, 0.8, plot1_score, fontsize=18, weight='bold', color='y')
    else:
        ax.plot(angles, stats,  'o-', color='r', linewidth=2)
        ax.fill(angles, stats, color='r', alpha=0.25)
        plt.text(10, 0.8, plot1_score, fontsize=18, weight='bold', color='r')
    ax.set_thetagrids(angles * 180 / np.pi, labels)
    plt.yticks(markers)
    ax.grid(True)

    fig.savefig("media/sample_1.png", dpi=100)


def spider2(request):
    daoc_total_score = request.session.get('daoc_total_score')
    rac_total_score = request.session.get('rac_total_score')
    rpc_total_score = request.session.get('rpc_total_score')
    compc_total_score = request.session.get('compc_total_score')

    labels = ['Risk Assessment', 'DAO Support', 'Compliance', 'Risk Parameters']
    markers = [1, 2, 3, 4]
    stats = [rac_total_score, daoc_total_score, compc_total_score, rpc_total_score]

    labels = np.array(labels)
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    stats = np.concatenate((stats, [stats[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    aac_av_score = request.session.get('aac_av_score')
    plot2_score = (str(aac_av_score) + '/4')
    if aac_av_score >= 3:
        ax.plot(angles, stats, 'o-', color='g', linewidth=2)
        ax.fill(angles, stats, color='g', alpha=0.25)
        plt.text(10, 0.8, plot2_score, fontsize=18, weight='bold', color='g')
    elif aac_av_score >= 2:
        ax.plot(angles, stats, 'o-', color='y', linewidth=2)
        ax.fill(angles, stats, color='y', alpha=0.25)
        plt.text(10, 0.8, plot2_score, fontsize=18, weight='bold', color='y')
    else:
        ax.plot(angles, stats, 'o-', color='r', linewidth=2)
        ax.fill(angles, stats, color='r', alpha=0.25)
        plt.text(10, 0.8, plot2_score, fontsize=18, weight='bold', color='r')
    ax.set_thetagrids(angles * 180 / np.pi, labels)
    plt.yticks(markers)
    ax.grid(True)

    fig.savefig("media/sample_2.png", dpi=100)


def spider3(request):
    daok_total_score = request.session.get('daok_total_score')
    rak_total_score = request.session.get('rak_total_score')
    rpk_total_score = request.session.get('rpk_total_score')
    compk_total_score = request.session.get('compk_total_score')

    labels = ['Risk Assessment', 'DAO Support', 'Compliance', 'Risk Parameters']
    markers = [1, 2, 3, 4]
    stats = [rak_total_score, daok_total_score, compk_total_score, rpk_total_score]

    labels = np.array(labels)
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    stats = np.concatenate((stats, [stats[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    aak_av_score = request.session.get('aak_av_score')
    plot3_score = (str(aak_av_score) + '/4')
    if aak_av_score >= 3:
        ax.plot(angles, stats, 'o-', color='g', linewidth=2)
        ax.fill(angles, stats, color='g', alpha=0.25)
        plt.text(10, 0.8, plot3_score, fontsize=18, weight='bold', color='g')
    elif aak_av_score >= 2:
        ax.plot(angles, stats, 'o-', color='y', linewidth=2)
        ax.fill(angles, stats, color='y', alpha=0.25)
        plt.text(10, 0.8, plot3_score, fontsize=18, weight='bold', color='y')
    else:
        ax.plot(angles, stats, 'o-', color='r', linewidth=2)
        ax.fill(angles, stats, color='r', alpha=0.25)
        plt.text(10, 0.8, plot3_score, fontsize=18, weight='bold', color='r')
    ax.set_thetagrids(angles * 180 / np.pi, labels)
    plt.yticks(markers)
    ax.grid(True)

    fig.savefig("media/sample_3.png", dpi=100)

def spider4(request):
    compr_total_score = request.session.get('compr_total_score')
    cusr_total_score = request.session.get('cusr_total_score')
    regr_total_score = request.session.get('regr_total_score')
    rar_total_score = request.session.get('rar_total_score')

    labels = ['Risk Assessment', 'Customer Review', 'Compliance', 'Regulatory Reporting']
    markers = [1, 2, 3, 4]
    stats = [rar_total_score, cusr_total_score, compr_total_score, regr_total_score]

    labels = np.array(labels)
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
    stats = np.concatenate((stats, [stats[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    aar_av_score = request.session.get('aar_av_score')
    plot4_score = (str(aar_av_score) + '/4')
    if aar_av_score >= 3:
        ax.plot(angles, stats, 'o-', color='g', linewidth=2)
        ax.fill(angles, stats, color='g', alpha=0.25)
        plt.text(10, 0.8, plot4_score, fontsize=18, weight='bold', color='g')
    elif aar_av_score >= 2:
        ax.plot(angles, stats, 'o-', color='y', linewidth=2)
        ax.fill(angles, stats, color='y', alpha=0.25)
        plt.text(10, 0.8, plot4_score, fontsize=18, weight='bold', color='y')
    else:
        ax.plot(angles, stats, 'o-', color='r', linewidth=2)
        ax.fill(angles, stats, color='r', alpha=0.25)
        plt.text(10, 0.8, plot4_score, fontsize=18, weight='bold', color='r')
    ax.set_thetagrids(angles * 180 / np.pi, labels)
    plt.yticks(markers)
    ax.grid(True)

    fig.savefig("media/sample_4.png", dpi=100)


def temp(request):
    return render(request, 'temp.html')
