from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('president', 'President'),
        ('minister', 'Minister'),
        ('chancellor', 'Chancellor'),
        ('voter', 'Voter'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='voter')
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    manifesto = models.TextField(blank=True, null=True)
    campaign_promises = models.TextField(blank=True, null=True)
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Election(models.Model):
    ELECTION_TYPE_CHOICES = (
        ('presidential', 'Presidential'),
        ('ministerial', 'Ministerial'),
        ('chancellor', 'Chancellor'),
        ('general', 'General'),
    )
    
    STATUS_CHOICES = (
        ('upcoming', 'Upcoming'),
        ('active', 'Active'),
        ('completed', 'Completed'),
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    election_type = models.CharField(max_length=20, choices=ELECTION_TYPE_CHOICES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_elections')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # Auto-update status based on dates
        now = timezone.now()
        if self.end_date < now:
            self.status = 'completed'
        elif self.start_date <= now <= self.end_date:
            self.status = 'active'
        else:
            self.status = 'upcoming'
        super().save(*args, **kwargs)
    
    @property
    def candidate_count(self):
        return self.candidates.count()
    
    @property
    def votes_count(self):
        return Vote.objects.filter(candidate__election=self).count()
    
    @property
    def winner(self):
        if self.status == 'completed':
            # Get candidate with most votes
            candidates = self.candidates.all()
            if candidates.exists():
                return max(candidates, key=lambda c: c.votes.count())
        return None
    
    @property
    def winner_name(self):
        winner = self.winner
        if winner:
            return winner.user.get_full_name() or winner.user.username
        return "No winner yet"
    
    @property
    def total_votes(self):
        return self.votes_count
    
    def __str__(self):
        return f"{self.title} ({self.get_election_type_display()}) - {self.get_status_display()}"

class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='candidacies')
    election = models.ForeignKey(Election, on_delete=models.CASCADE, related_name='candidates')
    platform = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'election')
    
    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} - {self.election.title}"

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='votes')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'candidate')
    
    def __str__(self):
        return f"{self.user.username} voted for {self.candidate.user.username}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
