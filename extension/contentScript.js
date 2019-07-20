var sel = window.getSelection();
console.log(sel);
var selectedText = sel.toString();

chrome.extension.sendRequest({action: selectedText}, function(response) {
  console.log(response);
});

