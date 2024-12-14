// background.js
chrome.runtime.onInstalled.addListener(() => {
    console.log('Extension installed');
    chrome.contextMenus.create({
        id: "textToSpeech",
        title: "Convert to Speech",
        contexts: ["selection"]
    });
});

chrome.contextMenus.onClicked.addListener(async (info, tab) => {
    if (info.menuItemId === "textToSpeech") {
        console.log("Selected text:", info.selectionText);
        
        try {
            // First check if we can inject the content script
            await chrome.scripting.executeScript({
                target: { tabId: tab.id },
                files: ['content.js']
            });

            // Then send the message
            chrome.tabs.sendMessage(tab.id, {
                action: "playAudio",
                text: info.selectionText
            }, (response) => {
                if (chrome.runtime.lastError) {
                    console.error('Error:', chrome.runtime.lastError);
                    alert('Please refresh the page and try again.');
                }
            });
        } catch (error) {
            console.error('Error:', error);
            alert('Cannot access this page. Try on another page.');
        }
    }
});