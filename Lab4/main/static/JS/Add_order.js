const date_input = document.getElementsByName("date");

date_input[0].addEventListener('change', ()=>{
    console.log(date_input[0].value);
    const selectedDate = new Date(date_input[0].value);
    const currentDate = new Date();
    // Рассчитываем возраст
    const age = currentDate.getFullYear() - selectedDate.getFullYear();
    selectedDate.setFullYear(currentDate.getFullYear());

    // Если дата рождения еще не наступила в текущем году
    if (currentDate < selectedDate) {
        age--;
    }

    // Определяем день недели
    const daysOfWeek = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"];
    const dayOfWeek = daysOfWeek[selectedDate.getDay()];

    // Показываем сообщение в зависимости от возраста
    if (age >= 18) {
        alert(`Вам ${age} лет. День недели вашей даты рождения: ${dayOfWeek}`);
    } else {
        const consent = confirm(`Вы несовершеннолетний. Для использования сайта требуется разрешение родителей. Продолжить?`);
        if (consent) {
            alert(`Вам ${age} лет. День недели вашей даты рождения: ${dayOfWeek}`);
        } else {
            alert("Доступ к сайту запрещен.");
        }
    }
});

const ticketList = document.getElementById('ticketList');
const checkedInputs = ticketList.getElementsByTagName('input');
const totalSumLabel = document.getElementById('totalSum');
const discountSelect = document.getElementById('discountSelect');
const promocodePlate = document.getElementById('promocodePlate');

let totalPrice = 0;

console.log(checkedInputs);

[...checkedInputs].forEach((element) => {


    element.addEventListener('change',async ()=>{
        const priceLabel = document.getElementById(`ticket-${element.value}-price`);
        if (element.checked) {
            totalPrice += +priceLabel.innerHTML;
        } else {
            totalPrice -= +priceLabel.innerHTML;
        }

        const pr = await getDiscount(discountSelect.value);
        totalSumLabel.innerHTML = "Total sum: " + totalPrice * (100 - pr.discount) / 100;
    })
});
discountSelect.addEventListener('change',async()=>{
    //console.log('aaaaaaaaaaaa');
    const pr = await getDiscount(discountSelect.value);
    console.dir(await getDiscount(discountSelect.value));
    totalSumLabel.innerHTML = "Total sum: " + totalPrice * (100 - pr.discount) / 100;

    promocodePlate.style.display = 'block';
    document.getElementById('promo_code').innerHTML = pr.discount;
});
function getDiscount(id){
return new Promise((resolve, reject) => {
    if (id == 'default') {
      resolve({ discount: 0 });
    } else {
      var xhr = new XMLHttpRequest();
      xhr.open('GET', `/promocodes/get/${id}`, true);
      xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
          if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            var promo = response.promo;
            resolve(promo);
          } else {
            reject(new Error('AJAX request failed'));
          }
        }
      };
      xhr.send();
    }
  });

}
