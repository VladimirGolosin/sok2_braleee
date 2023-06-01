// Call the copyGraphToBirdView function when the simulation ends
simulation.on('end', () => {
    copyGraphToBirdView();
});

// Function to copy the contents of the SVG graph to the bird view
function copyGraphToBirdView() {
    const visualizationSvg = document.getElementById('visualization').querySelector('svg');
    const birdViewSvg = document.getElementById('bird-svg');
    const birdViewContainer = document.querySelector('.bird-view.border-frame');
    const overlay = document.createElement('div');
    overlay.classList.add('overlay');
    overlay.textContent = 'Waiting for graph...';

    // Add the overlay to the bird view container
    birdViewContainer.appendChild(overlay);

    // Clear any existing content in the bird view SVG
    birdViewSvg.innerHTML = '';

    // Clone the visualization SVG's g tag and insert it into the bird view SVG
    const clonedG = visualizationSvg.querySelector('g').cloneNode(true);
    birdViewSvg.appendChild(clonedG);

    // Set the bird view SVG size to match the container size
    const birdViewWidth = birdViewContainer.clientWidth;
    const birdViewHeight = birdViewContainer.clientHeight;
    birdViewSvg.setAttribute('width', birdViewWidth);
    birdViewSvg.setAttribute('height', birdViewHeight);

    // Get the dimensions of the cloned g tag
    const clonedGBox = clonedG.getBBox();
    const clonedGWidth = clonedGBox.width;
    const clonedGHeight = clonedGBox.height;

    // Calculate the scaling factors to fit the g tag within the bird view SVG
    const scaleX = (birdViewWidth * 0.9) / clonedGWidth;
    const scaleY = (birdViewHeight * 0.9) / clonedGHeight;
    const scale = Math.min(scaleX, scaleY);

    // Apply the scaling to the g tag
    const translateX = (birdViewWidth - clonedGWidth * scale) / 2 - clonedGBox.x * scale;
    const translateY = (birdViewHeight - clonedGHeight * scale) / 2 - clonedGBox.y * scale;
    clonedG.setAttribute('transform', `translate(${translateX},${translateY}) scale(${scale})`);

    // Remove the overlay once the bird view is ready
    birdViewContainer.removeChild(overlay);
}