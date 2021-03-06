'use strict';

// PART 1: SHOW A FORTUNE

function showFortune(evt) {
  // TODO: get the fortune and show it in the #fortune-text div
  fetch('/fortune')
  .then(response => response.text())
  .then(responseData => {
    document.querySelector('#fortune-text').innerText = responseData;
  });
}

document.querySelector('#get-fortune-button').addEventListener('click', showFortune);

// PART 2: SHOW WEATHER

function showWeather(evt) {
  evt.preventDefault();

  const url = '/weather.json';
  const zipcode = document.querySelector('#zipcode-field').value;

  // TODO: request weather with that URL and show the forecast in #weather-info
  fetch(url)
  .then(response => response.json())
  .then(responseData => {
    document.querySelector('#weather-info').innerText = responseData.forecast;
  });
}

document.querySelector('#weather-form').addEventListener('submit', showWeather);

// PART 3: ORDER MELONS

function orderMelons(evt) {
  evt.preventDefault();

  // TODO: show the result message after your form
  // document.querySelector('#order-form').addEventListener('submit', evt => {
  //   evt.preventDefault();
  
  //   const formInputs = {
  //     type: document.querySelector('#type-field').value,
  //     amount: document.querySelector('#amount-field').value,
  //   };
  
  //   fetch('/new-order', {
  //     method: 'POST',
  //     body: JSON.stringify(formInputs),
  //     headers: {
  //       'Content-Type': 'application/json',
  //     },
  //   })
  //     .then(response => response.json())
  //     .then(responseJson => {
  //       alert(responseJson.status);
  //     });
  // });
      document.querySelector('#order-form').addEventListener('submit', evt => {
        orderMelons(evt);

      const formInputs = {
        qty: document.querySelector('#qty-field').value,
        melon_type: document.querySelector('#melon-type-field').value,
          };
          
      fetch('/order-melons.json', {
        method: 'POST',
        body: JSON.stringify(formInputs),
        headers: {
          'Content-Type': 'application/json',
        },
      })
        .then(response => response.json())
        .then(responseJson => {if (responseJson.code === "ERROR") 
        { document.querySelector('#order-status').classList.add('order-error'); 
          document.querySelector('#order-status').innerText = responseJson.msg}
          else {
          document.querySelector('#order-status').innerText = responseJson.msg};
          alert(responseJson.msg);
          //console.dir(responseJson.msg);
        });

    });
  };

document.querySelector('#order-form').addEventListener('submit', orderMelons);

function get_dog_pic(evt) {
  evt.preventDefault();

  const url = 'https://dog.ceo/api/breeds/image/random';

  fetch(url)
  .then(response => response.json())
  .then(responseData => { const picUrl = responseData.message;
    document.querySelector('#dog-image').insertAdjacentHTML('beforeend', `<div><img src=${picUrl}></div>`);
  })}

  document.querySelector('#dog-image').addEventListener('click',
    get_dog_pic);

// {/* <img src="img_girl.jpg" width="500" height="600"></img> */}