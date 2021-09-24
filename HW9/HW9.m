%HW 9
p4data = xlsread('HW9Data.xlsx', 'Problem4');
p5data = xlsread('HW9Data.xlsx', 'Problem5');
p6data = xlsread('HW9Data.xlsx', 'Problem6');
fprintf('Problem 4:')
data = p4data(:,2:4);
[st4 ,plotdata4] = controlchart(data,'charttype',{'xbar' 's'}, 'rules', 'we2');
plotdata4.lcl
plotdata4.cl
plotdata4.ucl
R4 = controlrules('we2',st4.mean,st4.mu,st4.sigma./sqrt(st4.n));

figure();
fprintf('Problem 5:')
data = p5data(:,2:6);
[st5, plotdata5] = controlchart(data,'charttype',{'xbar' 's'}, 'rules', 'we2');
plotdata5.lcl
plotdata5.cl
plotdata5.ucl
R5 = controlrules('we2',st5.mean,st5.mu,st5.sigma./sqrt(st5.n));



figure();
fprintf('Problem 6:')
[st6, plotdata6] = controlchart(p6data(:,2),'charttype',{'i', 'mr'}, 'rules', 'we2');
plotdata6.lcl
plotdata6.cl
plotdata6.ucl
