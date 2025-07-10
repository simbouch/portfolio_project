// Enhanced Hero Section Animations
// Professional, stunning animations for maximum impact with 60fps performance

// Ensure animations start after page is fully loaded
function initHeroAnimations() {

    // ========================================
    // SOPHISTICATED TYPEWRITER ANIMATION
    // ========================================

    function initAdvancedTypewriter() {
        const heroTitle = document.querySelector('.hero-title');

        if (!heroTitle) return;

        // Store original content
        const originalText = heroTitle.textContent.trim();

        // Hide elements initially
        heroTitle.style.opacity = '0';

        // Create typewriter container with enhanced structure
        const typewriterContainer = document.createElement('div');
        typewriterContainer.className = 'typewriter-container';
        typewriterContainer.innerHTML = `
            <span class="typewriter-text"></span>
            <span class="typewriter-name gradient-text"></span>
            <span class="typewriter-cursor">|</span>
        `;

        // Replace original title
        heroTitle.innerHTML = '';
        heroTitle.appendChild(typewriterContainer);
        heroTitle.style.opacity = '1';

        const typewriterText = typewriterContainer.querySelector('.typewriter-text');
        const typewriterName = typewriterContainer.querySelector('.typewriter-name');
        const cursor = typewriterContainer.querySelector('.typewriter-cursor');

        // Enhanced cursor animation with realistic blinking
        let cursorVisible = true;
        setInterval(() => {
            cursor.style.opacity = cursorVisible ? '0' : '1';
            cursorVisible = !cursorVisible;
        }, 530);

        // Sophisticated typing with realistic human-like timing
        const greeting = "Hello, I'm ";
        const name = "Bouchaib KHRIBECH";
        let greetingIndex = 0;
        let nameIndex = 0;

        // Clear initial content
        typewriterText.textContent = '';
        typewriterName.textContent = '';

        function typeGreeting() {
            if (greetingIndex < greeting.length) {
                typewriterText.textContent += greeting.charAt(greetingIndex);
                greetingIndex++;

                // Realistic typing speed with variation
                const baseSpeed = 80;
                const variation = Math.random() * 40;
                const pauseAfterSpace = greeting.charAt(greetingIndex - 1) === ' ' ? 100 : 0;

                setTimeout(typeGreeting, baseSpeed + variation + pauseAfterSpace);
            } else {
                // Pause before typing name for dramatic effect
                setTimeout(typeName, 400);
            }
        }

        function typeName() {
            if (nameIndex < name.length) {
                typewriterName.textContent += name.charAt(nameIndex);
                nameIndex++;

                // Special timing for name characters
                const char = name.charAt(nameIndex - 1);
                let delay = 90 + Math.random() * 60;

                // Longer pause at space between first and last name
                if (char === ' ') {
                    delay = 250;
                }
                // Slightly faster for vowels (more natural)
                else if ('aeiouAEIOU'.includes(char)) {
                    delay = 70 + Math.random() * 30;
                }
                // Slower for consonant clusters
                else if (nameIndex > 1 && !'aeiouAEIOU '.includes(name.charAt(nameIndex - 2))) {
                    delay = 110 + Math.random() * 40;
                }

                setTimeout(typeName, delay);
            } else {
                // Name typing complete - add special glow effect
                setTimeout(() => {
                    typewriterName.classList.add('name-complete');
                    // Hide cursor after name completion
                    setTimeout(() => {
                        cursor.style.opacity = '0';
                    }, 800);
                }, 600);
            }
        }

        // Start the animation sequence
        setTimeout(typeGreeting, 1000);
    }

    // ========================================
    // ENHANCED PROFILE PICTURE ANIMATIONS
    // ========================================

    function initProfileAnimations() {
        const profileImage = document.querySelector('.profile-image');
        const heroImage = document.querySelector('.hero-image');

        if (!profileImage) return;

        // Initial state - hidden for dramatic entrance
        profileImage.style.opacity = '0';
        profileImage.style.transform = 'scale(0.7) translateY(50px) rotateY(15deg)';
        profileImage.style.filter = 'blur(5px)';

        // Create enhanced floating container
        const floatingContainer = document.createElement('div');
        floatingContainer.className = 'floating-profile-container';

        // Wrap the image properly
        const parent = profileImage.parentNode;
        parent.insertBefore(floatingContainer, profileImage);
        floatingContainer.appendChild(profileImage);

        // Add multiple glow layers for depth
        const glowEffect = document.createElement('div');
        glowEffect.className = 'profile-glow-effect';
        floatingContainer.appendChild(glowEffect);

        // Add breathing animation container
        const breathingContainer = document.createElement('div');
        breathingContainer.className = 'breathing-container';
        breathingContainer.style.cssText = `
            position: absolute;
            top: -5px;
            left: -5px;
            right: -5px;
            bottom: -5px;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(52, 152, 219, 0.1) 0%, transparent 70%);
            animation: gentle-breathing 4s ease-in-out infinite;
            z-index: -2;
        `;
        floatingContainer.appendChild(breathingContainer);

        // Dramatic entrance animation sequence
        setTimeout(() => {
            profileImage.style.transition = 'all 1.8s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
            profileImage.style.opacity = '1';
            profileImage.style.transform = 'scale(1) translateY(0) rotateY(0deg)';
            profileImage.style.filter = 'blur(0px)';
        }, 2000);

        // Enhanced hover interactions
        let isHovering = false;

        floatingContainer.addEventListener('mouseenter', function() {
            isHovering = true;
            profileImage.style.transition = 'all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
            profileImage.style.transform = 'scale(1.08) translateY(-8px)';
            profileImage.style.filter = 'brightness(1.1) contrast(1.05)';
            glowEffect.style.opacity = '0.8';
            glowEffect.style.transform = 'scale(1.15)';
        });

        floatingContainer.addEventListener('mouseleave', function() {
            isHovering = false;
            profileImage.style.transition = 'all 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
            profileImage.style.transform = 'scale(1) translateY(0) rotateX(0deg) rotateY(0deg)';
            profileImage.style.filter = 'brightness(1) contrast(1)';
            glowEffect.style.opacity = '0.3';
            glowEffect.style.transform = 'scale(1)';
        });

        // Advanced 3D tilt effect with smooth interpolation
        let currentRotateX = 0;
        let currentRotateY = 0;
        let targetRotateX = 0;
        let targetRotateY = 0;

        floatingContainer.addEventListener('mousemove', function(e) {
            if (!isHovering) return;

            const rect = this.getBoundingClientRect();
            const centerX = rect.left + rect.width / 2;
            const centerY = rect.top + rect.height / 2;

            const deltaX = (e.clientX - centerX) / (rect.width / 2);
            const deltaY = (e.clientY - centerY) / (rect.height / 2);

            targetRotateX = deltaY * -8;
            targetRotateY = deltaX * 8;
        });

        // Smooth interpolation for 3D effect
        function animate3D() {
            currentRotateX += (targetRotateX - currentRotateX) * 0.1;
            currentRotateY += (targetRotateY - currentRotateY) * 0.1;

            if (isHovering) {
                profileImage.style.transform = `
                    scale(1.08)
                    translateY(-8px)
                    rotateX(${currentRotateX}deg)
                    rotateY(${currentRotateY}deg)
                `;
            }

            requestAnimationFrame(animate3D);
        }

        animate3D();
    }
    
    // ========================================
    // ENHANCED STAGGERED TEXT ANIMATIONS
    // ========================================

    function initStaggeredAnimations() {
        const subtitle = document.querySelector('.hero-content h2');
        const description = document.querySelector('.hero-content p');
        const buttons = document.querySelector('.hero-buttons');

        // Enhanced subtitle animation with word-by-word reveal
        if (subtitle) {
            subtitle.style.opacity = '0';
            subtitle.style.transform = 'translateX(-60px) scale(0.95)';
            subtitle.style.filter = 'blur(3px)';

            setTimeout(() => {
                subtitle.style.transition = 'all 1.2s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
                subtitle.style.opacity = '1';
                subtitle.style.transform = 'translateX(0) scale(1)';
                subtitle.style.filter = 'blur(0px)';

                // Add subtle glow effect after animation
                setTimeout(() => {
                    subtitle.style.textShadow = '0 0 20px rgba(52, 152, 219, 0.3)';
                }, 600);
            }, 3000);
        }

        // Enhanced description animation with character reveal
        if (description) {
            description.style.opacity = '0';
            description.style.transform = 'translateX(60px) scale(0.95)';
            description.style.filter = 'blur(3px)';

            setTimeout(() => {
                description.style.transition = 'all 1.4s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
                description.style.opacity = '1';
                description.style.transform = 'translateX(0) scale(1)';
                description.style.filter = 'blur(0px)';
            }, 3800);
        }

        // Enhanced buttons animation with magnetic entrance
        if (buttons) {
            const buttonElements = buttons.querySelectorAll('.btn');

            buttonElements.forEach((btn, index) => {
                btn.style.opacity = '0';
                btn.style.transform = 'translateY(40px) scale(0.8) rotateX(15deg)';
                btn.style.filter = 'blur(2px)';

                setTimeout(() => {
                    btn.style.transition = 'all 0.8s cubic-bezier(0.25, 0.46, 0.45, 0.94)';
                    btn.style.opacity = '1';
                    btn.style.transform = 'translateY(0) scale(1) rotateX(0deg)';
                    btn.style.filter = 'blur(0px)';

                    // Add entrance bounce effect
                    setTimeout(() => {
                        btn.style.transform = 'translateY(-5px) scale(1.02)';
                        setTimeout(() => {
                            btn.style.transform = 'translateY(0) scale(1)';
                        }, 200);
                    }, 400);
                }, 4600 + (index * 300));
            });
        }
    }
    
    // ========================================
    // ENHANCED BUTTON INTERACTIONS
    // ========================================
    
    function initEnhancedButtons() {
        const buttons = document.querySelectorAll('.hero-buttons .btn');
        
        buttons.forEach(button => {
            // Add magnetic effect
            button.addEventListener('mousemove', function(e) {
                const rect = this.getBoundingClientRect();
                const x = e.clientX - rect.left - rect.width / 2;
                const y = e.clientY - rect.top - rect.height / 2;
                
                this.style.transform = `translate(${x * 0.1}px, ${y * 0.1}px) scale(1.05)`;
            });
            
            button.addEventListener('mouseleave', function() {
                this.style.transform = 'translate(0, 0) scale(1)';
            });
            
            // Add ripple effect on click
            button.addEventListener('click', function(e) {
                const ripple = document.createElement('span');
                const rect = this.getBoundingClientRect();
                const size = Math.max(rect.width, rect.height);
                const x = e.clientX - rect.left - size / 2;
                const y = e.clientY - rect.top - size / 2;
                
                ripple.style.width = ripple.style.height = size + 'px';
                ripple.style.left = x + 'px';
                ripple.style.top = y + 'px';
                ripple.classList.add('hero-ripple');
                
                this.appendChild(ripple);
                
                setTimeout(() => {
                    ripple.remove();
                }, 600);
            });
        });
    }
    
    // ========================================
    // ENHANCED PARTICLE BACKGROUND SYSTEM
    // ========================================

    function initParticleEnhancement() {
        const heroSection = document.querySelector('.hero-section');
        if (!heroSection) return;

        // Check if user prefers reduced motion
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
            return;
        }

        // Check if mobile device for performance
        const isMobile = window.innerWidth <= 768;
        const particleCount = isMobile ? 8 : 25;

        // Create floating particles with varied properties
        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            particle.className = 'floating-particle';

            // Randomize particle properties
            const size = Math.random() * 3 + 2;
            const opacity = Math.random() * 0.6 + 0.2;
            const duration = Math.random() * 15 + 15;
            const delay = Math.random() * 10;

            particle.style.cssText = `
                left: ${Math.random() * 100}%;
                width: ${size}px;
                height: ${size}px;
                opacity: ${opacity};
                animation-delay: ${delay}s;
                animation-duration: ${duration}s;
            `;

            heroSection.appendChild(particle);
        }

        // Add interactive particle effect on mouse move
        if (!isMobile) {
            heroSection.addEventListener('mousemove', function(e) {
                const rect = this.getBoundingClientRect();
                const x = ((e.clientX - rect.left) / rect.width) * 100;
                const y = ((e.clientY - rect.top) / rect.height) * 100;

                // Create temporary interactive particle
                const interactiveParticle = document.createElement('div');
                interactiveParticle.className = 'floating-particle';
                interactiveParticle.style.cssText = `
                    left: ${x}%;
                    top: ${y}%;
                    width: 6px;
                    height: 6px;
                    background: rgba(52, 152, 219, 0.8);
                    animation: particle-burst 1s ease-out forwards;
                    pointer-events: none;
                `;

                this.appendChild(interactiveParticle);

                setTimeout(() => {
                    interactiveParticle.remove();
                }, 1000);
            });
        }
    }

    // ========================================
    // BACKGROUND GRADIENT ANIMATION
    // ========================================

    function initBackgroundAnimation() {
        const heroSection = document.querySelector('.hero-section');
        if (!heroSection) return;

        // Add dynamic gradient animation
        let gradientAngle = 135;

        function animateGradient() {
            gradientAngle += 0.5;
            if (gradientAngle >= 360) gradientAngle = 0;

            heroSection.style.background = `
                linear-gradient(${gradientAngle}deg,
                    rgba(44, 62, 80, 0.95) 0%,
                    rgba(52, 152, 219, 0.95) 50%,
                    rgba(231, 76, 60, 0.85) 100%)
            `;

            requestAnimationFrame(animateGradient);
        }

        // Start gradient animation only if not reduced motion
        if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
            animateGradient();
        }
    }
    
    // ========================================
    // INITIALIZE ALL HERO ANIMATIONS
    // ========================================

    // Initialize with proper timing sequence
    setTimeout(() => {
        console.log('🎭 Initializing enhanced hero animations...');

        // Start background animation immediately
        initBackgroundAnimation();

        // Initialize core animations with staggered timing
        setTimeout(() => initAdvancedTypewriter(), 200);
        setTimeout(() => initProfileAnimations(), 400);
        setTimeout(() => initStaggeredAnimations(), 600);
        setTimeout(() => initEnhancedButtons(), 800);
        setTimeout(() => initParticleEnhancement(), 1000);

        console.log('✨ Enhanced hero animations initialized successfully');
    }, 300);
}

// Initialize when DOM is ready and page is loaded
document.addEventListener('DOMContentLoaded', initHeroAnimations);

// Fallback initialization if DOMContentLoaded already fired
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHeroAnimations);
} else {
    initHeroAnimations();
}
