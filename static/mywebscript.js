function RunSentimentAnalysis() {
    var textToAnalyze = document.getElementById("textToAnalyze").value.trim();
    var systemResponseElement = document.getElementById("system_response");

    // Clear previous responses
    systemResponseElement.innerHTML = '';

    if (textToAnalyze === '') {
        systemResponseElement.innerHTML = "<p style='color: red;'>Please enter some text to analyze.</p>";
        return;
    }

    // Make the GET request to the Flask backend
    fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`)
        .then(response => {
            if (!response.ok) {
                return response.json().then(error => {
                    systemResponseElement.innerHTML = `<p style='color: red;'>${error.error}</p>`;
                });
            }
            return response.json();
        })
        .then(data => {
            if (data.response) {
                systemResponseElement.innerHTML = `<p>${data.response}</p>`;
            }
        })
        .catch(error => {
            systemResponseElement.innerHTML = `<p style='color: red;'>Error: ${error.message}</p>`;
        });
}
