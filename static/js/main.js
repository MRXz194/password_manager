document.addEventListener('DOMContentLoaded', function() {
    // Password 
    document.querySelectorAll('.password-toggle').forEach(button => {
        button.addEventListener('click', function() {
            const passwordField = this.previousElementSibling;
            const icon = this.querySelector('i');
            
            if (passwordField.type === 'password') {
                passwordField.type = 'text';
                icon.classList.remove('fa-eye');
                icon.classList.add('fa-eye-slash');
            } else {
                passwordField.type = 'password';
                icon.classList.remove('fa-eye-slash');
                icon.classList.add('fa-eye');
            }
        });
    });

    // Flash message 
    const flashMessages = document.querySelectorAll('.alert');
    flashMessages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => message.remove(), 300);
        }, 3000);
    });

    // Password strength 
    const passwordInput = document.querySelector('input[type="password"]');
    if (passwordInput) {
        passwordInput.addEventListener('input', function() {
            const password = this.value;
            const strength = calculatePasswordStrength(password);
            updatePasswordStrengthMeter(strength);
        });
    }

    // Copy password to clpb
    document.querySelectorAll('.copy-password').forEach(button => {
        button.addEventListener('click', async function() {
            const passwordField = this.closest('.password-item').querySelector('.password-value');
            try {
                await navigator.clipboard.writeText(passwordField.textContent);
                showToast('Password copied to clipboard!');
            } catch (err) {
                showToast('Failed to copy password', 'error');
            }
        });
    });
});

function calculatePasswordStrength(password) {
    let strength = 0;
    
    // Length check
    if (password.length >= 8) strength += 1;
    if (password.length >= 12) strength += 1;
    
    // Character type check
    if (/[0-9]/.test(password)) strength += 1;
    if (/[a-z]/.test(password)) strength += 1;
    if (/[A-Z]/.test(password)) strength += 1;
    if (/[^A-Za-z0-9]/.test(password)) strength += 1;
    
    return Math.min(strength, 5);
}

function updatePasswordStrengthMeter(strength) {
    const meter = document.querySelector('.password-strength-meter'); // Get the password strength meter
    if (!meter) return;
    
    const strengthText = ['Very Weak', 'Weak', 'Fair', 'Good', 'Strong', 'Very Strong'];
    const strengthClass = ['very-weak', 'weak', 'fair', 'good', 'strong', 'very-strong'];
    
    meter.querySelector('.strength-text').textContent = strengthText[strength];
    meter.querySelector('.strength-bar').className = `strength-bar ${strengthClass[strength]}`;
}

function showToast(message, type = 'success') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    
    document.body.appendChild(toast);
    
    setTimeout(() => {
        toast.classList.add('show');
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => toast.remove(), 300);
        }, 3000);
    }, 100);
}
