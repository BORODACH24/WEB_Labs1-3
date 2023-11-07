const label1 = document.querySelector('#label-1');
const label2 = document.querySelector('#label-2');
const joke = document.querySelector('#joke');
const fact = document.querySelector('#fact');

window.addEventListener('scroll', () => {
    let value = scrollY;
    //console.log(scrollY);
    if(scrollY<700){
        label1.style.transform = `translateY(${value*0.6}px)`
        label2.style.transform = `translateY(${value*0.6}px)`
        joke.style.transform = `translateX(-${value}px)`
        fact.style.transform = `translateX(${value}px)`
    }
})

const ad = document.querySelector('#ads');
const contextMenu = document.querySelector('#contextMenu');
let currentIndex = 0;
let rotationInterval;
let isPaused = false;
let interval = 5000;
const banners = document.querySelectorAll('#ads img');
const intervalInput = document.getElementById('interval');

const startButton = document.getElementById('startButton');
const stopButton = document.getElementById('stopButton');

if(contextMenu){

ad.addEventListener('contextmenu', e=>{
    e.preventDefault();
    if (contextMenu && contextMenu.contains(e.target)) {
        return;
    }
    let x = e.offsetX, y = e.offsetY,
    winWidth = ad.offsetWidth,
    winHeight = ad.offsetHeight,
    cmWidth = contextMenu.offsetWidth,
    cmHeight = contextMenu.offsetHeight;

//    if(x > (winWidth - cmWidth - shareMenu.offsetWidth)) {
//        shareMenu.style.left = "-200px";
//    } else {
//        shareMenu.style.left = "";
//        shareMenu.style.right = "-200px";
//    }
    x = x > winWidth - cmWidth ? winWidth - cmWidth - 5 : x;
    y = y > winHeight - cmHeight ? winHeight - cmHeight - 5 : y;
    console.log("winWidth = " + winWidth);
    console.log("cmWidth = " + cmWidth);
    contextMenu.style.left = `${x}px`;
    contextMenu.style.top = `${y}px`;
    contextMenu.style.visibility = "visible";
});
}
document.addEventListener("click", (event) => {
  if (contextMenu && !contextMenu.contains(event.target)) {
    contextMenu.style.visibility = "hidden";
  }
});

function rotateBanners() {
  banners[currentIndex].style.opacity = 0; // Fade out

  setTimeout(() => {
    banners[currentIndex].style.display = 'none'; // Hide the element
    currentIndex = (currentIndex + 1) % banners.length;
    banners[currentIndex].style.display = 'block'; // Show the next element
    //banners[currentIndex].style.opacity = 0; // Fade in
  }, 300); // Wait for the fade-out transition (0.5 seconds)
  setTimeout(() => {
    banners[currentIndex].style.opacity = 1; // Fade in
  }, 600); // Wait for the fade-out transition (0.5 seconds)

}
if(intervalInput){
    intervalInput.addEventListener('change', e => {
      interval = parseInt(e.target.value) * 1000;
      clearInterval(rotationInterval);
      if(isPaused){
        return;
      }
      rotationInterval = setInterval(rotateBanners, interval);
      console.log("interval = " + interval);
    });
}
function startRotation() {
  rotationInterval = setInterval(rotateBanners, interval);

  console.log("start");
  if(startButton && stopButton){
      startButton.disabled = true;
      stopButton.disabled = false;
  }
}

function stopRotation() {
  clearInterval(rotationInterval);

  console.log("stop");
  startButton.disabled = false;
  stopButton.disabled = true;
}
if(startButton){
    startButton.addEventListener('click', ()=>{
        isPaused = false;
        startRotation();
    });
}
if(stopButton){
    stopButton.addEventListener('click', ()=>{
        isPaused = true;
        stopRotation();
    });
}

document.addEventListener('visibilitychange', () => {
  if (document.visibilityState === "visible" && !isPaused) {
    startRotation();
  } else{
    stopRotation();
  }
});

// Start rotation initially
startRotation();


// Функция для начала отсчета
function startCountdown() {
  const countdownElement = document.getElementById("countdown");
  const minutesLabel = document.getElementById("minutes");
  const secondsLabel = document.getElementById("seconds");
  const startTime = sessionStorage.getItem("countdownStartTime");
  if (startTime) {
    // Получаем сохраненное время старта отсчета
    let savedTime = new Date(startTime);
    let currentTime = new Date();
    let elapsedTime = currentTime - savedTime;
    let remainingTime = 3600000 - elapsedTime; // 1 час в миллисекундах
    if (remainingTime > 0) {
      // Если осталось время
      const intervalId = setInterval(function () {
        const minutes = Math.floor((remainingTime % 3600000) / 60000);
        const seconds = Math.floor((remainingTime % 60000) / 1000);
        minutesLabel.textContent = minutes;
        secondsLabel.textContent = seconds;
        if (remainingTime <= 0) {
          // Когда отсчет завершен
          clearInterval(intervalId);
          countdownElement.textContent = "Отсчет завершен!";
        } else {
          // Уменьшаем оставшееся время на одну секунду
          remainingTime -= 1000;
        }
      }, 1000); // Запускаем обновление каждую секунду
    } else {
      // Если время истекло, отображаем сообщение
      countdownElement.textContent = "Отсчет завершен!";
    }
  } else {
    const currentTime = new Date();
    sessionStorage.setItem("countdownStartTime", currentTime);
    startCountdown(); // Запускаем отсчет снова
  }
}

// Вызываем функцию для начала отсчета
startCountdown();

const body = document.querySelector('body'),
      article = document.querySelector('article'),
      walk = {x: 20, y: 15},
      articleText = document.querySelector('.article__text');

function parallax(e) {
  const width = article.offsetWidth,
        height = article.offsetHeight;

  let { offsetX: x, offsetY: y} = e;

  const xWalk = Math.round((e.x / width / 2 * walk.x) - (walk.x / 2)),
        yWalk = Math.round((e.y / height / 2  * walk.y) - (walk.y / 2));

  article.style.transform = `rotateY(${-xWalk}deg) rotateX(${yWalk}deg)`;
}

article.addEventListener('mousemove', parallax);