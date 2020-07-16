from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from django.contrib import messages


def Login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        verification = request.POST['verification']

        user = auth.authenticate(username=username, password=password)

    

        if user is not None:
            if verification==('SGM_STU_001'):
                return redirect('mainpage/stu')

            elif verification==('SVT_STU_002'):
                return redirect('mainpage/stu')

            elif verification==('SVT_STU_002'):
                return redirect('mainpage/stu')

            elif verification==('ADH_STU_003'):
                return redirect('mainpage/stu')

            elif verification==('BJR_STU_004'):
                return redirect('mainpage/stu')

            elif verification==('RSM_STU_005'):
                return redirect('mainpage/stu')

            elif verification==('SRK_STU_006'):
                return redirect('mainpage/stu')

            elif verification==('PDU_STU_007'):
                return redirect('mainpage/stu')

            elif verification==('KRJ_STU_008'):
                return redirect('mainpage/stu')

            elif verification==('SGM_TEA_121'):
                return redirect('mainpage/tea')

            elif verification==('SVT_TEA_422'):
                return redirect('mainpage/tea')

            elif verification==('ADH_TEA_423'):
                return redirect('mainpage/tea')

            elif verification==('BJR_TEA_124'):
                return redirect('mainpage/tea')

            elif verification==('RSM_TEA_668'):
                return redirect('mainpage/tea')

            elif verification==('SRK_TEA_328'):
                return redirect('mainpage/tea')

            elif verification==('PDU_TEA_661'):
                return redirect('mainpage/tea')

            elif verification==('KRJ_TEA_100'):
                return redirect('mainpage/tea')

            elif verification==('ITEACH_SAW_343'):
                return redirect('mainpage/tea')

            elif verification==('ITEACH_ALC_343'):
                return redirect('mainpage/tea')
  
            else:
                messages.error(request, 'check verification code again')
                return redirect('login')

            auth.login(request, user)
            messages.info(request, 'done')

        else:
            messages.info(request, 'User does not exists...')
            return redirect('mainpage/stu')


    else:
        messages.info(request, 'check info...')
    return render(request, 'login.html')





def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        verification = request.POST['verification']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken...')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken...')
                return redirect('register')
                

            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                messages.success(request, 'user created')


                if verification==('SGM_STU_001'):
                    return redirect('mainpage/stu')

                elif verification==('SVT_STU_002'):
                    return redirect('mainpage/stu')

                elif verification==('ADH_STU_003'):
                    return redirect('mainpage/stu')

                elif verification==('BJR_STU_004'):
                    return redirect('mainpage/stu')

                elif verification==('RSM_STU_005'):
                    return redirect('mainpage/stu')

                elif verification==('SRK_STU_006'):
                    return redirect('mainpage/stu')

                elif verification==('PDU_STU_007'):
                    return redirect('mainpage/stu')

                elif verification==('KRJ_STU_008'):
                    return redirect('mainpage/stu')

                elif verification==('SGM_TEA_121'):
                    return redirect('mainpage/tea')

                elif verification==('SVT_TEA_422'):
                    return redirect('mainpage/tea')

                elif verification==('ADH_TEA_423'):
                    return redirect('mainpage/tea')

                elif verification==('BJR_TEA_124'):
                    return redirect('mainpage/tea')

                elif verification==('RSM_TEA_668'):
                    return redirect('mainpage/tea')

                elif verification==('SRK_TEA_328'):
                    return redirect('mainpage/tea')

                elif verification==('PDU_TEA_661'):
                    return redirect('mainpage/tea')

                elif verification==('KRJ_TEA_100'):
                    return redirect('mainpage/tea')

                elif verification==('ITEACH_SAW_343'):
                    return redirect('mainpage/tea')

                elif verification==('ITEACH_ALC_343'):
                    return redirect('mainpage/tea')
  
                else:
                    messages.error(request, 'check verification code again')
                    return redirect('register')

            return redirect('mainpage/stu')
        else:
            messages.error(request, 'Password did not match')
            return redirect('register')
                       
            
    else:
        messages.error(request, 'check your full form again...')
        
    return render(request, 'Registration.html')


def logout(request):
    auth.logout(request)
    return redirect('login')



    
    

            
                
           

           
            
            
                    

 

    