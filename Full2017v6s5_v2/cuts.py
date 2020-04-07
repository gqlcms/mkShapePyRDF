# cuts

# cuts

cuts["supercut"] ={
    'expr': '( \
                 (   (abs(Lepton_pdgId[0])==11 && Lepton_pt[0]>38 ) \
                 || (abs(Lepton_pdgId[0])==13 && Lepton_pt[0]>30 ) ) \
                && vbs_0_pt > 50 && vbs_1_pt > 30 \
                && PuppiMET_pt > 30 \
                && deltaeta_vbs >= 2.5  \
                && mjj_vbs >= 500 \
                && Mtw_lep < 185 \
                && (abs(vbs_0_eta) <2.5 || abs(vbs_0_eta) > 3.2)\
                && (abs(vbs_1_eta) <2.5 || abs(vbs_1_eta) > 3.2)\
                && (abs(vjet_0_eta) <2.5 || abs(vjet_0_eta) > 3.2)\
                && (abs(vjet_1_eta) <2.5 || abs(vjet_1_eta) > 3.2)\
            )',
    'parent' : None,
    'doVars': False,
    'doNumpy': False
}
#########################################################################
###############|----------------------------------|######################
###############|          Resolved category       |######################
###############|----------------------------------|######################
#########################################################################

#####################################
##  W-onshell, bveto --> Signal

cuts["res_sig"] = {
    'expr': 'VBS_category==1 \
            && vjet_0_pt > 30 && vjet_1_pt > 30 \
            && mjj_vjet > 65 && mjj_vjet < 105 \
            && bVeto \
            && whad_pt < 200\
            ',
    'parent' : 'supercut',
    'doVars': True,
    'doNumpy': True
}


#########################################################################
###############|----------------------------------|######################
###############|          Boosted category        |######################
###############|----------------------------------|######################
#########################################################################

#####################################
##  W-onshell, bveto --> Signal

cuts["boos_sig"] = {
    'expr': 'VBS_category==0 \
            && vjet_0_pt > 200 \
            && mjj_vjet > 65 && mjj_vjet < 105 \
            && bVeto \
            ',
    'parent' : 'supercut',
    'doVars': True,
    'doNumpy': True
}