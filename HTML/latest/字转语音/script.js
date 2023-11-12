// grab the UI elements to work with
const textEl = document.getElementById('text');
const voiceInEl = document.getElementById('voice');
const pitchInEl = document.getElementById('pitch');
const rateInEl = document.getElementById('rate');
const volumeInEl = document.getElementById('volume');
const pitchOutEl = document.querySelector('output[for="pitch"]');
const rateOutEl = document.querySelector('output[for="rate"]');
const volumeOutEl = document.querySelector('output[for="volume"]');
const speakEl = document.getElementById('speak');

// add UI event handlers
pitchInEl.addEventListener('change', updateOutputs);
rateInEl.addEventListener('change', updateOutputs);
volumeInEl.addEventListener('change', updateOutputs);
speakEl.addEventListener('click', speakText);

// update voices immediately and whenever they are loaded
updateVoices();
window.speechSynthesis.onvoiceschanged = updateVoices;

function updateOutputs() {
  // display current values of all range inputs
  pitchOutEl.textContent = pitchInEl.value;
  rateOutEl.textContent = rateInEl.value;
  volumeOutEl.textContent = volumeInEl.value;
}

function updateVoices() {
  // add an option for each available voice that isn't already added
  window.speechSynthesis.getVoices().forEach(voice => {
    const isAlreadyAdded = [...voiceInEl.options].some(option => option.value === voice.voiceURI);
    if (!isAlreadyAdded) {
      const option = new Option(voice.name, voice.voiceURI, voice.default, voice.default);
      voiceInEl.add(option);
    }
  });
}

function speakText() {
  // Stop other speaking progress
  window.speechSynthesis.cancel();

  // Create new utterance with all the properties
  const text = textEl.value;
  const utterance = new SpeechSynthesisUtterance(text);
  utterance.voice = window.speechSynthesis.getVoices().find((voice) => {
    return voice.voiceURI === voiceInEl.value
  });
  utterance.pitch = pitchInEl.value;
  utterance.rate = rateInEl.value;
  utterance.volume = volumeInEl.value;
  
  // Speak the utterance
  window.speechSynthesis.speak(utterance);
}