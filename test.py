# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 14:33:50 2016

@author: mukkamala
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 23:51:51 2016

@author: mukkamala
"""
 
from decimal import *

f1 = raw_input("Enter a file:  ")
filename = f1 + ".pdb"
fileObject = open(filename,"r")
outfile = open("output.pdb","w+")
fileObject.readline()


words=['CA','C','H','O','N']
chain={}

def sidechain():
    for line in fileObject:
        string = line.split()
        if string[0]=="ATOM":
            if f1=='1aky' :
                if len(string[2])> 4:
                    temp = string[2]
                    string[2]= string[2][0:4]
                    string.insert(3,temp[4:])
                    #print string
                if len(string[9])> 4:
                    temp = string[9]
                    string[9]= string[9][0:5]
                    string.insert(10,temp[5:])
            if f1=='1s04' :
                #print string
                if len(string[2])== 4:
                    #print "asfafs"
                    temp = string[2]
                    string[2]= string[2][0:4]
                    # string.insert(3,temp[4:])
                    #print string
                    
            else:
                if len(string[2])> 3:
                    temp = string[2]
                    string[2]= string[2][0:3]
                    string.insert(3,temp[3:])
                    #print "asfasf"
            #print string

                    #print string
            # if len(string[6])> 6:
            #     temp = string[6]
            #     string[6]= string[6][0:6]
            #     string.insert(7,temp[6:])
            # if len(string[9])> 4:
            #     temp = string[9]
            #     string[9]= string[9][0:5]
            #     string.insert(10,temp[5:])


            #print string
            if string[2] not in words:
                #print string
                if int(string[5]) in chain.keys():
                    x=float(chain[int(string[5])][6])
                    y=float(chain[int(string[5])][7])
                    z=float(chain[int(string[5])][8])
                    #print string
                    #print string[6]
                    #print string[7]
                    chain[int(string[5])]=[string[0],string[1],string[2],string[3],string[4],string[5],x+float(string[6]),y+float(string[7]),z+float(string[8]),string[9],float(chain[int(string[5])][10])+float(string[10]),string[11],chain[int(string[5])][12]+1]
                else:
                    #print string
                    chain[int(string[5])]=[string[0],string[1],string[2],string[3],string[4],string[5],float(string[6]),float(string[7]),float(string[8]),string[9],float(string[10]),string[11],1]
    
    
    c=1
    for key in chain.keys():
    	count=chain[key][12]
    	a=chain[key][5]
    	x=round(float(chain[key][6])/count,3)
    	y=round(float(chain[key][7])/count,3)
    	z=round(float(chain[key][8])/count,3)
    	val=round(chain[key][10]/count,2)
    	outfile.write( "ATOM"+(6-len(str(c)))*" "+str(c)+"  S   "+str(chain[key][3])+" "+str(chain[key][4])+(4-len(str(a)))*" "+str(a)+(12-len(str(x)))*" "+str(x)+(8-len(str(y)))*" "+str(y)+(8-len(str(z)))*" "+str(z)+"  1.00 "+str(val)+(16-len(str(val)))*" "+"C"+"\n")
    	c +=1
        
    fileObject.close()



def helix1():
    values={}
    keys=[]
    helix={}
    a=1
    f=open(filename,'r')
    f1=open("output2.pdb",'wb')
    for line in f:
        line=line.split()
        if "HELIX"==line[0]:
            helix[int(line[1])]=[int(line[5]),int(line[8])]
    ##
    f.close()
    f=open(filename,'r')
    for line in f:
        line=line.split()
        if "ATOM"==line[0] and line[2]=="CA" :#and (int(line[5]) in range(helix[h][0],helix[h][1]+4)) :
            # if f1 == '2p8y':
            #     if len(line[7])> 6:
            #         temp = line[7]
            #         line[7]= line[7][0:6]
            #         line.insert(8,temp[6:])
            #     if len(line[8])> 6:
            #         temp = line[8]
            #         line[8]= line[8][0:6]
            #         line.insert(9,temp[6:])
            if int(line[5]) not  in values:#range(helix[h][0],helix[h][1]+1):
                keys.append(int(line[5]))
                values[int(line[5])]=line

    # for h in helix.keys():
    #     for line in f:
    #         line=line.split()
    #         if "ATOM"==line[0] and line[2]=="CA" and (int(line[5]) in range(helix[h][0],helix[h][1]+4)) :
    #             if int(line[5]) in range(helix[h][0],helix[h][1]+1):
    #                 keys.append(int(line[5]))
    #             values[int(line[5])]=line
    #   #f=open(filename,'r')
    #print values.keys()
    for h in helix.keys():
        #print helixMap[h]
        for key in keys:
            if key in range(helix[h][0],helix[h][1]-2):
                ch=0
                if key in values.keys():
                    valx1=float(values[key][6])
                    valy1=float(values[key][7])
                    valz1=float(values[key][8])
                    valr1=float(values[key][10])
                    ch +=1
                else:
                    valx1=0
                    valy1=0
                    valz1=0
                    valr1=0
                    
                if key+1 in values.keys():
                    valx2=float(values[key+1][6])
                    valy2=float(values[key+1][7])
                    valz2=float(values[key+1][8])
                    valr2=float(values[key+1][10])
                    ch +=1
                else:
                    valx2=0
                    valy2=0
                    valz2=0
                    valr2=0
                    
                if key+2 in values.keys():
                    valx3=float(values[key+2][6])
                    valy3=float(values[key+2][7])
                    valz3=float(values[key+2][8])
                    valr3=float(values[key+2][10])
                    ch +=1
                else:
                    valx3=0
                    valy3=0
                    valz3=0
                    valr3=0
                    
                if key+4 in values.keys():
                    valx4=float(values[key+3][6])
                    valy4=float(values[key+3][7])
                    valz4=float(values[key+3][8])
                    valr4=float(values[key+3][10])
                    ch +=1
                else:
                    valx4=0
                    valy4=0
                    valz4=0
                    valr4=0
                    
                #print key,str(valx1+valx2+valx3+valx4/ch),str(valy1+valy2+valy3+valy4/ch),str(valz1+valz2+valz3+valz4/ch),str(valr1+valr2+valr3+valr4/ch)
                x=str(round(Decimal((valx1+valx2+valx3+valx4)/ch),3))
                y=str(round(Decimal((valy1+valy2+valy3+valy4)/ch),3))
                z=str(round(Decimal((valz1+valz2+valz3+valz4)/ch),3))
                k=str(round(Decimal((valr1+valr2+valr3+valr4)/ch),3))
                        #print "fghgvh"
                f1.write("ATOM"+(6-len(str(a)))*" "+str(a)+"  S   "+str(values[key][3])+" "+values[key][4]+(4-len(str(key)))*" "+str(key)+(12-len(x))*" "+x+(8-len(y))*" "+y+(8-len(z))*" "+z+"  1.00 "+str(k)+(16-len(str(k)))*" "+"S"+"\n")
                a+=1
    f.close()
    f1.close()

def betasheet():
    sheet={}
    keys=[]
    values={}
    a=1
    f=open(filename,'r')
    f1=open("output3.pdb",'wb')
    a=1
    for line in f:
        line=line.split()
        #print line

        if "SHEET"==line[0] :
            sheet[a]=[int(line[6]),int(line[9])]
            a+=1
    ##
    f.close()
    f=open(filename,'r')
    for line in f:
        line=line.split()
        if "ATOM"==line[0] and (line[2]=="CA" or line[2]=="N" or line[2]=="C"):
            if int(line[5]) not  in values:#range(helix[h][0],helix[h][1]+1):
                keys.append(int(line[5]))
                values[int(line[5])]=[]
                values[int(line[5])].append(line)
            else:
                values[int(line[5])].append(line)
    a=1
    #print values
    #print keys
    for s in sheet.keys():
        for key in keys:
            valx1=0
            valy1=0
            valz1=0
            valr1=0
            if key in range(sheet[s][0],sheet[s][1]+1):
                
                try:
                    if key in values.keys():
                        valx1=float(values[key][0][6])+float(values[key][1][6])+float(values[key][2][6])+float(values[key+1][0][6])
                        valy1=float(values[key][0][7])+float(values[key][1][7])+float(values[key][2][7])+float(values[key+1][0][7])
                        valz1=float(values[key][0][8])+float(values[key][1][8])+float(values[key][2][8])+float(values[key+1][0][8])
                        valr1=float(values[key][0][10])+float(values[key][1][10])+float(values[key][2][10])+float(values[key+1][0][10])
                        ch = 4 

                        x=str(round(Decimal((valx1)/ch),3))
                        y=str(round(Decimal((valy1)/ch),3))
                        z=str(round(Decimal((valz1)/ch),3))
                        k=str(round(Decimal((valr1)/ch),3))
                                #print "fghgvh"
                        f1.write("ATOM"+(6-len(str(a)))*" "+str(a)+"  S   "+str(values[key][0][3])+" "+values[key][0][4]+(4-len(str(key)))*" "+str(key)+(12-len(x))*" "+x+(8-len(y))*" "+y+(8-len(z))*" "+z+"  1.00 "+str(k)+(16-len(str(k)))*" "+"S"+"\n")
                        a+=1
                except:
                    afsadaf=1
    f.close()
    f1.close()
        
                    







            



    

sidechain()
helix1()
betasheet()
                    
                    
                
            
            
    
    
    


   
   