// всплывающе окна

let linkKeyHandler = null;
let linkclickCloseHandler = null;

function openPopup(popup) {
  popup.classList.add('popup_is-opened');
  linkKeyHandler = (evt) => keyHandler(evt, popup);
  linkclickCloseHandler = (evt) => clickCloseHandler(evt, popup);
  window.addEventListener('keydown', linkKeyHandler);
  document.addEventListener('click', linkclickCloseHandler);
}

function closePopup(popup) {
  popup.classList.remove('popup_is-opened');
  window.removeEventListener('keydown', linkKeyHandler);
  document.removeEventListener('click', linkclickCloseHandler);
  linkKeyHandler = null;
  linkclickCloseHandler = null;
}

function keyHandler(evt, popup) {
  if (evt.key === "Escape") {
    closePopup(popup);
  }
}

function clickCloseHandler(evt, popup) {
  const btnClose = evt.target.classList.contains('popup__close');
  const outPopup = evt.target.classList.contains('popup');
  if (btnClose || outPopup) {
    closePopup(popup);
  }
}

// Добавить звонок

const btnAddCall = document.querySelector('.button_popup_call');
const popupNewCall = document.querySelector('.popup_call_new');

btnAddCall.addEventListener('click', function(){
    openPopup(popupNewCall)
})

// Редактировать звонок

const calls = document.querySelectorAll('.call_li_item');
const popupEditCall = document.querySelector('.popup_call_eddit');
const formCall = document.forms.callForm;

calls.forEach((call) => {
  call.addEventListener('click', () => {
    const idCall = call.getAttribute('data-id')
    formCall.setAttribute('action', `"{% url 'edit_call' ${idCall} %}"`)
    formCall.name.value = call.querySelector('.call_datetime').getAttribute("data-date_time");
    console.log(call)
    console.log(formCall)

    formCall.full_name.value = call.querySelector('.call_full_name').textContent;
    formCall.question.value = call.querySelector('.call_question').textContent;
    formCall.telephone.value = call.querySelector('.call_telephone').textContent;
    formCall.result.value = call.querySelector('.call_result').textContent;
    openPopup(popupEditCall)
  })
})