/**
 * Modern Telegram Landing Page
 * Handles click tracking and interactive micro-animations
 */

document.addEventListener('DOMContentLoaded', () => {
  const primaryBtn = document.getElementById('primaryCtaBtn');

  // Track button intent without blocking native navigation
  if (primaryBtn) {
    primaryBtn.addEventListener('click', (event) => {
      // Micro haptic feel for devices supporting the Vibration API
      if ('vibrate' in navigator) {
        navigator.vibrate(40);
      }

      // Optional console log verification for telemetry
      console.log('User triggered Telegram join CTA link.');
    });
  }

  // Smooth appearance of feature cards on scroll
  const observerOptions = {
    threshold: 0.15,
    rootMargin: '0px 0px -40px 0px'
  };

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.feature-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(12px)';
    card.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
    revealObserver.observe(card);
  });
});
