simulation.on('end', () => {
    copyGraphToBirdView();
});

function copyGraphToBirdView() {
    const visualizationSvg = document.getElementById('visualization').querySelector('svg');
    const birdViewSvg = document.getElementById('bird-svg');
    const birdViewContainer = document.querySelector('.bird-view.border-frame');
    const overlay = document.createElement('div');
    overlay.classList.add('overlay');
    overlay.textContent = 'Waiting for graph...';

    birdViewContainer.appendChild(overlay);

    birdViewSvg.innerHTML = '';

    const clonedG = visualizationSvg.querySelector('g').cloneNode(true);
    birdViewSvg.appendChild(clonedG);

    const birdViewWidth = birdViewContainer.clientWidth;
    const birdViewHeight = birdViewContainer.clientHeight;
    birdViewSvg.setAttribute('width', birdViewWidth);
    birdViewSvg.setAttribute('height', birdViewHeight);

    const clonedGBox = clonedG.getBBox();
    const clonedGWidth = clonedGBox.width;
    const clonedGHeight = clonedGBox.height;

    const scaleX = (birdViewWidth * 0.9) / clonedGWidth;
    const scaleY = (birdViewHeight * 0.9) / clonedGHeight;
    const scale = Math.min(scaleX, scaleY);

    const translateX = (birdViewWidth - clonedGWidth * scale) / 2 - clonedGBox.x * scale;
    const translateY = (birdViewHeight - clonedGHeight * scale) / 2 - clonedGBox.y * scale;
    clonedG.setAttribute('transform', `translate(${translateX},${translateY}) scale(${scale})`);

    birdViewContainer.removeChild(overlay);
}