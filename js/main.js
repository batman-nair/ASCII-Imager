var charRatio = 0.6, charWidth = 8, charHeight = 15, charScale = 0.6;

text = document.createElement("pre");
document.body.appendChild(text);
text.style.height = 'auto';
text.style.width = 'auto';
text.style.position = 'absolute';
text.style.whiteSpace = 'pre';
text.style.lineHeight = '1.1em';
text.innerHTML = 'M';
charWidth = text.clientWidth;
charHeight = text.clientHeight;
charRatio = text.clientWidth/text.clientHeight;
document.body.removeChild(text);

var canvas = document.createElement('canvas'),
    ctx = canvas.getContext('2d');
var asciiOutput = document.querySelector("pre");
var previewImg = document.querySelector('img');
var isInverted = false;

function updateAsciiTextFromImgSrc(imgSrc, isInverted) {
    var img = new Image();
    img.src = imgSrc;
    img.onload = () => updateAsciiText(img, isInverted);
}

function updateAsciiText(img, isInverted) {
    var asciiShades = "M@GOCc+;:,. ".split(""),
	asciiDepth = asciiShades.length;
    if (isInverted)
	asciiShades = asciiShades.reverse();

    var widthLimit = previewImg.clientWidth, // screen.width*0.8,
	heightLimit = previewImg.clientHeight; //screen.height*0.8;
    var charCols = widthLimit/(charWidth*charScale),
	charRows = heightLimit/(charHeight*charScale);

    var minXScale = charCols/img.width,
	minYScale = charRows/(img.height*charRatio);
    var scale = minYScale;
    if (minXScale < minYScale)
	scale = minXScale;

    canvas.width = parseInt(img.width * scale);
    canvas.height = parseInt(img.height * scale * charRatio);
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

    var asciiText = "";
    for (var yy = 0; yy < canvas.height; ++yy) {
	for (var xx = 0; xx < canvas.width; ++xx) {
	    var pixel = ctx.getImageData(xx, yy, 1, 1);
	    var data = pixel.data;
	    var gray = 0.2627*data[0] + 0.6780*data[1] + 0.0593*data[2]; // ITU-R BT.2100 standard
	    if (gray > 255)
		gray = 255
	    var shade = 1;
	    while (gray > shade*255/asciiDepth)
		++shade;
	    asciiText += asciiShades[shade-1];
	}
	asciiText += '\n';
    }
    asciiOutput.innerText = asciiText;
    asciiOutput.style.fontSize = charScale + "em";
}

function previewAndMakeAscii() {
    var reader = new FileReader();
    var file = document.getElementById("file").files[0];
    reader.addEventListener("load", function () {
	previewImg.src = reader.result;
	updateAsciiTextFromImgSrc(reader.result, isInverted);
    }, false);

    if (file) {
	reader.readAsDataURL(file);
    }
}

updateAsciiTextFromImgSrc(previewImg.src, isInverted);

var slider = document.getElementById("font-scale");
slider.oninput = function() {
    charScale = parseFloat(this.value);
    updateAsciiTextFromImgSrc(previewImg.src);
}
var invert = document.getElementById("invert");
invert.oninput = function() {
    isInverted = this.checked;
    updateAsciiTextFromImgSrc(previewImg.src, isInverted);
}
