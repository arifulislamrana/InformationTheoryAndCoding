clc;
clear;
x1=(0:000000.1:1);
x2=flip(x1);
res=[];
for n=1:1:length(x1)
    p1=-x1(n)*log2(x1(n));
    if isnan(p1) p1=0; 
    end
    
    p2=-x2(n)*log2(x2(n));
    if isnan(p2) p2=0; 
    end
    res=[res p1+p2];
end
disp(res)

plot(x1,res)
title('hello');
xlabel('P');
ylabel('H(P)');