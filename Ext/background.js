var the_tab_id = '';
var toggle = false;
var status = 'off';


function getToggle(callback) {
    chrome.storage.local.get('toggle', function(data){
        if(data.toggle === undefined) {
            callback(true); // default value    
        } else {
            callback(data.toggle);    
        }
    });    
}    

function setToggle(value, callback){
    chrome.storage.local.set({toggle : value}, function(){
        if(chrome.runtime.lastError) {
            throw Error(chrome.runtime.lastError);
        } else {
            callback();
        }    
    });    
}    




function set_status() {
    getToggle(function(toggle){
        toggle = !toggle;
        setToggle(toggle, function(){
            status = 'off';
            if(toggle) { status = 'on'; }
        })
    })
}

function toggle_extension(tab){
    chrome.browserAction.setIcon({ path:status+'.png', tabId:tab.id });
    chrome.tabs.executeScript({ code: 'var extension_status = "'+status+'"' });
    // chrome.tabs.executeScript({ file: "./alg.js" });
    chrome.tabs.executeScript({ file: "./script.js" });
    the_tab_id = tab.id;
}

function my_listener(tabId, changeInfo, tab) {
    if (changeInfo.status == "complete"  && status == 'on') {
        toggle_extension(tab);
    }
}

chrome.browserAction.onClicked.addListener(function(tab) {
    set_status();
    toggle_extension(tab);
});

chrome.tabs.onUpdated.addListener(my_listener);



