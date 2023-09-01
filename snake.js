document.addEventListener('DOMContentLoaded', function () {
    const startButton = document.getElementById('startButton');
    const gameContainer = document.getElementById('gameContainer');
    
    let gameFrame = document.createElement('iframe');
    gameFrame.src = 'https://your-vercel-app-url'; // Thay thế bằng URL của ứng dụng Vercel
    gameFrame.style.display = 'none';
    gameContainer.appendChild(gameFrame);

    startButton.addEventListener('click', function () {
        gameFrame.style.display = 'block';
    });
});
