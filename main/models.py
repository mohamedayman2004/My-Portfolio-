from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('Languages', 'Languages'),
        ('AI_ML', 'AI & ML'),
        ('Data', 'Data Analytics'),
        ('Tools', 'Tools & Frameworks')
    ])
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    is_remote = models.BooleanField(default=False)
    
    # New field for sorting
    start_date = models.DateField(null=True, blank=True, help_text="Used for sorting. Pick the start date.")

    # This ensures it's always descending (Newest first)
    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.role} at {self.company}"

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Project Categories"

    def __str__(self):
        return self.name

class Project(models.Model):
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    # This enables image uploads in Admin
    image = models.ImageField(upload_to='projects/') 
    technologies = models.CharField(max_length=200) # e.g., "Python, TensorFlow"
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    
    @property
    def tech_list(self):
        return [tech.strip() for tech in self.technologies.split(',')] if self.technologies else []
    
    def __str__(self):
        return self.title

class Profile(models.Model):
    name = models.CharField(max_length=100, default="Mohamed Ayman")
    title = models.CharField(max_length=100, default="AI & ML Engineer")
    bio = models.TextField(default="AI Engineer and Data Scientist specializing in Machine Learning.")
    
    # Uploads to media/profile/ folder
    profile_image = models.ImageField(upload_to='profile/', default='default.jpg')
    
    # Social Links
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    email_link = models.EmailField(blank=True)
    cv_link = models.URLField(blank=True, help_text="Link to your resume PDF")

    def __str__(self):
        return self.name


class Certificate(models.Model):
    CATEGORY_CHOICES = [
        ('certificate', 'Certificate'),
        ('achievement', 'Achievement'),
    ]

    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200, help_text="e.g., Google, AWS, Coursera")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='certificate')
    date_earned = models.DateField(help_text="Date the certificate/achievement was earned")
    description = models.TextField(blank=True, help_text="Brief description of what this credential covers")
    credential_id = models.CharField(max_length=200, blank=True, help_text="Credential ID if available")
    credential_url = models.URLField(blank=True, help_text="Link to verify the credential")
    badge_image = models.ImageField(upload_to='certificates/', blank=True, help_text="Badge or logo image")

    class Meta:
        ordering = ['-date_earned']

    def __str__(self):
        return f"{self.title} — {self.issuer}"