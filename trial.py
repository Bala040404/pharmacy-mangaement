from tkinter import *

from module_contaning_med_dict import *

def absence_med():
    #label indicating the absence of medicine
    absence_label=Label(root,text="sorry "+e_med.get()+" not available")
    absence_label.grid()

def absence_quan():
    #label indicating the absence of medicine
    absence_label=Label(root,text="sorry the asked quantity not available")
    absence_label.grid()





def ok_med():
    
    
    
    def ok_quan():
        if int(e_quan.get())>med_dict[e_med.get()][1]:
            absence_quan()

        else:
            before_label=Label(root,text="available "+e_med.get()+" = "+str(med_dict[e_med.get()][1]))
            before_label.grid()
            med_dict[e_med.get()][1]-=int(e_quan.get())
            after_label=Label(root,text="available "+e_med.get()+" = "+str(med_dict[e_med.get()][1]))
            after_label.grid()
        
    
    
    
    
    
    
    
    
    #if the name enter by the user exsists then we enquire about the quantity
    if (e_med.get() in med_dict.keys()):
        #label asking the user for the quantity
        quan_label=Label(root,text="the quantity",bg="grey",fg="red")
        quan_label.grid()

        #entry box to get the quantity
        e_quan=Entry(root,bg="black",fg="white")
        e_quan.grid()

        #once the user clicks ok after typing the quantity of the med,ok_quan function is called
        ok_quan_but=Button(root,text="ok",command=ok_quan)
        ok_quan_but.grid()





    else:
        #we call absence is the med is not present
        absence_med()


root=Tk()

#heading label
h_l=Label(root,text="PHARMACY MANAGEMENT SYSTEM",bg="grey",fg="cyan")
h_l.grid()

#label asking the user to enter the name of the medicine
input_label=Label(root,text="The name of the medicine you want ",bg="grey",fg="red")
input_label.grid()

#entry box to get the medicine
e_med=Entry(root,bg="black",fg="white")
e_med.grid()

#once the user clicks ok after typing the name of the med,ok_med function is called
ok_med_but=Button(root,text="ok",command=ok_med)
ok_med_but.grid()










root.mainloop()