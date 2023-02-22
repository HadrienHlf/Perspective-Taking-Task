cyou=0;
iyou=0;
cthem=0;
ithem=0;
count=0;

for i=1:size(subs,2)
    if (subs{1,i}.id>30000)
        cyou=(getfield_list(subs,'conditions.TrueConsistentYouTrials.rt')+getfield_list(subs,'conditions.FalseConsistentYouTrials.rt'))/2;
        iyou=(getfield_list(subs,'conditions.TrueInconsistentYouTrials.rt')+getfield_list(subs,'conditions.FalseInconsistentYouTrials.rt'))/2;
        cthem=(getfield_list(subs,'conditions.TrueConsistentThemTrials.rt')+getfield_list(subs,'conditions.FalseConsistentThemTrials.rt'))/2;
        ithem=(getfield_list(subs,'conditions.TrueInconsistentThemTrials.rt')+getfield_list(subs,'conditions.FalseInconsistentThemTrials.rt'))/2;
        count=count+1;
    end
end

m_cyou=mean(cyou);
m_iyou=mean(iyou);
m_cthem=mean(cthem);
m_ithem=mean(ithem);

altolist=iyou-cyou;
egolist=ithem-cthem;

altomean=mean(altolist)
alosd=std(altolist)
egomean=mean(egolist)
egosd=std(egolist)

altocentric = m_iyou-m_cyou;
egocentric = m_ithem-m_cthem;
x = ['Inconsistent You','Consistent You','Inconsistent Them','Consistent Them',];
y = [cyou iyou; cthem ithem];
bar(y)
allscales=getfield_list(subs,'scales.allscales');
allscales = cat(1,allscales{:});

%
%[r, p] = corr((cyou+cthem+iyou+ithem)'/4, allscales{:,:},'rows','pairwise')
%nicecorrplot((cyou+cthem+iyou+ithem)'/4, allscales.barratt_motor, {'rt','impulsivity'})
