
// script.js
document.getElementById("uploadBtn").addEventListener("click", function() {
    const fileInput = document.getElementById("fileInput");
    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        const reader = new FileReader();
        reader.onload = function(event) {
            const imgElement = document.createElement("img");
            imgElement.src = event.target.result;
            const designDiv = document.createElement("div");
            designDiv.className = "design";
            designDiv.appendChild(imgElement);
            document.getElementById("designsContainer").appendChild(designDiv);
        };
        reader.readAsDataURL(file);
    }
});