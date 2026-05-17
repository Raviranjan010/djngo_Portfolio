const root = document.documentElement;
const loader = document.getElementById("loader");
const header = document.getElementById("site-header");
const progress = document.getElementById("scroll-progress");
const scrollTop = document.getElementById("scroll-top");
const menuToggle = document.getElementById("menu-toggle");
const navLinks = document.getElementById("nav-links");
const themeToggle = document.getElementById("theme-toggle");
const toast = document.getElementById("toast");

function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add("is-visible");
    window.setTimeout(() => toast.classList.remove("is-visible"), 3200);
}

function setTheme(theme) {
    root.dataset.theme = theme;
    localStorage.setItem("portfolio-theme", theme);
    const icon = themeToggle?.querySelector(".theme-icon");
    if (icon) icon.textContent = theme === "dark" ? "D" : "L";
}

const savedTheme = localStorage.getItem("portfolio-theme");
if (savedTheme) setTheme(savedTheme);

window.addEventListener("load", () => {
    window.setTimeout(() => loader?.classList.add("is-hidden"), 420);
});

window.addEventListener("scroll", () => {
    const scrollY = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const percent = docHeight > 0 ? (scrollY / docHeight) * 100 : 0;

    if (progress) progress.style.width = `${percent}%`;
    header?.classList.toggle("is-scrolled", scrollY > 18);
    scrollTop?.classList.toggle("is-visible", scrollY > 600);
}, { passive: true });

scrollTop?.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
});

menuToggle?.addEventListener("click", () => {
    const isOpen = navLinks.classList.toggle("is-open");
    menuToggle.classList.toggle("is-open", isOpen);
    menuToggle.setAttribute("aria-expanded", String(isOpen));
    document.body.classList.toggle("menu-open", isOpen);
});

navLinks?.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
        navLinks.classList.remove("is-open");
        menuToggle?.classList.remove("is-open");
        menuToggle?.setAttribute("aria-expanded", "false");
        document.body.classList.remove("menu-open");
    });
});

themeToggle?.addEventListener("click", () => {
    setTheme(root.dataset.theme === "dark" ? "light" : "dark");
});

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            revealObserver.unobserve(entry.target);
        }
    });
}, { threshold: 0.14 });

document.querySelectorAll(".reveal").forEach((el) => revealObserver.observe(el));

const skillObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.querySelectorAll(".meter span").forEach((bar) => {
            bar.style.width = `${bar.dataset.level}%`;
        });
        skillObserver.unobserve(entry.target);
    });
}, { threshold: 0.25 });

document.querySelectorAll(".skill-board").forEach((board) => skillObserver.observe(board));

document.querySelectorAll(".project-panel").forEach((panel) => {
    panel.addEventListener("pointermove", (event) => {
        const rect = panel.getBoundingClientRect();
        const x = ((event.clientX - rect.left) / rect.width - 0.5) * 5;
        const y = ((event.clientY - rect.top) / rect.height - 0.5) * -5;
        panel.style.transform = `translateX(8px) rotateX(${y}deg) rotateY(${x}deg)`;
    });
    panel.addEventListener("pointerleave", () => {
        panel.style.transform = "";
    });
});

const contactForm = document.getElementById("contact-form");
contactForm?.addEventListener("submit", async (event) => {
    event.preventDefault();
    const submit = contactForm.querySelector("button[type='submit']");
    const originalText = submit.textContent;
    submit.textContent = "Sending...";
    submit.disabled = true;

    try {
        const response = await fetch(contactForm.action, {
            method: "POST",
            body: new FormData(contactForm),
            headers: { "X-Requested-With": "XMLHttpRequest" },
        });
        const data = await response.json();
        if (!response.ok) throw new Error(data.message || "Please try again.");
        contactForm.reset();
        showToast(data.message);
    } catch (error) {
        showToast(error.message);
    } finally {
        submit.textContent = originalText;
        submit.disabled = false;
    }
});
