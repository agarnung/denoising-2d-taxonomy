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

// Open popup and display information based on 'elementId'
function openPopup(elementId) {
  // Get the popup and the description elements
  const popup = document.getElementById('popup');
  const description = document.getElementById('popup-description');
  const exampleBtn = document.getElementById('example-btn');  // Button to open the example popup
  
  // Set the content dynamically based on the 'elementId'
  switch(elementId) {
      case 'arithmetic':
          description.textContent = "Arithmetic filter reduces noise using arithmetic mean.";
          break;
      case 'geometric':
          description.textContent = "Geometric filter reduces noise using geometric mean.";
          break;
      case 'harmonic':
          description.textContent = "Harmonic filter reduces noise using harmonic mean.";
          break;
      case 'contraharmonic':
          description.textContent = "Contraharmonic filter reduces noise using contraharmonic mean.";
          break;
      // Add more cases as needed
      default:
          description.textContent = "Filter information not available.";
  }

  // Set a custom attribute to store the current elementId, to be used later for the example
  popup.setAttribute('data-element-id', elementId);

  // Show the main popup
  popup.classList.add('show');

  // Show the "Example" button (if not already visible)
  exampleBtn.style.display = 'block';
}

// Close the popup
function closePopup(popupId = 'popup') {
    const popup = document.getElementById(popupId);
    popup.classList.remove('show');
}

// Open "Example" popup and display example images based on the current 'elementId'
async function openExample() {
  const examplePopup = document.getElementById('example-popup');
  const imageContainer = examplePopup.querySelector('.image-container');
  const mainPopup = document.getElementById('popup');
  const elementId = mainPopup.getAttribute('data-element-id');  // Get the stored elementId

  // Build image paths dynamically based on the 'elementId'
  const noisyImageSrc = `./assets/${elementId}-noisy.png`;
  const filteredImageSrc = `./assets/${elementId}-clean.png`;
  const fallbackImageSrc = './assets/cross.jpg'; // Fallback image in case the images don't exist

  // Clear previous images in the container
  imageContainer.innerHTML = '';

  // Check if the images exist
  const noisyImageExists = await imageExists(noisyImageSrc);
  const filteredImageExists = await imageExists(filteredImageSrc);

  // Create the noisy image
  const noisyImage = document.createElement('img');
  noisyImage.src = noisyImageExists ? noisyImageSrc : fallbackImageSrc;
  noisyImage.alt = "Noisy Image";
  noisyImage.style.width = "100%";
  noisyImage.style.maxWidth = "250px";
  noisyImage.style.height = "auto";
  noisyImage.style.marginRight = "20px";

  // Create the filtered image
  const filteredImage = document.createElement('img');
  filteredImage.src = filteredImageExists ? filteredImageSrc : fallbackImageSrc;
  filteredImage.alt = "Filtered Image";
  filteredImage.style.width = "100%";
  filteredImage.style.maxWidth = "250px";
  filteredImage.style.height = "auto";

  // Append images to the container
  imageContainer.appendChild(noisyImage);
  imageContainer.appendChild(filteredImage);

  // Show the example popup
  examplePopup.classList.add('show');
}

// Function to check if an image exists
function imageExists(imageUrl) {
  const img = new Image();
  img.src = imageUrl;
  return new Promise((resolve) => {
    img.onload = () => resolve(true);  // Image exists
    img.onerror = () => resolve(false);  // Image doesn't exist
  });
}

// Open "More Info" popup
function openMoreInfo() {
  const moreInfoPopup = document.getElementById('more-info-popup');
  moreInfoPopup.classList.add('show');
}
