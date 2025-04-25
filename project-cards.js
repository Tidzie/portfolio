// Project card click functionality
document.addEventListener('DOMContentLoaded', function() {
    // Get all click-here buttons
    const buttons = document.querySelectorAll('.click-here-btn');
    
    // Add click event to each button
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            // Find the project content div that follows this button
            const content = this.nextElementSibling;
            
            // Toggle the hidden class
            content.classList.toggle('hidden');
            
            // Change button text
            if (content.classList.contains('hidden')) {
                this.textContent = 'Click Here';
            } else {
                this.textContent = 'Hide Details';
            }
        });
    });
}); 