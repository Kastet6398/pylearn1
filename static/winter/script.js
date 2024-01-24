function getRandomNumber(min, max) {
  return Math.random() * (max - min) + min;
}
function createSnowflake() {
  if (!document.hidden) {
    const snowflake = document.createElement('div');
    snowflake.className = 'snowflake';
    snowflake.innerHTML = '❄️';
    snowflake.style.left = `${getRandomNumber(0, window.innerWidth)}px`;
    document.body.appendChild(snowflake);

    snowflake.addEventListener('animationiteration', () => {
      snowflake.remove();
    });
  }
}
createSnowflake();
setInterval(createSnowflake, 0.04);
