var text = "";

chrome.extension.onRequest.addListener(onRequest);

function onRequest(request, sender, sendResponse) {
   text = "http://google.com/";
   text = text + request.action.toString();

   sendResponse({});
};


//create new tab of selected texxt
chrome.contextMenus.onClicked.addListener(function(tab) {
  chrome.tabs.create({url:text});
});

//create contextMenu
chrome.contextMenus.create({title:"Search '%s' on",contexts: ["selection"]});