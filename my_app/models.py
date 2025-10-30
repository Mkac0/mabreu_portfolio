from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    short_description = models.CharField(max_length=240)
    description = models.TextField(blank=True)
    tags = models.CharField(max_length=240, blank=True)
    project_url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-featured", "-created_at"]


    def __str__(self):
        return self.title
