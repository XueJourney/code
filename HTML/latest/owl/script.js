const $owlLogin = document.getElementById('owl-login');
const $passwordInput = document.getElementById('password');

$passwordInput.addEventListener('focus', () => {
  $owlLogin.classList.add('password');
});

$passwordInput.addEventListener('focusout', () => {
  $owlLogin.classList.remove('password');
});