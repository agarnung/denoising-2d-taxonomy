// When clicking caret, set nested items opened
document.querySelectorAll('.caret').forEach(caret => {
    caret.addEventListener('click', () => {
      const nested = caret.nextElementSibling;
      if (nested) {
        nested.style.display = nested.style.display === 'block' ? 'none' : 'block';
      }
    });
  });
  