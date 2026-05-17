import os
import django
from datetime import date

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from portfolio.models import Profile, Technology, Project, Experience, Education, Testimonial

def populate():
    print("Pre-populating portfolio database with premium editorial case studies...")
    
    # 1. Create or update profile
    profile, created = Profile.objects.get_or_create(
        name="Raviranjan Kumar",
        defaults={
            'title': "Principal Full-Stack Engineer",
            'hero_title': "Architecting High-Scale Systems with Precise Craftsmanship",
            'hero_subtitle': "Focused on building bespoke digital experiences that marry engineering precision with bold, premium aesthetics. No generic templates, no overused templates, just clean editorial space.",
            'bio_short': "I am an engineer specializing in Python/Django ecosystems, distributed architectures, and visually arresting user interfaces. I build things that scale seamlessly and load instantly.",
            'bio_detailed': "With years of experience leading engineering teams and building custom enterprise solutions, I reject the generic, cookie-cutter templates of the modern web. I believe in editorial grids, curated typography, and ultra-high contrast dark-mode spaces that put your technical achievements at the center.",
            'email': "raviranjan@example.com",
            'location': "Punjab, India",
            'github_url': "https://github.com/Raviranjan010",
            'linkedin_url': "https://linkedin.com",
            'twitter_url': "https://twitter.com",
            'instagram_url': "https://instagram.com",
            'meta_title': "Raviranjan Kumar | Principal Systems Architect",
            'meta_description': "Bespoke engineering portfolio of Raviranjan Kumar, specializing in Python, Django, robust software architectures, and premium web interface craftsmanship.",
            'meta_keywords': "Python, Django, Backend Architect, Software Engineer, Portfolio, Creative Web Developer"
        }
    )
    if created:
        print("[OK] Created Profile")
    else:
        print("[OK] Profile already exists")

    # 2. Technologies / Skills
    tech_data = [
        # Frontend
        ('React.js', 'frontend', 'devicon-react-original', 92, 1),
        ('Next.js', 'frontend', 'devicon-nextjs-original', 88, 2),
        ('Vanilla HTML/CSS', 'frontend', 'devicon-html5-plain-wordmark', 95, 3),
        
        # Backend
        ('Django / Python', 'backend', 'devicon-django-plain', 95, 1),
        ('Node.js', 'backend', 'devicon-nodejs-plain', 88, 2),
        ('FastAPI', 'backend', 'devicon-fastapi-plain', 85, 3),
        
        # Database
        ('PostgreSQL', 'database', 'devicon-postgresql-plain', 90, 1),
        ('Redis', 'database', 'devicon-redis-plain', 85, 2),
        ('Aiven Cloud DB', 'database', 'devicon-sqlite-plain', 80, 3),
        
        # DevOps / Cloud
        ('Docker Containers', 'devops', 'devicon-docker-plain', 90, 1),
        ('Google Cloud Run', 'devops', 'devicon-googlecloud-plain', 85, 2),
        ('CI/CD Pipelines', 'devops', 'devicon-githubactions-plain', 88, 3),
        
        # UI/UX Design
        ('Editorial Styling', 'design', 'fa-solid fa-compass-drafting', 92, 1),
        ('Figma Prototyping', 'design', 'devicon-figma-plain', 88, 2),
    ]

    technologies = {}
    for name, cat, icon, prof, order in tech_data:
        tech, created_t = Technology.objects.get_or_create(
            name=name,
            defaults={
                'category': cat,
                'icon_class': icon,
                'proficiency': prof,
                'featured': True,
                'order': order
            }
        )
        technologies[name] = tech
    print("[OK] Created 14 Core Technical Skills")

    # 3. Create Projects
    projects_data = [
        {
            'title': "AgriPower Subsidies Engine",
            'short_description': "A national-level agricultural power distribution portal designed for SDO and farmer workflows, processing millions of subsidies securely.",
            'description': "AgriPower is a distributed billing and document subsidy engine built on top of Django, PostgreSQL, and Aiven Cloud. It handles massive workflows where local farmers upload land registry documents, which undergo automatic optical character recognition (OCR) and Multi-Level SDO approvals.\n\nKey accomplishments:\n- Built database models capable of resolving multi-district tenancy checks under 50ms.\n- Integrated custom background task processing for PDF generation and digital signatures.\n- Implemented responsive role-based dashboards that run flawlessly on low-bandwidth rural connections.",
            'demo_url': "https://agripower.example.com",
            'github_url': "https://github.com/Raviranjan010/agripower",
            'featured': True,
            'order': 1,
            'stack': ['Django / Python', 'PostgreSQL', 'Docker Containers', 'Vanilla HTML/CSS']
        },
        {
            'title': "CareerForge Pro Payment Service",
            'short_description': "A microservice handling multi-currency Stripe checkouts, automated invoices, and dynamic PDF receipt generators.",
            'description': "CareerForge payment system processes global recurring subscriptions with automatic INR/USD currency conversions and multi-tier rate limiting.\n\nKey accomplishments:\n- Corrected dynamic currency fallbacks ensuring 100% accurate Indian Rupee charges in compliant markets.\n- Designed webhook handlers with robust idempotency keys preventing double-billing.\n- Created a headless Puppeteer receipt generator rendering gorgeous typography in PDF print envelopes.",
            'demo_url': "https://careerforge.example.com",
            'github_url': "https://github.com/Raviranjan010/careerforge",
            'featured': True,
            'order': 2,
            'stack': ['Node.js', 'React.js', 'Redis', 'CI/CD Pipelines']
        },
        {
            'title': "Bespoke Editorial CSS System",
            'short_description': "A UI library rejecting modern floating gradient cards in favor of solid high-contrast borders and paper textures.",
            'description': "An open-source custom user-interface kit focused on warm retro-modernism. Designed for portfolios and editorial web logs where text hierarchy reigns supreme.\n\nKey accomplishments:\n- Maintained sub-10KB stylesheet with zero reliance on Tailwind CSS or external layouts.\n- Engineered smooth custom cursor dynamics reacting to hover objects without input lag.\n- Provided native CSS-variable dark-mode triggers adhering to system preferences automatically.",
            'demo_url': "https://editorial.example.com",
            'github_url': "https://github.com/Raviranjan010/editorial-ui",
            'featured': True,
            'order': 3,
            'stack': ['Vanilla HTML/CSS', 'Next.js', 'Figma Prototyping', 'Editorial Styling']
        }
    ]

    for proj in projects_data:
        p, created_p = Project.objects.get_or_create(
            title=proj['title'],
            defaults={
                'short_description': proj['short_description'],
                'description': proj['description'],
                'demo_url': proj['demo_url'],
                'github_url': proj['github_url'],
                'featured': proj['featured'],
                'order': proj['order'],
                'image': 'projects/placeholder.jpg'  # Will display dynamic vector fallback if file not on disk
            }
        )
        
        # Link technologies
        for tech_name in proj['stack']:
            if tech_name in technologies:
                p.technologies.add(technologies[tech_name])
                
    print("[OK] Deployed 3 Rich Showcase Case Studies")

    # 4. Work Experience
    exp_data = [
        {
            'company': "Apex Software Labs",
            'role': "Lead Backend Architect",
            'location': "Remote, India",
            'start_date': date(2024, 6, 1),
            'current': True,
            'description': "- Scaled enterprise REST APIs, reducing latency by 42% through smart Redis indexing.\n- Mentored junior Python developers, implementing strict type-checking and automated pylint git hooks.\n- Designed secure transactional systems handling online payment processing in compliance with RBI standards.",
            'order': 1
        },
        {
            'company': "TechnoCraft Solutions",
            'role': "Systems Engineer",
            'location': "Punjab, India",
            'start_date': date(2022, 1, 15),
            'end_date': date(2024, 5, 28),
            'current': False,
            'description': "- Engineered high-traffic Django sites, optimizing static routing and database queries.\n- Developed responsive frontend layouts using Vanilla CSS, eliminating heavy dependencies on bloated grid libraries.\n- Configured Docker environments for local developer sandboxes and live Render deployments.",
            'order': 2
        }
    ]

    for exp in exp_data:
        Experience.objects.get_or_create(
            company=exp['company'],
            role=exp['role'],
            defaults={
                'location': exp['location'],
                'start_date': exp['start_date'],
                'end_date': exp.get('end_date'),
                'current': exp['current'],
                'description': exp['description'],
                'order': exp['order']
            }
        )
    print("[OK] Populated Work History Timeline")

    # 5. Testimonial
    Testimonial.objects.get_or_create(
        client_name="Harsh Vardhan",
        defaults={
            'client_title': "CTO at AgriGlobal Systems",
            'quote': "Raviranjan has a rare skill set: he writes rock-solid, secure Python architectures while maintaining an obsessive level of detail on the user interface. He didn't just build our subsidy engine; he crafted an editorial dashboard that our non-tech users enjoy using every day.",
            'project_relation': "Delivered AgriPower Subsidies Engine",
            'order': 1
        }
    )
    print("[OK] Added Peer Professional Reference")
    print("-------------------------------------------------------------")
    print("Database seeding completed! Your portfolio is primed and ready.")

if __name__ == '__main__':
    populate()
