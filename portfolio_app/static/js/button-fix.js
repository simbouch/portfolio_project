// CRITICAL BUTTON FIX - Ensures all project buttons work
document.addEventListener('DOMContentLoaded', function() {
    console.log('🔧 Button Fix Loading...');
    
    // Find all project buttons
    const projectButtons = document.querySelectorAll('.project-card .btn, .project-card a.btn');
    console.log(`Found ${projectButtons.length} project buttons`);
    
    projectButtons.forEach((button, index) => {
        console.log(`Fixing button ${index + 1}: ${button.textContent.trim()}`);
        
        // Ensure button is clickable
        button.style.pointerEvents = 'auto';
        button.style.cursor = 'pointer';
        button.style.position = 'relative';
        button.style.zIndex = '10';
        
        // Get the URL from href attribute
        const url = button.getAttribute('href');
        
        if (url && url !== '#') {
            console.log(`Button ${index + 1} URL: ${url}`);
            
            // Add click handler
            button.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                
                console.log(`🚀 Opening: ${url}`);
                window.open(url, '_blank', 'noopener,noreferrer');
            });
            
            // Add hover effect
            button.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-2px)';
                this.style.boxShadow = '0 4px 8px rgba(0,0,0,0.2)';
            });
            
            button.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
                this.style.boxShadow = '';
            });
        } else {
            console.warn(`Button ${index + 1} has no valid URL`);
        }
    });
    
    console.log('✅ Button Fix Complete!');
});
