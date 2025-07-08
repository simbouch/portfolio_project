// Project Filtering System

class ProjectFilter {
    constructor() {
        this.projects = [];
        this.currentFilter = 'all';
        this.init();
    }

    init() {
        this.loadProjects();
        this.bindEvents();
        this.animateProjects();
        this.setInitialFilter();
    }

    loadProjects() {
        const projectCards = document.querySelectorAll('.project-card[data-type]');
        this.projects = Array.from(projectCards).map((card, index) => {
            const type = card.dataset.type || 'all';
            card.dataset.index = index;
            return {
                element: card,
                type: type,
                index: index
            };
        });
        console.log('Loaded projects:', this.projects.length);
    }

    bindEvents() {
        // Filter button clicks
        document.addEventListener('click', (e) => {
            const filterBtn = e.target.closest('.filter-btn');
            if (filterBtn && filterBtn.dataset.filter) {
                const filter = filterBtn.dataset.filter;
                console.log('Project filter clicked:', filter);
                this.filterProjects(filter);
                this.updateFilterButtons(filterBtn);
            }
        });
    }

    filterProjects(filter) {
        this.currentFilter = filter;
        console.log('Filtering projects by:', filter);

        this.projects.forEach((project, index) => {
            const shouldShow = filter === 'all' || project.type === filter;
            const element = project.element;

            // Add transition for smooth animation
            element.style.transition = 'all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275)';

            if (shouldShow) {
                // Show the project with animation
                element.style.display = 'block';
                element.style.opacity = '0';
                element.style.transform = 'translateY(30px) scale(0.9)';

                // Animate in with staggered delay
                setTimeout(() => {
                    element.style.opacity = '1';
                    element.style.transform = 'translateY(0) scale(1)';
                }, index * 100);
            } else {
                // Hide the project with animation
                element.style.opacity = '0';
                element.style.transform = 'translateY(-30px) scale(0.9)';
                
                setTimeout(() => {
                    element.style.display = 'none';
                }, 400);
            }
        });

        // Update the count display
        this.updateProjectCount(filter);
    }

    updateFilterButtons(activeButton) {
        // Remove active class from all buttons
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.classList.remove('active');
            btn.classList.add('btn-outline-primary');
            btn.classList.remove('btn-primary');
        });

        // Add active class to clicked button
        activeButton.classList.add('active');
        activeButton.classList.remove('btn-outline-primary');
        activeButton.classList.add('btn-primary');
    }

    updateProjectCount(filter) {
        const visibleCount = this.projects.filter(project => 
            filter === 'all' || project.type === filter
        ).length;

        // Update or create count display
        let countDisplay = document.querySelector('.project-count');
        if (!countDisplay) {
            countDisplay = document.createElement('div');
            countDisplay.className = 'project-count text-center mt-3';
            const filtersContainer = document.querySelector('.btn-group').parentElement;
            filtersContainer.appendChild(countDisplay);
        }

        const totalCount = this.projects.length;
        const filterName = filter === 'all' ? 'All Projects' : 
                          filter.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase());
        
        countDisplay.innerHTML = `
            <small class="text-muted">
                <i class="fas fa-filter me-1"></i>
                Showing ${visibleCount} of ${totalCount} projects in "${filterName}"
            </small>
        `;
    }

    setInitialFilter() {
        // Set the "All Projects" button as active initially
        const allButton = document.querySelector('.filter-btn[data-filter="all"]');
        if (allButton) {
            allButton.classList.add('active');
            allButton.classList.remove('btn-outline-primary');
            allButton.classList.add('btn-primary');
        }
        this.updateProjectCount('all');
    }

    animateProjects() {
        // Animate projects on page load
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.classList.add('animate');
                        entry.target.style.opacity = '1';
                        entry.target.style.transform = 'translateY(0)';
                    }, index * 100);
                }
            });
        }, { threshold: 0.1 });

        this.projects.forEach(project => {
            project.element.style.opacity = '0';
            project.element.style.transform = 'translateY(30px)';
            project.element.style.transition = 'all 0.6s ease';
            observer.observe(project.element);
        });
    }
}

// Initialize project filtering when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Only initialize if we're on the projects page
    if (document.querySelector('.project-card')) {
        console.log('Initializing project filtering...');
        new ProjectFilter();
        console.log('Project filtering initialized');
    } else {
        console.log('No project cards found, skipping project filter initialization');
    }
});

// Simple fallback project filtering
function simpleProjectFilter() {
    console.log('Setting up simple project filter...');

    document.querySelectorAll('.filter-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const filter = this.dataset.filter;
            console.log('Simple project filter clicked:', filter);

            // Update active button
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.remove('active', 'btn-primary');
                btn.classList.add('btn-outline-primary');
            });
            this.classList.add('active', 'btn-primary');
            this.classList.remove('btn-outline-primary');

            // Filter project cards
            document.querySelectorAll('.project-card').forEach(card => {
                const type = card.dataset.type;
                const shouldShow = filter === 'all' || type === filter;

                if (shouldShow) {
                    card.style.display = 'block';
                    card.style.opacity = '1';
                    card.style.transform = 'translateY(0)';
                } else {
                    card.style.opacity = '0';
                    card.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        card.style.display = 'none';
                    }, 300);
                }
            });
        });
    });
}

// Initialize simple filter as backup
setTimeout(() => {
    if (document.querySelector('.project-card') && document.querySelector('.filter-btn')) {
        simpleProjectFilter();
        console.log('Simple project filter initialized as backup');
    }
}, 1500);

// Add some additional CSS for smooth transitions
const style = document.createElement('style');
style.textContent = `
    .project-card {
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
    
    .filter-btn {
        transition: all 0.3s ease;
        margin: 0 5px 10px 0;
    }
    
    .filter-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
    }
    
    .filter-btn.active {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(52, 152, 219, 0.4);
    }
    
    .project-count {
        animation: fadeIn 0.5s ease;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
`;
document.head.appendChild(style);
