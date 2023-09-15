// Create the script element to load the external JavaScript file
var script = document.createElement('script');
script.src = 'https://linangdata.com/calculatorEmbed/linangcalc.js';
document.head.appendChild(script);

// Create the div element to contain the iframe
var div = document.createElement('div');
div.style.width = '50px';
div.style.height = '50px';
div.style.backgroundImage = "url('https://linangdata.com/calculatorEmbed/icons/48x48.png')";

// Create the iframe element and set its attributes
var iframe = document.createElement('iframe');
iframe.id = 'linangcalc';
iframe.src = 'https://linangdata.com/calculatorEmbed/embeddable.html?placement=right';
iframe.width = '50';
iframe.height = '50';
iframe.scrolling = 'auto';
iframe.frameBorder = '0';
iframe.allowTransparency = 'true';
iframe.style.border = '0';
iframe.style.position = 'absolute';
iframe.style.opacity = '1.0';

// Append the iframe to the div
div.appendChild(iframe);

// Append the div to the body of the document
document.body.appendChild(div);
