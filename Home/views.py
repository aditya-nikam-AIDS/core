from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from  django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import pandas as pd
from Election import *
# Create your views here.
def home(request):
    return render(request,"base.html")
#@login_required
def login_page(request):
    if request.method=="POST":
        user_name=request.POST.get("user_name")
        password=request.POST.get("password")
        if not User.objects.filter(username=user_name).exists():
            messages.error(request,"Invalid User Name")
            return redirect(request,"login.html")
            
        user=authenticate(username=user_name,password=password)#this method check user name and password that would be authenticated password is encrypted
        if user is None:
            messages.error(request,"Invalid Password")
        else:
            login(request,user)
            return redirect("/home_prediction/")
    return render(request,"login.html")

def register_page(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        user_name=request.POST.get("user_name")
        password=request.POST.get("password")
        user=User.objects.filter(username=user_name)
        if user.exists():
            messages.info(request,"User already exists with this name")
            return redirect("/register/")
        user=User.objects.create(first_name=first_name,
                            last_name=last_name,
                            username=user_name)
        user.set_password(password)
        user.save()
        messages.info(request,"Account Created Successfully")

        return redirect("/register/")
    return render(request,"register.html")
def log_out_page(request):
    logout(request)
    return redirect("/login/")
def home_prediction(request):
    return render(request,"prediction.html")
# def prediction(request):
#     if request.method=="POST":
#        state=request.POST.get("state")
#        UPA=request.POST.getlist("UPA[]")
#        NDA=request.POST.getlist("NDA[]")
#        if state =="Choose...":
#          messages.info(request,"state has not been selected")
#          return redirect("/prediction/")
#        else:
#            # Using a double backslash
#         election_state = "Election\\" + state + ".csv"
#         df=pd.read_csv(election_state,encoding="windows-1252")
#         print(state)
#         print(NDA)
#         print(UPA)
#         df['NDA']=0
#         df['INDIA']=0
#         print(df)
#         df.fillna(0,inplace=True)
#         for b in NDA:
#           df['NDA']=df['NDA']+df[b]
#         for a in UPA:
#           df['INDIA']=df['INDIA']+df[a]
#         print(df)
#         INDIA=0
#         NDA=0
#         for index,row in df.iterrows():
#                if row['INDIA']>row['NDA']:
#                 INDIA=INDIA+1
#                else:
#                 NDA=NDA+1
#         messages.info(request,"state has been selected")
#         return render(request,"result.html",{"d":[NDA,INDIA],"n":["NDA","INDIA"]})

#     return render(request,"prediction.html")

# def prediction(request):
#     if request.method=="POST":
#        state=request.POST.get("state")
#        UPA=request.POST.getlist("UPA[]")
#        NDA=request.POST.getlist("NDA[]")
#        if state =="Choose...":
#          messages.info(request,"state has not been selected")
#          return redirect("/prediction/")
#        else:
#            # Using a double backslash
#         swing={'BJP':-13,'INC':5,'JDS':5}
#         election_state = "Election\\" + state + ".csv"
#         df=pd.read_csv(election_state,encoding="windows-1252")
#         print(state)
#         print(NDA)
#         print(UPA)
#         df['NDA']=0
#         df['INDIA']=0
#         print(df)
#         df.fillna(0,inplace=True)
#         for b in NDA:
#           df['NDA']=df['NDA']+df[b]+((df[b]*(swing[b]))/100)
#         for a in UPA:
#           df['INDIA']=df['INDIA']+df[a]+((df[a]*(swing[a]))/100)
#         print(df)
#         INDIA=0
#         NDA=0
#         for index,row in df.iterrows():
#                if row['INDIA']>row['NDA']:
#                 INDIA=INDIA+1
#                else:
#                 NDA=NDA+1
#         messages.info(request,"state has been selected")
#         return render(request,"result.html",{"d":[NDA,INDIA],"n":["NDA","INDIA"]})

#     return render(request,"prediction.html")

# def prediction(request):
#     if request.method=="POST":
#        state=request.POST.get("state")
#        INDIA=request.POST.getlist("INDIA")
#        NDA=request.POST.getlist("NDA")
#        if state =="Choose...":
#          messages.info(request,"state has not been selected")
#          return redirect("/prediction/")
#        else:
#            # Using a double backslash
#         #swing={'BJP':-13,'INC':5,'JDS':5}
#         df1=pd.read_csv("Election/ALL_STATE.csv")
#         df1.fillna(0,inplace=True)
#         print(df1)
#         swing=df1.loc[df1["State"] == state]
#         print("Swing",swing)
#         election_state = "Election\\" + state + ".csv"
#         df=pd.read_csv(election_state,encoding="windows-1252")
#         print(state)
#         print(NDA)
#         print(INDIA)
#         df['NDA']=0
#         df['INDIA']=0
#         df.fillna(0,inplace=True)
#         print(df)
      
#         for b in NDA:
#             if b in df.columns:
#               t=int(swing.loc[:,b].values)
#               df['NDA']=df['NDA']+df[b]+((df[b]*(t))/100)
#         for a in INDIA:
#             if a in df.columns:
#               t=int(swing.loc[:,a].values)
#               df["INDIA"]=df["INDIA"]+df[a]+((df[a]*(t))/100)
#         print(df)
#         INDIA=0
#         NDA=0
#         for index,row in df.iterrows():
#                if row['INDIA']>row['NDA']:
#                 INDIA=INDIA+1
#                else:
#                 NDA=NDA+1
#         messages.info(request,"state has been selected")
#         return render(request,"result.html",{"d":[NDA,INDIA],"n":["NDA","INDIA"],"state":state})

#     return render(request,"prediction.html")
# def prediction(request):
#     if request.method=="POST":
#        state=request.POST.get("state")
#        INDIA=request.POST.getlist("INDIA")
#        NDA=request.POST.getlist("NDA")
#        if state =="Choose...":
#          messages.info(request,"state has not been selected")
#          return redirect("/prediction/")
#        else:
#            # Using a double backslash
#         #swing={'BJP':-13,'INC':5,'JDS':5}
#         df1=pd.read_csv("Election/ALL_STATE.csv")
#         df1.fillna(0,inplace=True)
#         print(df1)
#         swing=df1.loc[df1["State"] == state]
#         print("Swing",swing)
#         election_state = "Election\\" + state + ".csv"
#         df=pd.read_csv(election_state,encoding="windows-1252")
#         print(state)
#         print(NDA)
#         print(INDIA)
#         df['NDA']=0
#         df['INDIA']=0
#         df.fillna(0,inplace=True)
#         print(df)
      
#         for b in NDA:
#             if b in df.columns:
#               t=int(swing.loc[:,b].values)
#               df['NDA']=df['NDA']+df[b]+((df[b]*(t))/100)
#         for a in INDIA:
#             if a in df.columns:
#               t=int(swing.loc[:,a].values)
#               df["INDIA"]=df["INDIA"]+df[a]+((df[a]*(t))/100)
#         print(df)
       
#         assembly="Assembly\\" + state + ".csv"
#         state_assembly=pd.read_csv(assembly,encoding="windows-1252")
#         state_assembly.fillna(0,inplace=True)
#         state_assembly["NDA"]=0
#         state_assembly["INDIA"]=0
#         for p_n in state_assembly.columns:
#            if p_n in NDA:
#               state_assembly["NDA"]+=state_assembly[p_n]
#            if p_n in INDIA:
#               state_assembly["INDIA"]+=state_assembly[p_n]
#         print(state_assembly) 
#         NDA=0
#         INDIA=0 
#         for (index1,row1),(index2,row2) in zip(df.iterrows(),state_assembly.iterrows()):
#                if row1["NDA"]-row1["INDIA"]>50000 and row2["NDA"]>row2["INDIA"]:
#                 NDA=NDA+1
#                 print("1")
#                elif row1["INDIA"]-row1["NDA"]>50000 and row2["INDIA"]>row2["NDA"]:
#                 INDIA=INDIA+1
#                 print("2")
#                elif row2["INDIA"]>row2["NDA"]:
#                 INDIA=INDIA+1
#                 print("3")
#                else:
#                 NDA=NDA+1
#                 print("4")
#         messages.info(request,"state has been selected")
#         return render(request,"result.html",{"d":[NDA,INDIA],"n":["NDA","INDIA"],"state":state})

#     return render(request,"prediction.html")

def prediction(request):
    if request.method=="POST":
       state=request.POST.get("state")
       INDIA=request.POST.getlist("INDIA")
       NDA=request.POST.getlist("NDA")
       if state =="Choose...":
         messages.info(request,"state has not been selected")
         return redirect("/prediction/")
       else:
            df1=pd.read_csv("Election/ALL_STATE.csv")
            df1.fillna(0,inplace=True)
            print(df1)
            swing=df1.loc[df1["State"] == state]
            print("Swing",swing)
            election_state = "Election\\" + state + ".csv"
            state_name="Assembly\\"+state+".csv"
            loksabha=pd.read_csv(election_state,encoding="windows-1252")
            loksabha['NDA']=0
            loksabha['INDIA']=0
            loksabha.fillna(0,inplace=True)
            print(loksabha)
            for b in NDA:
                if b in loksabha.columns:
                   t=int(swing.loc[:,b].values)
                   loksabha['NDA']=loksabha['NDA']+loksabha[b]+((loksabha[b]*(t))/100)
            for a in INDIA:
                if a in loksabha.columns:
                    t=int(swing.loc[:,a].values)
                    loksabha["INDIA"]=loksabha["INDIA"]+loksabha[a]+((loksabha[a]*(t))/100)
            print(loksabha)
            state_assembly=pd.read_csv(state_name,encoding="windows-1252")
            state_assembly.fillna(0,inplace=True)
            print(state_assembly)
            state_assembly.drop(columns="Strong_Party",axis="columns",inplace=True)
            group_the_constituency=state_assembly.groupby("Constituency_Name")
            print(group_the_constituency)
            base=group_the_constituency.sum()
            base["NDA"]=0
            base["INDIA"]=0
            for a in base.columns:
                if a in NDA:
                    base["NDA"]+=base[a]
            for b in base.columns:
                if b in INDIA:
                    base["INDIA"]+=base[b]
            st_nda=base["NDA"].sum()
            st_india=base["INDIA"].sum()

            # Declaring the two variable India and NDa for counting their Seats
            NDA=0
            INDIA=0 
            #algorithm for Predicting the result
            for (index1,row1),(index2,row2) in zip(loksabha.iterrows(),base.iterrows()):
                if row1["NDA"]-row1["INDIA"]>50000 and row2["NDA"]>row2["INDIA"]:
                    NDA=NDA+1
                elif row1["INDIA"]-row1["NDA"]>50000 and row2["INDIA"]>row2["NDA"]:
                    INDIA=INDIA+1
                elif row2["INDIA"]>row2["NDA"]:
                    INDIA=INDIA+1
                else:
                    NDA=NDA+1
            return render(request,"result.html",{"d":[NDA,INDIA],"n":["NDA","INDIA"],"state":state,'a':[st_nda,st_india]})
    return render(request,"prediction.html")

