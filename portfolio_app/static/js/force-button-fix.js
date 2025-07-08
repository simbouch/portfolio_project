// Force fix for project buttons - guaranteed to work
console.log('🔧 Force Button Fix Loading...');

document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 Forcing button fixes...');
    
    // Wait a moment for page to fully load
    setTimeout(function() {
        // Find all project buttons and fix them
        const projectButtons = document.querySelectorAll('.btn');
        let fixedButtons = 0;
        
        projectButtons.forEach(function(button, index) {
            const buttonText = button.textContent.trim();
            
            // Fix "View Code" buttons
            if (buttonText.includes('View Code') || buttonText.includes('Explore Code')) {
                // Remove any existing click handlers
                button.onclick = null;
                
                // Add new working click handler
                button.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    
                    console.log('🔗 Button clicked:', buttonText);
                    
                    // Open GitHub profile in new tab
                    window.open('https://github.com/simbouch', '_blank', 'noopener,noreferrer');
                    
                    return false;
                });
                
                // Also fix the href attribute
                button.href = 'https://github.com/simbouch';
                button.target = '_blank';
                button.rel = 'noopener noreferrer';
                
                // Visual indicator that button is fixed
                button.style.borderColor = '#28a745';
                button.title = 'Fixed - Opens GitHub Profile';
                
                fixedButtons++;
                console.log(`✅ Fixed button ${index + 1}: ${buttonText}`);
            }
            
            // Fix "Live Demo" buttons
            if (buttonText.includes('Live Demo') || buttonText.includes('GitHub Profile')) {
                button.onclick = null;
                
                button.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    
                    console.log('🔗 Demo button clicked:', buttonText);
                    window.open('https://github.com/simbouch', '_blank', 'noopener,noreferrer');
                    
                    return false;
                });
                
                button.href = 'https://github.com/simbouch';
                button.target = '_blank';
                button.rel = 'noopener noreferrer';
                button.style.borderColor = '#007bff';
                button.title = 'Fixed - Opens GitHub Profile';
                
                fixedButtons++;
                console.log(`✅ Fixed demo button ${index + 1}: ${buttonText}`);
            }
        });
        
        console.log(`🎉 Fixed ${fixedButtons} buttons total`);
        
        // Add visual indicator to page
        const indicator = document.createElement('div');
        indicator.innerHTML = `
            <div style="position: fixed; top: 10px; right: 10px; background: #28a745; color: white; padding: 10px; border-radius: 5px; z-index: 9999; font-size: 12px;">
                ✅ ${fixedButtons} buttons fixed!
            </div>
        `;
        document.body.appendChild(indicator);
        
        // Remove indicator after 3 seconds
        setTimeout(() => {
            indicator.remove();
        }, 3000);
        
    }, 1000);
});

// Also add click handler to document for any missed buttons
document.addEventListener('click', function(e) {
    const target = e.target.closest('.btn');
    if (target) {
        const buttonText = target.textContent.trim();
        
        if (buttonText.includes('View Code') || buttonText.includes('Explore Code') || 
            buttonText.includes('Live Demo') || buttonText.includes('GitHub Profile')) {
            
            console.log('🔗 Fallback click handler:', buttonText);
            
            // Force open GitHub
            e.preventDefault();
            e.stopPropagation();
            window.open('https://github.com/simbouch', '_blank', 'noopener,noreferrer');
            
            return false;
        }
    }
});

console.log('✅ Force Button Fix Script Loaded!');
