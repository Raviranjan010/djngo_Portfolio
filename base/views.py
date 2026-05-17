from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST


STUDENT = {
    "name": "Ravi Ranjan Kashyap",
    "initials": "RRK",
    "university": "Lovely Professional University",
    "course": "Computer Science Engineering",
    "branch": "Computer Science Engineering",
    "semester": "Second Year",
    "location": "Punjab, India",
    "email": "raviranjan@example.com",
    "phone": "+91 98765 43210",
    "placed": False,
    "profile_image": "base/img/profile.png",
    "intro_headline": "Designing polished web experiences with engineering discipline.",
    "intro_sub": (
        "I am a Computer Science Engineering student at Lovely Professional University "
        "focused on modern web development, UI/UX design, artificial intelligence, "
        "animation, and scalable digital products."
    ),
    "career_goal": (
        "To grow into a product-minded full-stack engineer who can turn ideas into "
        "fast, accessible, visually refined software for real users."
    ),
    "vision": (
        "To create technology that feels useful, elegant, and human while connecting "
        "engineering depth with thoughtful visual design."
    ),
    "mission": (
        "To keep building, learning, and shipping practical products that combine "
        "clean code, strong interaction design, and meaningful problem solving."
    ),
    "socials": {
        "github": "https://github.com/Raviranjan010",
        "linkedin": "https://linkedin.com",
        "instagram": "https://instagram.com",
        "behance": "https://behance.net",
    },
    "skills": [
        {"name": "HTML", "level": 94, "category": "Frontend"},
        {"name": "CSS", "level": 92, "category": "Frontend"},
        {"name": "JavaScript", "level": 84, "category": "Frontend"},
        {"name": "Python", "level": 86, "category": "Backend"},
        {"name": "Django", "level": 82, "category": "Backend"},
        {"name": "Figma", "level": 86, "category": "Design"},
        {"name": "Canva", "level": 88, "category": "Design"},
        {"name": "UI/UX Design", "level": 90, "category": "Design"},
        {"name": "Responsive Design", "level": 93, "category": "Frontend"},
        {"name": "Animation Design", "level": 80, "category": "Design"},
    ],
    "interests": [
        {"name": "UI/UX Design", "desc": "Interfaces with clarity, rhythm, and emotional precision."},
        {"name": "Artificial Intelligence", "desc": "Intelligent systems that make products more adaptive."},
        {"name": "Web Development", "desc": "Fast, responsive web apps with reliable Django foundations."},
        {"name": "Business Innovation", "desc": "Turning practical problems into product opportunities."},
        {"name": "Photography", "desc": "Composition, lighting, and visual storytelling."},
        {"name": "Video Editing", "desc": "Motion, pacing, and cinematic post-production."},
        {"name": "Creative Technology", "desc": "Experiments that blend design, code, and interaction."},
    ],
    "projects": [
        {
            "title": "E-Commerce Website",
            "desc": "A polished storefront concept with catalog browsing, product detail flow, cart patterns, and conversion-focused UI.",
            "tags": ["Django", "Python", "CSS", "JavaScript"],
            "category": "Full Stack",
            "featured": True,
            "metric": "Commerce",
        },
        {
            "title": "Interactive To-Do App",
            "desc": "A productivity interface with task states, priority labels, local persistence, and smooth micro-interactions.",
            "tags": ["JavaScript", "HTML", "CSS"],
            "category": "Frontend",
            "featured": True,
            "metric": "Interaction",
        },
        {
            "title": "BMI Calculator with Graphs",
            "desc": "A health metric tool with visual feedback, chart-ready layout, and clear result interpretation.",
            "tags": ["Python", "JavaScript", "Charts"],
            "category": "Data UI",
            "featured": True,
            "metric": "Analytics",
        },
        {
            "title": "Timeline Project",
            "desc": "A scroll-aware timeline for presenting milestones with clean motion and compact mobile behavior.",
            "tags": ["HTML", "CSS", "Animation"],
            "category": "UI System",
            "featured": False,
            "metric": "Motion",
        },
        {
            "title": "Sticker Tag Project",
            "desc": "A digital organization tool for tagging visual assets with flexible grouping and playful interface details.",
            "tags": ["JavaScript", "CSS", "UX"],
            "category": "Tooling",
            "featured": False,
            "metric": "Utility",
        },
        {
            "title": "Portfolio Websites",
            "desc": "Custom personal websites built around identity, visual hierarchy, responsive layouts, and maintainable templates.",
            "tags": ["Django", "UI/UX", "Responsive"],
            "category": "Brand System",
            "featured": False,
            "metric": "Identity",
        },
    ],
    "achievements": [
        {"year": "2026", "title": "Portfolio Architecture", "desc": "Built a Django portfolio with reusable templates and dynamic context."},
        {"year": "2025", "title": "Design Systems Practice", "desc": "Created consistent UI kits and responsive interface studies in Figma."},
        {"year": "2025", "title": "Frontend Experiments", "desc": "Explored animation, layout, and interaction patterns through hands-on projects."},
        {"year": "2024", "title": "Creative Production", "desc": "Developed photography, editing, and visual storytelling workflows."},
    ],
}


def _context(page):
    return {
        **STUDENT,
        "page": page,
        "featured_projects": [project for project in STUDENT["projects"] if project["featured"]],
    }


def home(request):
    return render(request, "base/home.html", _context("home"))


def about(request):
    return render(request, "base/about.html", _context("about"))


@require_POST
def contact(request):
    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    message = request.POST.get("message", "").strip()

    if not name or not email or not message:
        return JsonResponse({"ok": False, "message": "Please complete all required fields."}, status=400)

    return JsonResponse({
        "ok": True,
        "message": "Thanks, Ravi received your message draft successfully.",
    })
