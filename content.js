// content.js
if (!window.audioListenerInitialized) {
    window.audioListenerInitialized = true;
    
    console.log("Content script loaded - first time initialization");
    
    // Keep track of current audio
    let currentAudio = null;
    
    chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
        console.log("Message received in content script:", request);
        
        if (request.action === "playAudio") {
            // Stop any currently playing audio
            if (currentAudio) {
                currentAudio.pause();
                currentAudio = null;
            }
            
            const audioUrl = `http://localhost:5001/play-audio?text=${encodeURIComponent(request.text)}`;
            console.log("Creating audio with URL:", audioUrl);
            
            currentAudio = new Audio(audioUrl);
            currentAudio.play()
                .then(() => {
                    console.log("Audio playing successfully");
                    sendResponse({ status: "success" });
                })
                .catch(error => {
                    console.error('Error playing audio:', error);
                    sendResponse({ status: "error", message: error.toString() });
                });
            
            return true;
        }
    });
}