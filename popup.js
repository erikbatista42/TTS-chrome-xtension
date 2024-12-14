document.addEventListener('DOMContentLoaded', () => {
  // Get the active tab
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    // Execute script in the active tab to get selected text
    chrome.scripting.executeScript({
      target: { tabId: tabs[0].id },
      function: getSelectedTextAndSpeak
    });
  });
});

function getSelectedTextAndSpeak() {
  const selectedText = window.getSelection().toString();
  
  if (selectedText) {
    // Send text to your TTS service
    fetch('http://localhost:5001/tts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text: selectedText }),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  } else {
    alert('Please select some text first');
  }
}