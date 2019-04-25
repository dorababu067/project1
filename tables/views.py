import pandas as pd
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.contrib.auth import authenticate,login
from . forms import UserRegistrationForm

df = pd.read_csv('department.csv')

# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['pwd']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(first_table)
    else:
        return render(request,'login.html')

def create_user_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect(index)
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'user_creation.html', context)
    

#first table operations
def first_table(request):
    mans = []
    tems = []
    fs = []
    ls = []
    flg = []
    fsm = []
    nmax=[]
    nmin=[]
    tot = []
    if request.method == "POST":
        #request.POST.get()
        dept = request.POST['department']
        print(dept)
        nlarge = request.POST['nlarge']
        nsmall = request.POST['nsmall']
        select_dp = df[df['Department']== dept]
        # print(select_dp)
        managers =  select_dp.iloc[:,2]
        # print(managers)
        teams   =  select_dp.iloc[:,1]
        for man,tem,first,last,large,small,total in zip(managers.head(10),
                            teams,select_dp['1'].head(10),
                            select_dp['50'].head(10),
                            select_dp.max(axis=1,skipna=True),
                            select_dp.min(axis=1,skipna=True),
                            select_dp.sum(axis=1,skipna=True)):
            mans.append(man)
            tems.append(tem)
            fs.append(first)
            ls.append(last)	
            tot.append(total)
            flg.append(large)
            fsm.append(small)

        selected =  select_dp.iloc[:,3:]
        # print(selected)
        selected_max = []
        selected_min = []
        for row in selected.values:
            temp = sorted(list(row),reverse=True)
            temp1 = sorted(list(row))
            nmax.append(temp)
            nmin.append(temp1)
        for max,min in zip(nmax,nmin):
           selected_max.append(max[int(nlarge)-1])
           selected_min.append(min[int(nsmall)-1])
        # print(selected_max)
        # print(selected_min)
        zip_obj = zip( mans,tems,fs,ls,flg,selected_max,fsm,selected_min,tot)
        data = []
        for m,t,fs,ls,mx,nmx,sm,nsm,tot  in zip_obj:
            dictionary = {}
            dictionary['manager']= t
            dictionary['team']  = m
            dictionary['first']= fs
            dictionary['last']= ls
            dictionary['large']= mx
            dictionary['nlarge'] = nmx
            dictionary['small']= sm
            dictionary['nsmall'] = nsm
            dictionary['sum']= tot
            data.append(dictionary)
        # print(data)
        staticdata = []
        static_obj = zip(df.Manager.head(10),df.Team.head(10),df['1'].head(10),df['50'].head(10),df.max(axis=1,skipna=True).head(10),df.min(axis=1,skipna=True).head(10),df.sum(axis=1,skipna=True).head(10))
        for m,t,fs,ls,mx,sm,tot  in static_obj:
            dictionary = {}
            dictionary['manager']=m
            dictionary['team']  = t
            dictionary['first']= fs
            dictionary['last']= ls
            dictionary['large']= mx
            dictionary['nlarge'] = mx
            dictionary['small']= sm
            dictionary['nsmall'] = sm
            dictionary['sum']= tot
            staticdata.append(dictionary)
        # print(staticdata)
        contex = {
            "data" : data,
            "static_data" : staticdata ,
            "dept" : dept,
            "nlarge" : nlarge,
            "nsmall" : nsmall,       
            }
        return render(request,'tables_body1.html',contex)

    contex = {
        "departments": zip(
                df.Manager.head(10),
                df.Team.head(10),
                df['1'].head(10),
                df['50'].head(10),
                df.max(axis=1,skipna=True).head(10),
                df.min(axis=1,skipna=True).head(10),
                df.sum(axis=1,skipna=True).head(10),
            ),
        "departments1": zip(
                df.Manager.head(10),
                df.Team.head(10),
                df['1'].head(10),
                df['50'].head(10),
                df.max(axis=1,skipna=True).head(10),
                df.min(axis=1,skipna=True).head(10),
                df.sum(axis=1,skipna=True).head(10),
            )
                
        }
    return render(request,'tables_body.html',contex)


def second_table(request):
    mans = []
    tems = []
    fs = []
    ls = []
    flg = []
    fsm = []
    nmax=[]
    nmin=[]
    tot = []
    if request.method == "POST":
        dept = request.POST['department']
        print(dept)
        nlarge = request.POST['nlarge']
        nsmall = request.POST['nsmall']
        select_dp = df[df['Department']== dept]
        # print(select_dp)
        managers =  select_dp.iloc[:,2]
        # print(managers)
        teams   =  select_dp.iloc[:,1]
        for man,tem,first,last,large,small,total in zip(managers.head(10),
                            teams,select_dp['1'].head(10),
                            select_dp['50'].head(10),
                            select_dp.max(axis=1,skipna=True),
                            select_dp.min(axis=1,skipna=True),
                            select_dp.sum(axis=1,skipna=True)):
            mans.append(man)
            tems.append(tem)
            fs.append(first)
            ls.append(last)	
            tot.append(total)
            flg.append(large)
            fsm.append(small)

        selected =  select_dp.iloc[:,3:]
        # print(selected)
        selected_max = []
        selected_min = []
        for row in selected.values:
            temp = sorted(list(row),reverse=True)
            temp1 = sorted(list(row))
            nmax.append(temp)
            nmin.append(temp1)
        for max,min in zip(nmax,nmin):
           selected_max.append(max[int(nlarge)-1])
           selected_min.append(min[int(nsmall)-1])
        # print(selected_max)
        # print(selected_min)
        zip_obj = zip( mans,tems,fs,ls,flg,selected_max,fsm,selected_min,tot)
        data = []
        for m,t,fs,ls,mx,nmx,sm,nsm,tot  in zip_obj:
            dictionary = {}
            dictionary['manager']= t
            dictionary['team']  = m
            dictionary['first']= fs
            dictionary['last']= ls
            dictionary['large']= mx
            dictionary['nlarge'] = nmx
            dictionary['small']= sm
            dictionary['nsmall'] = nsm
            dictionary['sum']= tot
            data.append(dictionary)
        # print(data)
        staticdata = []
        static_obj = zip(df.Manager.head(10),df.Team.head(10),df['1'].head(10),df['50'].head(10),df.max(axis=1,skipna=True).head(10),df.min(axis=1,skipna=True).head(10),df.sum(axis=1,skipna=True).head(10))
        for m,t,fs,ls,mx,sm,tot  in static_obj:
            dictionary = {}
            dictionary['manager']=m
            dictionary['team']  = t
            dictionary['first']= fs
            dictionary['last']= ls
            dictionary['large']= mx
            dictionary['nlarge'] = mx
            dictionary['small']= sm
            dictionary['nsmall'] = sm
            dictionary['sum']= tot
            staticdata.append(dictionary)
        # print(staticdata)
        contex = {
            "data" : data,
            "static_data" : staticdata,
            "dept" : dept,
            "nlarge" : nlarge,
            "nsmall" : nsmall,            
            }
        return render(request,'table_body2.html',contex)

    contex = {
        "departments": zip(
                df.Manager.head(10),
                df.Team.head(10),
                df['1'].head(10),
                df['50'].head(10),
                df.max(axis=1,skipna=True).head(10),
                df.min(axis=1,skipna=True).head(10),
                df.sum(axis=1,skipna=True).head(10),
            ),
        "departments1": zip(
                df.Manager.head(10),
                df.Team.head(10),
                df['1'].head(10),
                df['50'].head(10),
                df.max(axis=1,skipna=True).head(10),
                df.min(axis=1,skipna=True).head(10),
                df.sum(axis=1,skipna=True).head(10),
            )
                
        }
    return render(request,'tables_body.html',contex)











