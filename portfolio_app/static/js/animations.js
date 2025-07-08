// Advanced Portfolio Animations and Interactive Effects

document.addEventListener('DOMContentLoaded', function() {
    
    // ========================================
    // SCROLL REVEAL ANIMATIONS
    // ========================================
    
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
                
                // Add staggered animation for children
                const children = entry.target.querySelectorAll('.loading');
                children.forEach((child, index) => {
                    setTimeout(() => {
                        child.classList.add('animate');
                    }, index * 100);
                });
            }
        });
    }, observerOptions);
    
    // Observe elements for animation
    const animateElements = document.querySelectorAll('.loading, .project-card, .card, .skill-item');
    animateElements.forEach(el => observer.observe(el));
    
    // ========================================
    // ENHANCED PROJECT CARD INTERACTIONS
    // ========================================
    
    const projectCards = document.querySelectorAll('.project-card');
    
    projectCards.forEach(card => {
        // Add ripple effect on click
        card.addEventListener('click', function(e) {
            const ripple = document.createElement('div');
            ripple.classList.add('ripple-effect');
            
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            const x = e.clientX - rect.left - size / 2;
            const y = e.clientY - rect.top - size / 2;
            
            ripple.style.width = ripple.style.height = size + 'px';
            ripple.style.left = x + 'px';
            ripple.style.top = y + 'px';
            
            this.appendChild(ripple);
            
            setTimeout(() => {
                ripple.remove();
            }, 600);
        });
        
        // Enhanced hover effects
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-15px) scale(1.02) rotateX(5deg)';
            
            // Animate badges
            const badges = this.querySelectorAll('.badge');
            badges.forEach((badge, index) => {
                setTimeout(() => {
                    badge.style.transform = 'translateY(-3px) scale(1.1)';
                }, index * 50);
            });
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = '';
            
            // Reset badges
            const badges = this.querySelectorAll('.badge');
            badges.forEach(badge => {
                badge.style.transform = '';
            });
        });
    });
    
    // ========================================
    // TYPING ANIMATION FOR HERO TEXT
    // ========================================
    
    function typeWriter(element, text, speed = 100) {
        let i = 0;
        element.innerHTML = '';
        
        function type() {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                i++;
                setTimeout(type, speed);
            }
        }
        type();
    }
    
    // Apply typing animation to hero title
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        const originalText = heroTitle.textContent;
        setTimeout(() => {
            typeWriter(heroTitle, originalText, 80);
        }, 500);
    }
    
    // ========================================
    // PARALLAX SCROLLING EFFECTS
    // ========================================
    
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const parallaxElements = document.querySelectorAll('.parallax-element');
        
        parallaxElements.forEach(element => {
            const speed = element.dataset.speed || 0.5;
            const yPos = -(scrolled * speed);
            element.style.transform = `translateY(${yPos}px)`;
        });
    });
    
    // ========================================
    // SKILL BARS ANIMATION
    // ========================================
    
    const skillBars = document.querySelectorAll('.skill-progress');
    const skillObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progressBar = entry.target;
                const percentage = progressBar.dataset.percentage || 0;
                
                setTimeout(() => {
                    progressBar.style.width = percentage + '%';
                }, 200);
            }
        });
    }, { threshold: 0.5 });
    
    skillBars.forEach(bar => skillObserver.observe(bar));
    
    // ========================================
    // SMOOTH SCROLL FOR NAVIGATION
    // ========================================
    
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // ========================================
    // FLOATING ELEMENTS ANIMATION
    // ========================================
    
    function createFloatingElements() {
        const container = document.querySelector('.hero-section');
        if (!container) return;
        
        for (let i = 0; i < 5; i++) {
            const element = document.createElement('div');
            element.classList.add('floating-element');
            element.style.cssText = `
                position: absolute;
                width: ${Math.random() * 20 + 10}px;
                height: ${Math.random() * 20 + 10}px;
                background: rgba(52, 152, 219, ${Math.random() * 0.3 + 0.1});
                border-radius: 50%;
                left: ${Math.random() * 100}%;
                top: ${Math.random() * 100}%;
                animation: float ${Math.random() * 3 + 2}s ease-in-out infinite;
                animation-delay: ${Math.random() * 2}s;
                pointer-events: none;
            `;
            container.appendChild(element);
        }
    }
    
    createFloatingElements();
    
    // ========================================
    // BUTTON ENHANCEMENT EFFECTS
    // ========================================
    
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.classList.add('btn-floating');
        });
        
        button.addEventListener('mouseleave', function() {
            this.classList.remove('btn-floating');
        });
        
        // Add pulse effect to primary buttons
        if (button.classList.contains('btn-primary')) {
            button.classList.add('btn-pulse');
        }
    });
    
    // ========================================
    // LOADING SCREEN ANIMATION
    // ========================================
    
    window.addEventListener('load', function() {
        const loadingScreen = document.querySelector('.loading-screen');
        if (loadingScreen) {
            loadingScreen.style.opacity = '0';
            setTimeout(() => {
                loadingScreen.style.display = 'none';
            }, 500);
        }
        
        // Trigger initial animations
        document.body.classList.add('loaded');
    });
    
    // ========================================
    // CURSOR TRAIL EFFECT
    // ========================================
    
    let mouseX = 0, mouseY = 0;
    let trailElements = [];
    
    // Create trail elements
    for (let i = 0; i < 10; i++) {
        const trail = document.createElement('div');
        trail.classList.add('cursor-trail');
        trail.style.cssText = `
            position: fixed;
            width: 4px;
            height: 4px;
            background: rgba(52, 152, 219, ${1 - i * 0.1});
            border-radius: 50%;
            pointer-events: none;
            z-index: 9999;
            transition: all 0.1s ease;
        `;
        document.body.appendChild(trail);
        trailElements.push(trail);
    }
    
    document.addEventListener('mousemove', function(e) {
        mouseX = e.clientX;
        mouseY = e.clientY;
        
        trailElements.forEach((trail, index) => {
            setTimeout(() => {
                trail.style.left = mouseX + 'px';
                trail.style.top = mouseY + 'px';
            }, index * 20);
        });
    });
    
});

// CSS for ripple effect
const style = document.createElement('style');
style.textContent = `
    .ripple-effect {
        position: absolute;
        border-radius: 50%;
        background: rgba(52, 152, 219, 0.3);
        transform: scale(0);
        animation: ripple 0.6s linear;
        pointer-events: none;
    }
    
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
