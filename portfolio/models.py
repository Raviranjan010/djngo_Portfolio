from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator

class Profile(models.Model):
    name = models.CharField(max_length=100, help_text="Your full name")
    title = models.CharField(max_length=150, help_text="Professional title (e.g. Lead Full-Stack Architect)")
    hero_title = models.CharField(max_length=200, blank=True, help_text="Main headline on Hero section")
    hero_subtitle = models.TextField(blank=True, help_text="Supporting sub-headline on Hero section")
    bio_short = models.TextField(help_text="A short, catchy one-paragraph bio")
    bio_detailed = models.TextField(blank=True, help_text="Detailed about me story")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True, help_text="Your professional portrait")
    about_image = models.ImageField(upload_to='profile/', blank=True, null=True, help_text="Secondary image for about section")
    resume = models.FileField(upload_to='resume/', blank=True, null=True, help_text="PDF Resume download")
    
    # Contact Info
    email = models.EmailField(help_text="Primary professional email")
    phone = models.CharField(max_length=20, blank=True, help_text="Optional contact number")
    location = models.CharField(max_length=100, help_text="City, Country")
    
    # Social Links
    github_url = models.URLField(blank=True, help_text="GitHub profile URL")
    linkedin_url = models.URLField(blank=True, help_text="LinkedIn profile URL")
    twitter_url = models.URLField(blank=True, help_text="Twitter/X profile URL")
    instagram_url = models.URLField(blank=True, help_text="Instagram profile URL")
    behance_url = models.URLField(blank=True, help_text="Behance/Dribbble profile URL")
    
    # SEO Settings
    meta_title = models.CharField(max_length=80, blank=True, help_text="SEO Title Tag (e.g. Raviranjan | Creative Portfolio)")
    meta_description = models.CharField(max_length=160, blank=True, help_text="SEO Meta Description (150-160 chars)")
    meta_keywords = models.CharField(max_length=255, blank=True, help_text="Comma-separated SEO keywords")

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profile"

    def __str__(self):
        return f"{self.name} - Profile Settings"


class Technology(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('devops', 'DevOps / Cloud'),
        ('design', 'UI/UX Design'),
        ('other', 'Other Tools'),
    ]
    
    name = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    icon_class = models.CharField(max_length=100, blank=True, help_text="Devicon/FontAwesome class name (e.g. devicon-python-plain)")
    proficiency = models.IntegerField(default=80, validators=[MinValueValidator(0), MaxValueValidator(100)], help_text="Proficiency percentage (0-100)")
    featured = models.BooleanField(default=True, help_text="Show in featured skills section")
    order = models.IntegerField(default=0, help_text="Custom display ordering")

    class Meta:
        verbose_name = "Technology / Skill"
        verbose_name_plural = "Technologies & Skills"
        ordering = ['category', 'order', 'name']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class Project(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    short_description = models.CharField(max_length=250, help_text="Brief summary shown on portfolio cards")
    description = models.TextField(help_text="Detailed markdown-compatible description of the project")
    image = models.ImageField(upload_to='projects/', help_text="Primary portfolio image (1200x800px recommended)")
    image_gallery = models.ImageField(upload_to='projects/gallery/', blank=True, null=True, help_text="Secondary image for inside details")
    technologies = models.ManyToManyField(Technology, related_name="projects", help_text="Select tools/languages used")
    demo_url = models.URLField(blank=True, verbose_name="Live Demo URL")
    github_url = models.URLField(blank=True, verbose_name="GitHub Repository URL")
    featured = models.BooleanField(default=False, help_text="Feature this project prominently on the homepage")
    order = models.IntegerField(default=0, help_text="Sorting order (lower numbers display first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank if currently working here")
    current = models.BooleanField(default=False, help_text="Is this your current role?")
    description = models.TextField(help_text="Detail your key accomplishments and responsibilities (bullet points recommended)")
    order = models.IntegerField(default=0, help_text="Sorting order (lower numbers display first)")

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.role} at {self.company}"


class Education(models.Model):
    institution = models.CharField(max_length=150)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    description = models.TextField(blank=True, help_text="Honors, activities, or key modules")
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Education History"
        verbose_name_plural = "Education History"
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_title = models.CharField(max_length=100, help_text="e.g. CTO, ACME Corp or Co-Founder")
    quote = models.TextField(help_text="Testimonial text")
    client_image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    project_relation = models.CharField(max_length=150, blank=True, help_text="e.g. Built AgriPower System")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Testimonial from {self.client_name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
