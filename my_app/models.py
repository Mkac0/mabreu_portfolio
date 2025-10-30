from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, help_text="A unique, URL-friendly title.")
    description = models.TextField()
    github_url = models.URLField(max_length=200, default='http://placeholder.github.com')
    live_url = models.URLField(max_length=200, blank=True, null=True, help_text="Link to the live deployed version.")
    image = models.ImageField(upload_to='project_images/', blank=True, null=True, help_text="A main image or screenshot of the project.")
    date_completed = models.DateField(null=True, blank=True)
    is_featured = models.BooleanField(default=False, help_text="Check to display on the main page.")
    
    class Meta:
        ordering = ['-date_completed']
        
    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)
    CATEGORY_CHOICES = [
        ('BK', 'Backend'),
        ('FE', 'Frontend'),
        ('DB', 'Database'),
        ('OT', 'Other'),
    ]
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default='BK')
    proficiency = models.PositiveIntegerField(default=3, help_text="Level of expertise (e.g., 1=Basic, 5=Expert)")
    
    class Meta:
        ordering = ['category', 'name']
        
    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=100, help_text="Job Title or Position")
    company = models.CharField(max_length=100, help_text="Company or Institution Name")
    location = models.CharField(max_length=100, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, help_text="Leave blank if currently working here.")
    description = models.TextField(help_text="Key responsibilities and accomplishments in bullet points.")
    
    class Meta:
        ordering = ['-start_date'] 
        
    def __str__(self):
        return f"{self.title} at {self.company}"