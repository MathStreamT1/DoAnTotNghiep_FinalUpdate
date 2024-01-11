# yourapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import OLP, ICPC, PROCON
from django.contrib.auth.decorators import user_passes_test
from .forms import OLPForm, OLPDeleteForm, ICPCForm, ICPCDeleteForm, PROCONForm, PROCONDeleteForm


def olp_list(request, selected_year=None):
    # Fetch all OLP objects from the database and order them by rank and system
    olps = OLP.objects.all().order_by('-year','system')

    grouped_achievements = {}

    for olp in olps:
        year = olp.year
        if year not in grouped_achievements:
            grouped_achievements[year] = [olp]
        else:
            grouped_achievements[year].append(olp)

    if selected_year:
        # Filter the achievements based on the selected year
        grouped_achievements = {selected_year: grouped_achievements.get(selected_year, [])}

    return render(request, 'achievement/olp_list.html', {'grouped_achievements': grouped_achievements, 'selected_year': selected_year})

def olp_create(request):
    if request.method == 'POST':
        form = OLPForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('olp_list')  # Redirect to a view that lists all OLP objects
    else:
        form = OLPForm()

    return render(request, 'achievement/olp_create.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def olp_update(request, olp_id):
    olp = get_object_or_404(OLP, id=olp_id)

    if request.method == 'POST':
        form = OLPForm(request.POST, instance=olp)
        if form.is_valid():
            form.save()
            return redirect('olp_list')
    else:
        form = OLPForm(instance=olp)

    return render(request, 'achievement/olp_form.html', {'form': form, 'action': 'Update'})

@user_passes_test(lambda u: u.is_superuser)
def olp_delete(request, olp_id):
    olp = get_object_or_404(OLP, id=olp_id)

    if request.method == 'POST':
        form = OLPDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            olp.delete()
            return redirect('olp_list')
    else:
        form = OLPDeleteForm()

    return render(request, 'achievement/olp_delete.html', {'form': form, 'olp': olp})

# Phần cho nội dung về danh sách giải thi ICPC 
def icpc_list(request, selected_year=None):
    # Fetch all ICPC objects from the database
    icpcs = ICPC.objects.all()

    grouped_achievements = {}
  
    for icpc in icpcs:
        year = icpc.year

        # Group by year
        if year not in grouped_achievements:
            grouped_achievements[year] = [icpc]
        else:
            grouped_achievements[year].append(icpc)

    if selected_year:
        # Filter the achievements based on the selected year
        grouped_achievements = {selected_year: grouped_achievements.get(selected_year, [])}

    return render(request, 'achievement/icpc_list.html', {'grouped_achievements': grouped_achievements, 'selected_year': selected_year})

def icpc_create(request):
    if request.method == 'POST':
        form = ICPCForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('icpc_list')  # Redirect to a view that lists all OLP objects
    else:
        form = ICPCForm()

    return render(request, 'achievement/icpc_create.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def icpc_update(request, icpc_id):
    icpc = get_object_or_404(ICPC, id=icpc_id)

    if request.method == 'POST':
        form = ICPCForm(request.POST, instance=icpc)
        if form.is_valid():
            form.save()
            return redirect('icpc_list')
    else:
        form = ICPCForm(instance=icpc)

    return render(request, 'achievement/icpc_form.html', {'form': form, 'action': 'Update'})

@user_passes_test(lambda u: u.is_superuser)
def icpc_delete(request, icpc_id):
    icpc = get_object_or_404(ICPC, id=icpc_id)

    if request.method == 'POST':
        form = ICPCDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            icpc.delete()
            return redirect('icpc_list')
    else:
        form = ICPCDeleteForm()

    return render(request, 'achievement/icpc_delete.html', {'form': form, 'icpc': icpc})

#Phần cho nội dung về PROCON ( theo PROCON JAPAN)
def procon_list(request, selected_year=None):
    # Fetch all PROCON objects from the database and order them by rank and system
    procons = PROCON.objects.all()

    grouped_achievements = {}

    for procon in procons:
        year = procon.year
        if year not in grouped_achievements:
            grouped_achievements[year] = [procon]
        else:
            grouped_achievements[year].append(procon)

    if selected_year:
        # Filter the achievements based on the selected year
        grouped_achievements = {selected_year: grouped_achievements.get(selected_year, [])}

    return render(request, 'achievement/procon_list.html', {'grouped_achievements': grouped_achievements, 'selected_year': selected_year})

@user_passes_test(lambda u: u.is_superuser)
def procon_update(request, procon_id):
    procon = get_object_or_404(PROCON, id=procon_id)

    if request.method == 'POST':
        form = PROCONForm(request.POST, instance=procon)
        if form.is_valid():
            form.save()
            return redirect('procon_list')
    else:
        form = PROCONForm(instance=procon)

    return render(request, 'achievement/procon_form.html', {'form': form, 'action': 'Update'})


@user_passes_test(lambda u: u.is_superuser)
def procon_delete(request, procon_id):
    procon = get_object_or_404(PROCON, id=procon_id)

    if request.method == 'POST':
        form = PROCONDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            procon.delete()
            return redirect('procon_list')
    else:
        form = PROCONDeleteForm()

    return render(request, 'achievement/procon_delete.html', {'form': form, 'procon': procon})



def procon_create(request):
    if request.method == 'POST':
        form = PROCONForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('procon_list')  # Redirect to a view that lists all OLP objects
    else:
        form = PROCONForm()

    return render(request, 'achievement/procon_create.html', {'form': form})