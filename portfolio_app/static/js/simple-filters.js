// Simple, Reliable Filtering System for Gallery and Projects

console.log('🔧 Simple Filters Loading...');

// Gallery Filtering System
function initGalleryFilters() {
    console.log('🖼️ Initializing Gallery Filters...');
    
    const filterButtons = document.querySelectorAll('.photo-filters .filter-btn');
    const galleryItems = document.querySelectorAll('.gallery-item');
    
    console.log(`Found ${filterButtons.length} filter buttons and ${galleryItems.length} gallery items`);
    
    if (filterButtons.length === 0 || galleryItems.length === 0) {
        console.log('❌ No gallery elements found, skipping gallery filters');
        return;
    }
    
    // Add click listeners to filter buttons
    filterButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const filter = this.getAttribute('data-filter');
            console.log(`🎯 Gallery filter clicked: "${filter}"`);
            
            // Update active button state
            filterButtons.forEach(btn => {
                btn.classList.remove('active');
                btn.style.backgroundColor = '';
                btn.style.color = '';
                btn.style.borderColor = '';
            });
            
            // Set active button style
            this.classList.add('active');
            this.style.backgroundColor = '#3498db';
            this.style.color = 'white';
            this.style.borderColor = '#3498db';
            this.style.transform = 'translateY(-2px)';
            this.style.boxShadow = '0 4px 15px rgba(52, 152, 219, 0.4)';
            
            // Filter gallery items
            let visibleCount = 0;
            galleryItems.forEach((item, index) => {
                const category = item.getAttribute('data-category');
                const shouldShow = filter === 'all' || category === filter;
                
                console.log(`Item ${index}: category="${category}", shouldShow=${shouldShow}`);
                
                if (shouldShow) {
                    visibleCount++;
                    item.style.display = 'block';
                    item.style.opacity = '0';
                    item.style.transform = 'translateY(20px) scale(0.9)';
                    
                    // Animate in with delay
                    setTimeout(() => {
                        item.style.transition = 'all 0.5s ease';
                        item.style.opacity = '1';
                        item.style.transform = 'translateY(0) scale(1)';
                    }, index * 100);
                } else {
                    item.style.transition = 'all 0.3s ease';
                    item.style.opacity = '0';
                    item.style.transform = 'translateY(-20px) scale(0.9)';
                    
                    setTimeout(() => {
                        item.style.display = 'none';
                    }, 300);
                }
            });
            
            console.log(`✅ Gallery filtered: ${visibleCount} items visible`);
            
            // Update count display
            updateGalleryCount(filter, visibleCount, galleryItems.length);
        });
    });
    
    // Set initial active state
    const allButton = document.querySelector('.photo-filters .filter-btn[data-filter="all"]');
    if (allButton) {
        allButton.click();
    }
    
    console.log('✅ Gallery filters initialized successfully');
}

// Project Filtering System
function initProjectFilters() {
    console.log('📁 Initializing Project Filters...');
    
    const filterButtons = document.querySelectorAll('.btn-group .filter-btn, .btn-group .btn');
    const projectCards = document.querySelectorAll('.project-card[data-type]');
    
    console.log(`Found ${filterButtons.length} filter buttons and ${projectCards.length} project cards`);
    
    if (filterButtons.length === 0 || projectCards.length === 0) {
        console.log('❌ No project elements found, skipping project filters');
        return;
    }
    
    // Add click listeners to filter buttons
    filterButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const filter = this.getAttribute('data-filter');
            if (!filter) return; // Skip buttons without data-filter
            
            console.log(`🎯 Project filter clicked: "${filter}"`);
            
            // Update active button state
            filterButtons.forEach(btn => {
                btn.classList.remove('active', 'btn-primary');
                btn.classList.add('btn-outline-primary');
                btn.style.transform = '';
                btn.style.boxShadow = '';
            });
            
            // Set active button style
            this.classList.add('active', 'btn-primary');
            this.classList.remove('btn-outline-primary');
            this.style.transform = 'translateY(-2px)';
            this.style.boxShadow = '0 4px 15px rgba(52, 152, 219, 0.4)';
            
            // Filter project cards
            let visibleCount = 0;
            projectCards.forEach((card, index) => {
                const type = card.getAttribute('data-type');
                const shouldShow = filter === 'all' || type === filter;
                
                console.log(`Project ${index}: type="${type}", shouldShow=${shouldShow}`);
                
                if (shouldShow) {
                    visibleCount++;
                    card.style.display = 'block';
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(30px) scale(0.9)';
                    
                    // Animate in with delay
                    setTimeout(() => {
                        card.style.transition = 'all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
                        card.style.opacity = '1';
                        card.style.transform = 'translateY(0) scale(1)';
                    }, index * 150);
                } else {
                    card.style.transition = 'all 0.3s ease';
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(-30px) scale(0.9)';
                    
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            });
            
            console.log(`✅ Projects filtered: ${visibleCount} items visible`);
            
            // Update count display
            updateProjectCount(filter, visibleCount, projectCards.length);
        });
    });
    
    // Set initial active state
    const allButton = document.querySelector('.btn-group .filter-btn[data-filter="all"], .btn-group .btn[data-filter="all"]');
    if (allButton) {
        allButton.click();
    }
    
    console.log('✅ Project filters initialized successfully');
}

// Update gallery count display
function updateGalleryCount(filter, visible, total) {
    let countDisplay = document.querySelector('.gallery-count');
    if (!countDisplay) {
        countDisplay = document.createElement('div');
        countDisplay.className = 'gallery-count text-center mt-3 mb-4';
        const filtersContainer = document.querySelector('.photo-filters');
        if (filtersContainer) {
            filtersContainer.parentNode.insertBefore(countDisplay, filtersContainer.nextSibling);
        }
    }
    
    const filterName = filter === 'all' ? 'All Photos' : 
                      filter.charAt(0).toUpperCase() + filter.slice(1);
    
    countDisplay.innerHTML = `
        <div class="alert alert-info">
            <i class="fas fa-filter me-2"></i>
            <strong>${filterName}</strong>: Showing ${visible} of ${total} photos
        </div>
    `;
}

// Update project count display
function updateProjectCount(filter, visible, total) {
    let countDisplay = document.querySelector('.project-count');
    if (!countDisplay) {
        countDisplay = document.createElement('div');
        countDisplay.className = 'project-count text-center mt-3 mb-4';
        const filtersContainer = document.querySelector('.btn-group');
        if (filtersContainer) {
            filtersContainer.parentNode.insertBefore(countDisplay, filtersContainer.nextSibling);
        }
    }
    
    const filterName = filter === 'all' ? 'All Projects' : 
                      filter.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase());
    
    countDisplay.innerHTML = `
        <div class="alert alert-success">
            <i class="fas fa-project-diagram me-2"></i>
            <strong>${filterName}</strong>: Showing ${visible} of ${total} projects
        </div>
    `;
}

// Initialize everything when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    console.log('🚀 DOM loaded, initializing filters...');
    
    // Wait a moment for other scripts to load
    setTimeout(() => {
        // Initialize gallery filters if on gallery page
        if (document.querySelector('.gallery-item')) {
            initGalleryFilters();
        }
        
        // Initialize project filters if on projects page
        if (document.querySelector('.project-card[data-type]')) {
            initProjectFilters();
        }
        
        console.log('🎉 All filters initialized!');
    }, 500);
});

// Also try to initialize on window load as backup
window.addEventListener('load', function() {
    setTimeout(() => {
        if (document.querySelector('.gallery-item') && !document.querySelector('.gallery-count')) {
            console.log('🔄 Backup: Initializing gallery filters...');
            initGalleryFilters();
        }
        
        if (document.querySelector('.project-card[data-type]') && !document.querySelector('.project-count')) {
            console.log('🔄 Backup: Initializing project filters...');
            initProjectFilters();
        }
    }, 1000);
});

console.log('✅ Simple Filters Script Loaded Successfully!');
