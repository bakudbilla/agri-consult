document.addEventListener('DOMContentLoaded', function() {
    // Close flash message after 5 seconds
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(flashMessage => {
        setTimeout(() => {
            flashMessage.style.display = 'none';
        }, 5000);
    });
});