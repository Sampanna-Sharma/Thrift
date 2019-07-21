

function get_div(element)
{
    var container =document.createElement('div')
    var title = document.createElement('div')
    var img = document.createElement('img')
    var a = document.createElement('a')
    a.href = element.url
    img.src = element.image_link
    img.height = 50
    img.width = 50
    title.innerText = element.title
    var price = document.createElement('div')
    price.innerText = element.price
    var rating = document.createElement('div')
    a.appendChild(img)
    rating.innerText = element.rating
    container.appendChild(a)
    container.appendChild(title)
    container.appendChild(rating)
    container.appendChild(price)
    return container

    
}

chrome.runtime.onMessage.addListener(function(message,sender,sendResponse){
    console.log(message.data)
    var cont = []
    data = JSON.parse(message.data)
    for(var i=0;i<data.length;i++)
    {
        var p = data[i]
        if(p.daraz)
        {
        
        cont.push(get_div(p.daraz));
        document.getElementById('print').innerText= p.title
        


        }
        else if(p.bestdeals)
        {
            cont.push(get_div(p.bestdeals));
        }  
        else if(p.smartdoko)
        {
            cont.push(get_div(p.smartdoko));
        } 
        else if(p.nepbay)
        {
            cont.push(get_div(p.nepbay))
        }
        else if(data[i].sastodeal)
        {
            cont.push(get_div(p.sastodeal))
        }
    }
    for(var i=0;i<cont.length;i++)
    {
        console.log(cont[i])
        document.getElementById('heading1').appendChild(cont[i])
    }
});