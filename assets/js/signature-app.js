var wrapper = document.getElementById("signature-pad");
var clearButton = wrapper.querySelector("[data-action=clear]");
var canvas = wrapper.querySelector("canvas");
var signaturePad = new SignaturePad(canvas, {
    backgroundColor: "rgb(255,255,255)",
    minWidth: 0.4,
    maxWidth: 2,
    dotSize: 1.2,
    onEnd: function () {
        signature = signaturePad.toDataURL("image/jpeg");
        document.getElementById('id_hidden_image').value = signature;
    }
  });

// Adjust canvas coordinate space taking into account pixel ratio,
// to make it look crisp on mobile devices.
// This also causes canvas to be cleared.
function resizeCanvas() {
    // When zoomed out to less than 100%, for some very strange reason,
    // some browsers report devicePixelRatio as less than 1
    // and only part of the canvas is cleared then.
    var ratio =  Math.max(window.devicePixelRatio || 1, 1);

    // This part causes the canvas to be cleared
    canvas.width = canvas.offsetWidth * ratio;
    canvas.height = canvas.offsetHeight * ratio;
    canvas.getContext("2d").scale(ratio, ratio);

    // This library does not listen for canvas changes, so after the canvas is automatically
    // cleared by the browser, SignaturePad#isEmpty might still return false, even though the
    // canvas looks empty, because the internal data of this library wasn't cleared. To make sure
    // that the state of this library is consistent with visual state of the canvas, you
    // have to clear it manually.
    signaturePad.clear();
}

window.onresize = resizeCanvas;
resizeCanvas();

clearButton.addEventListener("click", function (event) {
    signaturePad.clear();
});
