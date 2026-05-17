from django.shortcuts import render

# ─── Student Data ─────────────────────────────────────────────────────────────
STUDENT = {
    "name": "Ravi Ranjan Kashyap",
    "initials": "RRK",
    "tagline": "CS Engineering Student",
    "university": "Lovely Professional University",
    "course": "Computer Science Engineering",
    "semester": "2nd Year · 4th Semester",
    "location": "Punjab, India",
    "email": "raviranjan@example.com",
    "phone": "+91 98765 43210",
    "placed": False,

    "intro_headline": "Crafting Digital Experiences That Matter",
    "intro_sub": (
        "I'm a Computer Science student at LPU who lives at the intersection of "
        "design and technology. I build modern web products, experiment with AI, "
        "and obsess over every pixel, interaction, and line of code."
    ),

    "career_goal": (
        "To become a full-stack product engineer who builds scalable, "
        "beautifully designed digital products — contributing to meaningful "
        "startups or leading-edge companies that push boundaries."
    ),
    "vision": (
        "To bridge the gap between technical engineering and thoughtful design — "
        "creating software that not only works flawlessly but feels genuinely human."
    ),

    # Social Links
    "socials": {
        "github":   "https://github.com/Raviranjan010",
        "linkedin": "https://linkedin.com",
        "twitter":  "https://twitter.com",
        "instagram":"https://instagram.com",
        "behance":  "https://behance.net",
    },

    # Skills with levels
    "skills": [
        {"name": "HTML5 & CSS3",    "level": 95, "category": "frontend"},
        {"name": "JavaScript",      "level": 82, "category": "frontend"},
        {"name": "Python",          "level": 88, "category": "backend"},
        {"name": "Django",          "level": 80, "category": "backend"},
        {"name": "UI/UX Design",    "level": 85, "category": "design"},
        {"name": "Figma",           "level": 82, "category": "design"},
        {"name": "Responsive Design","level": 92,"category": "design"},
        {"name": "Canva",           "level": 90, "category": "design"},
        {"name": "Animation Design","level": 78, "category": "design"},
    ],

    # Interests
    "interests": [
        {"icon": "🎨", "name": "UI/UX Design",       "desc": "Human-centered digital experiences"},
        {"icon": "🤖", "name": "Artificial Intelligence","desc": "ML models & intelligent systems"},
        {"icon": "🌐", "name": "Web Development",     "desc": "Modern, performant frontends & backends"},
        {"icon": "💡", "name": "Business Innovation", "desc": "Tech-driven product thinking"},
        {"icon": "📷", "name": "Photography",         "desc": "Visual storytelling through a lens"},
        {"icon": "🎬", "name": "Video Editing",       "desc": "Cinematic post-production workflows"},
    ],

    # Projects
    "projects": [
        {
            "title":       "E-Commerce Platform",
            "desc":        "A full-featured online store with product catalogue, cart system, and secure checkout flow. Built with Django and custom CSS animations.",
            "tags":        ["Django", "Python", "CSS3", "JavaScript"],
            "category":   "fullstack",
            "demo_url":    "#",
            "github_url":  "https://github.com/Raviranjan010",
            "featured":    True,
        },
        {
            "title":       "Interactive To-Do App",
            "desc":        "A productivity app with drag-and-drop tasks, local storage persistence, priority labels, and smooth micro-animations.",
            "tags":        ["JavaScript", "HTML5", "CSS3"],
            "category":   "frontend",
            "demo_url":    "#",
            "github_url":  "https://github.com/Raviranjan010",
            "featured":    True,
        },
        {
            "title":       "BMI Calculator + Graphs",
            "desc":        "Health metrics tool with real-time Chart.js visualizations, body-type classification, and a clean data-driven interface.",
            "tags":        ["Python", "JavaScript", "Chart.js"],
            "category":   "frontend",
            "demo_url":    "#",
            "github_url":  "https://github.com/Raviranjan010",
            "featured":    True,
        },
        {
            "title":       "Animated Timeline",
            "desc":        "Scroll-driven interactive timeline component with milestone reveals, smooth easing, and mobile-responsive layout.",
            "tags":        ["HTML5", "CSS3", "JavaScript"],
            "category":   "frontend",
            "demo_url":    "#",
            "github_url":  "https://github.com/Raviranjan010",
            "featured":    False,
        },
        {
            "title":       "Sticker Tag System",
            "desc":        "A custom tagging and labelling web tool for categorising digital stickers with drag-and-drop organization.",
            "tags":        ["JavaScript", "CSS3", "HTML5"],
            "category":   "frontend",
            "demo_url":    "#",
            "github_url":  "https://github.com/Raviranjan010",
            "featured":    False,
        },
        {
            "title":       "Portfolio Website",
            "desc":        "A handcrafted, premium student portfolio site built with Django, featuring dark mode, smooth animations, and a fully dynamic backend.",
            "tags":        ["Django", "Python", "CSS3", "JavaScript"],
            "category":   "fullstack",
            "demo_url":    "#",
            "github_url":  "https://github.com/Raviranjan010",
            "featured":    False,
        },
    ],

    # Achievements
    "achievements": [
        {"year": "2024", "title": "Top Design Project", "desc": "Awarded best UI/UX project in department hackathon"},
        {"year": "2024", "title": "LPU Tech Fest Finalist", "desc": "Top 10 finalist in web development challenge"},
        {"year": "2023", "title": "Self-Taught Django", "desc": "Completed full Django course with 3 production deployments"},
        {"year": "2023", "title": "Figma Certified",   "desc": "Completed Figma UI Design certification course"},
    ],
}


def home(request):
    """Homepage view — hero, skills, projects, placement status."""
    ctx = {
        **STUDENT,
        "featured_projects": [p for p in STUDENT["projects"] if p["featured"]],
        "page": "home",
    }
    return render(request, "base/home.html", ctx)


def about(request):
    """About page — detailed background, interests, achievements."""
    ctx = {
        **STUDENT,
        "page": "about",
    }
    return render(request, "base/about.html", ctx)
