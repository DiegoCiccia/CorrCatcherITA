# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:26:29 2020

@author: 39380
"""
import tkinter as tk
import pandas as pd

window=tk.Tk()
window.geometry("400x100")
window.title("Corrispettivi AdE")
window.configure(background='#49A')


def corr():
    file=open("CORR.txt").read()
    dict={}
    partitaiva=[]
    date=[]
    imponibtot22=[]
    impostot22=[]
    giotot22=[]
    imponibtot10=[]
    impostot10=[]
    giotot10=[]
    imponibtot4=[]
    impostot4=[]
    giotot4=[]
    void=[]
    tottot=[]
    
    
    filez=file.split("#")
    for item in filez:
      text=item.split()
      tot=0
      
      
      for word in text:
        if word == "il":
          ind=text.index("il")+1
          date.append(str(text[ind]))
          
      for word in text:
        if word == "partita":
          ind2=text.index("partita")+2
          partitaiva.append(text[ind2])
          
      
          
      if "22.00" in text or "10.00" in text or "4.00" in text:
        try:
          ind=text.index("22.00")
          whole=text[ind:ind+6]                   
          
          imponibile=whole[2]
          impon2=imponibile[-3:].replace(",", ".")
          impon1=imponibile[:-3].replace(".", "")
          imponibile=float(impon1+impon2)
          
          imposta=whole[4]
          impos2=imposta[-3:].replace(",", ".")
          impos1=imposta[:-3].replace(".", "")
          imposta=float(impos1+impos2)
          
          totday=str(imponibile+imposta)
          
          imponibtot22.append(imponibile)
          impostot22.append(imposta)
          giotot22.append(totday)
          tot=tot+float(totday)
          
          
        except:
          pass
      
        try:
          ind=text.index("10.00")
          whole=text[ind:ind+6]
                    
          imponibile=whole[2]
          impon2=imponibile[-3:].replace(",", ".")
          impon1=imponibile[:-3].replace(".", "")
          imponibile=float(impon1+impon2)
          
          imposta=whole[4]
          impos2=imposta[-3:].replace(",", ".")
          impos1=imposta[:-3].replace(".", "")
          imposta=float(impos1+impos2)
          
          totday=str(imponibile+imposta)
          
          imponibtot10.append(imponibile)
          impostot10.append(imposta)
          giotot10.append(totday)
          tot=tot+float(totday)
          
        except:
          pass
      
        try:
          ind=text.index("4.00")
          whole=text[ind:ind+6]
          
          imponibile=whole[2]
          impon2=imponibile[-3:].replace(",", ".")
          impon1=imponibile[:-3].replace(".", "")
          imponibile=float(impon1+impon2)
          
          imposta=whole[4]
          impos2=imposta[-3:].replace(",", ".")
          impos1=imposta[:-3].replace(".", "")
          imposta=float(impos1+impos2)
          
          totday=str(imponibile+imposta)
          
          imponibtot4.append(imponibile)
          impostot4.append(imposta)
          giotot4.append(totday)
          tot=tot+float(totday)
          
          
        except:
          pass
      
       
        tottot.append(tot)
        
    dict["P.I C.F."]=partitaiva
    dict["Data"]=date
    if len(imponibtot22)>0:
        dict["Impb 22%"]=imponibtot22
        dict["Iva 22%"]=impostot22
        dict["Tot 22%"]=giotot22
    else:
        for n in range(len(partitaiva)):
            void.append(0)
        dict["Impb 22%"]=void
        dict["Iva 22%"]=void
        dict["Tot 22%"]=void
        void=[]
    
    if len(imponibtot10)>0:        
        dict["Impb 10%"]=imponibtot10
        dict["Iva 10%"]=impostot10
        dict["Tot 10%"]=giotot10
    else:
        for n in range(len(partitaiva)):
            void.append(0)
        dict["Impb 10%"]=void
        dict["Iva 10%"]=void
        dict["Tot 10%"]=void
        void=[]
        
    if len(imponibtot4)>0:        
        dict["Impb 4%"]=imponibtot4
        dict["Iva 4%"]=impostot4
        dict["Tot 4%"]=giotot4
    else:
        for n in range(len(partitaiva)):
            void.append(0)
        dict["Impb 4%"]=void
        dict["Iva 4%"]=void
        dict["Tot 4%"]=void
        void=[]
    dict["Tot"]=tottot
    
        
    frame=pd.DataFrame(dict, columns=["P.I C.F.", "Data","Impb 22%","Iva 22%", "Tot 22%", "Impb 10%", "Iva 10%","Tot 10%", "Impb 4%", "Iva 4%","Tot 4%", "Tot"])
    frame.to_csv("out.csv", index= False)
    
    
    text="File out.csv creato/aggiornato"
    text_ou=tk.Label(window, text=text,fg="red")
    text_ou.grid(row=4, column=2)
    
tk.Button(window, text='Stampa Elenco Corrispettivi ed Aliquote', command=corr).grid(row=0,column=2,sticky=tk.W, pady=4)

if __name__ == '__main__':
    window.mainloop()
