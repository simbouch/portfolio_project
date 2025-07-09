// Advanced Gallery & Photo Display System

class AdvancedGallery {
    constructor() {
        this.currentImageIndex = 0;
        this.images = [];
        this.filteredImages = [];
        this.currentFilter = 'all';
        this.init();
    }

    init() {
        this.createLightboxModal();
        this.bindEvents();
        this.loadGalleryImages();
        this.initializeFilters();
        this.animateGalleryItems();
    }

    createLightboxModal() {
        const modal = document.createElement('div');
        modal.className = 'lightbox-modal';
        modal.id = 'lightboxModal';
        modal.innerHTML = `
            <div class="lightbox-content">
                <button class="lightbox-close" id="lightboxClose">
                    <i class="fas fa-times"></i>
                </button>
                <button class="lightbox-nav lightbox-prev" id="lightboxPrev">
                    <i class="fas fa-chevron-left"></i>
                </button>
                <button class="lightbox-nav lightbox-next" id="lightboxNext">
                    <i class="fas fa-chevron-right"></i>
                </button>
                <img class="lightbox-image" id="lightboxImage" src="" alt="">
                <div class="lightbox-info">
                    <h4 id="lightboxTitle"></h4>
                    <p id="lightboxDescription"></p>
                    <div class="lightbox-meta" id="lightboxMeta"></div>
                </div>
            </div>
        `;
        document.body.appendChild(modal);
    }

    bindEvents() {
        // Gallery item clicks
        document.addEventListener('click', (e) => {
            if (e.target.closest('.gallery-item')) {
                const item = e.target.closest('.gallery-item');
                const index = parseInt(item.dataset.index);
                this.openLightbox(index);
            }
        });

        // Lightbox controls
        document.addEventListener('click', (e) => {
            if (e.target.closest('#lightboxClose') || e.target.id === 'lightboxModal') {
                this.closeLightbox();
            }
            if (e.target.closest('#lightboxPrev')) {
                this.previousImage();
            }
            if (e.target.closest('#lightboxNext')) {
                this.nextImage();
            }
        });

        // Keyboard navigation
        document.addEventListener('keydown', (e) => {
            const modal = document.getElementById('lightboxModal');
            if (modal.classList.contains('active')) {
                switch(e.key) {
                    case 'Escape':
                        this.closeLightbox();
                        break;
                    case 'ArrowLeft':
                        this.previousImage();
                        break;
                    case 'ArrowRight':
                        this.nextImage();
                        break;
                }
            }
        });

        // Filter buttons
        document.addEventListener('click', (e) => {
            const filterBtn = e.target.closest('.filter-btn');
            if (filterBtn) {
                const filter = filterBtn.dataset.filter;
                this.filterImages(filter);
                this.updateFilterButtons(filterBtn);
            }
        });

        // Touch/swipe support for mobile
        this.addTouchSupport();
    }

    loadGalleryImages() {
        const galleryItems = document.querySelectorAll('.gallery-item');

        this.images = Array.from(galleryItems).map((item, index) => {
            const img = item.querySelector('img');
            const title = item.querySelector('.gallery-overlay h5')?.textContent || 'Untitled';
            const description = item.querySelector('.gallery-overlay p')?.textContent || '';
            const category = item.dataset.category || 'all';

            item.dataset.index = index;

            return {
                src: img.src,
                alt: img.alt,
                title: title,
                description: description,
                category: category,
                element: item
            };
        });

        this.filteredImages = [...this.images];
    }

    openLightbox(index) {
        this.currentImageIndex = index;
        const image = this.filteredImages[index];
        
        const modal = document.getElementById('lightboxModal');
        const lightboxImage = document.getElementById('lightboxImage');
        const lightboxTitle = document.getElementById('lightboxTitle');
        const lightboxDescription = document.getElementById('lightboxDescription');
        const lightboxMeta = document.getElementById('lightboxMeta');
        
        lightboxImage.src = image.src;
        lightboxImage.alt = image.alt;
        lightboxTitle.textContent = image.title;
        lightboxDescription.textContent = image.description;
        
        // Add metadata
        lightboxMeta.innerHTML = `
            <span><i class="fas fa-tag me-1"></i>${image.category}</span>
            <span><i class="fas fa-camera me-1"></i>Photography</span>
            <span><i class="fas fa-eye me-1"></i>View ${index + 1} of ${this.filteredImages.length}</span>
        `;
        
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
        
        // Preload adjacent images
        this.preloadAdjacentImages(index);
    }

    closeLightbox() {
        const modal = document.getElementById('lightboxModal');
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }

    previousImage() {
        if (this.currentImageIndex > 0) {
            this.currentImageIndex--;
        } else {
            this.currentImageIndex = this.filteredImages.length - 1;
        }
        this.updateLightboxImage();
    }

    nextImage() {
        if (this.currentImageIndex < this.filteredImages.length - 1) {
            this.currentImageIndex++;
        } else {
            this.currentImageIndex = 0;
        }
        this.updateLightboxImage();
    }

    updateLightboxImage() {
        const image = this.filteredImages[this.currentImageIndex];
        const lightboxImage = document.getElementById('lightboxImage');
        const lightboxTitle = document.getElementById('lightboxTitle');
        const lightboxDescription = document.getElementById('lightboxDescription');
        const lightboxMeta = document.getElementById('lightboxMeta');
        
        // Fade out
        lightboxImage.style.opacity = '0';
        
        setTimeout(() => {
            lightboxImage.src = image.src;
            lightboxImage.alt = image.alt;
            lightboxTitle.textContent = image.title;
            lightboxDescription.textContent = image.description;
            
            lightboxMeta.innerHTML = `
                <span><i class="fas fa-tag me-1"></i>${image.category}</span>
                <span><i class="fas fa-camera me-1"></i>Photography</span>
                <span><i class="fas fa-eye me-1"></i>View ${this.currentImageIndex + 1} of ${this.filteredImages.length}</span>
            `;
            
            // Fade in
            lightboxImage.style.opacity = '1';
        }, 200);
        
        this.preloadAdjacentImages(this.currentImageIndex);
    }

    preloadAdjacentImages(index) {
        const preloadIndexes = [index - 1, index + 1];
        preloadIndexes.forEach(i => {
            if (i >= 0 && i < this.filteredImages.length) {
                const img = new Image();
                img.src = this.filteredImages[i].src;
            }
        });
    }

    filterImages(filter) {
        this.currentFilter = filter;

        if (filter === 'all') {
            this.filteredImages = [...this.images];
        } else {
            this.filteredImages = this.images.filter(img => img.category === filter);
        }

        // Update gallery display with improved animation
        this.images.forEach((image, index) => {
            const shouldShow = filter === 'all' || image.category === filter;
            const element = image.element;

            // Reset any existing transitions
            element.style.transition = 'all 0.3s ease';

            if (shouldShow) {
                element.style.display = 'block';
                element.style.opacity = '0';
                element.style.transform = 'translateY(20px) scale(0.9)';

                // Animate in with staggered delay
                setTimeout(() => {
                    element.style.opacity = '1';
                    element.style.transform = 'translateY(0) scale(1)';
                }, index * 100);
            } else {
                element.style.opacity = '0';
                element.style.transform = 'translateY(-20px) scale(0.9)';
                setTimeout(() => {
                    element.style.display = 'none';
                }, 300);
            }
        });

        // Update filtered image indexes
        this.updateFilteredIndexes();
    }

    updateFilteredIndexes() {
        this.filteredImages.forEach((image, index) => {
            image.element.dataset.filteredIndex = index;
        });
    }

    updateFilterButtons(activeButton) {
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        activeButton.classList.add('active');
    }

    initializeFilters() {
        // Set initial active filter
        const allButton = document.querySelector('.filter-btn[data-filter="all"]');
        if (allButton) {
            allButton.classList.add('active');
        }
    }

    animateGalleryItems() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.classList.add('animate');
                    }, index * 100);
                }
            });
        }, { threshold: 0.1 });

        document.querySelectorAll('.gallery-item.loading').forEach(item => {
            observer.observe(item);
        });
    }

    addTouchSupport() {
        let startX = 0;
        let startY = 0;
        
        document.addEventListener('touchstart', (e) => {
            startX = e.touches[0].clientX;
            startY = e.touches[0].clientY;
        });
        
        document.addEventListener('touchend', (e) => {
            if (!document.getElementById('lightboxModal').classList.contains('active')) return;
            
            const endX = e.changedTouches[0].clientX;
            const endY = e.changedTouches[0].clientY;
            const diffX = startX - endX;
            const diffY = startY - endY;
            
            // Horizontal swipe
            if (Math.abs(diffX) > Math.abs(diffY) && Math.abs(diffX) > 50) {
                if (diffX > 0) {
                    this.nextImage();
                } else {
                    this.previousImage();
                }
            }
            
            // Vertical swipe down to close
            if (diffY < -100) {
                this.closeLightbox();
            }
        });
    }
}

// Initialize gallery when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    // Only initialize if we're on a page with gallery items
    if (document.querySelector('.gallery-item')) {
        new AdvancedGallery();
    }
});

// Add some CSS for smooth transitions
const style = document.createElement('style');
style.textContent = `
    .lightbox-image {
        transition: opacity 0.3s ease;
    }

    .gallery-item {
        transition: opacity 0.3s ease, transform 0.3s ease;
    }
`;
document.head.appendChild(style);

// Simple fallback filtering system
function simpleGalleryFilter() {
    // Add click listeners to filter buttons
    document.querySelectorAll('.filter-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const filter = this.dataset.filter;

            // Update active button
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            this.classList.add('active');

            // Filter gallery items
            document.querySelectorAll('.gallery-item').forEach(item => {
                const category = item.dataset.category;
                const shouldShow = filter === 'all' || category === filter;

                if (shouldShow) {
                    item.style.display = 'block';
                    item.style.opacity = '1';
                    item.style.transform = 'translateY(0)';
                } else {
                    item.style.opacity = '0';
                    item.style.transform = 'translateY(20px)';
                    setTimeout(() => {
                        item.style.display = 'none';
                    }, 300);
                }
            });
        });
    });

    // Set initial active state
    const allButton = document.querySelector('.filter-btn[data-filter="all"]');
    if (allButton) {
        allButton.classList.add('active');
    }
}

// Initialize simple filter as backup
document.addEventListener('DOMContentLoaded', () => {
    // Wait a bit for the main gallery to initialize
    setTimeout(() => {
        if (document.querySelector('.gallery-item') && document.querySelector('.filter-btn')) {
            simpleGalleryFilter();
        }
    }, 1000);
});
