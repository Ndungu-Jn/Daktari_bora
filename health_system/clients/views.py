from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Client, ClientProgram
from programs.models import Program
from .forms import ClientForm, ClientProgramForm
from django.http import HttpResponseForbidden

@login_required
def client_list(request):
    query = request.GET.get('q', '')
    # Filter clients to show only those created by the current user
    clients = Client.objects.filter(created_by=request.user)
    
    if query:
        clients = clients.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(contact_number__icontains=query)
        )
    
    return render(request, 'clients/client_list.html', {
        'clients': clients,
        'query': query
    })

@login_required
def client_detail(request, pk):
    # Get client only if it belongs to the current user
    client = get_object_or_404(Client, pk=pk, created_by=request.user)
    client_programs = ClientProgram.objects.filter(client=client)
    
    return render(request, 'clients/client_detail.html', {
        'client': client,
        'client_programs': client_programs
    })

@login_required
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.created_by = request.user
            client.save()
            messages.success(request, 'Client registered successfully!')
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm()
    
    return render(request, 'clients/client_form.html', {
        'form': form,
        'title': 'Register New Client'
    })

@login_required
def client_update(request, pk):
    # Only allow updating clients created by the current user
    client = get_object_or_404(Client, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client updated successfully!')
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientForm(instance=client)
    
    return render(request, 'clients/client_form.html', {
        'form': form,
        'title': 'Update Client'
    })

@login_required
def enroll_client_in_program(request, client_id):
    # Only allow enrolling clients created by the current user
    client = get_object_or_404(Client, pk=client_id, created_by=request.user)
    
    if request.method == 'POST':
        form = ClientProgramForm(request.POST, user=request.user)  # Pass user here
        if form.is_valid():
            program = form.cleaned_data['program']
            status = form.cleaned_data['status']
            
            # Check if client is already enrolled in the program
            if ClientProgram.objects.filter(client=client, program=program).exists():
                messages.error(request, 'Client is already enrolled in this program.')
            else:
                ClientProgram.objects.create(
                    client=client,
                    program=program,
                    status=status
                )
                messages.success(request, f'Client enrolled in {program.name} successfully!')
            
            return redirect('client_detail', pk=client.pk)
    else:
        form = ClientProgramForm(user=request.user)  # Pass user here too
    
    return render(request, 'clients/enroll_program.html', {
        'form': form,
        'client': client
    })