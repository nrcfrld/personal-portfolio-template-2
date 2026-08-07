document.addEventListener('DOMContentLoaded', () => {
    // Initialize Lucide Icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // Theme Toggle Logic
    const themeToggleBtn = document.querySelector('.theme-toggle');
    const html = document.documentElement;
    const themeIcon = document.getElementById('theme-icon');

    if (themeToggleBtn) {
        // Initialize theme based on preference or data attribute if we want to save it later
        
        themeToggleBtn.addEventListener('click', () => {
            const currentTheme = html.getAttribute('data-theme');
            const targetTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            html.setAttribute('data-theme', targetTheme);
            
            if (themeIcon) {
                themeIcon.setAttribute('data-lucide', targetTheme === 'dark' ? 'sun' : 'moon');
                if (typeof lucide !== 'undefined') {
                    lucide.createIcons();
                }
            }
        });
    }

    // Mobile Menu Logic
    const menuBtn = document.getElementById('menu-toggle');
    const menuOverlay = document.getElementById('mobile-menu');
    const mobileMenuLinks = document.querySelectorAll('.mobile-overlay a');
    
    if (menuBtn && menuOverlay) {
        menuBtn.addEventListener('click', () => {
            menuOverlay.classList.toggle('active');
            document.body.classList.toggle('menu-open');
            menuBtn.textContent = menuOverlay.classList.contains('active') ? 'Close' : 'Menu';
        });

        // Close menu when a link is clicked
        mobileMenuLinks.forEach(link => {
            link.addEventListener('click', () => {
                menuOverlay.classList.remove('active');
                document.body.classList.remove('menu-open');
                menuBtn.textContent = 'Menu';
            });
        });
    }

    // Smooth scroll link highlighting (Desktop)
    const navLinks = document.querySelectorAll('.nav-links a');
    const sections = document.querySelectorAll('section');

    if (navLinks.length > 0 && sections.length > 0) {
        window.addEventListener('scroll', () => {
            let current = '';
            sections.forEach(section => {
                const sectionTop = section.offsetTop;
                if (window.pageYOffset >= sectionTop - 150) {
                    current = section.getAttribute('id');
                }
            });

            navLinks.forEach(link => {
                const href = link.getAttribute('href');
                if (href) {
                    link.style.opacity = href === `#${current}` ? '1' : '0.5';
                }
            });
        });
    }

    // Scroll Animation Observer
    const revealElements = document.querySelectorAll('.reveal');
    
    if (revealElements.length > 0) {
        const revealOptions = {
            threshold: 0.1, // Trigger when 10% of element is visible
            rootMargin: "0px 0px -50px 0px" // Trigger slightly before it hits the bottom
        };

        const revealObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (!entry.isIntersecting) return;
                
                // Add active class to trigger animation
                entry.target.classList.add('active');
                
                // Unobserve after animation so it doesn't animate again when scrolling up
                observer.unobserve(entry.target);
            });
        }, revealOptions);

        revealElements.forEach(el => revealObserver.observe(el));
    }
});
