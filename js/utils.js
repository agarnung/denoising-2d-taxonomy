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

// Open popup and display information
function openPopup(elementId) {
  // Get the popup element
  const popup = document.getElementById('popup');
  const description = document.getElementById('popup-description');
  
  // Set the content dynamically based on the clicked item
  switch(elementId) {
      case 'median-filter':
          description.textContent = "The Median Filter is a non-linear filter that replaces each pixel value by the median of the values in its neighborhood.";
          break;
      case 'gaussian-filter':
          description.textContent = "The Gaussian filter is a linear filter that smooths an image by averaging the pixels within a certain radius, weighted by a Gaussian distribution.";
          break;
      case 'wiener-filter':
          description.textContent = "The Wiener filter is used to reduce noise in an image by estimating the local image variance and smoothing accordingly.";
          break;
  }

  // Show the main popup
  popup.classList.add('show');
}

// Close the main popup
function closePopup(popupId = 'popup') {
    const popup = document.getElementById(popupId);
    popup.classList.remove('show');
}

// Open "More Info" popup
function openMoreInfo() {
  const moreInfoPopup = document.getElementById('more-info-popup');
  moreInfoPopup.classList.add('show');
}

// Open "Papers" popup
function openPapers() {
  const papersPopup = document.getElementById('papers-popup');
  papersPopup.classList.add('show');
}
