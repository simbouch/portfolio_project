// Debug script to test project buttons

console.log('🔧 Debug Buttons Script Loading...');

document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 DOM loaded, checking project buttons...');
    
    // Find all project buttons
    const viewCodeButtons = document.querySelectorAll('a[href*="github"]');
    const demoButtons = document.querySelectorAll('a[href*="demo"]');
    
    console.log(`Found ${viewCodeButtons.length} GitHub buttons`);
    console.log(`Found ${demoButtons.length} demo buttons`);
    
    // Add click listeners to GitHub buttons
    viewCodeButtons.forEach((button, index) => {
        const href = button.getAttribute('href');
        console.log(`GitHub Button ${index + 1}: ${href}`);
        
        button.addEventListener('click', function(e) {
            console.log(`🔗 GitHub button clicked: ${href}`);
            
            // Check if href is valid
            if (!href || href === '#' || href === '') {
                e.preventDefault();
                console.error('❌ Invalid GitHub URL:', href);
                alert('GitHub URL is missing or invalid!');
                return false;
            }
            
            // Check if it's a valid GitHub URL
            if (!href.includes('github.com')) {
                console.warn('⚠️ Not a GitHub URL:', href);
            }
            
            console.log('✅ Opening GitHub URL:', href);
        });
    });
    
    // Add click listeners to demo buttons
    demoButtons.forEach((button, index) => {
        const href = button.getAttribute('href');
        console.log(`Demo Button ${index + 1}: ${href}`);
        
        button.addEventListener('click', function(e) {
            console.log(`🔗 Demo button clicked: ${href}`);
            
            if (!href || href === '#' || href === '') {
                e.preventDefault();
                console.error('❌ Invalid demo URL:', href);
                alert('Demo URL is missing or invalid!');
                return false;
            }
            
            console.log('✅ Opening demo URL:', href);
        });
    });
    
    // Check for any buttons with empty or invalid hrefs
    const allProjectButtons = document.querySelectorAll('.btn[href], a.btn');
    let invalidButtons = 0;
    
    allProjectButtons.forEach((button, index) => {
        const href = button.getAttribute('href');
        if (!href || href === '#' || href === '' || href === 'None') {
            invalidButtons++;
            console.error(`❌ Invalid button ${index + 1}:`, button.textContent.trim(), 'href:', href);
            
            // Highlight invalid buttons
            button.style.border = '2px solid red';
            button.style.backgroundColor = '#ffebee';
            button.title = 'Invalid URL - check console for details';
        }
    });
    
    if (invalidButtons > 0) {
        console.error(`❌ Found ${invalidButtons} buttons with invalid URLs`);
    } else {
        console.log('✅ All buttons have valid URLs');
    }
    
    // Test if buttons are clickable (not blocked by CSS or other elements)
    const testButton = document.querySelector('a[href*="github"]');
    if (testButton) {
        const styles = window.getComputedStyle(testButton);
        console.log('Button styles:', {
            pointerEvents: styles.pointerEvents,
            display: styles.display,
            visibility: styles.visibility,
            zIndex: styles.zIndex
        });
    }
    
    console.log('🎉 Button debugging complete!');
});

// Add CSS to highlight problematic buttons
const style = document.createElement('style');
style.textContent = `
    .btn[href="#"], .btn[href=""], .btn[href="None"] {
        border: 2px solid red !important;
        background-color: #ffebee !important;
        cursor: not-allowed !important;
    }
    
    .btn[href="#"]:hover, .btn[href=""]:hover, .btn[href="None"]:hover {
        background-color: #ffcdd2 !important;
    }
`;
document.head.appendChild(style);

console.log('✅ Debug Buttons Script Loaded Successfully!');
