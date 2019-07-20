var sel = window.getSelection();
var selectedText = sel.toString();

chrome.extension.sendRequest({action: selectedText}, function(response) {
  resp = JSON.parse(response);
  console.log(resp);  
});
