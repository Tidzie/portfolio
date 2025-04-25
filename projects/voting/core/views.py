from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from .models import UserProfile, Election, Candidate, Vote
from datetime import date

def home(request):
    return render(request, 'core/home.html')

@login_required
def dashboard(request):
    user_profile = request.user.userprofile
    role = user_profile.role
    
    # Common data for all dashboards
    active_elections = Election.objects.filter(status='active')
    upcoming_elections = Election.objects.filter(status='upcoming')
    completed_elections = Election.objects.filter(status='completed')
    
    # Calculate statistics based on role
    context = {
        'active_elections': active_elections,
        'upcoming_elections': upcoming_elections,
        'completed_elections': completed_elections,
        'total_active': active_elections.count(),
        'total_upcoming': upcoming_elections.count(),
        'total_completed': completed_elections.count(),
    }
    
    if role == 'president':
        # Get candidate information if the president is a candidate
        user_candidacies = Candidate.objects.filter(user=request.user)
        context['user_candidacies'] = user_candidacies
        return render(request, 'core/president_dashboard.html', context)
    elif role == 'minister':
        # Get candidate information if the minister is a candidate
        user_candidacies = Candidate.objects.filter(user=request.user)
        context['user_candidacies'] = user_candidacies
        return render(request, 'core/minister_dashboard.html', context)
    elif role == 'chancellor':
        # Get candidate information if the chancellor is a candidate
        user_candidacies = Candidate.objects.filter(user=request.user)
        context['user_candidacies'] = user_candidacies
        return render(request, 'core/chancellor_dashboard.html', context)
    else:  # voter
        # Get voter's votes
        user_votes = Vote.objects.filter(user=request.user)
        context['user_votes'] = user_votes
        
        # Elections the voter hasn't voted in yet
        voted_election_ids = user_votes.values_list('candidate__election_id', flat=True)
        elections_to_vote = active_elections.exclude(id__in=voted_election_ids)
        context['elections_to_vote'] = elections_to_vote
        
        return render(request, 'core/voter_dashboard.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Check age requirements based on role
            selected_role = form.cleaned_data.get('role')
            dob = form.cleaned_data.get('date_of_birth')
            today = date.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            
            # Age requirements for different roles
            if selected_role == 'president' and age < 40:
                form.add_error('role', 'You must be at least 40 years old to register as President.')
            elif selected_role == 'minister' and age < 35:
                form.add_error('role', 'You must be at least 35 years old to register as Minister.')
            elif selected_role == 'chancellor' and age < 30:
                form.add_error('role', 'You must be at least 30 years old to register as Chancellor.')
            elif selected_role == 'voter' and age < 18:
                form.add_error('role', 'You must be at least 18 years old to register as Voter.')
            else:
                user = form.save()
                # Special roles need approval
                if selected_role != 'voter':
                    user.userprofile.is_approved = False
                    user.userprofile.save()
                    messages.success(request, f'Account created for {user.username}! Your role as {selected_role} requires approval.')
                else:
                    messages.success(request, f'Account created for {user.username}! You can now login.')
                return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def update_profile(request):
    if request.method == 'POST':
        user = request.user
        profile = user.userprofile
        
        # Update user basic info
        if 'first_name' in request.POST:
            user.first_name = request.POST.get('first_name')
        if 'last_name' in request.POST:
            user.last_name = request.POST.get('last_name')
        if 'email' in request.POST:
            user.email = request.POST.get('email')
        
        # Update profile fields
        if 'bio' in request.POST:
            profile.bio = request.POST.get('bio')
            
        # Only update the following fields for eligible roles
        if profile.role in ['PRESIDENT', 'MINISTER', 'CHANCELLOR']:
            if 'education' in request.POST:
                profile.education = request.POST.get('education')
            if 'experience' in request.POST:
                profile.experience = request.POST.get('experience')
            if 'manifesto' in request.POST:
                profile.manifesto = request.POST.get('manifesto')
            if 'campaign_promises' in request.POST:
                profile.campaign_promises = request.POST.get('campaign_promises')
            
            # Handle profile picture upload for eligible roles
            if request.FILES and 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
        
        # Save changes
        user.save()
        profile.save()
        
        messages.success(request, 'Your profile has been updated successfully.')
        return redirect('core:dashboard')
    
    return redirect('core:dashboard')
