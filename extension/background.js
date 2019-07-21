var text = "";
response=[];
var product_name="";

//chrome.extension.onRequest.addListener(onRequest);

function onRequest(info, tab) {
  product_name = info.selectionText;
  //console.log(selection);
};

//create new tab of selected texxt
chrome.contextMenus.onClicked.addListener(function(tab) {
  
  let xhr = new XMLHttpRequest();
  var text= "http://35.173.235.215:5000/?ProductName="+product_name.replace(/ /g,"%20");
  
  console.log(text);
   
   xhr.open("GET", text);
   xhr.send();
  xhr.onload = function(){
  response = xhr.response;
  console.log(response);
  }

  chrome.runtime.sendMessage({data :response }, function(response){

  });
  
});



//create contextMenu
chrome.contextMenus.create({title:"Search '%s' on",contexts: ["all"], "onclick" : onRequest, "id": "parent"});
