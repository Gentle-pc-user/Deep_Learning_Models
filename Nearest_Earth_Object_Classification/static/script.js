// Simple ripple effect for buttons
document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.ripple');
    buttons.forEach(button => {
        button.addEventListener('click', function(e) {
            let x = e.clientX - e.getBoundingClientRect().left;
            let y = e.clientY - e.getBoundingClientRect().top;

            let ripples = document.createElement('span');
            ripples.style.left = x + 'px';
            ripples.style.top = y + 'px';
            ripples.style.position = 'absolute';
            ripples.style.background = 'rgba(255, 255, 255, 0.4)';
            ripples.style.transform = 'translate(-50%, -50%)';
            ripples.style.pointerEvents = 'none';
            ripples.style.borderRadius = '50%';
            ripples.style.width = '200px';
            ripples.style.height = '200px';
            ripples.style.animation = 'rippleAnim 0.6s linear';
            
            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripples);

            setTimeout(() => {
                ripples.remove();
            }, 600);
        });
    });
});