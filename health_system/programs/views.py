from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Program
from .forms import ProgramForm

@login_required
def program_list(request):
    # Filter programs to show only those created by the current user
    programs = Program.objects.filter(created_by=request.user).order_by('name')
    return render(request, 'programs/program_list.html', {'programs': programs})

@login_required
def program_detail(request, pk):
    # Get program only if it belongs to the current user
    program = get_object_or_404(Program, pk=pk, created_by=request.user)
    return render(request, 'programs/program_detail.html', {'program': program})
 
@login_required
def program_create(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            program = form.save(commit=False)
            program.created_by = request.user
            program.save()
            messages.success(request, 'Program created successfully!')
            return redirect('program_detail', pk=program.pk)
    else:
        form = ProgramForm()
    
    return render(request, 'programs/program_form.html', {'form': form, 'title': 'Create Program'})

@login_required
def program_update(request, pk):
    # Only allow updating programs created by the current user
    program = get_object_or_404(Program, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            messages.success(request, 'Program updated successfully!')
            return redirect('program_detail', pk=program.pk)
    else:
        form = ProgramForm(instance=program)
    
    return render(request, 'programs/program_form.html', {'form': form, 'title': 'Update Program'})