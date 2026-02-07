// Project Cards Toggle Functionality
function toggleProject(button) {
    const projectCard = button.closest('.project-card');
    const projectContent = projectCard.querySelector('.project-content');
    
    if (projectContent.classList.contains('hidden')) {
        // Show project details
        projectContent.classList.remove('hidden');
        button.textContent = 'Show Less';
        button.style.background = 'linear-gradient(135deg, #00bfa5, #57cbff)';
        
        // Add slide animation
        projectContent.style.animation = 'slideDown 0.4s ease forwards';
    } else {
        // Hide project details
        projectContent.classList.add('hidden');
        button.textContent = 'Click Here';
        button.style.background = 'linear-gradient(135deg, #64ffda, #00bfa5)';
    }
}

// Add slide animation keyframes
const slideStyle = document.createElement('style');
slideStyle.textContent = `
    @keyframes slideDown {
        from {
            opacity: 0;
            transform: translateY(-20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
`;
document.head.appendChild(slideStyle);

// Initialize all project cards
document.addEventListener('DOMContentLoaded', () => {
    const projectCards = document.querySelectorAll('.project-card');
    
    projectCards.forEach(card => {
        const button = card.querySelector('.click-here-btn');
        if (button) {
            button.addEventListener('click', () => toggleProject(button));
        }
    });
});

// Optional: Add keyboard navigation for project cards
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        const projectContents = document.querySelectorAll('.project-content:not(.hidden)');
        projectContents.forEach(content => {
            content.classList.add('hidden');
            const button = content.closest('.project-card').querySelector('.click-here-btn');
            if (button) {
                button.textContent = 'Click Here';
                button.style.background = 'linear-gradient(135deg, #64ffda, #00bfa5)';
            }
        });
    }
});
