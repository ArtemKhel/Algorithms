
var elementsInsideBody = [...document.body.getElementsByTagName('*')];



var blacklist = ['javascript']

function findAndReplace(){
    filter = new Aho_Corasic(blacklist)
    elementsInsideBody.forEach(element =>{
        element.childNodes.forEach(child =>{
            if(child.nodeType === 3){
                let value = child.nodeValue;
                value = filter.replace(value)
                child.nodeValue = value;
            }
        });
        
    });
}

window.onload = findAndReplace();