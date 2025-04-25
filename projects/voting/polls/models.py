class Election(models.Model):
    ELECTION_TYPES = (
        ('presidential', 'Presidential'),
        ('minister', 'Minister'),
        ('chancellor', 'Chancellor'),
        ('other', 'Other'),
    )
    
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('upcoming', 'Upcoming'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    election_type = models.CharField(max_length=20, choices=ELECTION_TYPES)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    candidate_registration_end_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    min_candidates = models.PositiveIntegerField(default=2)
    max_candidates = models.PositiveIntegerField(default=10)
    is_active = models.BooleanField(default=True)
    results_published = models.BooleanField(default=False)
    require_approval = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('polls:admin_election_detail', args=[self.id])
    
    def get_candidates_count(self):
        return self.candidate_set.count()
    
    def get_votes_count(self):
        return Vote.objects.filter(candidate__election=self).count()
    
    def is_registration_open(self):
        now = timezone.now()
        if self.candidate_registration_end_date:
            return self.start_date <= now < self.candidate_registration_end_date
        return self.start_date <= now < self.end_date
    
    def update_status(self):
        now = timezone.now()
        if not self.is_active:
            return
        
        if now < self.start_date:
            self.status = 'upcoming'
        elif self.start_date <= now < self.end_date:
            self.status = 'ongoing'
        elif now >= self.end_date:
            self.status = 'completed'
        self.save(update_fields=['status'])
    
    class Meta:
        ordering = ['-start_date']


class Candidate(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    platform = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('user', 'election')
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.election.title}"
    
    def get_votes_count(self):
        return self.votes.count()


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, related_name='votes', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'candidate')
    
    def __str__(self):
        return f"{self.user.username} voted for {self.candidate.user.username} in {self.candidate.election.title}" 