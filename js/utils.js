// When clicking caret, set nested items opened
document.querySelectorAll('.caret').forEach(caret => {
  caret.addEventListener('click', () => {
    // Toggle the display of nested items
    const nested = caret.nextElementSibling;
    if (nested) {
      nested.style.display = nested.style.display === 'block' ? 'none' : 'block';
    }

    // Toggle the active state of the caret to change the icon
    caret.classList.toggle('active');
  });
});

