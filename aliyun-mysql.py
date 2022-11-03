#coding:utf8
import sys,os

arg=sys.argv[1];

x=['q','a','z','w','s','x','c','d','e','r','f','v','b','g','t','y','h','n','m','j','u','i','k','l','o','p','1','2','3','4','5','6','7','8','9','0'];
y=[];
for z in x:
    for i in x:
        y.append(z+i);
for o in y:
    a =arg.split('.')[0]+o+'.mysql.rds.aliyuncs.com';
    os.system("ping "+a+" -n 1");
