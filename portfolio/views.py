from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Profile, Technology, Project, Experience, Education, Testimonial, ContactMessage

def get_portfolio_context():
    # Attempt to retrieve existing profile or provide high-quality elegant fallback data
    profile = Profile.objects.first()
    if not profile:
        profile = Profile(
            name="Raviranjan Kumar",
            title="Principal Systems Architect & Designer",
            hero_title="Architecting Resilient Systems with Immersive Craftsmanship",
            hero_subtitle="Focused on building bespoke digital experiences that marry engineering precision with bold, premium aesthetics. No grids, no generic shadows, just pure industrial design.",
            bio_short="I am a software engineer and digital craftsman specializing in Django ecosystems, system architectures, and visually arresting user interfaces. I build things that load instantly, scale robustly, and look stunning.",
            bio_detailed="Over the years, I've developed full-scale power distribution management apps, custom enterprise integrations, and high-performance resume rewriting engines. My philosophy is to reject standard generic templates in favor of structured typography, warm contrast spaces, and high-precision execution.",
            email="raviranjan@example.com",
            location="Punjab, India",
            github_url="https://github.com/Raviranjan010",
            linkedin_url="https://linkedin.com",
            twitter_url="https://twitter.com",
            meta_title="Raviranjan Kumar | Principal Systems Architect",
            meta_description="Bespoke engineering portfolio of Raviranjan Kumar, specializing in Python, Django, robust software architectures, and luxury web interface craftsmanship.",
            meta_keywords="Python, Django, Backend Architect, Software Engineer, Portfolio, Creative Web Developer"
        )
    
    # Fetch experience, education, projects, skills, testimonials
    projects = Project.objects.all().prefetch_related('technologies')
    experiences = Experience.objects.all()
    education = Education.objects.all()
    testimonials = Testimonial.objects.all()
    
    # Categorize skills for filter tabs
    skills = Technology.objects.filter(featured=True)
    skills_by_category = {}
    for cat_key, cat_name in Technology.CATEGORY_CHOICES:
        cat_skills = skills.filter(category=cat_key)
        if cat_skills.exists():
            skills_by_category[cat_name] = cat_skills
            
    # Include all categories for dynamic filter
    all_categories = [{'key': key, 'name': name} for key, name in Technology.CATEGORY_CHOICES]

    return {
        'profile': profile,
        'projects': projects,
        'experiences': experiences,
        'education': education,
        'testimonials': testimonials,
        'skills_by_category': skills_by_category,
        'all_categories': all_categories,
        'all_skills': skills
    }

@ensure_csrf_cookie
def index_view(request):
    context = get_portfolio_context()
    return render(request, 'portfolio/index.html', context)


def project_detail_view(request, slug):
    project = get_object_or_404(Project.objects.prefetch_related('technologies'), slug=slug)
    
    # Check if loaded via AJAX (useful for smooth modal previews)
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.GET.get('ajax') == 'true'
    
    if is_ajax:
        return render(request, 'portfolio/project_modal_content.html', {'project': project})
        
    return render(request, 'portfolio/project_detail.html', {'project': project})


@require_POST
def contact_view(request):
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    subject = request.POST.get('subject', '').strip()
    message = request.POST.get('message', '').strip()

    if not name or not email or not message:
        return JsonResponse({
            'status': 'error',
            'message': 'All fields are required.'
        }, status=400)

    # Save to database
    contact_msg = ContactMessage.objects.create(
        name=name,
        email=email,
        subject=subject or 'Portfolio Contact Message',
        message=message
    )

    return JsonResponse({
        'status': 'success',
        'message': f"Thank you, {name}! Your message has been safely received. I will reach out shortly."
    })
