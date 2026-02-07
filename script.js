// Mobile Navigation
const burger = document.querySelector('.burger');
const nav = document.querySelector('.nav-links');
const navLinks = document.querySelectorAll('.nav-links li');

burger.addEventListener('click', () => {
    // Toggle Nav
    nav.classList.toggle('nav-active');
    
    // Animate Links
    navLinks.forEach((link, index) => {
        if (link.style.animation) {
            link.style.animation = '';
        } else {
            link.style.animation = `navLinkFade 0.5s ease forwards ${index / 7 + 0.3}s`;
        }
    });
    
    // Burger Animation
    burger.classList.toggle('toggle');
});

// Navbar scroll effect
window.addEventListener('scroll', () => {
    const header = document.querySelector('header');
    if (window.scrollY > 100) {
        header.style.padding = '0.7rem 5%';
        header.style.backgroundColor = 'rgba(10, 25, 47, 0.98)';
    } else {
        header.style.padding = '1rem 5%';
        header.style.backgroundColor = 'rgba(10, 25, 47, 0.95)';
    }
});

// Smooth Scrolling for Navigation Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
            // Close mobile menu if open
            nav.classList.remove('nav-active');
        }
    });
});

// Progress bar animation on scroll
const progressBars = document.querySelectorAll('.progress');
const progressObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const progress = entry.target;
            const width = progress.style.width;
            progress.style.width = '0%';
            setTimeout(() => {
                progress.style.width = width;
            }, 100);
        }
    });
}, { threshold: 0.5 });

progressBars.forEach(bar => {
    progressObserver.observe(bar);
});

// Profile image slider rotation
const profileImages = document.querySelectorAll('.profile-slider img');
let currentImageIndex = 0;

if (profileImages.length > 0) {
    setInterval(() => {
        profileImages[currentImageIndex].style.opacity = '0';
        currentImageIndex = (currentImageIndex + 1) % profileImages.length;
        profileImages[currentImageIndex].style.opacity = '1';
    }, 3000);
}

// Particle effect for hero section (optional enhancement)
function createParticle() {
    const particle = document.createElement('div');
    particle.style.cssText = `
        position: fixed;
        width: 4px;
        height: 4px;
        background: rgba(100, 255, 218, 0.3);
        border-radius: 50%;
        pointer-events: none;
        z-index: 0;
        animation: particleFloat ${Math.random() * 3 + 2}s linear forwards;
    `;
    
    const startX = Math.random() * window.innerWidth;
    particle.style.left = startX + 'px';
    particle.style.top = window.innerHeight + 'px';
    
    document.body.appendChild(particle);
    
    setTimeout(() => {
        particle.remove();
    }, 5000);
}

// Add particle animation keyframes
const style = document.createElement('style');
style.textContent = `
    @keyframes particleFloat {
        0% {
            transform: translateY(0) translateX(0);
            opacity: 1;
        }
        100% {
            transform: translateY(-100vh) translateX(${Math.random() * 100 - 50}px);
            opacity: 0;
        }
    }
    
    @keyframes navLinkFade {
        from {
            opacity: 0;
            transform: translateX(50px);
        }
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
    
    .burger.toggle .line1 {
        transform: rotate(45deg) translate(5px, 5px);
    }
    
    .burger.toggle .line2 {
        opacity: 0;
    }
    
    .burger.toggle .line3 {
        transform: rotate(-45deg) translate(5px, -5px);
    }
`;
document.head.appendChild(style);

// Create particles periodically
setInterval(createParticle, 300);

// Typing effect enhancement for hero subtitle
const subtitle = document.querySelector('.subtitle');
if (subtitle && subtitle.classList.contains('typing-effect')) {
    // Remove cursor after typing animation
    setTimeout(() => {
        subtitle.style.borderRight = 'none';
    }, 3500);
}

// Contact form validation and enhancement
const contactForm = document.getElementById('contact-form');
if (contactForm) {
    const inputs = contactForm.querySelectorAll('input, textarea');
    
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.style.transform = 'scale(1.02)';
        });
        
        input.addEventListener('blur', function() {
            this.parentElement.style.transform = 'scale(1)';
        });
    });
    
    contactForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get form values
        const name = this.querySelector('input[type="text"]').value.trim();
        const email = this.querySelector('input[type="email"]').value.trim();
        const message = this.querySelector('textarea').value.trim();
        
        // Basic validation
        if (!name || !email || !message) {
            alert('Please fill in all fields.');
            return;
        }
        
        if (!isValidEmail(email)) {
            alert('Please enter a valid email address.');
            return;
        }
        
        // Here you would typically send the form data to a server
        console.log('Form submitted:', { name, email, message });
        
        // Show success message with animation
        const submitBtn = this.querySelector('.submit-button');
        const originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<i class="fas fa-check"></i> Message Sent!';
        submitBtn.style.background = 'linear-gradient(135deg, #00ff88, #00cc6a)';
        
        setTimeout(() => {
            submitBtn.innerHTML = originalText;
            submitBtn.style.background = '';
            this.reset();
        }, 3000);
    });
}

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Social links hover enhancement
document.querySelectorAll('.social-links a').forEach(link => {
    link.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-8px) scale(1.1)';
    });
    
    link.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
    });
});

// Project cards hover effect
document.querySelectorAll('.project-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-15px) scale(1.02)';
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0) scale(1)';
    });
});

// CS skill cards click effect
document.querySelectorAll('.cs-skill-card').forEach(card => {
    card.addEventListener('click', function() {
        this.style.transform = 'scale(0.95)';
        setTimeout(() => {
            this.style.transform = 'scale(1.05)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 200);
        }, 100);
    });
});

// Framework tags hover effect
document.querySelectorAll('.framework-tag').forEach(tag => {
    tag.addEventListener('mouseenter', function() {
        this.style.transform = 'scale(1.1) rotate(3deg)';
    });
    
    tag.addEventListener('mouseleave', function() {
        this.style.transform = 'scale(1) rotate(0)';
    });
});

// Education cards hover effect
document.querySelectorAll('.education-card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.style.borderLeftColor = '#57cbff';
        this.querySelector('i').style.transform = 'scale(1.2) rotate(360deg)';
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.borderLeftColor = '#64ffda';
        this.querySelector('i').style.transform = 'scale(1) rotate(0)';
    });
});

// Add loading animation
window.addEventListener('load', () => {
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.5s ease';
    setTimeout(() => {
        document.body.style.opacity = '1';
    }, 100);
});

// Console welcome message
console.log('%c Welcome to Talent\'s Portfolio! ', 'background: #64ffda; color: #0a192f; font-size: 20px; font-weight: bold; padding: 10px;');
console.log('%c Computer Science Student & Developer ', 'background: #0a192f; color: #64ffda; font-size: 14px; padding: 5px;');
console.log('%c Feel free to explore! ', 'background: #112240; color: #ccd6f6; font-size: 12px; padding: 5px;');
