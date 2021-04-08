from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt, json

def index(request):
    if 'uuid' in request.session:
        return redirect ('/synth')
    else:
        return render(request, "login_and_registration.html")

def register(request):
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        hash_browns =  bcrypt.hashpw(request.POST['password_form'].encode(), bcrypt.gensalt()).decode()
        created_user = User.objects.create(
            username= request.POST['username_form'],
            email= request.POST['email_form'],
            password= hash_browns
        )
        print(created_user)
        print(created_user.password)
        request.session['uuid'] = created_user.id
        return redirect("/synth")

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        selected_user = User.objects.get(email=request.POST['log_email_form'])
        request.session['uuid'] = selected_user.id
    return redirect("/synth")

def logout(request):
    request.session.flush()
    return redirect('/')

def synth_page(request):
    if 'uuid' in request.session:
        if 'oscillator1' in request.session:
            user_id= request.session['uuid']
            context={
                'all_patches': Patch.objects.all(),
                'selected_user': User.objects.get(id=user_id),
                'oscillator1': request.session['oscillator1'],
                'octave1': request.session['octave1'],
                'attackGain1': request.session['attackGain1'],
                'attackDur1': request.session['attackDur1'],
                'decayDur1': request.session['decayDur1'],
                'sustainGain1': request.session['sustainGain1'],
                'sustainDur1': request.session['sustainDur1'],
                'release1': request.session['release1'],

                'oscillator2': request.session['oscillator2'],
                'octave2': request.session['octave2'],
                'attackGain2': request.session['attackGain2'],
                'attackDur2': request.session['attackDur2'],
                'decayDur2': request.session['decayDur2'],
                'sustainGain2': request.session['sustainGain2'],
                'sustainDur2': request.session['sustainDur2'],
                'release2': request.session['release2'],
            }
        else:
            user_id= request.session['uuid']
            context={
                'all_patches': Patch.objects.all(),
                'selected_user': User.objects.get(id=user_id),
                'oscillator1': 'sine',
                'octave1': 1,
                'attackGain1': 0.2,
                'attackDur1': 0.08,
                'decayDur1': 0.1,
                'sustainGain1': 0.6,
                'sustainDur1': 999,
                'release1': 0.1,

                'oscillator2': 'square',
                'octave2': 1,
                'attackGain2': 0.02,
                'attackDur2': 0.08,
                'decayDur2': 0.1,
                'sustainGain2': 0.6,
                'sustainDur2': 999,
                'release2': 0.1,
            }
        return render(request, "synth_page.html", context)
    else:
        return redirect("/")

def synth_update(request):
    print('loading body')
    data=json.loads(request.body)
    request.session['oscillator1'] = data["oscillator1Ajax"]
    request.session['octave1'] = data['octave1Ajax']
    request.session['attackGain1'] = data["attackGain1Ajax"]
    request.session['attackDur1'] = data["attackDur1Ajax"]
    request.session['decayDur1'] = data["decayDur1Ajax"]
    request.session['sustainGain1'] = data["sustainGain1Ajax"]
    request.session['sustainDur1'] = data["sustainDur1Ajax"]
    request.session['release1'] = data["release1Ajax"]
    request.session['oscillator2'] = data["oscillator2Ajax"]
    request.session['octave2'] = data['octave2Ajax']
    request.session['attackGain2'] = data["attackGain2Ajax"]
    request.session['attackDur2'] = data["attackDur2Ajax"]
    request.session['decayDur2'] = data["decayDur2Ajax"]
    request.session['sustainGain2'] = data["sustainGain2Ajax"]
    request.session['sustainDur2'] = data["sustainDur2Ajax"]
    request.session['release2'] = data["release2Ajax"]
    return redirect("/synth")

def create_patch(request):
    errors = User.objects.patch_validator(request.POST)
    if len(errors) > 0:
        print("\n".join(f'{k}: {v}' for k,v in errors.items()))
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/synth")
    else:
        user_id= request.session['uuid']
        created_patch= Patch.objects.create(
            patch_name= request.POST["patch_name_form"],
            uploaded_by = User.objects.get(id=user_id),
            oscillator1 = request.POST["oscillator1_form"],
            octave1= float(request.POST['octave1_form']),
            attackGain1= float(request.POST["attackGain1_form"]),
            attackDur1= float(request.POST["attackDur1_form"]),
            decayDur1= float(request.POST["decayDur1_form"]),
            sustainGain1= float(request.POST["sustainGain1_form"]),
            sustainDur1= float(request.POST["sustainDur1_form"]),
            release1= float(request.POST["release1_form"]),

            oscillator2= request.POST["oscillator2_form"],
            octave2= float(request.POST['octave2_form']),
            attackGain2= float(request.POST["attackGain2_form"]),
            attackDur2= float(request.POST["attackDur2_form"]),
            decayDur2= float(request.POST["decayDur2_form"]),
            sustainGain2= float(request.POST["sustainGain2_form"]),
            sustainDur2= float(request.POST["sustainDur2_form"]),
            release2= float(request.POST["release2_form"])
        )
        created_patch.save()
        print(created_patch)
        return redirect("/synth")

def load_patch(request, patch_id):
    # selected_patch = Patch.objects.get(id=request.POST['patch_to_load'])
    selected_patch = Patch.objects.get(id=patch_id)
    request.session['oscillator1'] = selected_patch.oscillator1
    request.session['octave1'] = float(selected_patch.octave1)
    request.session['attackGain1'] = float(selected_patch.attackGain1)
    request.session['attackDur1'] = float(selected_patch.attackDur1)
    request.session['decayDur1'] = float(selected_patch.decayDur1)
    request.session['sustainGain1'] = float(selected_patch.sustainGain1)
    request.session['sustainDur1'] = float(selected_patch.sustainDur1)
    request.session['release1'] = float(selected_patch.release1)
    request.session['oscillator2'] = selected_patch.oscillator2
    request.session['octave2'] = float(selected_patch.octave2)
    request.session['attackGain2'] = float(selected_patch.attackGain2)
    request.session['attackDur2'] = float(selected_patch.attackDur2)
    request.session['decayDur2'] = float(selected_patch.decayDur2)
    request.session['sustainGain2'] = float(selected_patch.sustainGain2)
    request.session['sustainDur2'] = float(selected_patch.sustainDur2)
    request.session['release2'] = float(selected_patch.release2)
    return redirect("/synth")

def destroy_patch(request, patch_id):
    patch_to_destroy = Patch.objects.get(id=patch_id)
    patch_to_destroy.delete()
    return redirect ("/synth")


def dashboard(request):
    context={
        'all_patches': Patch.objects.all(),
        'all_users':User.objects.all(),
        'selected_user':User.objects.get(id=request.session['uuid']),
    }
    return render(request, 'dashboard.html', context)