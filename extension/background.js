var text = "";

chrome.extension.onRequest.addListener(onRequest);

function onRequest(request, sender, sendResponse) {
   let xhr = new XMLHttpRequest();
   var product_name=request.action.toString(); 
   var text= "http://127.0.0.1:5000/?ProductName="+product_name;
   xhr.open("GET", text);
   xhr.send();
  response=[];
  xhr.onload = function(){
    var response = xhr.response;
    response= JSON.parse(response);
    console.log(response.item[0]);
  }

};

//create new tab of selected texxt
chrome.contextMenus.onClicked.addListener(function(tab) {
  chrome.tabs.create({url: text});
});

//create contextMenu
chrome.contextMenus.create({title:"Search '%s' on",contexts: ["selection"]});