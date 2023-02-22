fname = 'summary.json'; 
fid = fopen(fname); 
raw = fread(fid,inf); 
str = char(raw'); 
fclose(fid); 
val = jsondecode(str);

subs = {[1, size(val,1)]};
for j = 1:size(val,1)
    s = struct('id',val(j).ID,'raw',val(j).raw,'conditions',val(j).conditions,'evolution',val(j).evolution);
    subs{1,j}=s;
end
