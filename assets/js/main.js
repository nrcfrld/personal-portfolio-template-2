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

    // Free template screenshot carousels and gallery dialog
    const templateCards = document.querySelectorAll('.template-card[data-template-title]');
    const templateDialog = document.querySelector('[data-template-dialog]');
    const templateDialogTitle = document.querySelector('[data-template-dialog-title]');
    const templateDialogGrid = document.querySelector('[data-template-dialog-grid]');
    const templateDialogClose = document.querySelector('[data-template-dialog-close]');
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const carouselControllers = [];

    templateCards.forEach((card, cardIndex) => {
        const preview = card.querySelector('[data-template-gallery-open]');
        const slides = Array.from(card.querySelectorAll('.template-slide'));
        const counter = card.querySelector('[data-template-counter]');
        let activeIndex = 0;
        let timerId;

        const showSlide = index => {
            activeIndex = index;
            slides.forEach((slide, slideIndex) => {
                slide.classList.toggle('is-active', slideIndex === activeIndex);
            });
            if (counter) {
                counter.textContent = `${String(activeIndex + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;
            }
        };

        const stopCarousel = () => {
            window.clearInterval(timerId);
            preview.classList.remove('is-running');
        };

        const startCarousel = () => {
            if (reduceMotion || templateDialog?.open) return;
            stopCarousel();
            preview.classList.add('is-running');
            if (slides.length < 2) return;
            timerId = window.setInterval(() => {
                showSlide((activeIndex + 1) % slides.length);
            }, 2000);
        };

        preview.addEventListener('mouseenter', stopCarousel);
        preview.addEventListener('mouseleave', startCarousel);
        preview.addEventListener('focus', stopCarousel);
        preview.addEventListener('blur', startCarousel);
        preview.addEventListener('click', () => {
            if (!templateDialog || !templateDialogTitle || !templateDialogGrid) return;

            carouselControllers.forEach(controller => controller.stop());
            templateDialogTitle.textContent = card.dataset.templateTitle;
            templateDialogGrid.replaceChildren(...slides.map((slide, index) => {
                const figure = document.createElement('figure');
                const image = document.createElement('img');
                const caption = document.createElement('figcaption');
                image.src = slide.src;
                image.alt = slide.alt;
                image.width = slide.naturalWidth || Number(slide.width);
                image.height = slide.naturalHeight || Number(slide.height);
                caption.textContent = `Screenshot ${String(index + 1).padStart(2, '0')}`;
                figure.append(image, caption);
                return figure;
            }));
            document.body.classList.add('dialog-open');
            templateDialog.showModal();
        });

        carouselControllers.push({ start: startCarousel, stop: stopCarousel });
        if (!reduceMotion) {
            window.setTimeout(startCarousel, cardIndex * 350);
        }
    });

    const closeTemplateDialog = () => {
        if (!templateDialog?.open) return;
        templateDialog.close();
    };

    templateDialogClose?.addEventListener('click', closeTemplateDialog);
    templateDialog?.addEventListener('click', event => {
        if (event.target === templateDialog) closeTemplateDialog();
    });
    templateDialog?.addEventListener('close', () => {
        document.body.classList.remove('dialog-open');
        carouselControllers.forEach(controller => controller.start());
    });

    document.addEventListener('visibilitychange', () => {
        carouselControllers.forEach(controller => {
            if (document.hidden) controller.stop();
            else controller.start();
        });
    });
});
